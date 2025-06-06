功能介紹
透過OpenWeatherMap API查詢指定城市的即時天氣資訊
顯示天氣描述、溫度、體感溫度、濕度
Gmail 寄送 Email 
Jinja2 套件產生簡單 HTML Email 內容

使用方式
Clone 我的專案
pip install requests jinja2 python-dotenv
申請並填入 OpenWeatherMap API 金鑰
填入資料到 .env 
WEATHER_API_KEY=你的天氣API金鑰
EMAIL_SENDER=你的Gmail帳號
EMAIL_PASSWORD=Gmail應用程式密碼
EMAIL_RECEIVER=收件人Email

在終端輸入 python main.py
