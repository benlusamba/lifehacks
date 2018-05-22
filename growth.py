#Portfolio Growth Calculator (incorporation Asset Allocation)

#User Inputs:
num1 = input('Waiting Time (Years): ')
num2 = input('Equity Allocation (Dollars): ')
num3 = input('Bond Allocation (Dollars): ')

#Transform string inputs into floats and integers for calculation:
a = int(float(num1))
b = int(float(num2))
c = int(float(num3))

#Define the customers asset allocation:
d = b/(b+c)
e = c/(b+c)

#Alternatively, these can be user inputs. We fix them for simplicity:
stock = 0.08
bond = 0.03

#Coumpound Interest
print ("Projected Net Worth (Dollars):", int(d*b*(1+stock)**a + (e*c*(1+bond)**a)))

#Doubling Time Calculator (CAGR)
projected_worth = int(d*b*(1+stock)**a + (e*c*(1+bond)**a))
multiple = projected_worth / (b+c)
print("Doubling Time (Years):", int(72/(100*(multiple**(1/a)-1))))
