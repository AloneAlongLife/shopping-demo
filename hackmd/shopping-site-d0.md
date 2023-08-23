# 從0開始做一個購物網站-架構整理 Day-0
###### tags: `從0開始做一個購物網站`
> 撰寫時間: 2023/08/23

[TOC]

## 零、前言
本系列將會記錄如何從無到有建立一個購物網站，不定期更新，但會盡量控制在一個禮拜內，因此文章標題仍以`Day-天數`紀錄。~~如果超過一個禮拜沒更新 大概率是做不下去了~~

此專案的Github連結: [https://github.com/AloneAlongLife/shopping-demo](https://github.com/AloneAlongLife/shopping-demo)

## 壹、語言與框架
### 一、前端
 - 語言
     - TypeScript(TSX)
     - SCSS
 - 框架
     - React

### 二、後端
 - 語言
     - Python(>=3.10)
 - 框架
     - FastAPI

## 貳、架構
### 一、頁面
 - 主頁面
     - 重點商品
     - 搜尋列
     - 個人資料
     - 購物車
     - 登入
 - 搜尋頁
     - 商品列表
         - 圖像顯示
         - 清單顯示
     - 過濾功能
     - 商品簡述
 - 商品頁
     - 商品圖片
     - 商品資料
     - 加入購物車
 - 個人資料
     - 更改密碼
     - 購買清單
 - 購物車頁面
     - 移除商品
     - 更改數量
     - 結帳
 - 管理頁面
     - 訂單列表
     - 更新狀態
     - 上架商品
     - 下架商品

### 二、API
 - GET
     - 重點商品
         - 列表[商品]
         - `200 OK`
     - 關鍵字搜尋
         - 列表[商品]
         - `200 OK`
     - 取得商品資料
         - 商品
         - `200 OK`
         - `404 Not Found` 商品不存在
     - 購買紀錄
         - 列表[購買紀錄]
         - `200 OK`
         - `401 Unauthorized` 未登入
     - 購物車
         - 列表[字典[商品, 整數]]
         - `200 OK`
         - `401 Unauthorized` 未登入
     - 個人資料
         - 使用者
         - `200 OK`
         - `401 Unauthorized` 未登入
     - 訂單列表
         - 列表[購買紀錄]
         - `200 OK`
         - `401 Unauthorized` 未登入
 - POST
     - 登入
         - 傳送
             - 帳號
             - 密碼
         - 回傳
             - `200 OK` 登入成功
             - JSON Web Tokens(JWT)
             - `403 Forbidden` 帳號密碼錯誤
     - 結帳
         - 回傳
             - `200 OK` 結帳成功
             - `400 Bad Request` 商品資料錯誤
             - `401 Unauthorized` 未登入
     - 上架商品
         - 傳送
             - 商品
         - 回傳
             - `201 Created` 上架成功
             - `401 Unauthorized` 未登入
             - `403 Forbidden` 權限不足
 - PUT
     - 新增至購物車
         - 傳送
             - 商品
             - 數量
         - 回傳
             - `200 OK` 新增成功
             - `401 Unauthorized` 未登入
             - `404 Not Found` 商品不存在
     - 更改數量
         - 傳送
             - 商品
             - 數量
         - 回傳
             - `200 OK` 更改成功
             - `401 Unauthorized` 未登入
             - `404 Not Found` 商品不存在
     - 更改密碼
         - 傳送
             - 舊密碼
             - 新密碼
         - 回傳
             - `200 OK` 更改成功
             - `401 Unauthorized` 未登入
             - `403 Forbidden` 舊密碼錯誤
     - 更新訂單狀態
         - 傳送
             - 購買紀錄編號
             - 狀態
         - 回傳
             - `200 OK` 更新成功
             - `401 Unauthorized` 未登入
             - `403 Forbidden` 權限不足
 - DELETE
     - 自購物車移除
         - 傳送
             - 商品UUID
         - 回傳
             - `204 No Content` 移除成功
             - `401 Unauthorized` 未登入
             - `404 Not Found` 商品不存在
     - 下架商品
         - 傳送
             - 商品UUID
         - 回傳
             - `204 No Content` 下架成功
             - `401 Unauthorized` 未登入
             - `403 Forbidden` 權限不足
             - `404 Not Found` 商品不存在

### 三、資料結構
 - 商品
     - UUID
         - 字串
     - 剩餘數量
         - 整數
     - 標題
         - 字串
     - 簡述
         - 字串
     - 價錢
         - 整數
     - 是否為重點商品
         - 布林
     - 圖片張數
         - 整數
 - 使用者
     - UUID
         - 字串
     - 名稱
         - 字串
     - 密碼
         - 字串(加密)
     - 電話號碼
         - 字串
     - 密碼更改時間
         - 整數
     - 購買紀錄
         - 列表[整數]
     - 購物車
         - 列表[字典[字串, 整數]]
     - 是否為管理員
         - 布林
 - 購買紀錄
     - 編號
         - 整數
     - 商品列表
         - 列表[字典[字串, 整數]]
     - 金額
         - 整數
     - 狀態
         - 整數
     - 購買人
         - 字串
 - JSON Web Tokens(JWT)
     - 使用者UUID
         - 字串
     - IP(加密)
         - 字串
     - 密碼更改時間
         - 整數
     - 過期時間: 1天

---
下一篇: [我還沒想好標題](https://hackmd.io/@zhihao/shopping-site-d1)