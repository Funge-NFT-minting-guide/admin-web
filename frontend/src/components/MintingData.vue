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
      <CCardHeader>{{ projectName }}</CCardHeader>
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
  },
}
</script>
