#at first we initialize the counter variable
counter = 1
#takes the number as a input
number = int(input("Enter the number to get the multiplication table: "))
while(counter < 11):
    result = counter * number #it calculates the multiplication
    print(number , "*" , counter , "=" , result) #it prints the result
    counter += 1 #it is used to increase the value of the counter variable