# GeoCalc: calculator for solving perimeters, areas, circumferences, surface areas and volumes for conventional shapes
import math


def main():
    while True:
        print("\nWelcome to the GeoCalc.")
        print("Which shape do you need to calculate?\n1. square\n2. rectangle \n3. triangle\n4. circle\n5. trapezoid"
              "\n6. cube\n7. rectangular prism\n8. sphere\n9. cylinder\n10. cone")
        choice = int(input("Enter here (1-9): "))
        # Square P= 4s, A= s^2
        if choice == 1:
            l = float(input("Enter the length of one side: "))
            p = l*4
            a = l**2
            print("Perimeter: ", round(p, 4), "\nArea: ", round(a, 4))

        # Rectangle P= 2(l+w), A= l*w
        if choice == 2:
            l = float(input("Enter the length of the rectangle: "))
            w = float(input("Enter the width of the rectangle: "))
            p = 2*(l*w)
            a = l*w
            print("Perimeter: ", round(p, 4), "\nArea: ", round(a, 4))

        # Triangle P= a+b+c, A= (1/2)*b*h
        if choice == 3:
            s_a = float(input("Enter side A length: "))
            s_b = float(input("Enter side B length: "))
            s_c = float(input("Enter side C length: "))
            sum_sides = s_a + s_b + s_c  # Perimeter calculation

            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = (1 / 2) * base * height  # Correct area formula

            print("Perimeter:", round(sum_sides, 4), "\nArea:", round(area, 4))

        # Circle Circumference= 2PIr or C= PId, A= PIr^2
        if choice == 4:
            r = None
            circ = None
            choice = input("Are you using radius or diameter to find the circumference? (r/d): ")
            if choice == "r":
                r = float(input("Enter radius: "))
                circ = 2*(math.pi*r)
            if choice == "d":
                d = float(input("Enter diameter: "))
                circ = math.pi * d
            a = math.pi*(r**2)
            print("Circumference: ", round(circ, 4), "\nArea: ", round(a, 4))

        # Trapezoid A= (1/2)*(b1+b2)*h
        if choice == 5:
            b = float(input("Enter the base of the trapezoid: "))
            h = float(input("Enter the height of the trapezoid: "))
            a = (1/2)*(b*h)*h
            print("Area: ", round(a, 4))

        # Cube SA= 6s^2, V= s^3
        if choice == 6:
            s = float(input("Enter the length of a side: "))
            sa = 6*(s**2)
            v = s**3
            print("Surface area:", round(sa, 4), "Volume: ", round(v, 4))

        # Rectangular Prism SA= 2(lw+lh+wh), V= l*w*h
        if choice == 7:
            l = float(input("Enter the length: "))
            w = float(input("Enter the width: "))
            h = float(input("Enter the height: "))
            sa = 2*((l*w)+(l*h)+(w*h))
            v = l*w*h
            print("Surface area:", round(sa, 4), "Volume: ", round(v, 4))

        # Sphere SA= 4PIr^2, V= (4/3PIr^3)
        if choice == 8:
            r = float(input("Enter radius: "))
            sa = 4*(math.pi*r**2)
            v = 4/(3*(math.pi*r**3))
            print("Surface area:", round(sa, 4), "Volume: ", round(v, 4))

        # Cylinder SA= 2PIr^2+2PIr*h, V= PIr^2*h
        if choice == 9:
            r = float(input("Enter radius: "))
            h = float(input("Enter the height: "))
            sa = (2*(math.pi*r**2))+(2*(math.pi*(r*h)))
            v = (math.pi*r**2)*h
            print("Surface area:", round(sa, 4), "Volume: ", round(v, 4))

        # Cone SA= PIr^2+PI*r*l, V= (1/3)PIr^2*h
        if choice == 10:
            choice = input("Are you finding surface area, volume, or both? (a/b/c): ")
            if choice == "a":
                r = float(input("Enter radius: "))
                l = float(input("Enter the length: "))
                sa = (math.pi*r**2)+(r*l)
                print("Surface area: ", round(sa, 4))
            if choice == "b":
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                v = (1/3)*((math.pi*r**2)*h)
                print("Volume: ", round(v, 4))
            if choice == "c":
                r = float(input("Enter radius: "))
                l = float(input("Enter the length: "))
                sa = (math.pi * r ** 2) + (r * l)
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                v = (1 / 3) * ((math.pi * r ** 2) * h)
                print("Surface area:", round(sa, 4), "Volume: ", round(v, 4))

        again = input("Would you like more help? (Y/N): ").upper()
        if again == "Y":
            continue
        if again == "N":
            print("\nThank you for using GeoCalc. Goodbye.")
            break


main()
