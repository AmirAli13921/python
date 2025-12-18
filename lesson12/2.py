available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppings in request_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding: {requested_toppings}")
    else:
        print(f"Sorry we dont have {requested_toppings}")
print('\nFinished making your pizza!')