<template>
  <div class="container">
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6 text-white bg-danger">
        <h3 class="text-center">What's on your mind?</h3>
        <form @submit.prevent="post" autocomplete="off" ref="post_form">
          <div class="form-group">
            <textarea
              id="body"
              cols="30"
              rows="10"
              class="form-control"
              v-model="body"
            ></textarea>
          </div>
        </form>
        <button class="btn btn-dark" @click="sub">Submit</button>
      </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "New",
  data() {
    return {
      body: "",
    };
  },
  methods: {
    sub() {
      console.log(`Bearer ${this.$store.state.token}`);
      axios
        .post(
          "http://localhost:8000/posts/",
          {
            body: this.body,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.token}`,
            },
          }
        )
        .then(() => {
          alert("Your post has been saved!");
          this.$router.push("/");
        });
    },
  },
  mounted() {
    if (!this.$store.state.auth) {
      this.$router.push("/");
    }
  },
};
</script>

<style scoped>
#body {
  margin-top: 2em;
}
</style>
