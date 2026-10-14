firstNumber = float(input("Enter your first number: "))

operation = input("Enter the operation (+, -, *, /): ")

secondNumber = float(input("Enter your second number: "))

if operation == "+":
    if firstNumber.is_integer() or secondNumber.is_integer():
     result = int(firstNumber) + int(secondNumber)   
     print("The result is: " ,(result))

    else:
     result = (firstNumber) + (secondNumber)
     print("The result is: " ,(result))


elif operation == "-":
  if firstNumber.is_integer() or secondNumber.is_integer():
     result = int(firstNumber) - int(secondNumber)
     print("The result is: " , (result))

  else:
    result = (firstNumber) - (secondNumber)
    print("The result is: " , (result))


elif operation =="*":
  if firstNumber.is_integer() or secondNumber.is_integer():
   result = int(firstNumber) * int(secondNumber)
   print("The result is: " , (result))

  else:
    result = float(firstNumber) * float(secondNumber)
    print("The result is: " , (result))


elif operation =="/":
    if secondNumber != 0:
     result = float(firstNumber) * float(secondNumber)
     print("The result is: " , (result))

    else:
      print("Error: Cannot divide by zero!")

      
else:
  print("Invalid operation!")