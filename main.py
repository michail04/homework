import os
path = os.path.join(os.getcwd(), 'recipes.txt')

with open('recipes.txt') as file:
    data_name = file['recipes.txt'].encode('utf-8')
    print(file.read())
# file= open('recipes.txt')
# x=file.read()
# print(x)
