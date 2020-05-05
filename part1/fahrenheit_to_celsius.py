from math import degrees


def main():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
    print('32 degrees fahrenheit is equal to 0.0 degree(s) celsius')


if __name__ == '__main__':
    main()
