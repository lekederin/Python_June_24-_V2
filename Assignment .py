'''
write a program that performs an arithmetic function on two numbers based on user option

Write a temperature converter program

Write a program that converts dollar to naira and vise versa using the 1640/naira to a dollar as exchange rate

'''

# try:
#     Num1 = (int(input('Type in Number One: ')))
#     Num2 = (int(input('Type in Number Two: ')))
#     Sign = (input('Type in the choice of arithmetic operation (Mul: *, Add +, Minus -, div/): '))
#     if Sign == '+':
#         def SumNum (Num1, Num2):
#             result = Num1 + Num2
#             print (result)
#         SumNum (Num1, Num2)
#     elif Sign == '*':
#         def MulNum (Num1, Num2):
#             result = Num1 * Num2
#             print(result)
#         MulNum(Num1, Num2)
#     elif Sign == '-':
#         def MinNum (Num1, Num2):
#             result = Num1 - Num2
#             print(result)
#         MinNum(Num1, Num2)
#     elif Sign == '/':
#         def DivNum (Num1, Num2):
#             result = Num1 / Num2
#             print(result)
#         DivNum(Num1, Num2)
#     else: 
#         print('Please try again this the appropiate symbol')
# except: 
#     print('Please type in an integer')



# Num1 = float(input('Enter Numeric Value: '))
# Var1 = input('What Temperature scale are you converting from: ')
# Var2 = input('What Temperature scale are you converting to: ')
# if Var1 == 'Celsius' or Var1 == 'celsius':
#     if Var2 == 'kelvin' or Var2 == 'Kelvin':
#                 answ = Num1 + 273.15
#                 print(f'The answer to your Conversion is {answ} K')
#     elif Var2 == 'Fahrenheit' or Var2 == 'fahrenheit':
#                 answr = Num1 * 1.8 + 32
#                 print(f'The answer to your Conversion is {answr} F')

# elif Var1 == 'Fahrenheit' or Var1 == 'fahrenheit':
#     if Var2 == 'Celsius' or Var2 == 'celsius':
#                 ansa = (Num1 - 32) * 5/9
#                 print(f'The answer to your Conversion is {ansa} C')
#     elif Var2 == 'Kelvin' or Var2 == 'kelvin':
#                 answar = (Num1 - 32) * 5/9 + 273.15
#                 print(f'The answer to your Conversion is {answar} K')

# elif Var1 == 'Kelvin' or Var1 == 'kelvin':
#     if Var2 == 'Celsius' or Var2 == 'celsius':
#                 answer = Num1 - 273.15
#                 print(f'The answer to your Conversion is {answer} °C')
#     elif Var2 == 'Fahrenheit' or Var2 == 'fahrenheit':
#                 answer1 = (Num1 - 273.15) * 9/5 + 32
#                 print(f'The answer to your Conversion is {answer1} °F')

# else:
#     print('Invalid input for temperature scales.')



# def dollar2naira (Money): 
#     result = Money * 1640
#     print(f'{result}NGN')

# def naira2dollar (Money):
#     result = Money / 1640
#     print (f'{result}USD')

# Money = int(input('How much are you Exchanging?: '))
# currency = (input('In Capital letters, what currency are you exchanging from /USD or NGN?: '))

# if currency == 'USD':
#     dollar2naira (Money)
    
# elif currency == 'NGN':
#     naira2dollar (Money)
# else:   
#     print('Type in the Appropiate value')


'''
Practice Exerise for Python Basics
'''
#  Write a program that takes a list of integers as input and returns the sum of all the integers in the list

# try:
#     A = (input('Write Num 1 '))
#     B = (input('Write Num 2 '))
#     C = (input('Write Num 3 '))
#     D = (input('Write Num 4 '))
#     E = (input('Write Num 5 '))

#     F = int (A+B+C+D+E)
#     print (f'The sum of your Numbers is {F}')
# except:
#     print('Invalid number')



# def LekeList():
#     Alist = []
#     while True:
#         try:
#             Parainput = (input ('Input your number (Type in "stop" when done): '))
#             if Parainput.casefold() == 'stop':
#                 break
#             number = int(Parainput)
#             Alist.append(number)
#         except ValueError:
#             print('Please enter a valid number or stop to finish')
#     print(Alist)

# LekeList()




#Write a program that takes a list of integers as input and returns the sum of all the integers in the list

def LekeList():
    Alist = []
    while True:
        try:
            Parainput = (input ('Input your number (Type in "stop" when done): '))
            if Parainput.casefold() == 'stop':
                break
            number = int(Parainput)
            Alist.append(number)
        except ValueError:
            print('Please enter a valid number or stop to finish')
    

    SumNum = sum(Alist)
    print(f' The sum of the numbers is {SumNum}')
LekeList()

LekeList()


