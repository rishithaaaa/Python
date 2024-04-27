from info import resources
from info import MENU

profit = 0


def get_report():
    for i in resources:
        print(f"{i}: {resources[i]}")


def check_resources(coffee_items):
    for i in coffee_items:
        if coffee_items[i] > resources[i]:
            # or print(f"Sorry there is not enough {i}")
            return False, i
    return True, ""


def reduce_resources(coffee_resources):
    for i in coffee_resources:
        resources[i] = resources[i] - coffee_resources[i]


def return_change(q, d, n, p, coffee_ordered):
    q = q * 0.25
    d = d * 0.10
    n = n * 0.05
    p = p * 0.01
    total_amount = q+d+n+p

    return total_amount - coffee_ordered["cost"]


def start_coffee_machine(coffee_chosen, choice_of_coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    change = return_change(quarters, dimes, nickels, pennies, coffee_chosen)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print(f"Here is {round(change,2)} in change")
    print(f"Here is your {choice_of_coffee} enjoy!")
    reduce_resources(coffee_chosen["ingredients"]);
    return True


is_on = True

while is_on:
    is_available =[]
    options = ["espresso", "latte", "cappuccino", "report","off","on"]
    choice = input("What would you like? Type espresso/latte/cappuccino/report\n").lower()
    if choice not in options:
        print("Select only from the options given. Check for typos if any")
    elif choice == "off":
        print("Coffee Machine is turned off")
        is_on = False
        break
    elif choice == "report":
        get_report()
    else:
        coffee = MENU[choice]
        is_available = check_resources(coffee["ingredients"])
        if is_available[0]:
            if start_coffee_machine(coffee, choice):
                profit += coffee["cost"]
                resources["proft"] = profit
        else:
            print(f"Sorry there is not enough {is_available[1]}")


# print the report
# check the resources
# please insert coins
# cal the amount
# return the extra change if more || refund if not sufficient
# reduce the resources when used.
