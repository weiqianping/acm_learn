<template>
    <div class="login-register">
      <h1>{{ isLogin ? '登录' : '注册' }}</h1>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <form @submit.prevent="handleSubmit">
        <div class="email-row">
          <input type="email" v-model="email" placeholder="邮箱" required />
          <button type="button" @click="sendVerificationCode" :disabled="isCountingDown" v-if="!isLogin">
            {{ isCountingDown ? `${countdown}秒后重试` : '发送验证码' }}
          </button>
        </div>
        <div v-if="!isLogin">
          <input type="text" v-model="code" placeholder="验证码" required />
          <input type="text" v-model="username" placeholder="用户名" required />
          <input type="password" v-model="password" placeholder="密码" required />
          <input type="password" v-model="confirmPassword" placeholder="确认密码" required />
        </div>
        <div v-else>
          <input type="text" v-model="username" placeholder="用户名" required />
          <input type="password" v-model="password" placeholder="密码" required />
        </div>
        <button type="submit">{{ isLogin ? '登录' : '注册' }}</button>
      </form>
      <button @click="toggleView">{{ isLogin ? '切换到注册' : '切换到登录' }}</button>
    </div>
  </template>
  
  <script>
  import { useToast } from 'vue-toastification'
  import { useRouter } from 'vue-router'
  import { useStore } from '@/store'
  import api from '@/services/api';
  
  
  export default {
    name: 'LoginRegister',
    data() {
      return {
        isLogin: true,
        email: '',
        password: '',
        confirmPassword: '',
        username: '',
        code: '',
        isCountingDown: false,
        countdown: 60,
        errorMessage: ''
      }
    },
    setup() {
      const toast = useToast()
      const router = useRouter()
      const { login } = useStore()
      return { toast, router, login }
    },
    methods: {
      async handleSubmit() {
        this.errorMessage = ''
        if (this.isLogin) {
          await this.handleLogin()
        } else {
          await this.register()
        }
      },
      async handleLogin() {
        try {
          const response = await api.login(this.email, this.username, this.password);
          console.log('登录成功:', response);
          this.toast.success('登录成功');
          // 保存 Token 和用户信息
          localStorage.setItem('token', response.token);
          
          localStorage.setItem('user', JSON.stringify(response.user));
          //localStorage.setItem('user', response.user);
          // 更新全局状态
          this.login(response.user);
        } catch (error) {
          this.errorMessage = error.response ? error.response.data : error.message;
        }
      },
      async register() {
        // 注册逻辑
        if (this.password !== this.confirmPassword) {
          this.errorMessage = '密码和确认密码不一致';
          return;
        }
        try {
          //console.log(this.verificationCode)
          const response = await api.register(this.email, this.username, this.password, this.code);
          console.log('注册成功:', response);
          this.toast.success('注册成功');
          this.router.push('/login');
        } catch (error) {
          this.errorMessage = error.response ? error.response.data : error.message;
        }
      },
      async sendVerificationCode() {
        try {
          await api.sendVerificationCode(this.email);
          this.toast.success('验证码发送成功');
          this.startCountdown();
        } catch (error) {
          this.toast.error('发送验证码失败: ' + (error.response ? error.response.data : error.message));
        }
      },
      startCountdown() {
        this.isCountingDown = true;
        const interval = setInterval(() => {
          this.countdown -= 1;
          if (this.countdown <= 0) {
            clearInterval(interval);
            this.isCountingDown = false;
            this.countdown = 60;
          }
        }, 1000);
      },
      toggleView() {
        this.isLogin = !this.isLogin;
        this.email = '';
        this.password = '';
        this.confirmPassword = '';
        this.username = '';
        this.verificationCode = '';
        this.errorMessage = '';
      }
    }
  }
  </script>
  
  <style scoped>
  .login-register {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .login-register h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .login-register form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    max-width: 300px;
  }
  
  .login-register input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
  }
  
  .email-row {
    display: flex;
    gap: 0.5rem;
  }
  
  .email-row input {
    flex: 1;
  }
  
  .email-row button {
    padding: 0.5rem;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .email-row button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .login-register button {
    padding: 0.5rem;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .login-register button:hover {
    background-color: #38a169;
  }
  
  .error-message {
    color: red;
    margin-bottom: 1rem;
  }
  </style>