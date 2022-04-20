<template>
  <div>
    <CRow>
      <CCol :lg="12">
        <CCard class="mb-4">
          <CCardHeader> Guide </CCardHeader>
          <CCardBody>
            <CRow>
              <CCol :sm="12" :lg="12">
                <CTable border hover>
                  <CTableHead>
                    <CTableRow>
                      <CTableHeaderCell scope="col">Date</CTableHeaderCell>
                      <CTableHeaderCell scope="col">Title</CTableHeaderCell>
                      <CTableHeaderCell scope="col"></CTableHeaderCell>
                    </CTableRow>
                  </CTableHead>
                  <CTableBody>
                    <CTableRow>
                      <CTableHeaderCell scope="row">1</CTableHeaderCell>
                      <CTableDataCell>MarkAAAAAAAAAAA</CTableDataCell>
                      <CTableDataCell>Otto</CTableDataCell>
                    </CTableRow>
                  </CTableBody>
                </CTable>
              </CCol>
            </CRow>
            <CRow><br /></CRow>
            <CRow>
              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <CButton
                  color="primary"
                  class="me-md-2"
                  @click="addFAQModalVisible = true"
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
  <div v-show="addFAQModalVisible">
    <CModal :visible="addFAQModalVisible" @close="closeAddFAQModal">
      <CModalHeader>
        <CModalTitle>
          <CFormLabel for="question">Question</CFormLabel>
          <CFormInput id="question" v-model="newQuestion" />
        </CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CFormLabel for="answer"><h5>Answer</h5></CFormLabel>
        <CFormTextarea id="answer" v-model="newAnswer" />
      </CModalBody>
      <CModalFooter>
        <CButton color="secondary" @click="closeAddFAQModal"> Close </CButton>
        <CButton color="primary" @click="requestAddFAQ">Save changes</CButton>
      </CModalFooter>
    </CModal>
  </div>
  <div v-show="editFAQModalVisible">
    <CModal :visible="editFAQModalVisible" @close="editFAQModalVisible = false">
      <CModalHeader>
        <CModalTitle>
          <CFormLabel for="question">Question</CFormLabel>
          <CFormInput id="question" v-model="editQuestion" />
        </CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CFormLabel for="answer"><h5>Answer</h5></CFormLabel>
        <CFormTextarea id="answer" v-model="editAnswer" />
      </CModalBody>
      <CModalFooter>
        <CButton color="secondary" @click="editFAQModalVisible = false">
          Close
        </CButton>
        <CButton color="primary" @click="requestEditFAQ">Save changes</CButton>
      </CModalFooter>
    </CModal>
  </div>
</template>

<script>
export default {
  name: 'Guide',
  setup() {},
}
</script>
