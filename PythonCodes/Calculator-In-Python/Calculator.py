# Basic Calculator
while True:
      #Ask the 1t number
      num1 = input("Enter first number (or q to quit): ")
      if num1 == "q":
            print("Goodbye")
            break
      num1 = float(num1)

      #Ask for the operator
      operator = input("Enter operator (+, -, *, /): ")

      #Ask for the 2nd number
      while True:
            num2 = input("Enter second number (or q to quit): ")
            if num2 == "q":
                  print("Goodbye")
                  exit()
            num2 = float(num2)
            if num2 == 0: #check if the num2 is zero
                print("WARNING: Division by zero")
                continue
            else:
                 break

      #Perform calculation
      if operator =='+':
          print(num1 + num2)
      elif operator =='-':
          print(num1 - num2)
      elif operator =='*':
          print(num1 * num2)
      elif operator =='/':
         print(num1 / num2)
      else:
          print("Invalid operator")