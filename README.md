# Waffles

**Hello, World!** This is a social media application that I developed, titled *Waffles*.

## Frameworks/Libraries used

1. Django
  - Django REST Framework
  - Django Channels
  - Simple JWT
  - Django signals
2. Vue.js
  - Vuex
  - Vue 3
  - Vue Router 
 ## Backend

Using Django as the backend server-side, it provides an API for managing users, posts, and messages.
Django REST Framework is used for view sets, handling API requests, and managing data, meanwhile Django Channels handles websocket connections, accessible from the native `WebSocket` JS class. Anytime a new message is created, Django Signals will take care of sending the message to the corresponding user(s) by way of class methods.

### API

- POST /auth/login/ - Basic Login Authentication. If correct credentials are provided, then it will return a JSON Web Token used for authentication in restricted endpoints.

- GET /users/ - Provides JSON serialization of all users, with any specific user being accessible at /users/<ID>

- GET /posts/ - Similar to /users/, it provides JSON serialization of all posts.

- POST /posts/ - When provided JWT as a Bearer authentication token, allows the user to create a post.

- WSCONNECT /ws/chat/ - Connects the client to a chat websocket, requiring that the user provides a valid token as a parameter (`/ws/chat/?token=<TOKEN>`)

## Frontend

The frontend is a Vue.js single page application that uses Vue router in order to provide a better user experience. Bootstrap is used as the primary CSS framework, with other JS libraries such as JQuery used for UI.
