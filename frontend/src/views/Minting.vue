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
                      <div class="fs-5 fw-semibold">
                        {{ totalTweets }}
                      </div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-danger py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Minting Data</div>
                      <div class="fs-5 fw-semibold">{{ totalData }}</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-success py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Minting Info</div>
                      <div class="fs-5 fw-semibold">{{ totalInfo }}</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-warning py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">Today</div>
                      <div class="fs-5 fw-semibold">{{ todayInfo }}</div>
                    </div>
                  </CCol>
                  <CCol>
                    <div
                      class="border-start border-start-4 border-start-warning py-1 px-3 mb-3"
                    >
                      <div class="text-medium-emphasis small">This Week</div>
                      <div class="fs-5 fw-semibold">{{ weekInfo }}</div>
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
                <CTableRow v-for="data in mintingMap" :key="data[0]">
                  <MintingData
                    :tweetId="data[1].mintingData.id"
                    :profileImageUrl="data[1].mintingData.profile_image_url"
                    :projectName="data[1].mintingData.user"
                    :tweetText="data[1].mintingData.text"
                    :followers="data[1].mintingData.followers"
                    @requestDataButton="reqDataButton"
                  />
                  <!--
                  <MintingInfo
                    :tweetId="minting.id"
                    :projectName="minting.user"
                  />
                  -->
                  <component
                    v-for="info in data[1].mintingInfo"
                    :key="info.compId"
                    :is="info.comp"
                    :tweetId="info.tweetId"
                    :compId="info.compId"
                    :objectId="info.objectId"
                    :projectName="data[1].mintingData.user"
                    :profileImageUrl="data[1].mintingData.profile_image_url"
                    :followers="data[1].mintingData.followers"
                    :url="data[1].mintingData.url"
                    @requestInfo="reqInfo"
                    @requestSaveMintingInfo="reqSaveButton"
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
import { ref, reactive, watch, computed } from 'vue'
import {
  getMintingTweets,
  getMintingDataTotal,
  getMintingInfoTotal,
  getMintingInfoByTid,
  putMintingTweetsFlag,
  getMintingTweetsTotal,
  getMintingInfoTotalDate,
} from '@/api/minting'

export default {
  name: 'Minting',
  setup() {
    const mintingMap = reactive(new Map())
    const toasts = ref([])
    const totalTweets = ref()
    const totalData = ref()
    const totalInfo = ref()
    const todayInfo = ref()
    const weekInfo = ref()
    const progressPercentage = computed(() => {
      return Math.floor((totalInfo.value / totalData.value) * 100)
    })
    const progressData = [
      { title: 'Processing', icon: 'cilCheck', value: progressPercentage },
    ]
    const watcher = ref(0)
    let offset = 0

    const loadData = async ($state) => {
      try {
        const response = await getMintingTweets(
          JSON.stringify({ processed: false, invalid: false, outdated: false }),
          -1,
          offset,
        )
        if (response.data.length === 0) $state.complete()
        else {
          for (var data of response.data) {
            await getMintingInfoByTid(data.id)
              .then((info) => {
                mintingMap.set(data.id, {
                  mintingData: data,
                  mintingInfo: info.data,
                  infoIndex: info.length,
                })
              })
              .catch(() => {
                mintingMap.set(data.id, {
                  mintingData: data,
                  mintingInfo: [
                    {
                      comp: 'MintingInfo',
                      compId: 0,
                      tweetId: data.id,
                      objectId: null,
                    },
                  ],
                  infoIndex: 0,
                })
              })
          }
          console.log(mintingMap)
          await $state.loaded()
        }
        offset += response.data.length
        watcher.value = !watcher.value
      } catch (error) {
        $state.error()
      }
    }
    const creatToast = (title, content) => {
      toasts.value.push({
        title: title,
        content: content,
      })
    }
    const reqInfo = (tid, cid) => {
      let minting = mintingMap.get(tid)
      if (!cid) {
        minting.mintingInfo.push({
          comp: 'MintingInfo',
          compId: ++minting.infoIndex,
          tweetId: tid,
          objectId: null,
        })
      } else {
        let idx = minting.mintingInfo.indexOf(
          minting.mintingInfo.find((item) => item.compId === cid),
        )
        minting.mintingInfo.splice(idx, 1)
      }
    }
    const reqDataButton = (tid, bid) => {
      putMintingTweetsFlag(tid, bid)
      mintingMap.delete(tid)
      offset -= 1
      watcher.value = !watcher.value
    }
    const reqSaveButton = (tid, cid, bid) => {
      putMintingTweetsFlag(tid, bid)
      creatToast('Notification', 'Successfully saved.')
      if (!cid) {
        mintingMap.delete(tid)
        offset -= 1
        watcher.value = !watcher.value
      }
    }
    watch(watcher, () => {
      getMintingTweetsTotal().then((response) => {
        totalTweets.value = response.data
      })
      getMintingDataTotal(JSON.stringify({ invalid: false })).then(
        (response) => {
          totalData.value = response.data
        },
      )
      getMintingInfoTotal().then((response) => {
        totalInfo.value = response.data
      })
      var year = new Date().getUTCFullYear()
      var month = new Date().getMonth()
      var day = new Date().getUTCDate()
      var today = `${year}-${month + 1}-${day}`
      var tomorrow = `${year}-${month + 1}-${day + 1}`
      getMintingInfoTotalDate(today, tomorrow).then((response) => {
        todayInfo.value = response.data
      })
    })
    return {
      progressData,
      mintingMap,
      toasts,
      loadData,
      reqInfo,
      reqDataButton,
      reqSaveButton,
      totalTweets,
      totalData,
      totalInfo,
      todayInfo,
      weekInfo,
      progressPercentage,
    }
  },
}
</script>
