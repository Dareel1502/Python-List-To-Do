
def bmi_converter_input(prompt):
    while True:
        try: 
            value = float(input(prompt))
            if value <= 0: 
                print ("Please Enter A number. ")
            else: 
                return value
        except ValueError:
            print("Invalid Input.")         
            

weightinput = bmi_converter_input("Enter Your Weight: " )

heightinput_feet = bmi_converter_input("Enter Your Height: ")

heightinput = heightinput_feet * 0.3048

bmi = float(weightinput / (heightinput ** 2))

if bmi >= 18 and bmi <= 24.9:
   print (f"Your Bmi is: {bmi:.2f} Normal")
elif bmi <= 17.9: 
    print (f"Your Bmi is: {bmi:.2f} Malnourished")   
elif bmi >= 25: 
   print (f"Your Bmi is: {bmi:.2f} Abnormal")













