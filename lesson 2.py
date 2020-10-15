

#Первое задание: Практика

# 1.Проверить, является ли введеное число четным.

# print("Введите число, чтобы проверить, является ли введеное число четным: ")
# x = int(input())
# if x % 2 == 0:
#    print("Четное!")
# else:
#    print("Не четное!")
#_____________________________________________________________________________
#
#
# 2. Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.
#
# print("Введите число")
# x = int(input())
# if (x % 3 == 0) and (x % 5 == 0) and (x % 10 != 0):
#    print("гуд")
# else:
#    print("нэт")
#______________________________________________________________________________
#
#
#
#
# #3. Ввести число, вывести все его делители.
#
# # print("Введите число, чтобы вывести все его делители: ")
# # x = int(input())
# # y = 0
# # while (y <= x):
# #    y += 1
# #    if x % y == 0:
# #        print(y)
# #_______________________________________________________________________________
#
#

#4. Ввести число, вывести его разряды и их множители.

# x = int(input("Введите число, чтоб узнать его разряды и множители: "))
# y = 10 #Вводим десяток, для того чтоб успользовать кратность десяти
# z = 1 #Стартовое число для перебора
# print("Разряды числа " + str(x) + ": ")
# while z <= x:
#     a = x//z%y
#     z *= 10
#     print(a)
# print("Их возможные множители:")
# i = 2
# while i < x:
#     if x % i == 0:
#         print(i)
#         x /= i
#     else:
#         i += 1
# print(x)


#     #Второе задание. Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.
#
# print("Введите свое имя")
# playerName = str(input())
# print("Приветствую тебя " + (playerName) + "!"
#      "Я хочу поиграть с тобой в маленькую игру!" + "\n" +
#      "Я поймал тебя, но у тебя есть шанс выбраться отсюда и для этого ты должен решить 3 мои загадки!"
#      + "\n" + "Первая загадка!" + "\n" + "У Олиной мамы пять дочек: Вика, Аня, Марта, Кира... Как зовут пятую?")
# ant1 = str(input())
# if ant1 == ("Оля"):
#    ant1 = True
#    print("Ты стал на шаг ближе к свободе!")
# else:
#    ant1 = False
#    print("Даже ребенок ответил бы правильно...." + "\n" +
#          "Но не ты" + "\n" +
#          "АХАХАХАХАХ")
# import time
# time.sleep(2)
# print("Вторая загадка!" + "\n" +
#      "В отеле 4 этажа. Чем выше этаж, тем больше людей там живет." + "\n" +
#      "На какой этаж чаще ездит лифт?")
# ant2 = str(input())
# if ant2 == ("1") or ("Первый"):
#    ant2 = True
#    print("Ты слишком умен!!!")
# else:
#    ant2 = False
#    print("Боже, как же ты туп!!!")
# import time
# time.sleep(2)
# print("Третья загадка!" + "\n" +
#      "Что может в одно и то же время может стоять и ходить, висеть и стоять, ходить и лежать?")
# ant3 = str(input())
# if ant3 == ("Часы"):
#    ant3 = True
#    print("В точку!")
# else:
#    ant3 = False
#    print("Это, и правда, было нелегко....")
# import time
# time.sleep(2)
# print("Давай проверим все твои ответы:")
# import time
# time.sleep(1)
# print("Хмммм......")
# import time
# time.sleep(1)
# if ant1 and ant2 and ant3:
#    print("Твой ум легендарен. Я не смею больше тебя задерживать!")
# elif (ant1 and ant2 and ant3) == 0:
#    print("Ты навсегда останешься со мной, мой глупенький друг!!")
# else:
#    print("Ты был близок!")
# import time
# time.sleep(7)
#_______________________________________________________________________________
#
#     #Третье задание. Задача fizz-buzz
#
# print("Необходимо ввести 3 целых числа." + "\n" + "Введите 1-е число")
# fizz = int(input())
# print("Введите 2-е число")
# buzz = int(input())
# print("Введите 3-е число")
# x = int(input())
# y = 0
# List = []
# while (y < x):
#    y += 1
#    if (y % fizz == 0) and (y % buzz == 0):
#        List += ["FB"]
#    elif (y % fizz == 0):
#        List += ["F"]
#    elif (y % buzz == 0):
#        List += ["B"]
#    else:
#        List += [y]
# print(List)
#________________________________________________________________________________
#
# x = input("Необходимо ввести 3 целых числа через пробел: ")
# fizz, buzz, end = list(map(int, x.split()))
# List = []
# for y in range(1, end + 1):
#    if  (y % fizz == 0) and (y % buzz == 0):
#        List.append('FB')
#    elif (y % fizz == 0):
#        List += ["F"]
#    elif (y % buzz == 0):
#        List += ["B"]
#    else:
#        List += [y]
# print(List)
#________________________________________________________________________________
#
#
#
## ДЗ 3 лекции                                                        нужна помощь
# file = open('fileRead.txt')
# List = []
# counter = 0
# List1 = []
# for line in file:
#     fizz, buzz, end = list(map(int, line.split()))      # предыдущий результат копируется на следующий
#     List1.append(line)
#     print(List1)
#     for y in range(1, end + 1):
#         if  (y % fizz == 0) and (y % buzz == 0):
#             List.append('FB')
#         elif (y % fizz == 0):
#             List += ["F"]
#         elif (y % buzz == 0):
#             List += ["B"]
#         else:
#             List += [y]
#     print(List)
#     file2 = open('fileWrite.txt', 'w')
#     file2.write(str(List))                              # Как разбить на \n?
# file.close()
# file2.close()


