export default [
  {
    component: 'CNavItem',
    name: 'Dashboard',
    to: '/',
    icon: 'cil-speedometer',
    badge: {
      color: 'primary',
      text: 'NEW',
    },
  },
  {
    component: 'CNavItem',
    name: 'Minting',
    to: '/minting',
    icon: 'cil-diamond',
  },
  {
    component: 'CNavGroup',
    name: 'Tips',
    to: '/tips',
    icon: 'cil-lightbulb',
    items: [
      {
        component: 'CNavItem',
        name: 'Guide',
        to: '/tips/guide',
        icon: 'cil-education',
      },
      {
        component: 'CNavItem',
        name: 'FAQ',
        to: '/tips/faq',
        icon: 'cil-infinity',
      },
      {
        component: 'CNavItem',
        name: 'Association',
        to: '/tips/association',
        icon: 'cil-link-alt',
      },
    ],
  },
  {
    component: 'CNavGroup',
    name: 'Accounts',
    to: '/accounts',
    icon: 'cil-people',
    items: [
      {
        component: 'CNavItem',
        name: 'Users',
        to: '/accounts/users',
        icon: 'cil-user',
      },
      {
        component: 'CNavItem',
        name: 'Statistics',
        to: '/accounts/statistics',
        icon: 'cil-chart',
      },
    ],
  },
]
