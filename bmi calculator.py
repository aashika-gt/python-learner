#BMI CALCULATOR
weight = int(input("please enter your weight in kg "))
height = float(input("please enter your height in meter"))

bmi = weight / (height ** 2)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")