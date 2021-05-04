<template>
  <div class="container">
    <div class="card text-white bg-danger mb-3">
      <div class="card-body">
        <h5 class="card-title">{{ $props.newPost.author.username }}</h5>
        <p class="card-text">{{ $props.newPost.body }}</p>
        <p class="like-number">{{ $props.newPost.likes }} likes</p>
        <i class="far fa-heart like" @click="like()" ref="heart"></i>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ShowPost",
  props: ["newPost"],
  methods: {
    like() {
      if (this.$store.state.auth) {
        /* user is authenticated */ let heart = this.$refs.heart;
        if (heart.className === "far fa-heart like" /* not liked yet */) {
          this.$props.newPost.likes++;
          heart.className = "fas fa-heart like";
        } else {
          this.$props.newPost.likes--;
          heart.className = "far fa-heart like";
        }
        axios("http://localhost:8000/posts/" + this.$props.newPost.id + "/", {
          method: "PUT",
          body: this.$store.state.username,
        });
        // update the like count, the server will do the rest
      } else {
        // user is not authenticated
        this.$router.push("/login");
      }
    },
  },
};
</script>
<style scoped>
.like {
  float: right;
  cursor: pointer;
}
.like-number {
  font-size: small;
}
.like-number-holder {
  width: auto;
}
</style>
