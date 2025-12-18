request_topping = ['onion', 'pineapple', 'cheese']

if request_topping:
    for request in request_topping:
        print(f"Adding {request}")
    print('\nFinished making your pizza')
else:
    print('Are you sure you want to plain your pizza?')