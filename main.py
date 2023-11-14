from bs4 import BeautifulSoup
import requests
import smtplib,ssl


URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers_a ={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
MY_EMAIL = ""
MY_PASSWORD = ""
response = requests.get(URL,headers = headers_a)
website = response.text
soup = BeautifulSoup(website,'html.parser')
price = float(soup.find(class_='a-offscreen').get_text().split('$')[1])

context = ssl.create_default_context()

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,to_addrs = MY_EMAIL,msg="Time to buy")
