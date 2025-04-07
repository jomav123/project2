def lab4_(num1, num2):
    result = num1 * num2
    print(f"{num1}x{num2}= {result}")
    return result

if __name__ == "__main__":
    # You can still manually run this if needed:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    lab4_(num1, num2)