# Write a function named make_model. It will accept a list of dictionaries where each dictionary represents a car, 
# and return a list of strings where each string is the make and model of the car concatenated together.

cars = []
cars.append({'make': 'Toyota', 'model': 'Camry'})
cars.append({'make': 'Honda', 'model': 'Accord'})
cars.append({'make': 'Ford', 'model': 'Fiesta'})
cars.append({'make': 'Ford', 'model': 'F-150'})
# print(cars)
# ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']

def make_model(cars):
    new_list = []
    for cars in cars:
        new_list.append(cars['make'] + " " + cars['model'])
    return new_list 


# print(make_model(cars))

# Write a function named extract_time_components. It should take in a string that is a 24-hour time with the hour, minutes, and seconds seperated by :s, and return a dictionary with keys hour, minutes, and seconds with corresponding integer values.


def extract_time_component(time):


# >>> extract_time_components('21:30:00')
# {'hours': 21, 'minutes': 30, 'seconds': 0}
# >>> extract_time_components('09:01:53')
# {'hours': 9, 'minutes': 1, 'seconds': 53}

    time_break = {}
    for character in time:
        time_break.update({'hour' : int(time[0:2])})
        time_break.update({'minutes' : int(time[3:5])})
        time_break.update({'seconds' : int(time[-2])})
    return time_break

print(extract_time_component('21:30:00'))