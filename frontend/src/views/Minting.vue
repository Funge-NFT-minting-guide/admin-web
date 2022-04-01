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
                <CTableRow v-for="(data, index) in mintingData" :key="data.id">
                  <MintingData
                    :tweetId="data.id"
                    :profileImageUrl="data.profile_image_url"
                    :projectName="data.user"
                    :tweetText="data.text"
                    :followers="data.followers"
                    @requestDataButton="reqDataButton"
                  />
                  <!--
                  <MintingInfo
                    :tweetId="minting.id"
                    :projectName="minting.user"
                  />
                  -->
                  <component
                    v-for="info in mintingInfo[index]"
                    :key="info.compId"
                    :is="info.comp"
                    :tweetId="info.tweetId"
                    :compId="info.compId"
                    @requestInfo="reqInfo"
                  />
                </CTableRow>
              </CTableBody>
            </CTable>
            <infinite-loading @infinite="loadData" />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import { ref } from 'vue'
import { getMintingTweets } from '@/api/minting'

export default {
  name: 'Minting',
  setup() {
    const progressData = [{ title: 'Processing', icon: 'cilCheck', value: 53 }]
    const mintingData = ref([])
    const mintingInfo = ref([])
    let offset = 0
    let infoIndex = []
    const loadData = async ($state) => {
      try {
        const response = await getMintingTweets(
          { processed: false },
          -1,
          offset,
        )
        if (response.data.length === 0) $state.complete()
        else {
          mintingData.value.push(...response.data)
          initMintingInfo(offset)
          $state.loaded()
        }
        offset += response.data.length
      } catch (error) {
        $state.error()
      }
    }
    const initMintingInfo = (dataOffset) => {
      mintingData.value.slice(dataOffset).forEach((minting, index) => {
        infoIndex.push(-1)
        mintingInfo.value.push([
          {
            comp: 'MintingInfo',
            compId: ++infoIndex[index + dataOffset],
            tweetId: minting.id,
          },
        ])
      })
    }
    const reqInfo = (tid, cid) => {
      let midx = mintingData.value.indexOf(
        mintingData.value.find((item) => item.id === tid),
      )
      if (!cid) {
        mintingInfo.value[midx].push({
          comp: 'MintingInfo',
          compId: ++infoIndex[midx],
          tweetId: tid,
        })
        console.log(infoIndex[midx])
      } else {
        let idx = mintingInfo.value[midx].indexOf(
          mintingInfo.value[midx].find((item) => item.compId === cid),
        )
        mintingInfo.value[midx].splice(idx, 1)
      }
    }
    const reqDataButton = (tid, bid) => {
      console.log(bid)
      let midx = mintingData.value.indexOf(
        mintingData.value.find((item) => item.id === tid),
      )
      // TODO: connect to api
      mintingData.value.splice(midx, 1)
      mintingInfo.value.splice(midx, 1)
      infoIndex.splice(midx, 1)
      offset - 1
    }
    return {
      progressData,
      mintingData,
      mintingInfo,
      loadData,
      reqInfo,
      reqDataButton,
    }
  },
}
</script>
