try:
    num1 = int(input("Enter a first number="))
    num2 = int(input("Enter a second number="))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input. only integers are allowed")
except Exception as e:
    print("An unexpected error occurred:", e)
