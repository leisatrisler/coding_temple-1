# Question 1: Write a funtion to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + str(user_name).upper() + "!")


hello_name("Leisa")

# Question 2: Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing.


def first_odds():
    x = 1
    while x <= 100:
        if x % 2:
            print(x)
        x += 1
    return None


# Note: % is called a Modulo Operator.(It returns the remainder of the dividing the left hand by the right hand, used to get the remainder of the problem.)
print(first_odds())

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])


my_list = [1, 35, 87, 5, 9]
max_num_in_list(my_list)
# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not the divisible by 100, unless it is also divisable by 400. The return should be Boolean type(True/False).


def is_leap_(a_year):
    if a_year == a_year // 4 * 4:
        if not a_year == a_year // 100 * 100:
            if a_year == a_year // 400 * 400:
                return True

            return True

    return False


print(is_leap_(2024))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be Boolean type.


def is_consecutive(x, y):
    numbers = range(x, y)
    for number in numbers:
        print(number)
        x = [1, 2, 3, 5, 9]
        return sorted(x) == list(range(min(x), max(x)+1))


print(is_consecutive(1,  5))
