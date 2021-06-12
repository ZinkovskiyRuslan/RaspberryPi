import requests

def send_telegram(text: str):
    token = "1884974244:AAFdrPUpTiJiQ-L-yonu-IpW0-O_sG780J0"
    url = "https://api.telegram.org/bot"
    channel_id = "-596762421"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception(r.content)
    
if __name__ == '__main__':
  send_telegram("hello world!")
