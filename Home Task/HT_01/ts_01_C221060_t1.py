# 1. Converts string '123' to integer 123
result1 = int("123")
print("1. Converting '123' to integer:", result1)

# 2. Converts string '123.45' to float 123.45
result2 = float("123.45")
print("2. Converting '123.45' to float:", result2)

# 3. Converts integer 123 to string '123'
result3 = str(123)
print("3. Converting 123 to string:", result3)

# 4. Converts integer 0 to boolean False
result4 = bool(0)
print("4. Converting 0 to boolean:", result4)

# 5. Converts integer 1 to boolean True
result5 = bool(1)
print("5. Converting 1 to boolean:", result5)

# 6. Converts ASCII value 97 to character 'a'
result6 = chr(97)
print("6. Converting ASCII 97 to character:", result6)

# 7. Converts character 'a' to ASCII value 97
result7 = ord('a')
print("7. Converting character 'a' to ASCII:", result7)

# 8. Converts string 'hello' to a list of characters ['h', 'e', 'l', 'l', 'o']
result8 = list("hello")
print("8. Converting 'hello' to list:", result8)

# 9. Converts string 'hello' to a tuple ('h', 'e', 'l', 'l', 'o')
result9 = tuple("hello")
print("9. Converting 'hello' to tuple:", result9)

# 10. Converts string 'hello' to a set of unique characters {'h', 'e', 'l', 'o'}
result10 = set("hello")
print("10. Converting 'hello' to set:", result10)

# 11. Converts binary string '1010' to integer 10
result11 = int('1010', 2)
print("11. Converting binary '1010' to integer:", result11)

# 12. Converts integer 255 to hexadecimal string '0xff'
result12 = hex(255)
print("12. Converting integer 255 to hexadecimal:", result12)

# 13. Converts integer 255 to octal string '0o377'
result13 = oct(255)
print("13. Converting integer 255 to octal:", result13)

# 14. Converts integer 255 to binary string '0b11111111'
result14 = bin(255)
print("14. Converting integer 255 to binary:", result14)

# 15. Converts float 3.1415 to string '3.1415'
result15 = str(3.1415)
print("15. Converting float 3.1415 to string:", result15)

# 16. Converts integer 10 to complex number (10+0j)
result16 = complex(10)
print("16. Converting integer 10 to complex:", result16)

# 17. Converts string 'nan' to float NaN (Not a Number)
result17 = float("nan")
print("17. Converting 'nan' to float NaN:", result17)

# 18. Returns the length of string 'hello'
result18 = len("hello")
print("18. Getting length of 'hello':", result18)

# 19. Converts string 'hello' to uppercase 'HELLO'
result19 = "hello".upper()
print("19. Converting 'hello' to uppercase:", result19)

# 20. Converts string 'HELLO' to lowercase 'hello'
result20 = "HELLO".lower()
print("20. Converting 'HELLO' to lowercase:", result20)

# 21. Capitalizes the first letter of string 'hello' to 'Hello'
result21 = "hello".capitalize()
print("21. Capitalizing 'hello' to 'Hello':", result21)

# 22. Converts 'hello world' to title case 'Hello World'
result22 = "hello world".title()
print("22. Converting 'hello world' to title case:", result22)

# 23. Swaps case of 'hello' to 'HELLO' and vice versa
result23 = "hello".swapcase()
print("23. Swapping case of 'hello':", result23)

# 24. Removes leading and trailing spaces from '   hello   '
result24 = "   hello   ".strip()
print("24. Stripping leading and trailing spaces from '   hello   ':", result24)

# 25. Removes leading character 'h' from 'hello'
result25 = "hello".lstrip('h')
print("25. Removing leading 'h' from 'hello':", result25)

# 26. Removes trailing character 'o' from 'hello'
result26 = "hello".rstrip('o')
print("26. Removing trailing 'o' from 'hello':", result26)

