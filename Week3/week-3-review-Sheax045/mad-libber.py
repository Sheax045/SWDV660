title = print("Madlib Maker")
measurementInput = input("measurement: ")
foodInput = input("food: ")
transportationInput = input("mode of transportation: ")


madlib = "99 {0}(s) of {1} on the {2}\n99 {0}(s) of {1}\nTake one down and pass it around\n98 {0}(s) of {1} on the {2}"

print(madlib.format(measurementInput, foodInput, transportationInput))


