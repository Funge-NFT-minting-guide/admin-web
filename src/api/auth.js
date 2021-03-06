import { instance } from './http'

export function login(loginInfo) {
  return instance.post(`/admin/signin`, loginInfo, {
    headers: { 'Content-Type': 'application/json' },
    withCredetials: true,
    credentials: 'include',
  })
}

export function logout() {
  return instance.get('/admin/signout')
}

export function prot() {
  return instance.get('/admin/protected')
}
