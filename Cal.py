while True:
    print("1 for addition\n2 for subtraction\n3 for multliplication\n4 for division\n5 for quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        sum = first_num + second_num
        print("Addition of two numbers: ",sum)
        
    elif choice == '2':
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        sum = first_num - second_num
        print("Subtraction of two number: ",sum)

    elif choice == '3':
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        sum = first_num * second_num
        print("Multiplication of two numbers: ",sum)

    elif choice == '4':
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        sum = first_num/second_num
        print("Division of two numbers: ",sum)

    elif choice == '5':
        break

    else:
        print("Please enter correct choice:)")