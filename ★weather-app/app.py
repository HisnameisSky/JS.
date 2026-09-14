import urllib.request
import urllib.error
import json

# getWeather 関数
async def get_weather(city: str):
    url = f"https://weather-proxy.freecodecamp.rocks/api/city/{city}"
    try:
        # 非同期/同期リクエストでデータを取得
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                raise Exception(f"HTTP error! status: {response.status}")
            
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as error:
        print(error)
        return None

# showWeather 関数
async def show_weather(city: str):
    if not city:
        return

    data = await get_weather(city)

    if not data:
        print("Something went wrong, please try again later") # alertの代わり
        return

    # オプショナルチェイニング (?.) と ヌル合体演算子 (??) の再現
    def get_val(data_dict, keys, default="N/A"):
        curr = data_dict
        for k in keys:
            if isinstance(curr, list) and isinstance(k, int) and 0 <= k < len(curr):
                curr = curr[k]
            elif isinstance(curr, dict) and k in curr:
                curr = curr[k]
            else:
                return default
        return curr if curr is not None else default

    # データ（箱）から各値を取り出して画面（UI要素）へ設定するデータ移動
    weather_icon = get_val(data, ["weather", 0, "icon"])
    main_temperature = get_val(data, ["main", "temp"])
    feels_like = get_val(data, ["main", "feels_like"])
    humidity = get_val(data, ["main", "humidity"])
    wind = get_val(data, ["wind", "speed"])
    wind_gust = get_val(data, ["wind", "gust"])
    weather_main = get_val(data, ["weather", 0, "main"])
    location = get_val(data, ["name"])

    # 画面表示
    print(f"Location: {location}")
    print(f"Weather: {weather_main} (Icon: {weather_icon})")
    print(f"Temperature: {main_temperature}°C (Feels like: {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s (Gust: {wind_gust} m/s)")

# 実行シミュレーション（ボタンクリック時の動作）
import asyncio

async def main():
    selected_city = "tokyo"  # ドロップダウンで選択された値
    if selected_city:
        await show_weather(selected_city)

if __name__ == "__main__":
    asyncio.run(main())