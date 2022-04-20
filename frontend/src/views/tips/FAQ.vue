<template>
  <div>
    <CRow>
      <CCol :lg="12">
        <CCard class="mb-4">
          <CCardHeader> FAQ </CCardHeader>
          <CCardBody>
            <CRow v-for="faq in faqList" :key="faq._id">
              <CCol :sm="12" :lg="12">
                <CAccordion>
                  <CAccordionItem :item-key="1">
                    <CAccordionHeader> {{ faq.question }} </CAccordionHeader>
                    <CAccordionBody>
                      <div>
                        <CCard>
                          <CCardBody>
                            {{ faq.answer }}
                          </CCardBody>
                        </CCard>
                      </div>
                      <div><br /></div>
                      <div
                        class="d-grid gap-2 d-md-flex justify-content-md-end"
                      >
                        <CButton
                          color="primary"
                          class="me-md-2"
                          @click="openEditFAQModal(faq._id)"
                        >
                          Edit
                        </CButton>
                        <CButton
                          color="danger"
                          class="me-md-2"
                          @click="requestDeleteFAQ(faq._id)"
                        >
                          Delete
                        </CButton>
                      </div>
                    </CAccordionBody>
                  </CAccordionItem>
                </CAccordion>
                <br />
              </CCol>
            </CRow>
            <infinite-loading @infinite="loadData" />
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
import { ref, reactive } from 'vue'
import { getFAQ, postFAQ, putFAQ, deleteFAQ } from '@/api/tips'

export default {
  name: 'FAQ',
  setup() {
    const addFAQModalVisible = ref(false)
    const editFAQModalVisible = ref(false)
    const faqList = reactive(new Array())
    const newQuestion = ref()
    const newAnswer = ref()
    const editOid = ref()
    const editQuestion = ref()
    const editAnswer = ref()
    let offset = 0

    const getFAQbyOid = (oid) => {
      return faqList.find((item) => item._id == oid)
    }

    const getOffsetOfFaqByOid = (oid) => {
      return faqList.indexOf(getFAQbyOid(oid))
    }

    const loadData = async ($state) => {
      try {
        const response = await getFAQ(offset)

        if (response.data.length === 0) $state.complete()
        else {
          faqList.push(...response.data)
          offset += response.data.length
        }

        await $state.loaded()
      } catch (error) {
        console.log(error)
      }
    }

    const closeAddFAQModal = () => {
      newQuestion.value = ''
      newAnswer.value = ''
      addFAQModalVisible.value = false
    }

    const requestAddFAQ = async () => {
      let faq = { question: newQuestion.value, answer: newAnswer.value }
      await postFAQ(faq)
      newQuestion.value = ''
      newAnswer.value = ''
      addFAQModalVisible.value = false
      loadData()
    }

    const openEditFAQModal = (oid) => {
      let faq = getFAQbyOid(oid)

      editOid.value = faq._id
      editQuestion.value = faq.question
      editAnswer.value = faq.answer
      editFAQModalVisible.value = true
    }

    const requestEditFAQ = () => {
      let idx = getOffsetOfFaqByOid(editOid.value)
      faqList[idx].question = editQuestion.value
      faqList[idx].answer = editAnswer.value
      putFAQ(faqList[idx])
      editFAQModalVisible.value = false
    }

    const requestDeleteFAQ = (oid) => {
      let idx = getOffsetOfFaqByOid(oid)
      faqList.splice(idx, 1)
      deleteFAQ(oid)
      offset -= 1
    }

    return {
      addFAQModalVisible,
      editFAQModalVisible,
      openEditFAQModal,
      closeAddFAQModal,
      requestAddFAQ,
      requestEditFAQ,
      requestDeleteFAQ,
      newQuestion,
      newAnswer,
      editQuestion,
      editAnswer,
      loadData,
      faqList,
    }
  },
}
</script>
