import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MyMap from '@/components/MyMap'
import ElementUITest from '@/components/ElementUITest'
import Introduction from '@/components/Introduction'

Vue.use(Router)
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/intro',
      name: 'Introduction',
      component: Introduction
    },
    {
      path: '/map',
      name: 'MyMap',
      component: MyMap
    },
    {
      path: '/test',
      name: 'ElementUITest',
      component: ElementUITest
    }
  ]
})
export default router
