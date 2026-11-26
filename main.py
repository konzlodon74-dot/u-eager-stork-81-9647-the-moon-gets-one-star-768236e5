import os

LINE = "★☆☆☆☆ Ghosts me monthly, returns glowing, expects applause. My tides filed a complaint. 1/5."

assert 1 <= len(LINE) <= 120, len(LINE)
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
