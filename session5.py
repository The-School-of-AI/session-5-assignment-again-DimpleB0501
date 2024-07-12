"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
import math
import inspect


def time_it(fn, *args, repetitions = 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    start = time.perf_counter()
    if (repetitions <= 0):
        return 0
    for r in range(repetitions):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return ((end - start)/repetitions)


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    if args:
        raise TypeError("takes maximum 1 positional arguments")
    #print (kwargs)

    if kwargs:
        if 'repetitons' in kwargs :
            pass
        else:
            raise TypeError("maximum 2 keyword/named arguments")

    # Validations "if" block
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    elif number >= 10:
        raise ValueError("Value of number should be less than 10")
    elif start < 0 or end <= 0:
        print (f"start: {start}, end: {end}")
        raise ValueError("Value of start or end can't be negative")
    elif start > end:
        raise ValueError("Value of start should be less than end")
    sq_list = []
    # Return the list of number to the power of numbers from start to end
    for r in range(start, end):
        sq_list.append(int(math.pow(number, r)))
    #print (f"squared_power_list: {sq_list}")
    return sq_list


def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    if args:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    # Validations
    if isinstance(length, int) or isinstance(length, float):
        if length > 0:
            if not isinstance(sides, int):
                raise ValueError("sides can be int only")
            else:
                if sides < 3 or sides > 6:
                    raise ValueError("Sides can be between 3 and 6")
                else:
                    # Return area
                    return sides * (length ** 2) / (4 * math.tan(math.pi / sides))
        else:
            raise ValueError("Length cannot be negative")
    else:
        raise TypeError("Length can be int or float type only")

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    if args:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    if isinstance(temp, int) or isinstance(temp, float):
        if isinstance(temp_given_in, str):
            # Validations
            temp_allowed = ['f', 'F', 'c', 'C']
            if temp_given_in not in temp_allowed:
                raise ValueError("Only f or c is allowed")
            else:
                temp_given_in = temp_given_in.lower()

            if temp_given_in == 'f':
                if temp <= -459.67:
                    raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
                else:
                    return ((temp - 32) * 5/9)
            else:
                if temp <= -273.15:
                    raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
                else:
                    return ((temp * 9/5) + 32)
        else:
            raise TypeError("Charcater string expected")
    else:
        raise TypeError("Temperature can be int or float type only")

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    # Validations
    ### Speed allowed values
    time_val = {'ms': 60 * 60 * 1000, 's':  60 * 60, 'min':60, 'hr': 1, 'day': 1/24}
    dist_val = {'km': 1, 'm': 1000, 'ft': 3280.84,  'yrd':1093.61}

    #print (f"speed type: {type(speed)}")
    #print (f"arguments: {list(inspect.signature(speed_converter).parameters.values())}")
    if args:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    if isinstance(speed, int) or isinstance(speed, float):
        if not isinstance(time, str):
            raise TypeError ("Charcater string expected")
        else:
            time = time.lower()

        if not isinstance(dist, str):
            raise TypeError ("Charcater string expected for distance unit")
        else:
            dist = dist.lower()

        if speed > 0 and speed < 300000:
            ### Time allowed values
            time_allowed = ['ms', 's', 'min', 'hr', 'day']
            if time not in time_allowed:
                raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

            ### Distance allowed values
            dist_allowed = ['km', 'm', 'ft', 'yrd']
            if dist not in dist_allowed:
                raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")


            speed = (speed * dist_val[dist])/ time_val[time]
            speed = round(speed)
            print (f"speed: {round(speed)}")
            return speed
        elif speed <= 0.0:
            raise ValueError("Speed can't be negative")
        elif speed >= 300001:
            raise ValueError("Speed can't be greater than speed of light")
    else:
        raise TypeError("Speed can be int or float type only")
