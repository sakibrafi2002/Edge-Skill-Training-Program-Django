#at first we initialize the counter variable
counter = 1
#takes the number as a input
number = int(input("Enter the number to get the multiplication table: "))
while(counter < 11): #iterates from 1 to 10
    if counter == 3: #checks if the counter is 3 or not
        counter += 1 #it is used to increase the value of the counter variable
        continue # if the counter is 3 it skips below codes
    result = counter * number #it calculates the multiplication
    print(number , "*" , counter , "=" , result) #it prints the result
    counter += 1 #it is used to increase the value of the counter variable