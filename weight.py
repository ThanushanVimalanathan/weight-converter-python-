# weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram(k) or Pound(p): ")

if unit == "p":
    print("your weight is : ", float(weight*2.204),"kg")
    
elif unit == "k":
    print("your weight is : ", float(weight/2.204),"Lbs")

else:
    print("Invalid unit type...")
    
    