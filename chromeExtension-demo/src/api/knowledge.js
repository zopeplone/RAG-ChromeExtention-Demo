import request from '@/utils/request'

const storageKey = 'newKnowledge'
export async function getKnowledgeFromLocal(){
  let res = await chrome.storage.local.get([storageKey])
  return res[storageKey]
}

export async function sendKnowledge (str){
  return request({
    method: 'post',
    url: '/addKnowledge',
    data: { text: str }
  })

}