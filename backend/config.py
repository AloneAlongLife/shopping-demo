from os.path import isfile

from orjson import loads, dumps, OPT_INDENT_2

EXAMPLE_CONFIG = {
    "address": "0.0.0.0",
    "port": 8080,
    "secret": "",
    "db_url": "sqlite+aiosqlite://data.db",
    "check_same_thread": True,
    "debug": False
}

# 檢查設定檔是否存在
if not isfile("config.json"):
    # 若不存在，則重新生成
    with open("config.json", "wb") as config_file:
        config_file.write(dumps(EXAMPLE_CONFIG, option=OPT_INDENT_2))
    # 生成完成，等待用戶設定完成
    print("未找到設定檔，已重新生成，請前往更改內容。")
    input("更改完成後請按下Enter...")
