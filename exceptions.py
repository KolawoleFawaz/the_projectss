#To prevent your program from crashing due to errors
# an exception is a type of error that terminates the use of a program
#example

from contextlib import _AsyncGeneratorContextManager


numbers = [1,2,3]
print(numbers[4]) # there was no 4th index , so the program was terminated

#dealing with exceptions 
age = int(input("Age: "))
print(age) # if a different value type is supplied , there will be an error and the program would be terminated

#solution
try:
    age = int(input("Age: "))
except ValueError:
    print("you didn't enter valid age value.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
