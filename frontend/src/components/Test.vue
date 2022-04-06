<template>
  <CTable>
    <CTableBody>
      <CTableRow v-for="v in data" :key="v">
        <CTableCol>
          {{ v[0] }}
        </CTableCol>
        <CTableCol>
          {{ v[1].age }}
        </CTableCol>
        <CTableCol>
          {{ v[1].city }}
        </CTableCol>
      </CTableRow>
    </CTableBody>
  </CTable>
</template>

<script>
import { reactive } from 'vue'

export default {
  name: 'Test',

  setup() {
    const data = reactive(new Map())

    data.set('Jack', { age: 23, city: 'New York' })

    return {
      data,
    }
  },
}
</script>
