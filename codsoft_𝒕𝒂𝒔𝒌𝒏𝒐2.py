def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multi(a,b):
    return a*b
    
def divi(a,b):
    if a ==0:
        return "error divied by 0"
    return a/b
    

def main():
    print("Simple calculator")
    print("Select operation")
    print("1. add")
    print("2. sub")
    print("3. multiplay")
    print("4. divide")

    while True:
        choice = input("select opertaion: ")

        if choice in ["1","2","3", "4"]:
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))

            if choice == '1':
                print(f"The answer of {num1} + {num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"The answer of {num1} - {num2} = {sub(num1,num2)}")
            elif choice == '3':
                print(f"The answer of {num1} * {num2} = {multi(num1,num2)}")
            elif choice == '1':
                print(f"The answer of {num1}/{num2} = {divi(num1,num2)}")

            else:
                print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Goodbye!")







if __name__ == "__main__":
    main()