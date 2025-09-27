circle_perimeter_list = []
circle_area_list = []
rectangle_perimeter_list = []
rectangle_area_list = []

def circle_perimeter(r):
    pi = 3.14
    return 2 * pi * r

def circle_area(r):
    pi = 3.14
    return pi * r * r

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def rectangle_area(length, width):
    return length * width

while True:
    print("please enter what kind of performance do you want?")
    print("1) circle_perimeter")
    print("2) circle_area")
    print("3) rectangle_perimeter")
    print("4) rectangle_area")
    print("5) show list")
    print("6) remove items")
    print("7) exit")

    choose = int(input("please enter the number: "))

    if choose == 1:
        radius_input = float(input("Please enter the radius: "))
        result = circle_perimeter(radius_input)
        print("Your result is:", result)
        circle_perimeter_list.append(result)

    elif choose == 2:
        radius_input = float(input("Please enter the radius: "))
        result = circle_area(radius_input)
        print("Your result is:", result)
        circle_area_list.append(result)

    elif choose == 3:
        length_input = float(input("Please enter the length: "))
        width_input = float(input("Please enter the width: "))
        result = rectangle_perimeter(length_input, width_input)
        print("Your result is:", result)
        rectangle_perimeter_list.append(result)

    elif choose == 4:
        length_input = float(input("Please enter the length: "))
        width_input = float(input("Please enter the width: "))
        result = rectangle_area(length_input, width_input)
        print("Your result is:", result)
        rectangle_area_list.append(result)

    elif choose == 5:
        print("Circle perimeter list:", circle_perimeter_list)
        print("Circle area list:", circle_area_list)
        print("Rectangle perimeter list:", rectangle_perimeter_list)
        print("Rectangle area list:", rectangle_area_list)

    elif choose==6:
        print("which list do you want to remove???\n"
              "1)list of the circle perimeter:\n"
              "2)list of the circle area:\n"
              "3)list of the rectangle perimeter :\n"
              "4)list of the rectangle area :\n")
        choose = int(input("please enter your number:"))

        if choose == 1:
            if circle_perimeter_list:
                print("current list is :", circle_perimeter_list)
                print("=" * 50)
                remove = input("please enter which item do you want to remove:")
                for remove in circle_perimeter_list:
                    circle_perimeter_list.remove(remove)
            else:
                print("current list is empty!!!")

        elif choose == 2:
            if circle_area_list:
                print("current list is :", circle_area_list)
                print("=" * 50)
                remove = input("please enter which item do you want to remove:")
                for remove in circle_area_list:
                    circle_area_list.remove(remove)
            else:
                print("current list is empty!!!")
        elif choose == 3:
            if rectangle_perimeter_list:
                print("current list is :", rectangle_perimeter_list)
                print("=" * 50)
                remove = input("please enter which item do you want to remove:")
                for remove in rectangle_perimeter_list:
                    rectangle_perimeter_list.remove(remove)
            else:
                print("current list is empty!!!")
        elif choose == 4:
            if rectangle_area_list:
                print("current list is :", rectangle_area_list)
                print("=" * 50)
                remove = input("please enter which item do you want to remove:")
                for remove in rectangle_area_list:
                    rectangle_area_list.remove(remove)
            else:
                print("current list is empty!!!")
    elif choose==7:
        print("good bye!!!")
        break

