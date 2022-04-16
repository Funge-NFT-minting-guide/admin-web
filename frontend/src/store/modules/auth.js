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
  requestLogin({ commit }, payload) {
    login(payload)
      .then(async (response) => {
        if (response.status === 200) {
          await commit('setAuthStatus', true)
        }
      })
      .catch(() => {
        commit('setAuthStatus', false)
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
