import { instance } from './http'

export function getMintingTweets(query, order = -1, offset = 0, limit = 10) {
  return instance.get(`
    /minting/tweets?query=${query}&order=${order}&offset=${offset}&limit=${limit}`)
}

export function putMintingTweetsFlag(id, flag) {
  return instance.put(`
    /minting/tweets/${id}?flag=${flag}
    `)
}

export function getMintingInfoByTid(tweetId) {
  return instance.get(`/minting/info/${tweetId}?filter=tweetId`)
}

export function getMintingInfoByOid(objectId) {
  return instance.get(`/minting/info/${objectId}?filter=_id`)
}

export function postMintingInfo(info) {
  return instance.post('/minting/info', info)
}
