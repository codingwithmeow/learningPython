import re

# #re modülü
str = "Python Kursu : Python Programlama Rehberiniz | 40 saat"

# result = re.findall("Python",str) # iikincisi içerinde ilki arar ve ['Python', 'Python'] verir
# result1 = len(result) # yukarıdakinden kaçtane olduğuna bakmak için böyle yapabiliriz
# result2 = re.split(" ",str) # verilenden böler
# result3 = re.sub(" ","-",str) # \s yani boşluğu - ile değiştirir
# result4 = re.search("Python",str) # <re.Match object; span=(0, 6), match='Python'> match objesi oluşturur ilk bulduğunu gösterir diğerlerine bakmaz
# result5 = result4.span() # (0,6) verir
# result6 = result4.start() # başlangıcı verir
# result7 = result4.end() #bitişi verir
# result8 = result4.group() # bulduğu ifadeyi döndürür
# result9 = result4.string # arama işlemimindeki aradığı stringi döndürür

# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
# print(result8)
# print(result9)

# regular expression
"""
    [] Köşeli parantenler arasına yazıkan bütün karakterler aranır

    [abc] => a      : 1 match
             ac     : 2 match 
             Python : No match

    [a-e]  => [abcde]
    [1-5]  => [12345]
    [0-39] => [01239]  0 ile 3 arası

    [^abc] => abc dışındaki karakterler
    [^0-9] => rakam hatiricindeki bütün karekteleri bulur
"""
result = re.findall("[abc]",str)
result1 = re.findall("[Python]",str)
result1 = re.findall("[a-e]",str)
result1 = re.findall("[a-z]",str)
result1 = re.findall("[0-5]",str)
result1 = re.findall("[^abc]",str)
result1 = re.findall("[^0-9]",str)

# print(result) # buldğunda hepsini yazdırır
# print(result1)

"""
    . Her hangi bir tek karektei belirtir

        .. => a    : No Match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 match
"""
result = re.findall("...",str)
result1= re.findall("Py..on",str)

# print(result) 
# print(result1)

"""
    ^ Belirtilen karakterle başlıyor mu

        ^a => a    : 1 Match
              ab   : 1 match
              abc  : 1 match
              bac  : No match
"""
result = re.findall("^P" , str) #str en başında p var mı
print(result)

"""
    $ Belirtilen karakterle bitiyor mu

        a$ => a      : 1 match
              lamda  : 1 match
              Python : No match
"""
result = re.findall("t$" , str) #str sonunda t var mı
result = re.findall("saat$" , str) #str sonunda saat var mı

# print(result)

"""
    * Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder

        ma*n => mn   : 1 match
                man  : 1 match
                maan : 1 match
                main : No match (a nın arkasina i gelmiş n değil ondan no match)
"""
result = re.findall("sa*t" , str) #str sonunda saat var mı

# print(result)

"""
    + Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder

        ma+n => mn   : No match
                man  : 1 match
                maan : 1 match
                main : No match (a nın arkasina i gelmiş n değil ondan no match)
"""
result = re.findall("sa+t" , str) #str sonunda saat var mı

# print(result)

"""
    ? Bir karakterin sıfır ya da br kez olmasını kontrol eder

        ma?n => mn   : No match
                man  : 1 match
                maan : 1 match
                main : No match (a nın arkasina i gelmiş n değil ondan no match)
"""
result = re.findall("sa?t" , str) #str sonunda saat var mı

# print(result)

"""
    {} Karakter sayısını kontrol eder 

        al{2}      : a karekterinin arkasına l karekteri 2 kez tekrarlamalı
        al{2,3}    : a karekterinin arkasına l karekter en az 2 en fazla kez tekrarlamalı
        [0-9]{2,4} : en az 2 en çok 4 basamaklı sayılar
"""
result = re.findall("a{2}" , str) 
result = re.findall("[0-9]{2}" , str) #str de 2 basamaklı sayı var mı 

print(result)
""" 
    |  or demek

        a|b => a ya da b

            cde    : No match 
            ade    : 1 match
            acdbea : 3 match
"""

"""
    () gruplamak için kullanılır

        (a|b|c)xz : a,b,c karakterlerinin arkasına xz gelmelidir
"""

"""
    \ Özel karakterleri aramamazı sağlar

        \$a : karakterlerinin arkasına a karakterini arar.Yani 
              $ regular exp. tarafından yorumlanmaz

        \A  : Belirtilen karakter stringin başında mı
              \Athe : the stringin başında mı

        \Z  : Belirtilen karakter stringin sonunda mı
              the\Z : the stringin sonunda mı

        \b  : Belirtilen karakter stringin başındda mı ya da sonunda mı
              \bthe : the stringin başında mı
              the\b : the stringin sonunda mı

        \B  : Belirtilen karakter stringin başındda mı ya da sonunda değil mı
              \Bthe : the stringin başında mı
              the\B : the stringin sonunda mı

        \d  : [0-9] ile aynı anlama gelir yani rakamları arar
              \d : 12abcde

        \D  : [^0-9] ile aynı anlama gelir yani rakam olmayanları arar
              \D : 1ab44_50

        \s boşluk karakterini arar
        \S boşluk karakter dışındıkılari arar
        \w alfabetik karekterler rakamlar ve alt çizgi karakterleri arar
        \W \w nin tersi
""" 