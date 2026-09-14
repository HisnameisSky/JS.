from datetime import datetime
import locale

current_date = datetime.now()

current_date_format = f"Current Date and Time: {current_date.strftime('%a %b %d %Y %H:%M:%S')}"


print(current_date_format)

def format_date_mmddyyyy(date_obj: datetime) -> str:
    month = date_obj.month  # Pythonの月は 1〜12 (0始まりではない)
    day = date_obj.day
    year = date_obj.year
    return f"Formatted Date (MM/DD/YYYY): {month}/{day}/{year}"

def format_date_long(date_obj: datetime) -> str:
    # 英語表記 (en_US) の月名を取得するため一時的にロケールを変更
    # (環境依存を避けるため strftime ではなく辞書や明示的なフォーマットを使用可能)
    month_name = date_obj.strftime("%B")  # 例: "September"
    day = date_obj.day
    year = date_obj.year
    formatted_date = f"{month_name} {day}, {year}"
    return f"Formatted Date (Month Day, Year): {formatted_date}"


###

from datetime import datetime

# 現在の日時を取得
now = datetime.now()

# ① 日本で標準的な「年月日 時:分:秒」表記
print(now.strftime("%Y/%m/%d %H:%M:%S"))
# 出力例: 2026/09/04 06:05:09

# ② 英語の長形式表記（例: Friday, September 04, 2026）
print(now.strftime("%A, %B %d, %Y"))
# 出力例: Friday, September 04, 2026

# ③ 12時間表記（例: 06:05 AM）
print(now.strftime("%I:%M %p"))
# 出力例: 06:05 AM

# ④ ファイル名やログに適したハイフン・アンダースコア区切り
print(now.strftime("%Y%m%d_%H%M%S"))
# 出力例: 20260904_060509

print(now.strftime("%-m/%-d/%-d/%Y"))

date_str = "2026-09-04 06:05:09"

date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

#

from datetime import datetime
date_obj = datetime.strptime("2026-09-04 15:30:00", "%Y-%m-%d %H:%M:%S")

dt1=datetime.strptime("2026/09/04","%Y/%m/%d")
dt2 = datetime.strptime("Sep 04, 2026", "%b %d, %Y")
dt3 = datetime.strptime("03:30 PM", "%I:%M %p")

#

from datetime import datetime
from zoneinfo import ZoneInfo

naive_dt = datetime.now()
jst_dt=naive_dt.replace(tzinfo=ZoneInfo("Asia/Tokyo"))
utc_dt=jst_dt.astimezone(ZoneInfo("UTC"))

print("JST",jst_dt)
print("UTC",utc_dt)

now_utc = datetime.now(ZoneInfo("UTC"))
now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))

dt_with_tz = datetime.strptime("2026-09-04 15:30:00 +0900", "%Y-%m-%d %H:%M:%S %z")

print(dt_with_tz)