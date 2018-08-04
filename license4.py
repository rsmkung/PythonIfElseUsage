def can_drive(country):
    if country not in countries:
        print('Please enter Taiwan/America')
        return         # This can let the function end early
    age = input('Please enter your age: ')
    if int(age) >= countries[country]: # Finding the match age in the dictionary
        print("You may have a diver's license.")
    else:
        print("You may not have a driver's license.")

countries = {'Taiwan': 18, 'America': 16} # This is a dictionary
country = input('Please enter which country you are in: ')
can_drive(country)