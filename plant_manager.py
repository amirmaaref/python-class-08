import plant_library

is_ok = False
while True:
    try:
        plant_library.set_plant_type(input(plant_library.ENTER_PLANT_TYPE_MESSAGE))
        break
    except ValueError as e:
        print(e)


print(f'Selected Plant type is: {plant_library.plant_type}')