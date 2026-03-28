from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import uvicorn

app = FastAPI()

# 允许 Electron 跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/run_temu_task")
async def run_task():
    # 模拟 AI 抓取耗时
    await asyncio.sleep(2) 
    return {
        "status": "success",
        "data": [
            { "name": "Switch 2 磁吸保护壳", "temuPrice": "8.99", "factoryPrice": "6.50", "margin": "高利润" },
            { "name": "Fuse Beads 拼豆套装", "temuPrice": "12.50", "factoryPrice": "12.00", "margin": "中利润" }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)