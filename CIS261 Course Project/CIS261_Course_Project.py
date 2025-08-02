def get_employee_name():
    return input("Enter employee name or 'End' to finish: ")
def get_hours_worked():
    return float(input("Enter the total hours worked: "))
def get_hourly_rate():
    return float(input("Enter the hourly rate: "))
def get_tax_rate():
    return float(input("enter the income tax rate (as decimal so it can populate): "))
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay
def display_employee_data(name, hours, rate, gross, tax_rate, tax, net):
    print("\nEmployee Internal Database for Payroll:")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${tax:.2f}")
    print("-" * 30)
def display_totals(employee_count, total_hours,total_gross,total_tax, total_net):
    print("\nPayroll Totals:")
    print(f"Total Employees: {employee_count}")
    print(f"Total Hours Worked: {total_hours:.2f}")
    print(f"Total Gross pay: ${total_gross:.2f}")
    print(f"Total Income Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_tax:.2f}")
    print("=" * 30)

def main ():
    employee_count = 0
    total_gross = 0
    total_hours = 0
    total_tax = 0 
    total_net = 0

    while True:
        name = get_employee_name()
        if name.lower() == "end":
            break

        hours = get_hours_worked()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross,tax,net = calculate_pay(hours, rate, tax_rate)
        display_employee_data(name, hours, rate, gross, tax_rate, tax, net)

        employee_count += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    display_totals(employee_count, total_hours, total_gross, total_tax, total_net)

if __name__ == "__main__":
    name()