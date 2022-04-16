<template>
  <CDropdown v-if="isAuthenticated" variant="nav-item">
    <CDropdownToggle placement="bottom-end" class="py-0" :caret="false">
      <CAvatar :src="avatar" size="md" />
    </CDropdownToggle>
    <CDropdownMenu class="pt-0">
      <CDropdownHeader component="h6" class="bg-light fw-semibold py-2">
        Account
      </CDropdownHeader>
      <CDropdownItem> <CIcon icon="cil-user" /> Profile </CDropdownItem>
      <CDropdownItem @click="reqLogout">
        <CIcon icon="cil-lock-locked" /> Logout
      </CDropdownItem>
    </CDropdownMenu>
  </CDropdown>
</template>

<script>
import { logout } from '@/api/auth'
import { computed } from 'vue'
import { useStore } from 'vuex'
import avatar from '@/assets/images/avatars/8.jpg'
export default {
  name: 'AppHeaderDropdownAccnt',
  setup() {
    const store = useStore()
    const isAuthenticated = computed(() => store.getters.getAuthStatus)

    const reqLogout = async () => {
      await logout()
      location.reload()
    }

    return {
      avatar: avatar,
      isAuthenticated,
      reqLogout,
    }
  },
}
</script>
