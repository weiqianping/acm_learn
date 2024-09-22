import { reactive } from "vue";
import router from '@/router';

const state=reactive({
    isLoggedIn:!!localStorage.getItem('token'),
    username:localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')).username : '',
    avatar_url:localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')).avatar_url : '',
});

export function useStore(){
    const login=(user)=>{
        state.isLoggedIn=true;
        state.username=user.username;
        state.avatar_url=user.avatar_url;
        this.router.push('/');
    };

    const logout=()=>{
        state.isLoggedIn=false;
        state.username='';
        state.avatar_url='';
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        router.push('/loginregister');
    };
    
    return{
        state,
        login,
        logout,
    }
}

