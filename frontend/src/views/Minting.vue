<template>
  <div>
    <CRow>
      <CCol :lg="auto">
        <CCard class="mb-4">
          <CCardHeader> Minting Information </CCardHeader>
          <CCardBody>
            <CRow>
              <CCol :sm="12" :lg="12">
                <CRow>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-info py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Total Tweets</div>
                      <div class="fs-5 fw-semibold">9,123</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-danger py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Minting Data</div>
                      <div class="fs-5 fw-semibold">22,643</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-success py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Minting Info</div>
                      <div class="fs-5 fw-semibold">9,123</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-warning py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Today</div>
                      <div class="fs-5 fw-semibold">22,643</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-warning py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">This Week</div>
                      <div class="fs-5 fw-semibold"><Test /></div>
                    </div>
                  </CCol>
                </CRow>
                <hr class="mt-0" />
                <div
                  v-for="item in progressData"
                  :key="item.title"
                  class="progress-group"
                >
                  <div class="progress-group-header">
                    <CIcon :icon="item.icon" class="me-2" size="lg" />
                    <span class="title">{{ item.title }}</span>
                    <span class="ms-auto fw-semibold">{{ item.value }}%</span>
                  </div>
                  <div class="progress-group-bars">
                    <CProgress thin :value="item.value" color="success" />
                  </div>
                </div>
              </CCol>
            </CRow>
            <br />
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableBody>
                <CTableRow>
                  <CTableDataCell>
                    <CFormCheck disabled />
                  </CTableDataCell>
                  <CTableDataCell>
                    <CAvatar
                      size="xl"
                      src="https://pbs.twimg.com/profile_images/1475512050294362114/Dj4uIk2k_normal.jpg"
                    />
                  </CTableDataCell>
                  <CTableDataCell>
                    <CInputGroup class="flex-nowrap">
                      <CInputGroupText id="addon-wrapping">@</CInputGroupText>
                      <CFormInput
                        placeholder="MetaKongz"
                        aria-label="Username"
                        disabled
                      />
                    </CInputGroup>
                    <CInputGroup class="flex-nowrap">
                      <CInputGroupText>Origin</CInputGroupText>
                      <CFormTextarea v-model="message" disabled></CFormTextarea>
                    </CInputGroup>
                  </CTableDataCell>
                  <CTableDataCell>
                    <CIcon :icon="cilClone" size="xxl" />
                  </CTableDataCell>
                  <MintingInfo />
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import { cilClone } from '@coreui/icons'
import MintingInfo from '@/components/MintingInfo.vue'

export default {
  name: 'Dashboard',
  setup() {
    const progressData = [{ title: 'Processing', icon: 'cilCheck', value: 53 }]

    return {
      MintingInfo,
      progressData,
      message: 'test',
      cilClone,
    }
  },
}
</script>
