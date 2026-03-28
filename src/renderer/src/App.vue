<template>
  <div class="min-h-screen p-6 bg-gray-50 text-gray-800">
    <!-- 头部区域 -->
    <header class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">🤡 Temu AI 选品终端</h1>
        <p class="text-sm text-gray-500 mt-1">基于 OpenClaw 的自动化跨平台比价与数据抓取</p>
      </div>
      <button
        :disabled="isRunning"
        class="bg-orange-500 hover:bg-orange-600 text-white px-6 py-2 rounded-lg font-medium shadow-md transition-colors disabled:bg-gray-400"
        @click="runAgent"
      >
        {{ isRunning ? '🤖 AI 正在抓取中...' : '▶ 运行选品任务' }}
      </button>
    </header>

    <!-- 数据表格卡片 -->
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-100 bg-white">
        <h2 class="text-lg font-semibold text-gray-700">最新高潜商品池 (美区)</h2>
      </div>

      <table class="w-full text-left border-collapse bg-white">
        <thead>
          <tr class="bg-gray-50 text-sm text-gray-500">
            <th class="px-6 py-3 font-medium">商品品类</th>
            <th class="px-6 py-3 font-medium">Temu 均价</th>
            <th class="px-6 py-3 font-medium">1688 拿货底价</th>
            <th class="px-6 py-3 font-medium">预估利润差</th>
            <th class="px-6 py-3 font-medium">状态</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          <tr
            v-for="(item, index) in productList"
            :key="index"
            class="hover:bg-gray-50 transition-colors"
          >
            <td class="px-6 py-4 font-medium text-gray-800">{{ item.name }}</td>
            <td class="px-6 py-4 text-gray-600">$ {{ item.temuPrice }}</td>
            <td class="px-6 py-4 text-gray-600">¥ {{ item.factoryPrice }}</td>
            <td class="px-6 py-4">
              <span class="px-2 py-1 bg-green-100 text-green-700 rounded-md text-sm font-bold">
                {{ item.margin }}
              </span>
            </td>
            <td class="px-6 py-4">
              <a href="#" class="text-blue-500 hover:text-blue-700 text-sm">查看详情</a>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- 空状态展示 -->
      <div v-if="productList.length === 0" class="p-8 text-center text-gray-400 bg-white">
        暂无选品数据，点击右上角运行任务
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 💡 这里是 TypeScript 的魔法：定义数据结构，让编辑器给你完美的智能提示
interface Product {
  name: string
  temuPrice: string
  factoryPrice: string
  margin: string
}

// 响应式状态（加上类型注解）
const isRunning = ref<boolean>(false)
const productList = ref<Product[]>([])

// 模拟触发底层的 OpenClaw 任务
const runAgent = async (): Promise<void> => {
  isRunning.value = true

  setTimeout(() => {
    productList.value = [
      { name: 'Switch 2 磁吸保护壳', temuPrice: '8.99', factoryPrice: '6.50', margin: '高利润' },
      { name: 'Fuse Beads 拼豆套装', temuPrice: '12.50', factoryPrice: '12.00', margin: '中利润' },
      { name: '复古咖啡手摇磨豆机', temuPrice: '19.99', factoryPrice: '25.00', margin: '建议开发' }
    ]
    isRunning.value = false
  }, 2000)
}
</script>
