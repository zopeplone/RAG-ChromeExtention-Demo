<script setup>
import { onMounted, ref } from 'vue';
import { addNewKnowledge } from './mapper/knowledge'
import { ElMessage } from 'element-plus';
const addSelectListener =() =>{
  var str = ''
  // 添加 mouseup 事件监听器
  document.addEventListener('mouseup', handleMouseUp);

  // 添加 selectionchange 事件监听器
  document.addEventListener('selectionchange', handleSelectionChange);

  // 处理 mouseup 事件的回调函数
  function handleMouseUp(event) {
    // 在这里处理鼠标选中文本事件结束的逻辑
    if (str.length !== 0) {
      // console.log(event)
      // console.log('鼠标选中文本事件结束', str);
      let x = event.clientX + window.scrollX, y = event.clientY + window.scrollY
      showContent(x,y)
      str = ''
    }
  }
  // 处理 selectionchange 事件的回调函数
  function handleSelectionChange(event) {
    // 检查选中的文本范围是否为空
    const selection = window.getSelection();
    if (selection && selection.toString().length != 0) {
      // 在这里处理文本选中取消的逻辑
      str = selection.toString()
    }
    else{
      hideContent()
    }
  }
}
onMounted(()=>{
  addSelectListener()
  content.value.addEventListener('mousedown', function (event) {
    event.preventDefault();
  })
})
const content = ref(null)
const showContent = (x,y)=>{
  let {style} = content.value
  style.display = 'block'
  style.top = `${y}px`
  style.left = `${x}px`
}
const hideContent = ()=>{
  let { style } = content.value
  style.display = 'none'
}
const addSelectToKnowLedge =async ()=>{
  let str = window.getSelection().toString()
  await addNewKnowledge(str)
  hideContent()
}
</script>
<template>
  <div class="content" ref="content">
    <div class="content-box">
      <div class="content-box-item" @click="addSelectToKnowLedge">
        添加进知识库
      </div>
      <div class="content-box-item" style="border-right: none;">
        页面放入知识库
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.content {
  display: none;
  position: absolute;
  z-index: 100000;
  top: 0;
  background-color: #484848;
  width: 180px;
  height: 30px;
  border-radius: 20px;
  overflow: hidden;

  &-box{
    display: flex;
    align-items: center;
    height: 100%;
    &-item{
      flex-grow: 1;
      font-size: 12px;
      color: #fff;
      border-right: 1px solid #353535;
      text-align: center;
      cursor: pointer;
      align-content: center;
      height: 100%;
      &:hover{
        background-color: #5a5a5a;
        color: #353535;
      }
    }
  }
}
</style>