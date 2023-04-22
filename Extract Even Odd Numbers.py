# Read numbers.txt and Create even.txt and odd.txt
with open("numbers.txt", "r") as file_int, open("even.txt", "w") as file_even, open("odd.txt", "w") as file_odd:
# for each line in file_int
    for line in file_int:
        integer = int(line)
    #if even, write to even.txt
        if integer % 2 == 0:
            file_even.write(str(integer))
    #if odd, write to odd.txt
        else:
            file_odd.write(str(integer))
# print output
 