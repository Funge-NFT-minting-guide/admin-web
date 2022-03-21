<template>
  <span>test1!</span>
  <div v-for="data in test" :key="data.id">{{ data.text }}</div>
</template>

<script>
import http from './api'

export default {
  name: 'Test',
  data() {
    return {
      test: [],
    }
  },

  created() {
    http
      .get('/minting')
      .then((response) => (this.test = response.data))
      .catch((error) => {
        console.log(error)
      })
  },
}
</script>
