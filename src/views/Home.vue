<template>
  <div class="container">
    <div class="row" style="margin-top: 10vh"></div>
    <div class="row">
      <div class="col-3">aaa</div>
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
// @ is an alias to /src
import ShowPost from "@/components/ShowPost.vue";
export default {
  name: "Home",
  components: { ShowPost },
  data() {
    return {
      posts: [
        {
          body: "Me and the boys",
          author: {
            username: "Josef",
            image: "/images/",
            first_name: "lmao",
          },
          timestamp: "October 12, 2021",
          likes: 0,
          id: 23,
        },
        {
          body: "Pogggers",
          author: {
            username: "Hercules",
            image: "/images/no",
            first_name: "hercules",
          },
          timestamp: "October 17, 2021",
          likes: 5,
          id: 50,
        },
      ],
    };
  },
};
</script>
<style>
.card {
  margin-bottom: 5em;
}
</style>
