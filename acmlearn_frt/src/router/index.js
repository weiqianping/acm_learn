import {createRouter,createWebHistory} from 'vue-router'
import LoginRegister from '@/components/LoginRegister.vue'
import HomePage from '@/components/HomePage.vue'
import MediaManagement from '@/components/MediaManagement.vue'
import CourseManagement from '@/components/CourseManagement.vue'
import ChapterManagement from '@/components/ChapterManagement.vue'
import VideoManagement from '@/components/VideoManagement.vue'
import CourseCreate from '@/components/CourseCreate.vue'
import CourseEdit from '@/components/CourseEdit.vue'
import ChapterCreate from '@components/ChapterCreate.vue'
import ChapterEdit from '@components/ChapterEdit.vue'
import VideoCreate from '@components/VideoCreate.vue'
import VideoEdit from '@components/VideoEdit.vue'

const routes=[
    {
        path:'/',
        name:'HomePage',
        component:HomePage,
    },
    {
        path:'/loginregister',
        name:'LoginRegister',
        component:LoginRegister,
    },
    {
        path:'/mediamanagement',
        name:'MediaManagement',
        component:MediaManagement,
    },
    {
        path:'/coursemanagement',
        name:'CourseManagement',
        component:CourseManagement,
    },
    {
        path:'/chaptermanagement',
        name:'ChapterManagement',
        component:ChapterManagement,
    }
]
