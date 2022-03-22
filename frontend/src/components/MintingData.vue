<template>
  <CTableDataCell>
    <CFormCheck disabled />
  </CTableDataCell>
  <CTableDataCell>
    <CAvatar size="xl" :src="profileImageUrl" />
  </CTableDataCell>
  <CTableDataCell class="col-4">
    <CInputGroup class="flex-nowrap">
      <CInputGroupText id="addon-wrapping">@</CInputGroupText>
      <CFormInput :value="projectName" aria-label="Username" disabled />
    </CInputGroup>
    <CInputGroup class="flex-nowrap">
      <CInputGroupText>Origin</CInputGroupText>
      <CFormTextarea :value="tweetText" disabled></CFormTextarea>
    </CInputGroup>
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
}
</script>
