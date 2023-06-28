
def FizzBuzz(upperLimit):
    counter = 1
    while counter <= upperLimit:
        if upperLimit < 0 or upperLimit > 2*(10**5):
                break
        if counter % 3 == 0 and counter % 5 == 0:
                print("FizzBuzz")
        elif counter % 3 and not (counter % 5):
                print("Buzz")
        elif counter % 5 and not (counter % 3):
                print("Fizz")
        else:
                print(counter)
        counter += 1
number = input("Enter Upper Limit: ")
upperLimit = int(number)
FizzBuzz(upperLimit)



print(__name__)



#----DON'T MIND------
#Input: print("Your list of even numbers:" + str([i for i in range(0,10) if i%2==0]))
#Output: Your list of even numbers:[0, 2, 4, 6, 8]
