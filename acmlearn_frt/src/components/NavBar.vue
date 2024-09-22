<template>
    <header class="nav-bar">
      <div class="left-section">
          <h1>WZU-ACM学习平台</h1>
          <nav class="team-history">
            <router-link to="#">队史</router-link>
          </nav>
      </div>
      <nav class="right-section">
        <router-link to="/">首页</router-link>
        <router-link to="#" @click="checkLogin">课程列表</router-link>
        <router-link to="#">讨论区</router-link>
        <router-link to="/mediamanagement" @click="checkLogin">媒资管理</router-link>
        <router-lin v-if="true">登录/注册</router-lin>
        <div v-else class="user-profile" @click="goToPersonalCenter">
          <img src="state.avatar_url" alt="User Avatar" class="avatar"/>
          <span>{{ state.username }}</span>
        </div>
      </nav>
    </header>
  </template>
  
  <script>
  import {useStore} from '@/store';
  import router from '@/router';
  
  
  export default {
    name: 'NavBar',
    setup(){
      const {state}=useStore()
      const checkLogin=(event) => {
          if(!state.isLoggedIn){
              event.preventDefault();
              router.push('/loginregister');
          }
      };
      function goToPersonalCenter(event){
          if(state.isLoggedIn){
              router.push('/personal-center');
          }
      };
      return {
          state,
          checkLogin,
          goToPersonalCenter,
      };
    },
  }
  </script>
  
  <style>
  
  </style>