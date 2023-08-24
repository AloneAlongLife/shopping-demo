# 從0開始做一個購物網站-接收資料 Day-2
###### tags: `從0開始做一個購物網站`
> 撰寫時間: 2023/08/25

[TOC]

## 零、前言
本系列將會記錄如何從無到有建立一個購物網站，不定期更新，但會盡量控制在一個禮拜內，因此文章標題仍以`Day-天數`紀錄。~~如果超過一個禮拜沒更新 大概率是做不下去了~~

此專案的Github連結: [https://github.com/AloneAlongLife/shopping-demo](https://github.com/AloneAlongLife/shopping-demo)

Github的更新進度跟本系列**不會同步**，因為經驗的關係，專案的步驟對於新手可能會顯得有些無厘頭(例如第一個步驟就是先將設定檔寫好，但必須要先用過個套件後才會知道需要那些設定)，因此不會依照開發進度撰寫文章，所以可能會出現文章中的東西在專案裡沒有，或是專案中的語法在文章中沒有提到，還請耐心等待、多多包涵。

然後文章中有些語法我也不知道為甚麼~~就是抄來的~~，所以只會講個大概，或是我自己的理解，也歡迎各位進行補充、指正。

## 壹、使用者與伺服器間的溝通
在大多數時候，伺服器並不會主動向使用者傳遞資料，必須先由客戶端向伺服器發出請求，伺服器才能夠將資料傳給使用者；當然也有少數時候可以由伺服器主動傳遞資料給使用者，如`WebSocket`。

而伺服器如果要辨識每個請求分別來自哪個使用者，就必須依靠使用者發送的請求中所附帶的資料，而常見的附帶方式有以下幾種：
 - 路徑參數 - Path Parameters
    - 透過請求的路徑取得資料，如`/page/tutorial`，則`page`與`tutorial`可擇一做為資料接收。
 - 查詢參數 - Query Parameters
    - 透過在網址尾端附加的查詢字串附帶資料，如`/page/tutorial?id=0&type=web`，伺服器就會接收到`id=0`以及`type=web`的資料。
 - 請求主體 - Request Body
    - 常見於`POST`類別的請求，透過附加在請求中的資料傳遞參數，可傳送各種類型的資料與檔案，不限於文字。

## 貳、實作不同的接收方法
:::info
在開始之前，要先介紹一下，FastAPI在處理資料上是使用Pydantic模組，該模組會針對傳入的參數進行型別檢查與轉換，例如定義一個變數為整數型別，那傳入的值就必須是整數型別，如果傳入其他類型(例如：字串)，將會引發例外情形(Exception)。
:::
### 一、路徑參數
透過在路徑中使用`{變數名稱}`，即可將該部分的路徑作為參數傳入函式，如下程式碼所示：
```python=
from fastapi import FastAPI

app = FastAPI()

@app.get("/{text}")
def root(text: str):
    return f"Hello {text}!"
```
啟動服務後前往[http://localhost:8000/World](http://localhost:8000/World)，應該就會看到顯示的內容是`"Hello World!"`，也可自行將斜線後方的`World`替換為其他字串進行嘗試。
:::warning
:warning: 使用路徑傳值並不一定要使用最後一段作為參數，也可放在路經中間，例如`/page/{page_id}/content`，但要注意的是，在一段路徑中只能使用其中一部份作為參數，不可同時將兩段以上的路徑作為參數傳入，例如`/page/{page_id}/content/{content_id}`。
:::

### 二、查詢參數
透過在網址最末端使用`?`分隔網址與查詢字串，參數使用`=`賦值，在各參數之間使用`&`區隔，可以一次傳遞多個參數，但要注意的是網址是具有長度上限的，因此較不適合用於須傳送大量資料的場合。
```python=
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(text: str, times: int = 1):
    return f"Hello {text}!" * times
```
啟動服務後前往[http://localhost:8000?text=Python&times=2](http://localhost:8000?text=Python&times=2)，應該就會看到顯示的內容是`"Hello Python!Hello Python!"`，同樣，也可將`text`與`times`更改為不同的值試試看。
 - 將`times`更改為整數以外的數值
    - 如果將`times`更改為整數以外的數值，例如[http://localhost:8000?text=Python&times=a](http://localhost:8000?text=Python&times=a)，會看到頁面中出現一串的錯誤訊息，這個情形即為先前所說到的Pydantic的型別檢查，透過在函式的參數上定義型別，確保函式能夠接收正確的內容，從而避免運行中出現錯誤，更多內容可以查看[Pydantic的文件](https://docs.pydantic.dev/1.10/)
    :::warning
    :warning: 同樣由於SQLModel的關係，本系列文章使用的Pydantic版本為1.10，與目前最新版本的2.3會有些許差異，在查詢資料時還請特別注意。
    :::
 - 將`times`留空
    - 如果將`times`留空的的話，會發現仍然可以正常運作，顯示的內容會是`"Hello Python!"`，這是因為在函式中已經先將參數`times`預填為`1`，因此如果使用者沒有傳入任何參數的話，便會以預設值帶入，如果沒有填入預設值的話(如參數`text`)，如果劉空就會引發例外情形。

### 三、請求主體
請求主體的傳送方法主要是在前端中，將資料填入於發送函式的參數中，這邊建議使用FastAPI所產生的互動式文件進行操作。
```python=
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def root(text: str):
    return f"Hello {text}!"
```
啟動服務後前往[http://localhost:8000/docs#/default/root__post](http://localhost:8000/docs#/default/root__post)，點擊右側的`Try it out`即可進行互動，嘗試於下方的`text`輸入框中填入`FastAPI`，並且按下底下的`Execute`，即可於下方`Server response`的`Response body`欄位看到回傳資料，應該會是`"Hello FastAPI!"`。

## 參、測試小技巧
每次更改內容就必須終止Uvicorn並且重新啟動很麻煩嗎?可以嘗試於指令最後面加上`--reload`變成：
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
`--reload`參數的意思是告訴Uvicorn如果有偵測到伺服器的運作文件產生變動，就將服務重新載入，能夠有效增加開發人員的工作效率。

---
上一篇: [從0開始做一個購物網站-FastAPI淺介 Day-1](https://hackmd.io/@zhihao/shopping-site-d1)

下一篇: [從0開始做一個購物網站-Pydantic簡易教學 Day-3](https://hackmd.io/@zhihao/shopping-site-d3)
