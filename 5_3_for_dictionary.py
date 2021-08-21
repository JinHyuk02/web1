person = {'name' : 'egoing', 'adress' : 'seoul', 'interest' : 'web' }
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name' : 'egoing', 'adress' : 'Seoul', 'interest' : 'web'},
    {'name' : 'basta', 'adress' : 'Seoul', 'interest' : 'IOT'},
    {'name' : 'blackdew', 'adress' : 'Incheon', 'interest' : 'ML'}
]

print('==== persons =====')

for person in persons:
    for key in person:
        print(key, ':', person[key])

    print('----------------------')




