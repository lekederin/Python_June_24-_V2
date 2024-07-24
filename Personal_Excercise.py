'''
List Exercise:

Create a list of your favorite fruits.
Add a new fruit to the list.
Change the second fruit in the list.
Print the final list

'''

Favorite_Fruits = ['Mango', 'Tomato', 'Watermelon', 'Banana', 'Guava', 'Pawpaw']
Favorite_Fruits.append ('Cucumber')
Favorite_Fruits [1] = ['Domado']
#print (Favorite_Fruits)

'''
Tuple Exercise:

Create a tuple of your top 5 favorite movies.
Try to change the third movie (you should receive an error).
Print the tuple

'''

Favorite_Movies = ('BatMan', 'SuperMan', 'Harry Potter', 'Avatar Aang')
#print(Favorite_Movies)

#print(Favorite_Movies[-2])


'''
Dictionary Exercise:

Create a dictionary with keys: name, age, and hobby.
Update the age value.
Add a new key-value pair for favorite_color.
Print the dictionary.

'''

First_Dict = {'name': 'Leke', 'age': 27, 'hobby': 'Excellence'}
First_Dict['age'] = 30
First_Dict ['favorite_color'] = 'blue'

#print(First_Dict)

'''
Set Exercise:
Create a set of your favorite colors.
Add a new color to the set.
Remove a color from the set.
Perform a union operation with another set of colors.
Perform an intersection operation with another set of colors.
Print the final sets after each operation.

'''
favorite_color = {'Black', 'Yellow', 'Blue', 'Brown', 'Torquise'}
favorite_color.add('white')
favorite_color.remove('Torquise')

favorite_color2 = set(['Blacknese', 'Yellow', 'whitenasia', 'yellowfrican', 'Arabicnese'])

Set_Union = favorite_color.union(favorite_color2)
#print (Set_Union)

Set_intersecton = favorite_color.intersection(favorite_color2)
#print(Set_intersecton)

#print(favorite_color2)

'''
CONDITIONAL STATEMENTS
Exercises:
Write a program to check if a number is positive, negative, or zero.
Write a program that takes a score (0-100) and prints the corresponding grade (A, B, C, D, or F)

'''
A_Number = -4
if A_Number < 0:
    print('Negative')
elif A_Number == 0:
    print('Zero')
else: print('Positive')

Score_list = range(0, 101, 10)

print(list(Score_list))

for num in Score_list:
    if num < 30:
        print('F')
    elif num < 55:
        print('D')
    elif num < 75:
        print('B')
    else: print('A')