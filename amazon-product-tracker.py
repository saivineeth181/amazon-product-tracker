import requests
from bs4 import BeautifulSoup
import smtplib
import logging as log
log.basicConfig(level=log.DEBUG)

url = "https://www.amazon.in/Lenovo-Ideapad-Laptop-Windows-81WD00AVIN/dp/B087D4RVHY/ref=psdc_1375424031_t3_B089F5JGM1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def check_price():
    page = requests.get(url,headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[2:4] + price[5:8])

    if(converted_price < 50000):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('stmp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('GMAIL','PASSWORD')

    subject = 'PRICE FELL DOWN'
    body = 'check the amazon link : url = https://www.amazon.in/Lenovo-Ideapad-Laptop-Windows-81WD00AVIN/dp/B087D4RVHY/ref=psdc_1375424031_t3_B089F5JGM1'

    msg = f"Subject :{subject}\n\n{body}"

    server.sendmail
    (
        'saivineeth181@gmail.com',
        'vuppala.saivineeth2018@vitstudent.ac.in',
        msg
    )

    print("EMAIL SENT SUCCESSFULLY")
    server.quit()

while True:
    check_price()
    time.sleep(84600)
