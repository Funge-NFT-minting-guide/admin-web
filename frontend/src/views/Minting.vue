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
                <CTableRow v-for="(info, data) in minting" :key="data">
                  <MintingData
                    :tweetId="data.id"
                    :profileImageUrl="data.profile_image_url"
                    :projectName="data.user"
                    :tweetText="data.text"
                    :followers="data.followers"
                  />
                  <!--
                  <MintingInfo
                    :tweetId="minting.id"
                    :projectName="minting.user"
                  />
                  -->
                  <component
                    v-for="i in info"
                    :key="i.compId"
                    :is="i.comp"
                    :tweetId="i.tweetId"
                    :compId="i.compId"
                    @requestInfo="reqInfo"
                  />
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
  <div>{{ infoIndex }}</div>
</template>

<script>
import { getMintingTweets } from '@/api/minting'

export default {
  name: 'Minting',
  data() {
    return {
      infoIndex: [],
      mintingData: [],
      mintingInfo: [],
      minting: {},
    }
  },
  methods: {
    reqInfo(tid, cid) {
      var midx = this.mintingData.indexOf(
        this.mintingData.find((item) => item.id === tid),
      )
      if (!cid) {
        this.mintingInfo[midx].push({
          comp: 'MintingInfo',
          compId: ++this.infoIndex[midx],
          tweetId: tid,
        })
      } else {
        var idx = this.mintingInfo[midx].indexOf(
          this.mintingInfo[midx].find((item) => item.compId === cid),
        )
        this.mintingInfo[midx].splice(idx, 1)
      }
    },
  },
  created() {
    getMintingTweets().then((response) => (this.mintingData = response.data))
    this.infoIndex = new Array(this.mintingData.length).fill(0)
    this.mintingData.forEach((minting, index) => {
      this.mintingInfo.push([
        {
          comp: 'MintingInfo',
          compId: this.infoIndex[index],
          tweetId: minting.id,
        },
      ])
    })
    this.mintingData.forEach((k, i) => (this.minting[k] = this.mintingInfo[i]))
  },
  setup() {
    const progressData = [{ title: 'Processing', icon: 'cilCheck', value: 53 }]

    return {
      progressData,
    }
  },
}
</script>
