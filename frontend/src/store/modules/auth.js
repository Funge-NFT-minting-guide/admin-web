import { login } from '@/api/auth'

const state = () => ({
  isAuth: false,
})

const mutations = {
  setAuthStatus(state, flag) {
    state.isAuth = flag
  },
}

const actions = {
  async requestLogin({ commit }, payload) {
    await login(payload)
      .then((response) => {
        if (response && response.data) {
          localStorage.setItem('isAuthenticated', true)
          commit('setAuthStatus', true)
        } else {
          commit('setAuthStatus', false)
        }
      })
      .catch((err) => {
        console.log(err)
      })
  },
}

const getters = {
  getAuthStatus(state) {
    return state.isAuth
  },
}

export default {
  namespased: true,
  state,
  mutations,
  actions,
  getters,
}
