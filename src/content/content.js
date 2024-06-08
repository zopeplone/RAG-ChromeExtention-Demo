import { createApp } from 'vue'
import App from './App.vue'
export const knowLedgeKey = 'knowledge'
const root = document.createElement('div')
root.id = 'crxRoot'
document.body.append(root)

const app = createApp(App)
app.mount(root)