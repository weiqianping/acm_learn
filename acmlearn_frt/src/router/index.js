import {createRouter,createWebHistory} from 'vue-router'
import LoginRegister from '@/components/LoginRegister.vue'
import HomePage from '@/components/HomePage.vue'
import MediaManagement from '@/components/MediaManagement.vue'
import CourseManagement from '@/components/CourseManagement.vue'
import ChapterManagement from '@/components/ChapterManagement.vue'
import VideoManagement from '@/components/VideoManagement.vue'
import CourseCreate from '@/components/CourseCreate.vue'
import CourseEdit from '@/components/CourseEdit.vue'
import ChapterCreate from '@/components/ChapterCreate.vue'
import ChapterEdit from '@/components/ChapterEdit.vue'
import VideoCreate from '@/components/VideoCreate.vue'
import VideoEdit from '@/components/VideoEdit.vue'
import PersonalCenter from '@/components/PersonalCenter.vue'
import DiscussionForum from '../components/DiscussionForum.vue'
import CourseList from '@/components/CourseList.vue'

const routes=[
    {
        path:'/',
        name:'HomePage',
        component:HomePage,
    },
    {
        path:'/login-register',
        name:'LoginRegister',
        component:LoginRegister,
    },
    {
        path:'/media-management',
        name:'MediaManagement',
        component:MediaManagement,
    },
    {
        path:'/course-management',
        name:'CourseManagement',
        component:CourseManagement,
    },
    {
        path:'/chapter-management',
        name:'ChapterManagement',
        component:ChapterManagement,
    },
    {
        path:'/video-management',
        name:'VideoManagement',
        component:VideoManagement,
    },
    {
        path:'/course/create',
        name:'CourseCreate',
        component:CourseCreate,
    },
    {
        path:'/course/edit/:id',
        name:'CourseEdit',
        component:CourseEdit,
    },
    {
        path:'/chapter/create/:id',
        name:'ChapterCreate',
        component:ChapterCreate,
    },
    {
        path:'/chapter/edit/:id',
        name:'ChapterEdit',
        component:ChapterEdit,
    },
    {
        path:'/video/create/:id',
        name:'VideoCreate',
        component:VideoCreate,
    },
    {
        path:'/video/edit/:id',
        name:'VideoEdit',
        component:VideoEdit,
    },
    {
        path:'/personal-center',
        name:'PersonalCenter',
        component:PersonalCenter,
    },
    {
        path: '/course-list',
        name: 'CourseList',
        component: CourseList
      },
      {
        path: '/discussion-forum',
        name: 'DiscussionForum',
        component: DiscussionForum
      }
]

const router=createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes,
})

export default router