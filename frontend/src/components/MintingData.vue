<template>
  <CTableDataCell>
    <CFormCheck disabled />
  </CTableDataCell>
  <CTableDataCell>
    <CAvatar size="xl" :src="profileImageUrl" />
  </CTableDataCell>
  <CTableDataCell class="col-4">
    <!--
    <CInputGroup class="flex-nowrap">
      <CInputGroupText id="addon-wrapping">@</CInputGroupText>
      <CFormInput :value="projectName" aria-label="Username" disabled />
    </CInputGroup>
    <CInputGroup class="flex-nowrap">
      <CInputGroupText>Origin</CInputGroupText>
      <CFormTextarea :value="tweetText" disabled></CFormTextarea>
      <CCallout color="info">{{ tweetText }}</CCallout>
    </CInputGroup>
    -->
    <CCard>
      <CCardHeader>
        {{ projectName }}&nbsp;&nbsp;
        <CIcon :icon="cibTwitter" size="xxs"></CIcon>
        {{ followersConvertToKMB }}
      </CCardHeader>
      <CCardBody>
        <!--
        <CCardText v-for="tweetTextLine in tweetTextLines" :key="tweetTextLine">
          {{ tweetTextLine }}
        </CCardText>
        -->
        <CCardText v-html="tweetTextNewline" />
      </CCardBody>
    </CCard>
  </CTableDataCell>
  <CTableDataCell>
    <CButton color="danger" shape="rounded-pill">Delete</CButton>
    <br /><br />
    <CButton color="warning" shape="rounded-pill">Outdated</CButton>
  </CTableDataCell>
  <CTableDataCell>
    <CIcon :icon="cilClone" size="xxl" />
  </CTableDataCell>
</template>

<script>
import { cilClone } from '@coreui/icons'
import { cibTwitter } from '@coreui/icons'

export default {
  name: 'MintingData',
  props: {
    tweetId: {
      type: String,
      defalt: undefined,
      required: true,
    },
    profileImageUrl: {
      type: String,
      default: undefined,
      required: false,
    },
    projectName: {
      type: String,
      default: undefined,
      requred: true,
    },
    followers: {
      type: Number,
      default: undefined,
      required: true,
    },
    tweetText: {
      type: String,
      default: undefined,
      required: true,
    },
  },
  computed: {
    tweetTextLines: function () {
      return this.tweetText.split('\n')
    },
    tweetTextNewline: function () {
      return this.tweetText.replaceAll('\n', '<br />')
    },
    followersConvertToKMB: function () {
      var num = this.followers
      if (num >= 1000000000) {
        return (num / 1000000000).toFixed(1).replace(/\.0$/, '') + 'B'
      }
      if (num >= 1000000) {
        return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M'
      }
      if (num >= 1000) {
        return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'K'
      }
      return num
    },
  },
  setup() {
    return {
      cilClone,
      cibTwitter,
    }
  },
}
</script>
