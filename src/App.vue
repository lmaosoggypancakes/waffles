<template>
  <nav class="navbar navbar-expand-lg navbar-danger bg-danger">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="./assets/waffles.png" height="100" width="100" />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="$store.state.auth">
          <li class="nav-item">
            <div class="container">
              <button
                class="btn btn-dark"
                ref="to"
                data-to="/all"
                @click="$router.push('/all')"
              >
                All Posts
              </button>
            </div>
          </li>
          <li class="nav-item">
            <div class="container">
              <button
                class="btn btn-dark"
                ref="to"
                data-to="/freinds"
                @click="$router.push('/freinds')"
              >
                Freinds
              </button>
            </div>
          </li>
          <li class="nav-item">
            <div class="container">
              <button
                class="btn btn-dark"
                ref="to"
                data-to="/new"
                @click="$router.push('/new')"
              >
                New Post
              </button>
            </div>
          </li>
        </ul>
        <div class="d-flex">
          <div class="container">
            <button
              class="btn btn-dark"
              ref="to"
              data-to="/login"
              @click="$router.push('/login')"
            >
              Login
            </button>
          </div>
          <div class="container">
            <button
              class="btn btn-dark"
              ref="to"
              data-to="/register"
              @click="$router.push('/register')"
            >
              Register
            </button>
          </div>
          <div
            class="container"
            ref="to"
            data-to="/message"
            @click="$router.push('/message')"
          >
            <img
              src="./assets/message.png"
              height="50"
              width="50"
              id="to-dms"
            />
          </div>
        </div>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
body {
  background-color: #171717;
}
.row {
  width: 100%;
}
#to-dms {
  cursor: pointer;
}
</style>
<script>
export default {
  name: "App",
  mounted() {},
};
</script>
