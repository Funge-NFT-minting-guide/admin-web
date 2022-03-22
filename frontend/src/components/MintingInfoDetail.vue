<template>
  <CInputGroup class="flex-nowrap">
    <CFormSelect>
      <option>Public</option>
      <option>WL</option>
    </CFormSelect>
    <Datepicker class="date-picker" timePicker />
    <CFormFloating>
      <CFormInput id="priceInput" />
      <CFormLabel for="priceInput">Price</CFormLabel>
    </CFormFloating>
    <CFormSelect>
      <option>KLAY</option>
      <option>ETH</option>
    </CFormSelect>
    <CFormFloating>
      <CFormInput id="amountInput" :value="mintingAmount" />
      <CFormLabel for="amountInput">Amount</CFormLabel>
    </CFormFloating>
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
