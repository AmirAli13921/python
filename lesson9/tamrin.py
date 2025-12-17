trucks = ['scania', 'volvo', 'benz', 'leyland', 'renault']
print(trucks[0:4])
print(trucks[0:])
print(trucks[4])
print(trucks[-2])
print(trucks[-3])
print ('my favorite truck is:')
for fav in trucks:
    print(f'\t{fav.title()}')    
    -------------------------
    my_trucks = ['scania', 'DAF', 'benz']
friend_trucks = my_trucks[:]
print('my bigges truck is:')
print(my_trucks)
print('my friend ')