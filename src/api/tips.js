import { instance } from './http'

export function getFAQ(offset) {
  return instance.get(`/tips/faq?offset=${offset}`)
}

export function postFAQ(faq) {
  return instance.post('/tips/faq', faq)
}

export function putFAQ(faq) {
  return instance.put('/tips/faq', faq)
}

export function deleteFAQ(oid) {
  return instance.delete(`/tips/faq/${oid}`)
}
