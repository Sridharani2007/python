hours = int(input("Enter total working hours: "))
rate = int(input("Enter hourly rate: "))

if hours <= 40:
    pay = hours * rate
    print("Regular Pay:", pay)
else:
    overtime = hours - 40
    regular_pay = 40 * rate
    overtime_pay = overtime * rate * 1.5
    total_pay = regular_pay + overtime_pay
    print("Overtime Hours:", overtime)
    print("Total Pay:", total_pay)

