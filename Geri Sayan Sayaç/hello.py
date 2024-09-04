import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        #divmod bölüm ve kalanı döndürür.(ilk değeri ikinci değere böler.)

        timer = f'{mins:02d}:{secs:02d}'
        # argümandan sonra :02d ifadesi kaç basamaklı olacağını belirler.
        print(timer, end="\r", flush=True)
        time.sleep(1)
        seconds -= 1

while True:
    try:
        sure = int(input('Süre girin (Saniye): '))
        countdown_timer(sure)
        break #Eğer geçerli bir sayı girildiyse döngüden çık
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

