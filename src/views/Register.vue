<template>
  <div class="container">
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6 text-white bg-danger">
        <h3 class="text-center">Register</h3>
        <form
          @submit.prevent="register"
          autocomplete="off"
          aria-autocomplete="off"
          ref="reg_form"
        >
          <div class="form-group">
            <div class="input-group input">
              <span class="input-group-text">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-person-fill"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
                  />
                </svg>
              </span>
              <input
                type="text"
                class="form-control"
                placeholder="Username"
                v-model="username"
              />
            </div>
            <div class="input-group input">
              <span class="input-group-text">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-envelope"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2zm13 2.383-4.758 2.855L15 11.114v-5.73zm-.034 6.878L9.271 8.82 8 9.583 6.728 8.82l-5.694 3.44A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.739zM1 11.114l4.758-2.876L1 5.383v5.73z"
                  ></path>
                </svg>
              </span>
              <input
                type="text"
                class="form-control"
                placeholder="Email Address"
                v-model="email"
              />
            </div>
            <div class="input-group input">
              <span class="input-group-text">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-key"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M0 8a4 4 0 0 1 7.465-2H14a.5.5 0 0 1 .354.146l1.5 1.5a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0L13 9.207l-.646.647a.5.5 0 0 1-.708 0L11 9.207l-.646.647a.5.5 0 0 1-.708 0L9 9.207l-.646.647A.5.5 0 0 1 8 10h-.535A4 4 0 0 1 0 8zm4-3a3 3 0 1 0 2.712 4.285A.5.5 0 0 1 7.163 9h.63l.853-.854a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.793-.793-1-1h-6.63a.5.5 0 0 1-.451-.285A3 3 0 0 0 4 5z"
                  />
                  <path d="M4 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
                </svg>
              </span>
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                v-model="p1"
              />
            </div>
            <div class="input-group input">
              <span class="input-group-text">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-key"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M0 8a4 4 0 0 1 7.465-2H14a.5.5 0 0 1 .354.146l1.5 1.5a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0L13 9.207l-.646.647a.5.5 0 0 1-.708 0L11 9.207l-.646.647a.5.5 0 0 1-.708 0L9 9.207l-.646.647A.5.5 0 0 1 8 10h-.535A4 4 0 0 1 0 8zm4-3a3 3 0 1 0 2.712 4.285A.5.5 0 0 1 7.163 9h.63l.853-.854a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.793-.793-1-1h-6.63a.5.5 0 0 1-.451-.285A3 3 0 0 0 4 5z"
                  />
                  <path d="M4 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
                </svg>
              </span>
              <input
                type="password"
                class="form-control"
                placeholder="Confirm"
                v-model="p2"
              />
            </div>
          </div>
          <button class="btn btn-dark" type="submit">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      p1: "",
      p2: "",
      email: "",
    };
  },
  methods: {
    register() {
      if (this.p1 === this.p2) {
        axios
          .post("http://localhost:8000/users/", {
            username: this.username,
            password: this.p1,
            email: this.email,
          })
          .then((res) => alert(res.data));
      } else {
        alert("Passwords must match!");
      }
    },
  },
};
</script>

<style scoped>
.input {
  margin-bottom: 2em;
}
h3 {
  margin-bottom: 1em;
}
</style>
