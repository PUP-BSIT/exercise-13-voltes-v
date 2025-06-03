def pineda_menu():
    choice = 0
    while choice != 7:
        print("\n=== PINEDA'S MENU ===")
        print("Hello! I am Dyanna May!\n")
        print("1. Basic Information")
        print("2. My Goals")
        print("3. Comment From Caculitan")
        print("4. Comment From Corpus")
        print("5. Comment From Gulles")
        print("6. Comment From Morales")
        print("7. Go Back to  Voltes V Modules")
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        print("-----------------------------------------------------")

        match choice:
            case 1:
                print("\n ---- MY BASIC INFO ----\n")
                print("Name: Dyanna May D. Pineda")
                print("Age: 19")
                print("Birthday: October 10, 2005")
                print("Pet: My Catto ' Harith '")
                print("-----------------------------------------------------")
            case 2:
                print("\n ---- MY GOALS ----\n")
                print("• Goal 1: To pass INTE 202")
                print("• Goal 2: To graduate College")
                print("• Goal 3: To be stable and happy")
                print("• Goal 4: To have a bright and happy future")
                print("-----------------------------------------------------")
            case 3:
                print("Comment From Caculitan")
                print("Makakapasa tayo sa INTE 202 <<3")
                print("-----------------------------------------------------")
            case 4:
                print("Comment From Corpus")
                print("-----------------------------------------------------")
            case 5:
                print("Comment From Gulles")
                print("You will be stable and happy :)))")
                print("-----------------------------------------------------")
            case 6:
                print("Comment From Morales")
                print("PASADO KA NA DYANNAAA")
                print("-----------------------------------------------------")
            case 7:
                print("Exiting Pineda Menu")
                print("-----------------------------------------------------")
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")