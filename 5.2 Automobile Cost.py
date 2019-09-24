def ask_about_expenses():
    monthly_loan_pay = float(input("how much do you pay on your" + " loan every month: "))
    monthly_insurance_pay = float(input("how much do you pay on your" + " insurance every month: "))
    monthly_gas = float(input("how much do you pay for your" + " gas every month: "))
    monthly_oil = float(input("how much do you pay for your" + " oil every month: "))
    monthly_tire = float(input("how much do you pay on your" + " tires every month: "))
    monthly_maintenance = float(input("how much do you pay for your" + " maintenance every month: "))

    return monthly_loan_pay, monthly_insurance_pay, monthly_gas, monthly_oil, monthly_tire, monthly_maintenance


def calculate_total_expenses_per_month(payment_1, payment_2, payment_3, payment_4, payment_5, payment_6):
    total_expenses_per_month = payment_1 + payment_2 + payment_3 + payment_4 + payment_5 + payment_6
    return total_expenses_per_month


def calculate_total_expenses_per_annual(total_Expenses_Per_Month ):
    total_expenses_per_annual = total_Expenses_Per_Month * 12
    return total_expenses_per_annual


def print_details(total_expenses_per_month, total_expenses_per_annual):
    print("The total monthly cost for you is $" + format(total_expenses_per_month, ",.2f") + "\nThe total annual cost for you is $" + format(total_expenses_per_annual, ",.2f"))


def main():
    payment_loan, payment_insurance, payment_gas, payment_oil, payment_tire, payment_maintenance = ask_about_expenses()

    total_expenses_per_month = calculate_total_expenses_per_month(payment_loan, payment_insurance, payment_gas, payment_oil, payment_tire, payment_maintenance)

    total_expenses_per_annual = calculate_total_expenses_per_annual(total_expenses_per_month)

    print_details(total_expenses_per_month, total_expenses_per_annual)


main()
