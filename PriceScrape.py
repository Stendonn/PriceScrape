# Scrapes a price from a specified size from StockX

from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

driver = webdriver.Chrome()  # For Chrome
driver.get("https://stockx.com/adidas-ultra-boost-4pt0-core-black")
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, "html.parser")

allSizesList = soup.find_all('div', attrs={'class': 'inset'})  # Collects all the sizes
# Change the index to the appropriate size. "All"is the first index.
size = allSizesList[11]  # Size 8.5(11th in list)
tag = size.text
priceIndex = tag.find('$') + 1
price = ''
while priceIndex < len(tag):
    price += str(tag[priceIndex])
    priceIndex += 1

body = MIMEText("StockX: Name of Sneaker is $" + price)  # Body of the email
body['Subject'] = '[Bot] Here are your prices'  # Subject
body['From'] = 'sender@gmail.com'  # From
body['To'] = 'receiver@gmail.com'  # To

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)  # For Gmail accounts
s.login(user='sender@gmail.com', password='senderpassword')  # The sender's email and password
s.sendmail('sender@gmail.com', 'receiver@gmail.com', body.as_string())  # Sender, receiver, MIMEText to string
s.quit()
driver.close
