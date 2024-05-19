def main():
    display_main_menu()
    
    all_temps = get_user_input()
    
    average_temp = calc_average(all_temps)
    min_max = find_min_max(all_temps)
    sorted_temps = sort_temps(all_temps)
    median_temp = find_median(sorted_temps)
    print("In Ascending Order", sorted_temps)
    print("The Median Temperature is", median_temp)
    print("The Average Temperature is", average_temp)
    print("The Minimum and Maximum Temperatures are", min_max)
    print("The median temperature ", median_temp)
    

def display_main_menu():
    print("display_main_menu")

    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")

    user_input = input()

    all_temps = [float(num) for num in (user_input.split(","))]


    return all_temps

def sort_temps(all_temps):
    print("sort_temps")
    sorted_temps = sorted(all_temps)
    return sorted_temps

def calc_average(all_temps):
    print("calc_average")

    total_temp = sum(all_temps)

    length = len(all_temps)

    average_temp = total_temp / length

    return average_temp
    
def find_min_max(all_temps):
    print("find_min_max")
    min_temp = min(all_temps)
    max_temp = max(all_temps)

    min_max = [min_temp, max_temp]

    return min_max

def find_median(sorted_temps):
    middle_index = len(sorted_temps) // 2

    if len(sorted_temps) % 2 == 1:
        median_temp = sorted_temps[middle_index]
    else:
        # If the number of elements is even, calculate the average of the two middle elements
        median_temp = (sorted_temps[middle_index - 1] + sorted_temps[middle_index]) / 2
    
    return median_temp

if __name__ == '__main__':
    main()