import { createStore } from "vuex";

export default createStore({
  state: {
    auth: false,
    token: undefined,
  },
  mutations: {
    set_token(state, token) {
      console.log(token);
      state.token = token;
    },
  },
  actions: {
    set_token(ctx, token) {
      ctx.commit("set_token", token);
    },
  },
  modules: {},
});
