# Write a Python program to print out a set containing all the colours from
# color_list_1 which are not present in color_list_2.
# Test Data : color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output : {"Black", "White"}
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}
    final_list = set()
    for i in color_list_1:
        if i not in color_list_2:
            final_list.add(i)
    print(final_list)