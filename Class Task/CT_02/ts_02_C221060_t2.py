#Takes the mark of a student as input
marks = int(input("Enter the Marks(Must be between 0 to 100) : "))

#if the mark is between 70 to 100 then the student got A
if marks >= 70 and marks <= 100:
    print("Your grade is A")

#if the mark is between 60 to 69 then the student got B
elif marks >=60 and marks < 70:
    print("Your grade is B")

#if the mark is between 50 to 59 then the student got B
elif marks >=50 and marks < 60:
    print("Your grade is B")

#if the mark is less than 50 then the student is fail
elif marks < 50:
    print("You are fail")

#if the input is not in this range then the input is invalid
else:
    print("Give a valid mark as input")