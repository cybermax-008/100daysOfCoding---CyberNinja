w = float(input("Enter Weight:"))
h = float(input("Enter Height:"))
# Calculate BMI using the formulae
bmi = w/(h*h)
if bmi > 25:
    print("Overweight")
elif bmi > 18.5:
    print("Normal Weight")
else:
    print("Under Weight")
