#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b,c,d = int(input()) , int(input()) , int(input()) , int(input()) #обозначаем переменные и вводим данные
t=(a,b,c,d)
S1=sum(t) #сумму значений обозначаем переменной
S2=S1+b #находим стоимость обеда Маши
res=S2/S1 # обозначаем переменную для "увеличения"
print( 'Начальная стоимость:',S1,'Увеличение:',res) #выводим результат


# In[ ]:


my_str = 'Карл у Клары украл рекламу, а Клара у Карла украла бюджет' # 1. Создаем строку
len(my_str)                                               # 2. Получаем длину строки с помощью встроенного метода len()
my_str + '.'                                              # 3. Выполняем конкатенацию строк           
'ла' in my_str                                            # 4. Определяем вхождение подстроки 'ре'
my_str.count('ла')                                        # 5. Определяем количество вхождений подстроки 'ре'
my_str[-2]                                                # 6. Получаем предпоследний символ строки
my_str[1::2]                                              # 7. Получаем элементы с нечетными индексами
                                                         #  срез с элемента с индексом 1 по конец строки с шагом 2
my_str.count(' ') + 1                                     # 8. Определяем количество слов в строке
                                                         #  количество пробелов и + 1


# In[ ]:




