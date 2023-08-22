# Write a program that converts an integer in decimal format to binary format. 


# > Hint: The built-in bin() function in Python can convert decimal numbers to binary format. The function returns a string representation of the binary number, which includes a 0b prefix. 

# Your result should look like this:

# > 0b11011


decimal_number = int(input("Enter an integer in decimal format: "))

# Convert the decimal number to binary using the bin() function
binary_number = bin(decimal_number)


print("Binary representation:", binary_number)

