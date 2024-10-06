<template>
    <div>
      <h1>管理课程</h1>
      <el-button type="primary" @click="handleAddCourse">添加课程</el-button>
      <el-collapse v-model="activeNames">
        <el-collapse-item v-for="(course, courseIndex) in courses" :key="courseIndex" :name="courseIndex">
          <template #title>
            <span>{{ course.name }}</span>
            <el-button type="text" @click.stop="handleAddChapter(courseIndex)">添加章节</el-button>
            <el-button type="text" @click.stop="handleEditCourse(courseIndex)">编辑课程</el-button>
            <el-button type="text" @click.stop="handleDeleteCourse(courseIndex)">删除课程</el-button>
          </template>
          <el-collapse v-model="activeChapterNames[courseIndex]">
            <el-collapse-item v-for="(chapter, chapterIndex) in course.chapters" :key="chapterIndex" :name="chapterIndex">
              <template #title>
                <span>{{ chapter.name }}</span>
                <el-button type="text" @click.stop="handleAddVideo(courseIndex, chapterIndex)">添加视频</el-button>
                <el-button type="text" @click.stop="handleEditChapter(courseIndex, chapterIndex)">编辑章节</el-button>
                <el-button type="text" @click.stop="handleDeleteChapter(courseIndex, chapterIndex)">删除章节</el-button>
              </template>
              <ul>
                <li v-for="(video, videoIndex) in chapter.videos" :key="videoIndex">
                  <span>{{ video.name }}</span>
                  <el-button type="text" @click.stop="handleEditVideo(courseIndex, chapterIndex, videoIndex)">编辑视频</el-button>
                  <el-button type="text" @click.stop="handleDeleteVideo(courseIndex, chapterIndex, videoIndex)">删除视频</el-button>
                </li>
              </ul>
            </el-collapse-item>
          </el-collapse>
        </el-collapse-item>
      </el-collapse>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeNames: [],
        activeChapterNames: {},
        courses: [
          {
            name: '课程1',
            chapters: [
              {
                name: '章节1',
                videos: [
                  { name: '视频1' },
                  { name: '视频2' },
                ],
              },
              {
                name: '章节2',
                videos: [
                  { name: '视频3' },
                  { name: '视频4' },
                ],
              },
            ],
          },
          {
            name: '课程2',
            chapters: [
              {
                name: '章节3',
                videos: [
                  { name: '视频5' },
                  { name: '视频6' },
                ],
              },
            ],
          },
        ],
      };
    },
    methods: {
      handleAddCourse() {
        // 处理添加课程逻辑
        const newCourse = {
          name: `新课程${this.courses.length + 1}`,
          chapters: [],
        };
        this.courses.push(newCourse);
        this.activeNames.push(this.courses.length - 1);
      },
      handleAddChapter(courseIndex) {
        // 处理添加章节逻辑
        const newChapter = {
          name: `新章节${this.courses[courseIndex].chapters.length + 1}`,
          videos: [],
        };
        this.courses[courseIndex].chapters.push(newChapter);
        if (!this.activeChapterNames[courseIndex]) {
          this.$set(this.activeChapterNames, courseIndex, []);
        }
        this.activeChapterNames[courseIndex].push(this.courses[courseIndex].chapters.length - 1);
      },
      handleEditCourse(courseIndex) {
        // 处理编辑课程逻辑
        console.log('编辑课程', courseIndex);
      },
      handleDeleteCourse(courseIndex) {
        // 处理删除课程逻辑
        this.courses.splice(courseIndex, 1);
        this.activeNames.splice(courseIndex, 1);
      },
      handleAddVideo(courseIndex, chapterIndex) {
        // 处理添加视频逻辑
        const newVideo = {
          name: `新视频${this.courses[courseIndex].chapters[chapterIndex].videos.length + 1}`,
        };
        this.courses[courseIndex].chapters[chapterIndex].videos.push(newVideo);
      },
      handleEditChapter(courseIndex, chapterIndex) {
        // 处理编辑章节逻辑
        console.log('编辑章节', courseIndex, chapterIndex);
      },
      handleDeleteChapter(courseIndex, chapterIndex) {
        // 处理删除章节逻辑
        this.courses[courseIndex].chapters.splice(chapterIndex, 1);
        this.activeChapterNames[courseIndex].splice(chapterIndex, 1);
      },
      handleEditVideo(courseIndex, chapterIndex, videoIndex) {
        // 处理编辑视频逻辑
        console.log('编辑视频', courseIndex, chapterIndex, videoIndex);
      },
      handleDeleteVideo(courseIndex, chapterIndex, videoIndex) {
        // 处理删除视频逻辑
        this.courses[courseIndex].chapters[chapterIndex].videos.splice(videoIndex, 1);
      },
    },
  };
  </script>
  
  <style scoped>
  /* 添加一些样式以美化组件 */
  .el-collapse {
    width: 80%;
    margin: 0 auto;
  }
  
  .el-button--text {
    margin-left: 10px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin: 10px 0;
  }
  </style>