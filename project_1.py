# Tax Calculator
# Justin Speake
# 01-14-17

# This program calculates state and county sales tax at a fixed rate of 5% and 2.5% for a
# transaction subtotal collected from the user.  The program then outputs the individual
# tax amounts along with the transaction's grand total to the user in a uniform format.

# Get transasction subtotal from user, store to variable 'subtotal' as a floating point

subtotal = float(input("What is the dollar amount of the transaction? "))

# Define variables for state and county tax amounts, assign tax rates as 5% and 2.5% respectively
# Variables will be floating point type.

state_tax_rate = float(0.05)
county_tax_rate = float(0.025)

# Calculate state and county tax amount for transaction per data gathered from user.
# Find product of each 'tax_rate' variable and subtotal variable.
# Assign calculations to output variables remaining floating point type.

state_tax_amount = subtotal * state_tax_rate
county_tax_amount = subtotal * county_tax_rate

# Calculate transaction total and save to output variable 'transaction_total'
# Since all variable types are floating point, 'transaction_total' remain as such.

transaction_total = state_tax_amount + county_tax_amount + subtotal

# Print output variables to user uniformly formatted so that amount descriptions are left aligned
# and amounts are right aligned on the corresponding line, rounded to nearest hundredth.

print(format("transaction subtotal: ", '<23s'),
      format(subtotal, '12,.2f'))
print(format("state calculated tax: ", '<23s'),
      format(state_tax_amount, '12,.2f'))
print(format("county calculated tax: ", '<23s'),
      format(county_tax_amount, '12,.2f'))
print(format("transaction total: ", '<23s'),
      format(transaction_total, '12,.2f'))