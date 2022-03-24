<template>
  <CTable align="middle" class="mb-0 border" hover responsive>
    <CTableBody>
      <CTableRow>
        <CTableDataCell>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">@</CInputGroupText>
            <CFormInput :value="projName" aria-label="Username" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>Date</CInputGroupText>
            <Datepicker v-model="date" :enableTimePicker="false" />
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
          />
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">Site</CInputGroupText>
            <CFormInput :value="site" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>ETC.</CInputGroupText>
            <CFormInput :value="_etc" />
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
          <CButton color="info" shape="rounded-pill" @click="test">
            Save
          </CButton>
        </CTableDataCell>
      </CTableRow>
    </CTableBody>
  </CTable>
</template>

<script>
export default {
  name: 'MintingInfo',
  props: {
    tweetId: {
      type: String,
      default: undefined,
      required: false,
    },
    compId: {
      type: Number,
      defaul: 0,
      required: true,
    },
  },
  data() {
    return {
      infoDetailIndex: 0,
      infoDetail: [
        {
          comp: 'MintingInfoDetail',
          compId: this.infoDetailIndex,
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: undefined,
        },
      ],
    }
  },
  methods: {
    reqInfoDetail(id) {
      if (!id) {
        this.infoDetail.push({
          comp: 'MintingInfoDetail',
          compId: ++this.infoDetailIndex,
          mintingType: 'Public',
          mintingTime: false,
          mintingPrice: null,
          mintingCurrency: 'KLAY',
          mintingAmount: undefined,
        })
      } else {
        var idx = this.infoDetail.indexOf(
          this.infoDetail.find((item) => item.compId === id),
        )
        this.infoDetail.splice(idx, 1)
      }
    },
    reqInfo() {
      this.$emit('requestInfo', this.prop.tweetId, this.props.compId)
    },
    test() {
      console.log(this.infoDetailIndex)
    },
  },
}
</script>
