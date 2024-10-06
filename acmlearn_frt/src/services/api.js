import axios from 'axios';

const axiosInstance=axios.create({
    baseURL:'http://124.222.94.181:800/api/',
    withCreadentials:true,
});

//添加一个请求拦截器，用于在请求发送之前对请求配置进行修改。
//请求拦截器
axiosInstance.interceptors.request.use(config=>{
    const token=localStorage.getItem('token');
    if(token){
        config.headers['Authorization']='Token ${token}';
    }
    return config;
},error=>{
    return Promise.reject(error);
});
//(参数) => { 函数体 }

//响应拦截器
axiosInstance.interceptors.response.use(response=>{
    return response;
},error=>{
    return Promise.reject(error);
});

export default{
    //NavBar
    async login(email,username,password){
        try{
            const response=await axiosInstance.post('login/',{
                email,
                username,
                password
            });
            return response.data;
        }catch (error){
            console.error('Login failed:',error);
            throw error;
        }
    },
    async register(email,username,password,code){
        try{
            const response=await axiosInstance.post('register/',{
                email,
                username,
                password,
                code
            });
            return response.data;
        }catch (error){
            console.error('Register failed:',error);
            throw error;
        }
    },
}