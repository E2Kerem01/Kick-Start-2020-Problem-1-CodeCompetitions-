# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 00:33:34 2021

@author: gurse
"""
import time
case = int(input("Kaç işlem yapılacak = "))
d = []
def solve(Butce,Ev_Adet,b):
    b.sort()
    print(b)
    if case == 0:
        for i in range(case):
            print("Case # "+ i +" için {} alınır".format(d[i]))
    for i in range(Ev_Adet):
        Butce = Butce - b[i]
        if Butce < 0:
            print("Bu kadar ev alınır : {} ".format(i))
            d.append(i)
            break
while(case>0):
       case-=1
       EvAdet_Butce = (input("Ev_adet ve Bütce giriniz : "))
       c1 = list(EvAdet_Butce.split(" "))
       b2 = []
       for i in range(len(c1)):
           b2.append(int(c1[i]))
       Ev_Adet = b2[0]
       Butce = b2[1]
       a = (input("asd : "))
       c = list(a.split(" "))
       b = []
       for i in range(len(c)):
           b.append(int(c[i]))
       solve(Butce,Ev_Adet,b)
print("Case #1 "+str(d[0])+"\nCase #2 "+str(d[1])+"\nCase #3 "+str(d[2])+"\n")
time.sleep(1000)