# 27. Checks if 'hello' starts with 'h'
result27 = "hello".startswith('h')
print("27. Checking if 'hello' starts with 'h':", result27)

# 28. Checks if 'hello' ends with 'o'
result28 = "hello".endswith('o')
print("28. Checking if 'hello' ends with 'o':", result28)

# 29. Finds the first occurrence of 'e' in 'hello'
result29 = "hello".find('e')
print("29. Finding 'e' in 'hello':", result29)

# 30. Returns the index of the first occurrence of 'e' in 'hello'
result30 = "hello".index('e')
print("30. Index of 'e' in 'hello':", result30)

# 31. Replaces 'e' with 'a' in 'hello', resulting in 'hallo'
result31 = "hello".replace('e', 'a')
print("31. Replacing 'e' with 'a' in 'hello':", result31)

# 32. Splits 'hello world' by spaces into a list ['hello', 'world']
result32 = "hello world".split()
print("32. Splitting 'hello world' by spaces:", result32)

# 33. Splits 'hello,world' by comma into ['hello', 'world']
result33 = "hello,world".split(',')
print("33. Splitting 'hello,world' by comma:", result33)

# 34. Joins ['hello', 'world'] into a single string 'hello,world'
result34 = ",".join(['hello', 'world'])
print("34. Joining ['hello', 'world'] into 'hello,world':", result34)

# 35. Counts the occurrences of 'l' in 'hello', which is 2
result35 = "hello".count('l')
print("35. Counting occurrences of 'l' in 'hello':", result35)

# 36. Checks if all characters in 'hello' are alphabetic
result36 = "hello".isalpha()
print("36. Checking if 'hello' is alphabetic:", result36)

# 37. Checks if all characters in '123' are digits
result37 = "123".isdigit()
print("37. Checking if '123' is numeric:", result37)

# 38. Checks if all characters in 'abc123' are alphanumeric
result38 = "abc123".isalnum()
print("38. Checking if 'abc123' is alphanumeric:", result38)

# 39. Checks if the string '   ' contains only whitespace
result39 = "   ".isspace()
print("39. Checking if '   ' is whitespace:", result39)

# 40. Checks if 'Hello' is title-cased
result40 = "Hello".istitle()
print("40. Checking if 'Hello' is title-cased:", result40)

# 41. Checks if 'HELLO' is uppercase
result41 = "HELLO".isupper()
print("41. Checking if 'HELLO' is uppercase:", result41)

# 42. Checks if 'hello' is lowercase
result42 = "hello".islower()
print("42. Checking if 'hello' is lowercase:", result42)

# 43. Checks if 'hello123' is a valid Python identifier
result43 = "hello123".isidentifier()
print("43. Checking if 'hello123' is a valid identifier:", result43)

# 44. Pads '123' with zeros on the left to make it '00123'
result44 = "123".zfill(5)
print("44. Padding '123' with zeros to make it 5 characters:", result44)

# 45. Centers 'hello' in a string of width 10, with spaces on both sides
result45 = "hello".center(10)
print("45. Centering 'hello' in a field of width 10:", result45)

# 46. Left-aligns 'hello' in a string of width 10
result46 = "hello".ljust(10)
print("46. Left-aligning 'hello' in a field of width 10:", result46)

# 47. Right-aligns 'hello' in a string of width 10
result47 = "hello".rjust(10)
print("47. Right-aligning 'hello' in a field of width 10:", result47)

# 48. Splits 'hello world' into three parts: ('hello', ' ', 'world')
result48 = "hello world".partition(' ')
print("48. Partitioning 'hello world' by first space:", result48)

# 49. Splits 'hello world' from the right into three parts: ('hello', ' ', 'world')
result49 = "hello world".rpartition(' ')
print("49. Partitioning 'hello world' by last space:", result49)

# 50. Splits 'hello\nworld' into lines ['hello', 'world']
result50 = "hello\nworld".splitlines()
print("50. Splitting 'hello\\nworld' into lines:", result50)
