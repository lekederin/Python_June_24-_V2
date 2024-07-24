# Welcome to the first python class


'''

outlines:
Variables / Value / OPerators
python Data Types
    Strings
    Integer: Numbers, Floats, Complex
    Collection : List, Turple, Set, Dict

Control Statement:
    Conditional statement
    Loop / Iteration

Function
classes
Project

'''

# y = 10
# y2 = 10.3
# y3 = 7e46

# print(type(y))

# print(type(y2))

# print(type(y3))
# #Collection / Array : List, Tuple, Set & Dict

# #List
# hL = ['Parach', 343,'Adewunmi', 'True', 34.1, ['Boy', 'Girl']]

# Student_List = ['Adebiyi', 'Aishat', 'Leke', 'Fortune', 'Adewunmi', 'Boluwatife']

# #print(Student_List)

# #print(Student_List[0])

# Student_List.reverse()


# for eachitem in Student_List:
#     print(eachitem)

# #Converting from str to int and otherwise

# Str_test = '2039'
# print(type(Str_test))

# print(int(Str_test))
# print(type(Str_test))

# #Conditional Statments
# num1 = 10
# num2 = 17

# if num1 < 7 and num2 < 20:
#     print('Conditon met')
# else: print('Condition not met')

# if num1 == 10 or num2 > 15:
#     print ('Condition met')

'''
Write a program that takes a list or range of numbers

1. checks if the number is an odd or even number

2.  checks if the number is divisible by 3 and print (fizz)

3. Check if the number is divisible by 5 and print (Buzz)

4. If not divisible by any, print number

Assignment
Write a program that collects user option 1- 4
Create a list of at least five states and capital
1. display all states and capitals
2. add new states and capitals to the list
3. edit a particular state and capital
4. delete a particular state and its capital

.


''' Anou

States_and_Cap = {
    'Lagos': 'Ikeja', 
    'Osun': 'Oshogbo', 
    'Oyo': 'Ibadan', 
    'FCT': 'Abuja', 
    'Nasarawa': 'Lafia'
    }

# for i in States_and_Cap:
print (States_and_Cap)

# States_and_Cap ['Ogun'] = ('Abeokuta')
# print (States_and_Cap)

States_and_Cap.update({'Ogun' : 'Abeoluta', 'Kogi' : 'Lokoja'})
print(States_and_Cap)

States_and_Cap ['Lagos'] = 'V.I.'
print(States_and_Cap)

# Lagone = States_and_Cap.pop('Lagos')
# print(States_and_Cap)

# print (Lagone)

del States_and_Cap ['Lagos']
print(States_and_Cap)


# for i in range (1,11):
#     if i % 2 == 0:
#         print('Even')
#     else:
#          print('odd')
    
# for i in range (1,11):
#     if i % 3 == 0:
#         print ('Fizz')
#     elif i % 5 == 0:
#         print ('Buzz')
#     else:
#         print (i)
    