<script setup>
import { chatWithServer, getChatHistory,setChatHistory} from '@/api/chat';
import { onMounted, ref } from 'vue';

const inputText = ref('')
const historyList = ref([])
const sendMessage=async ()=>{
  historyList.value.push({text:inputText.value,loading:false})
  let data = {text:'',loading:true}
  let text = inputText.value
  historyList.value.push(data)
  inputText.value = ''
  let res =await chatWithServer(text)
  historyList.value[historyList.value.length-1] = {text:res.data.data,loading:false}
  setChatHistory(historyList.value)
}
onMounted(async ()=>{
  let res =await getChatHistory()
  let arr = Object.keys(res).map(key => res[key]);
  historyList.value = arr
})
const deleteChat = ()=>{
  historyList.value = []
  setChatHistory([])
}
</script>
<template>
  <div>
    <h1>Fibona Demo</h1>
    <el-scrollbar>
      <div class="content">
        <ChatItem v-for="(item,index) in historyList" :text="item.text" :isUser="index%2===0" :loading="item.loading"
          :key="index">

        </ChatItem>
      </div>
    </el-scrollbar>
    <div class="bottom">
      <el-button icon="Delete" circle @click="deleteChat()"></el-button>
      <el-input placeholder="请输入" v-model="inputText"></el-input>
      <el-button icon="Promotion" circle @click="sendMessage()"></el-button>
    </div>
  </div>
</template>


<style lang="scss" scoped>
h1 {
  color: #147ad6;
  text-align: center;
}

.bottom {
  position: fixed;
  background-color: #fff;
  bottom: 0;
  width: 100%;
  padding: 10px;
  font-size: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  .el-input {
    width: 70%;
  }

  .el-icon {
    background-color: #fff;
    border-radius: 50%;
    padding: 2px;
  }
}
.content {
  padding: 10px 12px;
  margin-bottom: 40px;
}

:deep(.el-input__wrapper) {
  border-radius: 20px !important;
}


</style>