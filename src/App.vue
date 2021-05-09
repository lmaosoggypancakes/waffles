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
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <div class="container">
              <button
                class="btn btn-dark"
                ref="to"
                data-to="/all"
                @click="$router.push('/')"
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
                v-if="$store.state.auth"
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
                v-if="$store.state.auth"
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
            <svg
              id="to-dms"
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-chat-right-dots-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M16 2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h9.586a1 1 0 0 1 .707.293l2.853 2.853a.5.5 0 0 0 .854-.353V2zM5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"
              />
            </svg>
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
