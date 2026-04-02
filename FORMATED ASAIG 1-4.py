H1 = int(input("Enter the number of H1: "))
M1 = int(input("Enter the number of M1: "))
H2 = int(input("Enter the number of H2: "))
M2 = int(input("Enter the number of M2: "))
if (H1, M1) >= (H2, M2) :
    print(f"time {H1}:{M1} comes first chronologically")
else :
    print(f"time {H2}:{M2} comes first chronologically")