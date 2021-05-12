import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . import models
from django.db.models.signals import post_save
class ChatConsumer(WebsocketConsumer):
    """
    Basic chat consumer that allows users to connect, providing the give a valid JWT auth token
    token authentication on websockets? cool, right? :)
    """
    connected_users = []
    def connect(self):
        print(self.scope["user"])
        self.__class__.connected_users.append(self) # keep track of all connected users
        self.accept()
    def receive(self, text_data):
        """
        Create a message from the raw data sent from the client. This message will not be sent to their respective consumers.
        """
        data = json.loads(text_data)
        message = models.Message(content=data["body"], user_from=self.scope["user"], user_to=models.User.objects.get(username=data['to']))
        message.save() # no need to worry about sending message because the signal helper function will take care of it
    def send_message(self, ctx):
        self.send(json.dumps(ctx))
    @classmethod
    def message_handler(cls, sender, **data):
        """
        Message handler that is called whenever a new Message object is saved into the database.
        Instead of grouping by rooms, this allows us to maintain one connection open but be able to receive messages from different people.
        """
        for user in cls.connected_users:
            print("Hello!") # find the right user.
            if user.scope["user"] == data["instance"].user_to:
                user.send_message(data["instance"].serialize())

post_save.connect(ChatConsumer.message_handler, sender=models.Message)