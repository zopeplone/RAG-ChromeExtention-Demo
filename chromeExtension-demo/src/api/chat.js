import request from '@/utils/request'
const storageKey = 'chatHistory'
export function chatWithServer(data){
  return request({
    method:'post',
    url:'/ask',
    data:{text:data}
  })
}
export async function getChatHistory(){
  let res = await chrome.storage.local.get([storageKey])
  return res[storageKey] || []
}
export async function setChatHistory(data){
  let obj = {}
  obj[storageKey] = data
  await chrome.storage.local.set(obj)
  return
}