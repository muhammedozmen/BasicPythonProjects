import requests
import schedule
import time

mobile_number = "+900000000000"

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Good morning!',
        'key': 'textbelt'
    })

    print(resp.json())

# Every morning at 6 am
# schedule.every().day.at('09:00').do(send_message)

# Every 10 seconds
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)