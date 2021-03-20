# CYRDG Backend exercise

## Question 1
```python=
def f(num):
    try:
        return str(format(num, ','))
    except:
        print("An exception occurred")
        return None
```

numericFormat.py
輸入為 數值(int / float) 若輸入型態錯誤 return None

## Question 2
pipe.py

使用unittest module 進行unit test

第一個參數為any type, 後續為不定長度輸入(function)
若輸入錯誤(輸入不為function)或function處理錯誤則拋出例外 return None

## Question 3
### Reading
1. 升級硬體(增加server記憶體 or CPU)
2. 觀察資料庫log 依照需求建立索引
3. 檢視資料庫查詢語句避免不必要查詢
4. 檢視table若情況許可優化資料表結構

### Writing
1. 升級硬體(增加server記憶體 or CPU)
2. 依照需求建立索引
3. 執行批次寫入,減少 commit 次數

## Question 4
### Requrement
1. BeautifulSoup4
2. requests

### Usage
使用 shell script 執行 application
```
./crawler.sh <action> <arg1> [<arg2>...]
```
crawler.sh 將會執行 crawler.py

crawler.py 將會將任務依照所輸入的參數派發給指定程式

若需新增任務只需新增python檔案即可

若錯誤則拋出例外
