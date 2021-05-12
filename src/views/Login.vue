<template>
  <div class="container">
    <success :show="show" msg="You have been logged in!"></success>
    <div class="row">
      <div class="col-3"></div>
      <div class="text-white bg-danger col-6">
        <h3 class="text-center">Login</h3>
        <form @submit.prevent="login" autocomplete="off" ref="form">
          <div class="form-group">
            <label for="username" ref="label-username" class="label-username"
              >Username</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              id="username-l"
              v-model="username"
              @click="update('username')"
              ref="username"
              @keydown="next"
              autofocus
            />
            <label for="password" ref="label-password" class="label-password"
              >Password</label
            >
            <input
              type="password"
              class="form-control form-control-sm"
              id="password-l"
              v-model="password"
              @click="update('password')"
              ref="password"
              @keydown="gotosubmit"
            />
          </div>
        </form>
        <div class="container">
          <button
            class="btn btn-dark login-submit"
            ref="submit"
            @click="login"
            :disabled="!(username && password)"
          >
            Login
          </button>
        </div>
      </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Success from "../components/Popup";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      show: "none",
    };
  },
  components: {
    Success,
  },
  methods: {
    login() {
      // loading symbol!.
      var form = this.$refs.form;
      var elements = form.elements;
      for (var i = 0, len = elements.length; i < len; ++i) {
        elements[i].disabled = true;
        elements[i].style.cursor = "not-allowed";
      }
      this.$refs.submit.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>`;
      axios("http://127.0.0.1:8000/auth/login/", {
        method: "POST",
        data: {
          username: this.username,
          password: this.password,
        },
      })
        .then((res) => {
          this.$store.state.auth = true;
          console.log(res.data);
          this.$store.commit("set_token", res.data.access);
          this.show = "block";
          // this.$router.push("/");
        })
        .catch(() => {
          // err
          alert("username and password combo don't match :(");
          this.$refs.submit.innerHTML = "Login";
          for (var i = 0, len = elements.length; i < len; ++i) {
            elements[i].disabled = false;
            elements[i].style.cursor = "initial";
          }
        });
    },
    update(name) {
      event.target.classList = "form-control form-control-lg";
      if (name === "username") {
        this.$refs["password"].classList = "form-control";
        this.$refs["label-username"].style.fontSize = "2em";
        this.$refs["label-password"].style.fontSize = "1em";
      } else if (name === "password") {
        this.$refs["username"].classList = "form-control";
        this.$refs["label-password"].style.fontSize = "2em";
        this.$refs["label-username"].style.fontSize = "1em";
      }
    },
    updateShow() {
      if (this.show === "block") this.show = "none";
      else this.show = "block";
    },
    next() {
      if (event.keyCode === 13 || event.keyCode === 9) {
        this.update("password");
        this.$refs["password"].focus();
      }
    },
    gotosubmit() {
      if (event.keyCode === 13) {
        this.login();
      }
    },
  },
};
</script>

<style>
.col-6.bg-danger {
  margin-top: 5em;
  padding: 3em;
  border-radius: 5px;
}
#username-l,
#password-l {
  margin-bottom: 2em;
  transition: all 250ms;
}
.label-username,
.label-password {
  transition: all 250ms;
}
.login-submit {
  margin: auto;
  margin-top: 5em;
  display: block;
  width: 50%;
  text-align: center;
}
</style>
