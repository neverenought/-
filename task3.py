from math import*
N = int(input('Количество чисел:'))
srznch = 0
sum = 0
for i in range(N):
    chislo = int(input('Число:'))
    srznch+=1
    sum += chislo
srznach=sum/srznch

print('Среднее арифмитическое:',srznch)