<template>
  <div class="mf" :style="{ display: show }">
    <div class="container bg text-white text-center">
      <div class="row">
        <h1>{{ msg }}</h1>
      </div>
      <div class="row">
        <button class="btn btn-dark" @click="$router.push('/')">OK</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  props: ["show", "msg"],
  watch: {
    show: function (e) {
      console.log(e);
    },
  },
};
</script>

<style scoped>
.mf {
  border-radius: 10px;
  position: fixed;
  bottom: 30vh;
  left: 0;
  right: 0;
  z-index: 100;
}
.container {
  border-radius: 5em;
  height: 30vh;
}
.btn {
  margin-top: 3em;
  margin-left: auto;
  margin-right: auto;
  width: 25%;
}
.bg {
  background-color: #b02d3a;
}
</style>
