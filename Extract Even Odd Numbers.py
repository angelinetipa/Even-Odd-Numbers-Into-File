# Read numbers.txt and Create even.txt and odd.txt
with open("numbers.txt", "r") as file_int, open("even.txt", "w") as file_even, open("odd.txt", "w") as file_odd:
# for each line in file_int
    for line in file_int:
        integer = int(line)
    #if even, write to even.txt
        if integer % 2 == 0:
            file_even.write(str(integer))
            file_even.write("\n")
    #if odd, write to odd.txt
        else:
            file_odd.write(str(integer))
            file_odd.write("\n")
# print output
with open("even.txt", "r") as file_even, open("odd.txt", "r") as file_odd:
    print("=" * 35, "\n\n\033[1m\033[3mEven numbers from file numbers.txt:\033[0m")
    for line in file_even:
        print(line.strip(), end = ",")

    print("\n\n\033[1m\033[3mOdd numbers from file numbers.txt:\033[0m")
    for line in file_odd:
        print(line.strip(), end = ",")
    print("\n")
    print("=" * 35)