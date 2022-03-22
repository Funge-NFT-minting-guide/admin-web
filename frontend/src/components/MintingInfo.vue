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
            <Datepicker :enableTimePicker="false" />
          </CInputGroup>
          <MintingInfoDetail />
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
          <CButton color="info" shape="rounded-pill">Save</CButton>
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
    projectName: {
      type: String,
      default: undefined,
      required: false,
    },
  },
}
</script>
