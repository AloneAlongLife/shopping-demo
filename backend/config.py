from os.path import isfile

from orjson import loads, dumps, OPT_INDENT_2
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

EXAMPLE_CONFIG = {
    "address": "0.0.0.0",
    "port": 8080,
    "secret": "",
    "db_url": "sqlite+aiosqlite:///data.db",
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

with open("config.json", "rb") as config_file:
    CONFIG: dict = loads(config_file.read())

ADDRESS: str = CONFIG.get("address", "0.0.0.0")
PORT: int = CONFIG.get("port", 8080)
SECRET: str = CONFIG.get("secret", "")
DEBUG: bool = CONFIG.get("debug", False)

db_url = CONFIG.get("db_url", "sqlite+aiosqlite:///data.db")
engine = create_async_engine(
    db_url,
    connect_args={
        "check_same_thread": db_url.startswith("sqlite"),
    }
)


# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False)
#     async with async_session() as session:
#         yield session
class get_session:
    async def __call__(self) -> AsyncSession:
        async_session = sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False)
        async with async_session() as session:
            yield session
    
    async def __aenter__(self):
        async_session = sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False)
        self.session: AsyncSession = async_session()
        return self.session
    
    async def __aexit__(self, _type, _value, _trace):
        await self.session.close()
        return True
