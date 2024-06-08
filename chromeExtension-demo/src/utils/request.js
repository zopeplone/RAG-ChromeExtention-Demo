
import axios from 'axios'
import { ElMessage } from 'element-plus'
// import store from '@/store'
// import { Route } from 'vue-router'
const service = axios.create({
  baseURL: 'http://127.0.0.1:7212', // url = base url + request url
  withCredentials: false,//false就可以解决跨域
  timeout: 500000,
})
//响应拦截器
service.interceptors.response.use(
  (response) => {

    if (response.status !== 200) {
      ElMessage.error(response.statusText)
    }
    else if (response.data.code === 0) {
      ElMessage.error(response.data.message)
    }
    return response
  },
  (error) => {
    console.error('err' + error)
    let { message } = error;
    if (message == "Network Error") {
      message = "后端接口连接异常";
    }
    else if (message.includes("timeout")) {
      message = "系统接口请求超时";
    }
    else if (message.includes("401")) {
      ElMessage.error('登陆状态失效')
      // router.push('/login')
    }
    else if (message.includes("Request failed with status code")) {
      message = "系统接口" + message.substr(message.length - 3) + "异常";
    }
    return Promise.reject(error).catch(error)
  }

)
//请求拦截器
service.interceptors.request.use(
  (config) => {
    // config.headers.token = useLoginStore().token
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default service