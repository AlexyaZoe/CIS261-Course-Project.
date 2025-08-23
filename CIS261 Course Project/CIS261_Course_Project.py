def get_dates():
    from_date = input("Enter from date (mm/dd/yyyy): ")
    to_date = input("Enter to date (mm/dd/yyyy): ")
    return from_date, to_date
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
def display_employee_data(from_date, to_date, hours, rate, tax_rate, gross, tax, net):
    print("\nEmployee Internal Database for Payroll:")
    print(f"Pay Period: {from_date} to {to_date}")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${:.2f}")
    print("-" * 30)
def display_totals(totals):
    print("\nPayroll Totals:")
    print(f"Total Employees: {totals['num_employees']}")
    print(f"Total Hours Worked: {totals['total_hours']:.2f}")
    print(f"Total Gross pay: ${totals['total_gross']:.2f}")
    print(f"Total Income Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net']:.2f}")
    print("=" * 30)

def main ():
    employee_count = 0
    total_gross = 0
    total_hours = 0
    total_tax = 0 
    total_net = 0

    while True:
        from_date, to_date = get_dates()
        name = get_employee_name()
        if name.lower() == "end":
            break

        hours = get_hours_worked()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross,tax,net = calculate_pay(hours, rate, tax_rate)
        employees.append([from_date, to_date, name, hours, rate, tax_rate,gross,tax, net])

        employee_count += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    totals = {
        "num_employees": 0,
        "total_hours": 0,
        "total_gross": 0,
        "total_tax": 0,
        "total_net": 0,
    }

    print("\n Employee Payroll details " )
    for emp in employees:
        display_employee_data(*emp[:6], emp[6], emp[5], emp[7], emp[8])
        totals["num_employees"] += 1
        totals["total_hours"] += emp[3]
        totals["total_gross"] += emp[6]
        totals["total_tax"] += emp[7]
        totals["total_net"] += emp[8]
    display_totals(totals)

if __name__ == "__main__":
    main()
