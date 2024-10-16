#Determine the number of dollars by dividing the total cents by 100.
#Calculate the remaining cents after accounting for dollars.
#Determine the number of quarters from the remaining cents.
#Calculate the remaining cents after accounting for quarters.
#Determine the number of dimes from the remaining cents.
#Calculate the remaining cents after accounting for dimes.
#Determine the number of nickels from the remaining cents.
#Calculate the remaining cents after accounting for nickels.
#The remaining cents are the number of pennies.
# Accepting input
cents = int(input())

# Calculating dollars, quarters, dimes, nickels, and pennies
dollars = cents // 100
remaining_cents = cents % 100

quarters = remaining_cents // 25
remaining_cents %= 25

dimes = remaining_cents // 10
remaining_cents %= 10

nickels = remaining_cents // 5
pennies = remaining_cents % 5

# Output
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)

#Division and Modulus Operations:

#// is the integer division operator that gives the number of times one number fits into another.
#% is the modulus operator that gives the remainder of the division.
#Sequential Calculations:

#Start with the largest denomination (dollars) and work down to the smallest (pennies).
#Example:

#If you input 287 cents:
#Dollars: 287 // 100 which is 2 dollars (remainder: 87 cents).
#Quarters: 87 // 25 which is 3 quarters (remainder: 12 cents).
#Dimes: 12 // 10 which is 1 dime (remainder: 2 cents).
#Nickels: 2 // 5 which is 0 nickels (remainder: 2 cents).
#Pennies: 2 pennies.