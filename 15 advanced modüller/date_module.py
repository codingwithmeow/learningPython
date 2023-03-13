"""
import datetime denince aşağıdaki iki modülde gelir ya da böyle de yapılabilir
"""
from datetime import datetime
from datetime import timedelta

now = datetime.now()
now = datetime.today()

result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second

result = datetime.ctime(now) # daha açıklayacağı bir ifade üretir.
result = datetime.strftime(now, "%Y") #sadece yılı verir
result = datetime.strftime(now, '%X') #sadece saati verir
result = datetime.strftime(now, "%d") #sadece günü verir
result = datetime.strftime(now, "%A") #günü string verir
result = datetime.strftime(now, "%B") #ayı string olarak verir
result = datetime.strftime(now, "%Y %B %A") #https://docs.python.org/3/library/datetime.html bakıabiilirsin 

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') #result obje oldu
result = result.year

birthday = datetime(1997,2,5,16,00,00)
result = datetime.timestamp(birthday) #saniye içerisinden getirir.
result = datetime.fromtimestamp(result) #yukarıda çevrilen saniye bilgisini datetime a geri çevirdik
result = datetime.fromtimestamp(0) #1970-01-01 03:00:00 bilgisayrın dğumgünü :)

result = now - birthday #timedelta objesi oluşuyor

# result = result.days #timedelta günü
# result = result.seconds #timedelta saniyesi

result = now + timedelta(days=10) # tarihe tarih eklemek için güzel bir fonksiyon
result = now + timedelta(days=10,minutes=10)


print(now)
print(result)
