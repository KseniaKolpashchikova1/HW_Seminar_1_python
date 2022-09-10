# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

daynumber = int (input ('Введите номер дня недели: '))
if daynumber > 5:
    print ('День недели является выходным')
else:
    print ('День недели является будним')   
# if daynumber == 1:
#     print('Понедельник')
# elif daynumber == 2:
#     print('Вторник')
# elif daynumber == 3:
#     print('Среда')
# elif daynumber == 4:
#     print('Четверг')
# elif daynumber == 5:
#     print('Пятница')
# elif daynumber == 6:
#     print('Суббота')
# elif daynumber == 7:
#     print('Воскресенье')
