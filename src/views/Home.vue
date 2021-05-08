<template>
  <div class="container">
    <div class="row" style="margin-top: 10vh"></div>
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6">
        <show-post
          v-for="post in posts"
          :key="post"
          :newPost="post"
        ></show-post>
      </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
import ShowPost from "@/components/ShowPost.vue";
export default {
  name: "Home",
  components: { ShowPost },
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    axios.get("http://localhost:8000/posts/").then((res) => {
      this.posts = res.data;
    });
  },
};
</script>
<style>
.card {
  margin-bottom: 5em;
}
</style>
