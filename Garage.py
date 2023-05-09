# Программа "Гараж"

cars = []

print("*" * 10 , " Garage beta.v.0.0.0.1 ","*" * 10)

responce = 1
while responce:
    print("""Выберите действие:
            1 - Add Auto
            2 - Delete Auto
            3 - List Auto
            4 - Search Auto
            5 - Sort Garage
            6 - EXIT""")
    responce = int(input(">> "))
    if responce == 1:
        car = input("New Auto: ")
        cars.append(car)
    elif responce == 2:
        car = input("Delete Auto: ")
        cars.remove(car)
    elif responce == 3:
        print(cars)
    elif responce == 4:
        car = input("Search: ")
        if car in cars:
            print("IN Garage! ")
        else:
            print("NOT IN Garage! ")
    elif responce == 5:
        cars.sort()
        print("Sorting!")
    else:
        print("Goodbye")

### Finish