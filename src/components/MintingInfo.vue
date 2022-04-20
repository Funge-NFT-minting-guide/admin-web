<template>
  <CTable align="middle" class="mb-0 border" hover responsive>
    <CTableBody>
      <CTableRow>
        <CTableDataCell>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">@</CInputGroupText>
            <CFormInput v-model="projName" aria-label="Username" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>Date</CInputGroupText>
            <Datepicker v-model="_date" :enableTimePicker="false" />
          </CInputGroup>
          <!--<MintingInfoDetail />-->
          <component
            v-for="detail in infoDetail"
            :key="detail.compId"
            :is="detail.comp"
            :mintingType="detail.mintingType"
            :mintingTime="detail.mintingTime"
            :mintingPrice="detail.mintingPrice"
            :mintingCurrency="detail.mintingCurrency"
            :mintingAmount="detail.mintingAmount"
            :compId="detail.compId"
            @requestInfoDetail="reqInfoDetail"
            @requestUpdateType="reqUpdateType"
            @requestUpdateTime="reqUpdateTime"
            @requestUpdatePrice="reqUpdatePrice"
            @requestUpdateCurrency="reqUpdateCurrency"
            @requestUpdateAmount="reqUpdateAmount"
          />
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">Site</CInputGroupText>
            <CFormInput v-model="_site" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>ETC.</CInputGroupText>
            <CFormInput v-model="_etc" />
          </CInputGroup>
        </CTableDataCell>
        <CTableDataCell>
          <CButton
            :value="compId"
            v-if="!compId"
            color="success"
            shape="rounded-pill"
            @click="reqInfo"
          >
            Add
          </CButton>
          <CButton
            :value="compId"
            v-if="compId"
            color="danger"
            shape="rounded-pill"
            @click="reqInfo"
          >
            Del&nbsp;
          </CButton>
          <br /><br />
          <CButton
            color="info"
            shape="rounded-pill"
            @click="reqSaveMintingInfo"
          >
            Save
          </CButton>
        </CTableDataCell>
      </CTableRow>
    </CTableBody>
  </CTable>
</template>

<script>
import { getMintingInfoByOid, postMintingInfo } from '@/api/minting'
import { ref, toRef, onMounted } from 'vue'

export default {
  name: 'MintingInfo',
  props: {
    tweetId: {
      type: String,
      default: null,
      required: false,
    },
    objectId: {
      type: String,
      default: null,
    },
    compId: {
      type: Number,
      default: 0,
      required: true,
    },
    projectName: {
      type: String,
      default: null,
    },
    profileImageUrl: {
      type: String,
      default: null,
    },
    followers: {
      type: Number,
      default: null,
    },
    url: {
      type: String,
      default: null,
    },
  },
  setup(props, { emit }) {
    const oid = toRef(props, 'objectId')
    const projName = toRef(props, 'projectName')
    const _date = ref()
    const _site = ref()
    const _etc = ref()
    let infoDetailIndex = 0
    const infoDetail = ref([])

    const initInfoDetail = () => {
      console.log(props.objectIdj)
      if (props.objectId != null) {
        getMintingInfoByOid(props.objectId)
          .then((response) => {
            for (var info of response.data) {
              infoDetail.value.push(...info.detail)
            }
          })
          .catch((error) => {
            if (error.response.status == 404) {
              infoDetail.value.push({
                comp: 'MintingInfoDetail',
                compId: infoDetailIndex,
                mintingType: 'Public',
                mintingTime: false,
                mintingPrice: null,
                mintingCurrency: 'KLAY',
                mintingAmount: null,
              })
            }
          })
      } else {
        infoDetail.value.push({
          comp: 'MintingInfoDetail',
          compId: infoDetailIndex,
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: null,
        })
      }
    }

    const findComponentById = (id) => {
      return infoDetail.value.find((item) => item.compId === id)
    }

    const reqInfoDetail = (id) => {
      if (id <= 0) {
        infoDetail.value.push({
          comp: 'MintingInfoDetail',
          compId: ++infoDetailIndex,
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: null,
        })
      } else {
        var idx = infoDetail.value.indexOf(findComponentById(id))
        infoDetail.value.splice(idx, 1)
      }
    }

    const reqInfo = () => {
      emit('requestInfo', props.tweetId, props.compId)
    }
    const reqUpdateType = (id, seleted) => {
      findComponentById(id).mintingType = seleted
    }
    const reqUpdateTime = (id, time) => {
      findComponentById(id).mintingTime = time
    }
    const reqUpdatePrice = (id, price) => {
      findComponentById(id).mintingPrice = price
    }
    const reqUpdateCurrency = (id, currency) => {
      findComponentById(id).mintingCurrency = currency
    }
    const reqUpdateAmount = (id, amount) => {
      findComponentById(id).mintingAmount = amount
    }

    const reqSaveMintingInfo = () => {
      postMintingInfo(
        JSON.stringify({
          objectId: oid.value,
          tweetId: props.tweetId,
          projectName: projName.value,
          profileImageUrl: props.profileImageUrl,
          date: _date.value,
          followers: props.followers,
          url: props.url,
          site: _site.value,
          etc: _etc.value,
          detail: infoDetail.value,
        }),
      )
      emit('requestSaveMintingInfo', props.tweetId, props.compId, 'processed')
    }

    onMounted(() => {
      initInfoDetail()
    })

    return {
      projName,
      _date,
      _site,
      _etc,
      infoDetail,
      reqInfoDetail,
      reqInfo,
      reqSaveMintingInfo,
      reqUpdateType,
      reqUpdateTime,
      reqUpdatePrice,
      reqUpdateCurrency,
      reqUpdateAmount,
    }
  },
}
</script>
