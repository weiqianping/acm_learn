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
      <router-link to="/course-list" @click="checkLogin">课程列表</router-link>
      <router-link to="discussion-forum">讨论区</router-link>
      <!--为了方便测试，先把检查登录，未登录自动跳到个人中心，关掉-->
      <router-link to="/media-management" @click="checkLogin">媒资管理</router-link>
      <router-link v-if="!state.isLoggedIn" to="/login-register">登录/注册</router-link>
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
    const checkLogin=() => {
        // if(!state.isLoggedIn){
        //     event.preventDefault();
        //     router.push('/login-register');
        // }
        return true;
    };
    function goToPersonalCenter(){
        if(state.isLoggedIn){
            router.push('/personal-center');
        }
    }
    return {
        state,
        checkLogin,
        goToPersonalCenter,
    };
  },
}
</script>

<style scoped>
.nav-bar {
  background-color: #42b983;
  color: white;
  padding: 0.25rem 1rem; /* 调整内边距 */
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 2rem; /* 进一步减小高度 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.left-section {
  display: flex;
  align-items: center;
  gap: 1rem; /* 调整间距 */
}

.left-section h1 {
  margin: 0;
  font-size: 0.9rem; /* 进一步减小字体大小 */
}

.left-section .team-history {
  display: flex;
  gap: 0.5rem; /* 调整间距 */
}

.right-section {
  display: flex;
  gap: 0.5rem; /* 调整间距 */
}

.nav-bar a, .nav-bar .user-profile {
  color: white;
  text-decoration: none;
  padding: 0.25rem 0.5rem; /* 调整内边距 */
  border-radius: 4px;
  transition: background-color 0.3s;
  cursor: pointer;
  display: inline-flex; /* 使用 flex 布局 */
  align-items: center; /* 垂直居中对齐 */
  font-size: 0.75rem; /* 进一步减小字体大小 */
}

.nav-bar a:hover, .nav-bar .user-profile:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.nav-bar a.router-link-exact-active {
  background-color: rgba(255, 255, 255, 0.2);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.5rem; /* 调整间距 */
}

.avatar {
  width: 1.5rem; /* 头像宽度 */
  height: 1.5rem; /* 头像高度 */
  border-radius: 50%; /* 圆形头像 */
}
</style>