#Банкомат
# nominal = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# zapros = int(input())
# proverka = 0
# while zapros != 0:
#     if zapros >= nominal[proverka]:
#         zapros -= nominal[proverka]
#         print(nominal[proverka])
#     else:
#         proverka += 1
#
#Банкомат. Мелкими купюрами не более 10 шт.
# nominal = {1: 10, 2: 10, 5: 10, 10: 10, 20: 10, 50: 10, 100: 10, 200: 10, 500: 10, 1000: 10}
# zapros = int(input())
# a = 0                     #функция для переворачивания числа
# while zapros>0:
#     a = a*10 + zapros%10
#     zapros = zapros//10
# print(zapros)             #конец функции
# proverka = 0
# while zapros != 0:
#     if zapros >= nominal[proverka]:
#         zapros -= nominal[proverka]
#         print(nominal[proverka])
#     else:
#         proverka += 1
#


#
# Лекция 5
# x = list(input("большой регистр: "))
# u = list(input("малый регистр: "))
# def up(x):
#     return x.upper()
# def low(u):
#     return u.lower()
# xUp = list(map(up, x))
# uUp = list(map(low, u))
# print(xUp)
# print(uUp)

# Функцуия возведения числа в квадрат
# x = int(input())
# def kvad(x):
#     return x*x
# print(kvad(x))

# в квадрат простые числа из списка использую map
# spisok = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# otbor = []
# index = 0
# delitel = 0
# for spisok[index] in spisok:
#     for i in range(2, spisok[index]+1):
#         for j in range(2, i):
#             if i%j==0:
#                 k += 1
#         if k == 0:
#             otbor.append(i)
#         else:
#             k = 0
# print(otbor)




#Черновик
#a = ""
#b = True
#c = False
#d = 0
#e = 1
#f = 5
#g = "test"
#result = d and a >>> 0 - первое False выражение
#result = b and a or f >>> 5 - and проп. дальше так как первое знач. b(True), or идет до первого True - это f(5)
#result = f and a or c or b or g and d >>> f and a = A, g and d = D, a or c = C, c or b = B, b or d = B(True)
#print(result)
#
#
# con1 = 0  # NEC, необходимые траты
# con2 = 0    # FFA, финансовая свобода
# con3 = 0  # EDU, образование
# con4 = 0   # LTSS, резерв и на большие покупки
# con5 = 0       # PLAY, развлечения
# con6 = 0       # GIVE, подарки
#
# # initializing percent rate
# con1rate = 0.55
# con2rate = 0.1
# con3rate = 0.1
# con4rate = 0.1
# con5rate = 0.1
# con6rate = 0.05
# # initializing expected income, expected necessity and other amounts
# gran = 1000
#
# # invitation, greetings etc.
# print ("""Hello.
# Привет
# Дай бабок:""")
#
# # initializing handler for standard input
# sum = 0
#
# while (sum < gran):
#     line = int(input())
#     if line <= 1000:
#        sum = sum + line
#
#        con1 = con1 + line * con1rate
#        con2 += line * con2rate
#        con3 += line * con3rate
#        con4 += line * con4rate
#        con5 += line * con5rate
#        con6 += line * con6rate
#
#
#
#        print("At the end we have:\n\
#        Necessity Envelop has:                       " + str(int(con1)) + "\n\
#        Financial Freedom Envelop has:               " + str(int(con2)) + "\n\
#        Education Envelop                            " + str(int(con3)) + "\n\
#        Long Term Saving for Spending Envelop has:   " + str(int(con4)) + "\n\
#        Play Envelop has:                            " + str(int(con5)) + "\n\
#        Give Envelop has:                            " + str(int(con6)) + "\n\
#        _______________________________________________________________")
#
#        if (sum < gran):
#           print("дай еще:")
#        else:
#           print("Спасибо  :)")
#     else:
#        print("не серьезно")

# x = int(input())
# y = 16 - x == 10
# result = "x Правда" if y else "x Ложь"
# print(result)

# List comprehension

# Без сокращений
# Создать список чисел
# card = [1, 3, 4, 5, 12, 17]
# # Создать козину для чисел
# cashier = []
# for item in card:
#     cashier.append(item)
# print(cashier)

# с сокращением
# card = [1, 3, 4, 5, 12, 17]
# cashier = [item for item in card]
# print(cashier)



# nominal.reverse()
# zapros = list(input())
# zapros.reverse()
# zapros = list(map(int, zapros))
# proverka = dict(zip(zapros, nominal))
# print(proverka)

# Практика лекция 6
# import math
# kvartira = int(input("Искомая квартира: "))
# etagnost = int(input("Этажность дома: "))
# KvEt = int(input("Кол-во квартир на этаже: "))
# KvPod = etagnost*KvEt
# PODEZD = kvartira/KvPod #2
# while kvartira > KvPod:
#     kvartira = kvartira - KvPod
# Etag = etagnost/KvPod*kvartira
# PODEZD = math.ceil(PODEZD)
# Etag = math.ceil(Etag)
# print("Подъезд - "+str(PODEZD))
# print("Этаж - "+str(Etag))

# Бриллианты
# number = int(input("Введите число: "))
# zv = []
# if number % 2 != 0 and number > 0:
#     for i in range(1, number+1, 2):
#         zv.append(i)
#     zv += zv[len(zv)-2::-1]
#
#     print(zv)
#
# else:
#     print("Введенное число либо четное, либо отрицательное")


slovar = {"Иванов Иван": [75,32,54,34], "Петров Петр": [59,45,97,45], "Непонятный Жора": [25,45,67,73], "Кривой Витя": [79,45,79,100]}
x = {}
for k, i in slovar.items():
    ball = (sum(i)/len(slovar))
    slovar[k] = ball