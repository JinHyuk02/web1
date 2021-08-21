persons = [
    ['egoing', 'Seoul', 'web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Incheon', 'ML'],
]
print(persons[0][0])

for person in persons:
    print(person[0]+','+person[1]+','+person[2])

person = ['egoing', 'Seoul', 'web']
name = person[0]
adress = person[1]
interest = person [2]
print(name, adress, interest)

print('----')

name, adress, interest = ['egoing', 'Seoul', 'web']
print(name, adress, interest)

print('----')

for name, adress, interest in persons:
    print(name+','+adress+','+interest)
