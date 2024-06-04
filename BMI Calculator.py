
def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a value greater than zero.")

        except ValueError:
            print("Invalid input.")


def calculate_bmi(weight, height):
    return weight/ (height ** 2)


def classification_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    
    elif 25 <= bmi < 29.9:
        return "Overweight"

    else:
        return "Obesity"
    

def main():
    print("Welcome to the BMI Calculator")

    weight = get_input("Enter your weight in kilograms: ")
    height = get_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classification_bmi(bmi)

    print (f"\n Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()



