import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import CoreuiVue from '@coreui/vue'
import CIcon from '@coreui/icons-vue'
import { iconsSet as icons } from '@/assets/icons'
import DocsCallout from '@/components/DocsCallout'
import DocsExample from '@/components/DocsExample'
import MintingInfo from '@/components/MintingInfo'
import MintingInfoDetail from '@/components/MintingInfoDetail'
import MintingData from '@/components/MintingData'
import Test from '@/components/Test.vue'

import Datepicker from 'vue3-date-time-picker'
import 'vue3-date-time-picker/dist/main.css'
import InfiniteLoading from 'v3-infinite-loading'
import 'v3-infinite-loading/lib/style.css'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(CoreuiVue)
app.use(InfiniteLoading)
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.component('DocsCallout', DocsCallout)
app.component('DocsExample', DocsExample)
app.component('Datepicker', Datepicker)
app.component('infinite-loading', InfiniteLoading)
app.component('MintingInfo', MintingInfo)
app.component('MintingInfoDetail', MintingInfoDetail)
app.component('MintingData', MintingData)
app.component('Test', Test)

app.mount('#app')
