<template>
  <CInputGroup class="flex-nowrap">
    <CFormSelect v-model="type.seleted" @change="reqUpdateType">
      <option
        v-for="item in type.items"
        :key="item"
        v-text="item"
        :value="item"
      />
    </CFormSelect>
    <Datepicker
      v-model="time"
      class="date-picker"
      timePicker
      @update:modelValue="reqUpdateTime"
    />
    <CFormFloating>
      <CFormInput id="priceInput" :value="price" @change="reqUpdatePrice" />
      <CFormLabel for="priceInput">Price</CFormLabel>
    </CFormFloating>
    <CFormSelect v-model="currency.seleted" @change="reqUpdateCurrency">
      <option
        v-for="item in currency.items"
        :key="item"
        v-text="item"
        :value="item"
      />
    </CFormSelect>
    <CFormFloating>
      <CFormInput
        id="amountInput"
        :value="mintingAmount"
        @change="reqUpdateAmount"
      />
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
import { ref } from 'vue'

export default {
  name: 'MintingInfoDetail',
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
  setup(props, { emit }) {
    const type = ref({
      items: ['Public', 'WL', 'OG'],
      seleted: props.mintingType,
    })
    const time = ref(0)
    const price = ref(props.mintingPrice)
    const currency = ref({
      items: ['KLAY', 'ETH'],
      seleted: props.mintingCurrency,
    })
    const amount = ref(props.mintingAmount)

    const reqInfoDetail = (e) => {
      emit('requestInfoDetail', e.target.value)
    }

    const reqUpdateType = (e) => {
      emit('requestUpdateType', props.compId, e.target.value)
    }

    const reqUpdateTime = () => {
      emit('requestUpdateTime', props.compId, time.value)
    }
    const reqUpdatePrice = (e) => {
      emit('requestUpdatePrice', props.compId, e.target.value)
    }
    const reqUpdateCurrency = (e) => {
      emit('requestUpdateCurrency', props.compId, e.target.value)
    }
    const reqUpdateAmount = (e) => {
      emit('requestUpdateAmount', props.compId, e.target.value)
    }

    return {
      type,
      time,
      price,
      currency,
      amount,
      reqInfoDetail,
      reqUpdateType,
      reqUpdateTime,
      reqUpdatePrice,
      reqUpdateCurrency,
      reqUpdateAmount,
    }
  },
}
</script>
