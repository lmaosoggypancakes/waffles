<template>
  <div class="container">
    <div class="row">
      <div class="col-3">
        <div class="friends bg-danger text-white">
          <div class="user" v-for="user in freinds" :key="user">
            <div class="row">
              <button class="btn btn-dark" @click="set_current(user.username)">
                {{ user.username
                }}<span :ref="user.username" class="badge badge-info"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="col-6 bg-danger text-white main">
        <h3 class="text-center">{{ current }}</h3>
        <div class="container bg-dark">
          <ul class="list-group list-group-flush messages" ref="messages">
            <li
              class="list-group-item message"
              v-for="message in messages"
              :key="message"
              v-html="message"
            ></li>
          </ul>
          <input
            type="text"
            class="form-control"
            @keydown="update"
            v-model="new_msg"
          />
        </div>
      </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Message",
  data: () => {
    return {
      freinds: [],
      ws: undefined,
      body: "",
      to: "hercules",
      current: undefined,
      messages: [],
      new_msg: "",
    };
  },
  components: {},
  methods: {
    send_message() {
      if (this.ws) {
        /* websocket must be initiated first */
        this.ws.send(
          JSON.stringify({
            to: this.to,
            body: this.body,
          })
        );
      }
    },
    set_current(username) {
      this.current = username;
      this.messages = [];
      /* clear all messages of past DM's, and alerts if any */
      this.$refs[username].innerHTML = "";
    },
    update(e) {
      if (e.keyCode === 13) {
        if (this.new_msg && this.current) {
          this.ws.send(
            JSON.stringify({
              body: this.new_msg,
              to: this.current,
            })
          );
          this.messages.push(this.new_msg);
          this.new_msg = "";
          // scroll to bottom
          setTimeout(() => {
            document
              .querySelector(".messages")
              .lastElementChild.scrollIntoView(false);
          }, 1000);
        }
      }
    },
  },
  async mounted() {
    if (!this.$store.state.auth) {
      this.$router.push("/");
    }
    this.ws = new WebSocket(
      "ws://localhost:8000/ws/chat/?token=" + this.$store.state.token
    );
    this.ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      const new_message = `<strong>${data.body}</strong> from ${data.from.username} <p style="float: right;">${data.timestamp}</p>`;
      if (this.current === data.from.username) {
        this.messages.push(new_message);
      } else {
        this.$refs[data.from.username].innerHTML = "!";
      }
    };
    let data = await axios.get("http://localhost:8000/friends/", {
      headers: {
        authorization: `Bearer ${this.$store.state.token}`,
      },
    });
    this.freinds = data.data;
    console.log(this.freinds);
  },
};
</script>

<style scoped>
.bg-danger {
  margin-top: 5em;
  padding: 2em;
  border-radius: 5px;
  width: 50%;
}
.row,
.container,
#app {
  height: 100%;
}
textarea {
  width: 100%;
  padding: 2em;
}
input {
  width: 100%;
  margin-top: auto;
}
.message {
  padding: 1em;
  margin-bottom: 1em;
  margin-top: 1em;
  border-radius: 20px;
  background-color: #dc3545;
  color: white;
}
.messages {
  height: 50vh;
  overflow-y: auto;
}
</style>
