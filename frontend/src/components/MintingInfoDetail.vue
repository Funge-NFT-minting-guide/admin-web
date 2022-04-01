<template>
  <CInputGroup class="flex-nowrap">
    <CFormSelect v-model="type.seleted">
      <option
        v-for="item in type.items"
        :key="item"
        v-text="item"
        :value="item"
      />
    </CFormSelect>
    <Datepicker v-model="time" class="date-picker" timePicker />
    <CFormFloating>
      <CFormInput id="priceInput" :value="price" />
      <CFormLabel for="priceInput">Price</CFormLabel>
    </CFormFloating>
    <CFormSelect v-model="currency.seleted">
      <option
        v-for="item in currency.items"
        :key="item"
        v-text="item"
        :value="item"
      />
    </CFormSelect>
    <CFormFloating>
      <CFormInput id="amountInput" :value="mintingAmount" />
      <CFormLabel for="amountInput">Amount</CFormLabel>
    </CFormFloating>
    <CButton
      :value="compId"
      v-if="!compId"
      color="secondary"
      variant="outline"
      @click="reqInfoDetail"
    >
      Add
    </CButton>
    <CButton
      :value="compId"
      v-if="compId"
      color="secondary"
      variant="outline"
      @click="reqInfoDetail"
    >
      Del&nbsp;
    </CButton>
  </CInputGroup>
</template>

<script>
import { ref, reactive } from 'vue'

export default {
  name: 'MintingInfoDetail',
  data() {
    return {}
  },
  props: {
    mintingType: {
      type: String,
      default: 'Public',
      required: false,
    },
    mintingTime: {
      type: Boolean,
      default: false,
      required: false,
    },
    mintingPrice: {
      type: Number,
      default: null,
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
    compId: {
      type: Number,
      require: true,
    },
  },
  methods: {
    reqInfoDetail(e) {
      this.$emit('requestInfoDetail', e.target.value)
    },
  },
  setup(props) {
    const type = reactive({
      items: ['Public', 'WL'],
      seleted: props.mintingType,
    })
    const time = ref(props.mintingTime)
    const price = ref(props.mintingPrice)
    const currency = ref({
      items: ['KLAY', 'ETH'],
      seleted: props.mintingCurrency,
    })
    const amount = ref(props.mintingAmount)

    return {
      type,
      time,
      price,
      currency,
      amount,
    }
  },
}
</script>
