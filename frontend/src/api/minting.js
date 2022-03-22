import { instance } from './http'

function getMintingTweets(order = -1, offset = 0, limit = 10) {
  return instance.get(`
    /minting/tweets?order=${order}&offset=${offset}&limit=${limit}`)
}

export { getMintingTweets }
