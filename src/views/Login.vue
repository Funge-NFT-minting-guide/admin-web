<template>
  <div class="bg-light min-vh-100 d-flex flex-row align-items-center">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol :md="8">
          <CCardGroup>
            <CCard class="p-4">
              <CCardBody>
                <h1>Login</h1>
                <p class="text-medium-emphasis">Sign In to your account</p>
                <CInputGroup class="mb-3">
                  <CInputGroupText>
                    <CIcon icon="cil-user" />
                  </CInputGroupText>
                  <CFormInput
                    v-model="username"
                    placeholder="Username"
                    autocomplete="username"
                  />
                </CInputGroup>
                <CInputGroup class="mb-4">
                  <CInputGroupText>
                    <CIcon icon="cil-lock-locked" />
                  </CInputGroupText>
                  <CFormInput
                    v-model="password"
                    type="password"
                    placeholder="Password"
                    autocomplete="current-password"
                  />
                </CInputGroup>
                <CRow>
                  <CCol :xs="6">
                    <CButton color="primary" class="px-4" @click="reqLogin">
                      Login
                    </CButton>
                  </CCol>
                </CRow>
              </CCardBody>
            </CCard>
          </CCardGroup>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
//import { useRouter } from 'vue-router'
import { login } from '@/api/auth'

export default {
  name: 'Login',

  setup() {
    const username = ref()
    const password = ref()
    const store = useStore()
    //const router = useRouter()

    const reqLogin = () => {
      let loginInfo = { username: username.value, password: password.value }
      login(loginInfo)
        .then(async (response) => {
          if (response.status === 200) {
            store.commit('setAuthStatus', true, { root: true })
            //router.push('/dashboard')
            location.href = '/dashboard'
          }
        })
        .catch(() => {
          alert('Login failed.')
        })
    }

    return {
      username,
      password,
      reqLogin,
    }
  },
}
</script>
