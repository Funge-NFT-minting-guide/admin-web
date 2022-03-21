<template>
  <CInputGroup class="flex-nowrap">
    <CFormSelect>
      <option>Public</option>
      <option>WL</option>
    </CFormSelect>
    <CInputGroupText>Time</CInputGroupText>
    <Datepicker v-model="time" timePicker />
    <CInputGroupText>Price</CInputGroupText>
    <CFormInput />
    <CFormSelect>
      <option>KLAY</option>
      <option>ETH</option>
    </CFormSelect>
    <CInputGroupText>Amount</CInputGroupText>
    <CFormInput v-bind:value="mintingAmount" />
    <CButton color="secondary" variant="outline">Add</CButton>
  </CInputGroup>
</template>

<script>
export default {
  name: 'MintingInfoDetail',
  data() {
    return {
      amounta: 0,
    }
  },
  props: {
    mintingType: {
      type: Boolean,
      default: undefined,
      required: false,
    },
    mintingTime: {
      type: Boolean,
      default: undefined,
      required: false,
    },
    mitingPrice: {
      type: Number,
      default: undefined,
      required: false,
    },
    mintingCurrency: {
      type: String,
      default: undefined,
      required: false,
    },
    mintingAmount: {
      type: String,
      default: undefined,
      required: false,
    },
  },
  setup(props) {
    console.log(props.mintingAmount)
  },
}
</script>
