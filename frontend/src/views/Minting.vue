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
                    :objectId="info.objectId"
                    :projectName="data.user"
                    :profileImageUrl="data.profile_image_url"
                    :followers="data.followers"
                    :url="data.url"
                    @requestInfo="reqInfo"
                    @requestSaveMintingInfo="reqDataButton"
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
  <CToaster placement="top-end">
    <CToast v-for="toast in toasts" :key="toast">
      <CToastHeader closeButton>
        <span class="me-auto fw-bold">{{ toast.title }}</span>
        <small>1 sec ago</small>
      </CToastHeader>
      <CToastBody>
        {{ toast.content }}
      </CToastBody>
    </CToast>
  </CToaster>
</template>

<script>
import { ref } from 'vue'
import {
  getMintingTweets,
  putMintingTweetsFlag,
  getMintingInfoByTid,
} from '@/api/minting'

export default {
  name: 'Minting',
  setup() {
    const progressData = [{ title: 'Processing', icon: 'cilCheck', value: 53 }]
    const mintingData = ref([])
    const mintingInfo = ref([])
    const toasts = ref([])
    let offset = 0
    let infoIndex = []
    const loadData = async ($state) => {
      try {
        const response = await getMintingTweets(
          JSON.stringify({ processed: false, invalid: false, outdated: false }),
          -1,
          offset,
        )
        if (response.data.length === 0) $state.complete()
        else {
          await mintingData.value.push(...response.data)
          await initMintingInfo(offset)
          await $state.loaded()
        }
        offset += response.data.length
      } catch (error) {
        $state.error()
      }
    }
    const initMintingInfo = (dataOffset) => {
      mintingData.value.slice(dataOffset).forEach((minting, index) => {
        infoIndex.push(-1)
        getMintingInfoByTid(minting.id)
          .then((response) => {
            mintingInfo.value.push([])
            for (var info of response.data) {
              mintingInfo.value[index + dataOffset].push({
                comp: 'MintingInfo',
                compId: ++infoIndex[index + dataOffset],
                tweetId: minting.id,
                objectId: info._id.$oid,
              })
            }
          })
          .catch((error) => {
            if (error.response.status == 404) {
              mintingInfo.value.push([
                {
                  comp: 'MintingInfo',
                  compId: ++infoIndex[index + dataOffset],
                  tweetId: minting.id,
                  objectId: null,
                },
              ])
            }
          })
      })
    }
    const creatToast = (title, content) => {
      toasts.value.push({
        title: title,
        content: content,
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
          objectId: null,
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
      let midx = mintingData.value.indexOf(
        mintingData.value.find((item) => item.id === tid),
      )
      putMintingTweetsFlag(tid, bid)
      mintingData.value.splice(midx, 1)
      mintingInfo.value.splice(midx, 1)
      infoIndex.splice(midx, 1)
      offset -= 1
      if (bid == 'processed') {
        creatToast('Notification', 'Successfully saved.')
      }
    }
    return {
      progressData,
      mintingData,
      mintingInfo,
      toasts,
      loadData,
      reqInfo,
      reqDataButton,
    }
  },
}
</script>
