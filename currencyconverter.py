def dollar(a):
    return a*93.90


def euro(a):
    return a*94.06

def rupees(a):
    return a*1.14

def russian_rouble(a):
    return a*1.552

def canadian_dollar(a):
    return a*70.799


def yen(a):
    return a*0.65


while True:
    print("\033[46;5;225m\033[4;30;245m", """
    Options :
    1. US Dollar to Taka
    2. Canadian Dollar to Taka
    3. Russian Rouble to Taka
    4. Euro to Taka
    5. Rupees to Taka
    6. Japanese Yen to Taka
    """)
    choice = input("Choose one! 1/2/3/4/5/6 : \n")
    user_input = int(input("Enter the amount : "))

    if choice == "1":
        print("US Dollar to Taka : \n")
        print(dollar(user_input), "Taka")

    elif choice == "2":
        print("Canadian Dollar to Taka : \n")
        print(canadian_dollar(user_input), "Taka")

    elif choice == "3":
        print("Russian Rouble to Taka : \n")
        print(russian_rouble(user_input), "Taka")

    elif choice == "4":
        print("Euro to Taka\n")
        print(euro(user_input), "Taka")

    elif choice == "5":
        print("Rupees to Taka : \n")
        print(rupees(user_input), "Taka")

    elif choice == "6":
        print("Japanese Yen to Taka : \n")
        print(yen(user_input), "Taka")


    asking = input("Do you want to run the program again? y/n : ")

    if asking == "n":
        break
        exit()

    else:
        continue


