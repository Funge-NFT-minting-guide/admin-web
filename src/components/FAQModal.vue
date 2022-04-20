<template>
  <CModal>
    <CModalHeader>
      <CModalTitle>
        <CFormFloating>
          <CFormInput id="question" />
          <CFormLabel for="question">Question</CFormLabel>
        </CFormFloating>
      </CModalTitle>
    </CModalHeader>
    <CModalBody>
      <CFormTextarea placeholder="Answer" />
    </CModalBody>
    <CModalFooter>
      <CButton
        color="secondary"
        @click="
          () => {
            addFAQModalVisible = false
          }
        "
      >
        Close
      </CButton>
      <CButton color="primary">Save changes</CButton>
    </CModalFooter>
  </CModal>
</template>

<script>
import { ref } from 'vue'
export default {
  name: 'FAQModal',
  setup() {
    const modalVisible = ref(true)

    return {
      modalVisible,
    }
  },
}
</script>
