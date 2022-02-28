import smtplib
import requests
from bs4 import BeautifulSoup
import time
from email.message import EmailMessage

url = 'https://www.defconlevel.com/current-level.php'


def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
        
    user = "undisputedbikesharing@gmail.com"
    msg['from'] = user
    password = "BO69rqe0eJi8"
        
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
        
    server.quit()


while(True):
    response = requests.get(url)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')


    for div in data.findAll('div',attrs={'header-defcon-level header-defcon-level-news-regions'}):
        text = div.text.strip().partition('\n')[0]
        if '(one)' in text.lower():
            email_alert("URGENT - NUCLEAR","DEFCON LEVEL 1 ACTIVATED","dekas.santos2@gmail.com")
            email_alert("URGENT - NUCLEAR","DEFCON LEVEL 1 ACTIVATED","joana.filipa.queiros@hotmail.com")
            
    print("Everything is calm.")
    time.sleep(900)
    

