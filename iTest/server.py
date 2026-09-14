import math
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TSからのアクセスを許可する「結界（CORS設定）」
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/wave")
def get_wave_data():
    """世界の根本ロジック（意志）：サイン波の座標群を計算して返す"""
    t = time.time() * 2.0  # 時間の進み（速度）
    points = []
    
    # 20個の点の座標を計算（解像度）
    for i in range(21):
        x = i * 20  # 画面上のX座標（0〜400）
        # 時間(t)と位置(i)に応じて変化するY座標のロジック
        y = 200 + math.sin(i * 0.5 + t) * 50
        points.append({"x": x, "y": y})
        
    return {"points": points}


# --- 既存のコードの一番下に追加 ---

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
