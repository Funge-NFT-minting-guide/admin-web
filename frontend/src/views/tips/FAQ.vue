<template>
  <div>
    <CRow>
      <CCol :lg="12">
        <CCard class="mb-4">
          <CCardHeader> FAQ </CCardHeader>
          <CCardBody>
            <CRow>
              <CCol :sm="12" :lg="12">
                <CAccordion>
                  <CAccordionItem :item-key="1">
                    <CAccordionHeader> Accordion Item #1 </CAccordionHeader>
                    <CAccordionBody>
                      <div>
                        <CCard>
                          <CCardBody>
                            This is some text within a card body.
                          </CCardBody>
                        </CCard>
                      </div>
                      <div><br /></div>
                      <div
                        class="d-grid gap-2 d-md-flex justify-content-md-end"
                      >
                        <CButton color="primary" class="me-md-2">Edit</CButton>
                        <CButton color="primary" class="me-md-2">
                          Delete
                        </CButton>
                      </div>
                    </CAccordionBody>
                  </CAccordionItem>
                </CAccordion>
              </CCol>
            </CRow>
            <CRow><br /></CRow>
            <CRow>
              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <CButton
                  color="primary"
                  class="me-md-2"
                  @click="
                    () => {
                      addFAQModalVisible = true
                    }
                  "
                >
                  Add
                </CButton>
              </div>
            </CRow>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
  <CModal
    :visible="addFAQModalVisible"
    @close="
      () => {
        addFAQModalVisible = false
      }
    "
  >
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
  name: 'FAQ',
  setup() {
    const addFAQModalVisible = ref(false)

    return {
      addFAQModalVisible,
    }
  },
}
</script>
