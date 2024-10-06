<template>
    <el-row class="tac">
      <el-col :span="6">
        <div class="media-management">
          <el-menu :default-active="activeTab" @select="handleSelect" mode="vertical">
            <!--
            <el-menu-item index="carousel">轮播图管理</el-menu-item>
            <el-menu-item index="notification">通知栏管理</el-menu-item>
            
            <el-menu-item index="post">帖子管理</el-menu-item>
            <el-menu-item index="teamHistory">队史管理</el-menu-item>
            -->
            <el-menu-item index="course">课程管理</el-menu-item>
          </el-menu>
        </div>
      </el-col>
      <el-col :span="18">
        <div class="content">
            <!--
            <CarouselManagement v-if="activeTab === 'carousel'" />
          <NotificationManagement v-if="activeTab === 'notification'" />
          <CourseManagement v-if="activeTab === 'course'" />
          <PostManagement v-if="activeTab === 'post'" />
          <TeamHistoryManagement v-if="activeTab === 'teamHistory'" />
            -->
            <CourseManagement v-if="activeTab === 'course'" />
        </div>
      </el-col>
    </el-row>
  </template>
  
  <script>
  import { ElMenu, ElMenuItem, ElRow, ElCol } from 'element-plus';
//   import CarouselManagement from '@/components/CarouselManagement.vue';
//   import NotificationManagement from '@/components/NotificationManagement.vue';
//   import PostManagement from '@/components/PostManagement.vue';
//   import TeamHistoryManagement from '@/components/TeamHistoryManagement.vue';
  import CourseManagement from '@/components/CourseManagement.vue';
  
  export default {
    name: 'MediaManagement',
    components: {
      ElMenu,
      ElMenuItem,
      ElRow,
      ElCol,
      CourseManagement,
    },
    data() {
      return {
        activeTab: 'course'  // 默认显示轮播图管理
      };
    },
    methods: {
      handleSelect(key) {
        this.activeTab = key;
        console.log(key,"==============>")
      }
    }
  };
  </script>
  
  <style scoped>
  .tac {
    display: flex;
    justify-content: center;
  }
  
  .media-management {
    padding: 0;
    width: 100%;
  }
  
  .content {
    border: 1px solid #ddd;
    padding: 1rem;
    border-radius: 8px;
    width: 100%;
  }
  </style>