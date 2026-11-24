basic = float(input("Basic pay: Rs. "))
allowances = float(input("Allowances: Rs. "))
hours = float(input("Overtime hours: "))
rate = float(input("Overtime rate per hour: Rs. "))
incentive = float(input("Incentive: Rs. "))
if basic < 0 or allowances < 0 or hours < 0 or rate < 0 or incentive < 0:
    print("Invalid input: values must be non-negative")
else:
    overtime = hours * rate
    gross = basic + allowances + overtime + incentive
    pf = basic * 0.08
    tax = gross * 0.05
    net = gross - pf - tax
    print("Gross salary: Rs.", round(gross, 2))
    print("PF deduction: Rs.", round(pf, 2))
    print("Tax deduction: Rs.", round(tax, 2))
    print("Net salary: Rs.", round(net, 2))
