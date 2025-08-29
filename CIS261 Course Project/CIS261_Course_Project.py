import os
from datetime import datetime

FILENAME = "employee_data.txt"

def get_dates():
    from_date = input("Enter a from date (mm/dd/yyyy): ")
    to_date = input("Enter a to date (mm/dd/yyyy): ")
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

def display_employee_data(from_date, to_date, name, hours, rate, tax_rate, gross, tax, net):
    print(f"From: {from_date} | To: {to_date} | Name: {name} | "
          f"Hours: {hours:.2f} | Rate: ${rate:.2f} | Gross: ${gross:.2f} | "
          f"Tax Rate: {tax_rate:.2f%} | Income Tax: ${tax:.2f} | Net Pay: ${net:.2f}")

def display_totals(totals):
    print("-" * 90)
    print(
        f"Totals: Employees: {totals['num_employees']} | "
        f"Hours: {totals['total_hours']:.2f} | "
        f"Gross: ${totals['total_gross']:.2f} |"
        f"Income Tax: ${totals['total_tax']:.2f} |"
        f"Net Pay:${totals['total_net']:.2f}"
    )
    print("=" * 90)

def save_employee_to_file(from_date, to_date, name, hours, rate, tax_rate):
    with open(FILENAME, "a") as file:
        file.write(f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n")

def generate_report():
    if not os.path.exists(FILENAME):
        print("No employee data can be located.")
        return

    report_date = input("Enter from date to run report (mm/dd/yyyy) or 'All': ")
    if report_date.lower() != "all":
       try:
           datetime.datetime.strptime(report_date, "%m/%d/%Y")
       except ValueError:
            print("Invalid date format, please try again.")
            return
    totals = {
        "num_employees": 0,
        "total_hours": 0,
        "total_gross": 0,
        "total_tax": 0,
        "total_net": 0,
    }

    print("\n Payroll Report")
    print("-" * 90)

    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            from_date, to_date, naem, hours, rate, tax_rate = line.split("|")
            if report_date.lower() != "all" and from_date != report_date:
                continue
            hours = float(hours)
            rate = float(rate)
            tax_rate = float(tax_rate)
            gross, tax, net = calculate_pay(hours, rate, tax_rate)
        def display_employee_date(from_date, to_date, name, hours,rate,tax_rate, gross, tax, net):

            totals["num_employees"] += 1
            totals["total_hours"] += hours
            totals["total_gross"] += gross
            totals["total_tax"] += tax
            totals["total_net"] += net

    display_totals(totals)

def main ():
    while True:
        print("\n Employee Payroll System")
        print("1- Enter employee Data")
        print("2 - Generate Payroll Report")
        print("3 - Exit the system")
        choice = input("Enter a number please: ").strip()

        if choice =="1":
            while True:
                from_date, to_date = get_dates()
                name = get_employee_name()
                if name.lower() == "end":
                    break
                hours = get_hours_worked()
                rate = get_hourly_rate()
                tax_rate = get_tax_rate()

                save_employee_to_file(from_date, to_date, name, hours, rate, tax_rate)
                print(f"Employee {name} saved to file\n")

        elif choice == "2":
            generate_report()

        elif choice == "3":
            print(" Exiting employee directory. ")
            break

        else:
            print("Invalid Selection, Please try yopur input again. ")

if __name__ == "__main__":
    main()