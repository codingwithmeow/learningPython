#error => hata

# print(a) => NameError

# int ('1a2') => ValueError

# print (10/0) => ZeroDivisionError

# print('TR'Y) =>SytaxError


while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))

        print(x/y)
    # except ZeroDivisionError:
    #     print('y can not be zero')
    # except ValueError:
    #     print('enter numerical value for x and yx ve y içim sayısal değer girin.')
    # except (ZeroDivisionError,ValueError) as e:
    #     print('Wrong info')
    #     print(e)
    # except:
    #     print('Wrong info')
    except Exception as ex:
        print('Wrong info',ex)
    else:
        break
    finally:
        print('try except ended.')