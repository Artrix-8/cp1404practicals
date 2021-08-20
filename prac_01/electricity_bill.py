print()
print("Electricity bill estimator")
cpd = float(input("Enter cents per kWh: "))
duk = float(input("Enter daily use in kWh: "))
nbd = float(input("Enter number of billing days: "))
bill = cpd*0.01*duk*nbd
print("Estimated bill: ${:.2f}".format(bill))
print()

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = float(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Invalid input")
    tariff = float(input("Which tariff? 11 or 31: "))
duk = float(input("Enter daily use in kWh: "))
nbd = float(input("Enter number of billing days: "))
if tariff == 11:
    bill = TARIFF_11 * duk * nbd
elif tariff == 31:
    bill = TARIFF_31 * duk * nbd
print("Estimated bill: ${:.2f}".format(bill))
