from sys import exit
mark = float(input("Enter the mark: "))
if mark < 0 or mark > 100 :
    exit("Error: you must enter a mark between 0 and 100")
if mark >= 90 :
   print("A")
elif mark >= 80:
   print("B")
elif mark >= 70:
   print("C") 
elif mark >= 60:
    print("D")
else :
    print("your graed is", gread)