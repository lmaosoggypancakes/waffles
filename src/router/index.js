import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import New from "../views/New.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/new",
    name: "New",
    component: New,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
