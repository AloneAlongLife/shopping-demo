# 從0開始做一個購物網站-FastAPI淺介 Day-1
###### tags: `從0開始做一個購物網站`
> 撰寫時間: 2023/08/24

[TOC]

## 零、前言
本系列將會記錄如何從無到有建立一個購物網站，不定期更新，但會盡量控制在一個禮拜內，因此文章標題仍以`Day-天數`紀錄。~~如果超過一個禮拜沒更新 大概率是做不下去了~~

此專案的Github連結: [https://github.com/AloneAlongLife/shopping-demo](https://github.com/AloneAlongLife/shopping-demo)

Github的更新進度跟本系列**不會同步**，因為經驗的關係，專案的步驟對於新手可能會顯得有些無厘頭(例如第一個步驟就是先將設定檔寫好，但必須要先用過個套件後才會知道需要那些設定)，因此不會依照開發進度撰寫文章，所以可能會出現文章中的東西在專案裡沒有，或是專案中的語法在文章中沒有提到，還請耐心等待、多多包涵。

然後文章中有些語法我也不知道為甚麼~~就是抄來的~~，所以只會講個大概，或是我自己的理解，也歡迎各位進行補充、指正。

## 壹、為何選用FastAPI
相比於其他Web框架，FastAPI的特點在其官網以及網路上其他的文章中都有詳細的介紹，在這裡就不多做贅述，主要就是快速、簡單、易用。

## 貳、快速建立一個Hello World
### 一、安裝套件
除了FastAPI外，還會需要運行服務的套件，在[FastAPI的文件](https://fastapi.tiangolo.com/zh/#_3)上提供了兩種選擇，分別是Uvicorn與Hypercorn，在這個系列中將會使用Uvicorn做為示範。

##### 透過pip安裝
```bash
pip install fastapi uvicorn
```

### 二、Hello World
新增一個`main.py`，並在其中寫入以下內容：
```python=1
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"
```
打開終端機，輸入：
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
應該會得到以下內容：
```
INFO:     Started server process [17204]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
這個時候打開瀏覽器，前往[http://localhost:8000](http://localhost:8000)，應該會看到一個`"Hello World"`出現在左上角，那就代表你已經成功啟動了伺服器。

### 三、拆分講解
1. 導入套件
```python=1
from fastapi import FastAPI
```

2. 建立一個Fast API Application
```python=3
app = FastAPI()
```

3. 建立路徑
```python=5
@app.get("/")
def read_root():
    return "Hello World"
```
在FastAPI中是利用修飾器(Decorator)去定義路徑，前面的`app`就是在上一步中所建立的物件，括號中的`"/"`就是路徑，而中間的`get`則代表請求這個路徑的方式，共有以下幾種：
- GET: `get`
- POST: `post`
- PUT: `put`
- DELETE: `delete`

在同一個路徑下，可以定義多種不同的請求方法，用以應對不同的狀況，例如：
```python=
@app.get("/")
def get_root():
    return "GET"

@app.post("/")
def post_root():
    return "POST"

@app.put("/")
def put_root():
    return "PUT"

@app.delete("/")
def delete_root():
    return "DELETE"
```

:::info
關於修飾器的運作方式相對比較複雜，在這裡就不做解釋，有興趣的可以自行查詢。
:::

## 參、測試API
在`/docs`的路徑下，FastAPI會自動生成文件，裡面包含了各個接口的路徑、需要填入的參數、發送請求的方法以及回傳的資料型態，並且可以即時進行互動，為開發者提供許多方便。

---
上一篇: [從0開始做一個購物網站-架構整理 Day-0](https://hackmd.io/@zhihao/shopping-site-d0)

下一篇: [從0開始做一個購物網站-傳遞資料 Day-2](https://hackmd.io/@zhihao/shopping-site-d2)
