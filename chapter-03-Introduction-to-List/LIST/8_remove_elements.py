#remove a element using del statement from a list
cars = ['BMW','Mercedes','Toyota','Audi']
del cars[3]
print(cars)


# remove a element using the pop() method

cars = ['BMW','Mercedes','Toyota','Audi']
popped_car = cars.pop()
print(cars)
print(popped_car)
print(f'the cars that i sell today is  {popped_car}')

#popped a car from any position in the list of cars
#tommorow i will sell the third car in my list of cars
popped_car = cars.pop(2)
print(f'the car that i will sell tomorrow is  {popped_car}')

# remove a car from the list of cars by using remove() method
cars = ['BMW','Mercedes','Toyota','Audi']
cars.remove('Mercedes')
print(cars)