class Temperature:
    def convertFahrenheit(celsius):
        print("Celsius = {}\nFahrenhiet = {}".format(celsius, 1.8 * celsius + 32))


    def convertCelsius(fahrenheit):
        print("Fahrenheit = {}\nCelsius = {}".format(fahrenheit, (fahrenheit - 32) / 1.8))


temp = Temperature
temp.convertFahrenheit(45)
temp.convertCelsius(12)
