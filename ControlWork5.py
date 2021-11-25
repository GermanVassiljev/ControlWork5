from random import *
#1
#N=randint(1,9)
#while N>0:
#    N-=1
#    print("   ~~~~~")
#    print("  |_____|")
#    print("  | []  |")
#    print("   _____ ")
#    print()
#2
#C=D=Class_1=Class_2=randint(20,25)
#Summ=0
#while D>=0:
#    D-=1
#    F=randint(1,5)
#    Summ+=F
#Summ=Summ/Class_1
#print("Средний балл первого класса: ",Summ)
#Summ=0
#while C>=0:
#    C-=1
#    F=randint(1,5)
#    Summ+=F
#Summ=Summ/Class_2
#print("Средний балл второго класса: ",Summ)
#3
#F=0
#D=2.0
#Class_P=randint(20,30)
#while Class_P>0:
#    Class_P-=1
#    Class_1=uniform(1.0,5.0)
#    if F<Class_1:
#        F=0
#        F+=Class_1
#    if D>Class_1:
#        D=0
#        D+=Class_1
#print("Наибольший балл: ", round(F,1))
#print("Наименьший балл: ", round(D,1))
#4
#Summ=0
#for i in range(0,13,1):
#    print("Плотность населения в районе ",i)
#    P=randint(1,20)
#    Q=randint(10,50)
#    Summ=0
#    Summ+=P/Q
#    print("Составляет: ",round(Summ,1))
#5
#y=0
#for i in range(1, 11, 1):
#    y = -0.5*i + i
#    print("x равняется ",i,". y значение выходит ",y)