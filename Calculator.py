import math

print("Area Calculator 📐")

# shapes
print("1 = Triangle")
print("2 = Rectangle")
print("3 = Square")
print("4 = Circle")
print("5 = Quit")

1 == "Triangle"
2 == "Rectangle"
3 == "Square"
4 == "Circle"
5 == "Quit"

answer = int(input("Which shape: "))

while answer >= 6:
    answer = int(input("Which shape: "))

if answer == 1:
    b = int(input("base: "))
    h = int(input("height: "))
    total = (1/2)*b*h
    print(f"The area is {total}")
elif answer == 2:
    l = int(input("length: "))
    w = int(input("width: "))
    total = l*w
    print(f"The area is {total}")
elif answer == 3:
    s = int(input("side: "))
    total = s**2
    print(f"The are is {total}")
elif answer == 4:
    r = int(input("radius: "))
    total = math.pi*r**2
    print(f"The area is {total}")
else:
    print("Quit")