# Python compound interest calculator = (p(1+r/n)^t)

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if(principle<=0):
        print("Principle can't be less than or equal zero")
        
while rate <=0:
    rate = float(input("Enter the rate amount: "))
    if(rate <=0):
        print("rate can't be less than or equal zero")

while time <=0:
    time = float(input("Enter the Time amount: "))
    if(time<=0):
        print("Time can't be less than or equal zero")
        
total = principle * pow((1+ rate /100), time)
        
print (f"Balance after {time} year/s: ${total: .2f}")