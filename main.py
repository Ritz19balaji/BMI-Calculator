def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)  # BMI formula

    # Classify BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

# Take user input
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# Calculate BMI
bmi, category = calculate_bmi(weight, height_cm)

# Display result
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
