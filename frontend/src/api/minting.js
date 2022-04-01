import { instance } from './http'

function getMintingTweets(query, order = -1, offset = 0, limit = 10) {
  return instance.get(`
    /minting/tweets?query=${query}&order=${order}&offset=${offset}&limit=${limit}`)
}

function putMintingTweetsFlag(id, flag) {
  return instance.put(`
    /minting/tweets/${id}?flag=${flag}
    `)
}

export { getMintingTweets, putMintingTweetsFlag }
