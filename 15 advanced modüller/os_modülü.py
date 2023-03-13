import os
import datetime

# result = os.name # nt çıktısıını verir bunun anlamı windows işletim s.kullanıyorsun
# result = os.getcwd() #bu dosyanın nerde olduğunu gösterir.

# #dizi deiştirme
# os.chdir('C:\\') #change directory c dosyasının altına geçer
# os.chdir('..') #üst klasöre gider
# os.chdir('..\\..') #2 üst klasöre gider

# #klasor olşturma
# os.mkdir("newdirectory") #dosyayı bu klasörde oluşturur
# os.makedirs("newdirectory/yeniklasör") #klasör altındda klasör oluşturma imkanı verir
# os.rename("newdirectory","yeniklasör") #adını değiştirmek için kullanılır
# os.rmdir("newdirectory")   #newdirectory dosyasını siler alt klasör olmamalı
# os.removedirs("newdirectory/yeniklasör") #dosyanın altındaki yeniklasörü sileros

# #listeleme
# result = os.listdir() #şu an bu çalıştığımız dosyadaki etkin dosyaları listeler
# result = os.listdir('C:\\') # parantezin içindeki dosyada etkin dosyaları listeler

# #filtreleme
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# # parantezin içerisendeki dosya hakında bilgi alma
# result = os.stat("date_module.py")
# result0 = result.st_size #dosya boyutunu byte cinsinden verir
# result1 = datetime.datetime.fromtimestamp(result.st_ctime) #dosyanın oluşturduğu tarihi verir
# result2 = datetime.datetime.fromtimestamp(result.st_atime) #dosyanın son erişilme tarihi verir
# result = datetime.datetime.fromtimestamp(result.st_mtime) #dosyanın son değiştirilme tarihini verir

# os.system("notepad.exe") #notead dosyası açari

#path
result = os.path.abspath("os_modülü.py")
result0 = os.path.dirname("C:/Users/Casper/Desktop/pyhton_denemeleri/os_modülü.py")
result1 = os.path.dirname(os.path.abspath("os_modülü.py"))
result2 = os.path.exist("C:/Users/Casper/Desktop/pyhton_denemeleri/os_modülü.py") #bu klasör var mı bakar
result3 = os.path.isdir("pyhton_denemeleri") #bu bir klasör mü bakar
result3 = os.path.isdir("pyhton_denemeleri/os_modülü.py") #bu bir klasör mü bakar
result4 = os.path.isfile("pyhton_denemeleri/os_modülü.py") #bu bir klasör mü bakar
result5 = os.path.join("C:\\","deneme","deneme1") #verilenleri birleştirebilirsin ilk dosya ile başlayıp sırayla altına koyar
result6 = os.path.split("C:\\deneme") #verilenleri birbirinden ayırır
result7 = os.path.splitext("os_modülü.py") #ismi ile uzantısını ayırır

print(result)
print(result0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
