import { sendKnowledge } from '@/api/knowledge'

const storageKey = 'newKnowledge'

export async function addNewKnowledge (str){
  let res = await chrome.storage.local.get([storageKey])
  if(res[storageKey]){
    res = res[storageKey]
  }
  else res = []
  res.push(str)
  let obj = {}
  obj[storageKey] = res
  await chrome.storage.local.set(obj)
  res = await sendKnowledge(str)
  return
}