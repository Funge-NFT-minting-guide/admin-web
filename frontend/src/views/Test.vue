<template>
  <div>{{ p() }}</div>
</template>

<script>
import { prot } from '@/api/auth'

export default {
  name: 'Test',

  methods: {
    p: async () => {
      let r = await prot()
      console.log(r.data)
    },
  },
}
</script>
