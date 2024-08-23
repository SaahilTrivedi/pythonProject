
sideA = float(input("Enter the side A in cm: \n"))
sideB = float(input("Enter the side B in cm: \n"))
sideC = float(input("Enter the side C in cm: \n"))

if sideA == sideB == sideC:
    print("Triangle is called Equilateral.")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("Triangle is called Isosceles.")
else:
    print("Triangle is called Scalene.")