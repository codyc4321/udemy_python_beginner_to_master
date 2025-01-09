
def count_digits_in_number():
    n = 12359
    counter = 0

    while n > 0:
        n = n // 10
        counter += 1

    print(f"Number of digits is {counter}")
    return counter


def sum_digits_of_number():
    n = 1234
    string = str(n)
    length = len(string)
    total = 0
    for index in range(length):
        total += int(string[index])
    print(f"The total is {total}")
    return total


def reverse_a_number():
    n = 12359
    reversed = ""
    while n > 0:
        r = n % 10
        string_last_number = str(r)
        reversed += string_last_number
        n = n // 10
    reversed_as_int = int(reversed)
    print(f"The reversed number is {reversed}")
    return reversed_as_int


def reverse_a_number_using_arithmetic():
    n = int(input("Enter a number to reverse: "))
    reversed = 0
    while n > 0:
        r = n % 10
        n = n // 10
        reversed = reversed * 10 + r
    print(f"Reversed number by arithmetic is: {reversed}")
    return reversed



if __name__ == "__main__":
    digits = count_digits_in_number()
    assert digits == 5

    sum = sum_digits_of_number()
    assert sum == 10

    reversed = reverse_a_number()
    assert reversed == 95321

    reverse_a_number_using_arithmetic()

