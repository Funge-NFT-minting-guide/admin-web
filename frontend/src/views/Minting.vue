<template>
  <div>
    <CRow>
      <CCol :lg="12">
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
                      <div class="fs-5 fw-semibold">123</div>
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
            <CTable
              align="middle"
              class="mb-0 border"
              style="width: 100%"
              hover
              responsive
            >
              <CTableBody>
                <CTableRow v-for="minting in mintingData" :key="minting.id">
                  <MintingData
                    :tweetId="minting.id"
                    :profileImageUrl="minting.profile_image_url"
                    :projectName="minting.user"
                    :tweetText="minting.text"
                  />
                  <MintingInfo
                    :tweetId="minting.id"
                    :projectName="minting.user"
                  />
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
import { getMintingTweets } from '@/api/minting'

export default {
  name: 'Minting',
  data() {
    return {
      mintingData: [],
    }
  },

  created() {
    getMintingTweets().then((response) => (this.mintingData = response.data))
  },

  setup() {
    const progressData = [{ title: 'Processing', icon: 'cilCheck', value: 53 }]

    return {
      progressData,
    }
  },
}
</script>
