<template>
  <CTable align="middle" class="mb-0 border" hover responsive>
    <CTableBody>
      <CTableRow>
        <CTableDataCell>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">@</CInputGroupText>
            <CFormInput :value="projectName" aria-label="Username" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>Date</CInputGroupText>
            <Datepicker v-model="mintingDate" :enableTimePicker="false" />
          </CInputGroup>
          <!--<MintingInfoDetail />-->
          <component
            v-for="detail in infoDetail"
            :key="detail"
            :is="detail.comp"
            :mintingType="detail.mintingType"
            :mintingTime="detail.mintingTime"
            :mintingPrice="detail.mintingPrice"
            :mintingCurrency="detail.mintingCurrency"
            :mintingAmount="detail.mintingAmount"
            :compId="detail.compId"
            @requestAddInfoDetail="reqInfoDetail"
          />
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">Site</CInputGroupText>
            <CFormInput />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>ETC.</CInputGroupText>
            <CFormInput />
          </CInputGroup>
        </CTableDataCell>
        <CTableDataCell>
          <CButton color="success" shape="rounded-pill">Add</CButton>
          <br /><br />
          <CButton color="info" shape="rounded-pill" @click="test">
            Save
          </CButton>
        </CTableDataCell>
      </CTableRow>
    </CTableBody>
  </CTable>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'MintingInfo',
  props: {
    tweetId: {
      type: String,
      default: undefined,
      required: false,
    },
    projectName: {
      type: String,
      default: undefined,
      required: false,
    },
  },
  data() {
    return {
      infoDetailIndex: 0,
      infoDetail: [
        {
          comp: 'MintingInfoDetail',
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: undefined,
          compId: this.infoDetailIndex,
        },
      ],
    }
  },
  methods: {
    reqInfoDetail(id) {
      if (!id) {
        this.infoDetail.push({
          comp: 'MintingInfoDetail',
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: undefined,
          compId: ++this.infoDetailIndex,
        })
      } else {
        var idx = this.infoDetail.indexOf(
          this.infoDetail.find((item) => item.compId == id),
        )
        this.infoDetail.splice(idx, 1)
      }
    },
    test() {
      console.log(this.infoDetailIndex)
    },
  },
  setup() {
    const mintingDate = ref()

    return {
      mintingDate,
    }
  },
}
</script>
