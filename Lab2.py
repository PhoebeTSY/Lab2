def main():
    print("ET0735(DevOps for AIoT)-Lab2-Introduction to Python")
    display_main_menu()
    listfloat = get_user_input()
    calc_average(listfloat)
    calc_min_max_temperature(listfloat)
    ascending = sort_temperature(listfloat)
    calc_median_temperature(ascending)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input('Enter the number: ')
    x = x.split(",")
    thislist = x
    listfloat = [float(x) for x in thislist]
    print(listfloat)
    return(listfloat)


def calc_average(listfloat):
    print("calc_average temperature")
    y = (len(listfloat))
    z = (sum(listfloat))
    average = z / y
    print("The average temperature is: " + str(average))

def calc_min_max_temperature(listfloat):
    minimum_value = min(listfloat)
    print("The minimum temperature is " + str(minimum_value))
    maximum_value = max(listfloat)
    print("The maximum temperature is " + str(maximum_value))

def sort_temperature(listfloat):
    ascending = sorted(listfloat)
    print(ascending)
    return(ascending)

def calc_median_temperature(ascending):
    mid = len(ascending) // 2
    median = (ascending[mid] + ascending[~mid]) / 2
    print("Median of list is : " + str(median))
    return(0)

if __name__ == "__main__":
    main()