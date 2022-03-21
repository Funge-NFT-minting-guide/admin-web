<template>
  <CTable align="middle" class="mb-0 border" hover responsive>
    <CTableBody>
      <CTableRow>
        <CTableDataCell>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText id="addon-wrapping">@</CInputGroupText>
            <CFormInput placeholder="MetaKongz" aria-label="Username" />
          </CInputGroup>
          <CInputGroup class="flex-nowrap">
            <CInputGroupText>Date</CInputGroupText>
            <Datepicker :enableTimePicker="false" />
          </CInputGroup>
          <MintingInfoDetail minting-amount="112" />
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
import { cilClone } from '@coreui/icons'
export default {
  name: 'MintingInfo',
  setup() {
    return {
      message: 'test',
      cilClone,
    }
  },
}
</script>
