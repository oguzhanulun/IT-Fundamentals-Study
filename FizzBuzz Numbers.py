# Task : Print the Fizz Buzz numbers.
# - Print numbers from 1 to 100 inclusively following these instructions:
# - If a number is multiple of 3, print "Fizz" instead of this number,
# - If a number is multiple of 5, print "Buzz" instead of this number,
# - For numbers that are multiples of both 3 and 5, print "FizzBuzz",
# - Print the rest of the numbers unchanged.
# - Output each value on a separate line.
x = int(input("Enter your number for >> Fizz Buzz <<   :"))
def FizzBuzz(a) :
    count = 1
    while count <= a :
        if count % 5 == 0 and count % 3== 0 :
            print("FizzBuzz")
        elif count%5 == 0 :
            print("Buzz")
        elif count%3 == 0 :
            print("Fizz")
        else :
            print(count)
        count += 1
print(FizzBuzz(x))