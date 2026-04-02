"hello,world".upper()
print("hello,world".upper())

title ="pythoon for everyone"
title[0]
title = title.replace("for everyone", "")
start = title.upper()
title = title + "program"
print(title)


qoute = "Let it be, let it be, let it be"
result1 = qoute.replace("it be", "not", 5)
print(result1)


qoute = "Let it be, let it be, let it be"
result1 = qoute.find("let be")
result2 = qoute.find("small")
result3 = qoute.find("let be, 12")
print(result1,result2,result3)


number = int(input("please enter a number: "))
if number > 0:
    if number %3 == 0:
        print("The number is positive and diviable by 3")
    
else:
      print("The number is positive but not diviable by 3")
      
      
major  = (input("enter a major: "))
major.lower()
gender  = (input("enter a gender: "))
gender.upper()
if major.find("eng") >= 0:
    if gender == "female":
       print("you are wonderful  girlie Eng")
    else:
       print("you are male")
else:
    print("you are not ENG")