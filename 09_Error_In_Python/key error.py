data: dict[str, str] = {'name': 'Bob',
                        'job': 'Programmer',
                        'race': 'bob is bob', 
                        'best-friend': 'James'}
print(data['job'])
#no key for salary
#print(data['salary'])

#.get() method help to get something which doesn't exist and return none or 
#msg you want to print

print(data.get('salary', 'Default'))
