# Name: Hetavi Gheewala
# Date: 07/10/2023


# Display your own name
Your_Name = (input("Enter your name: "))
print("Your Name",Your_Name)

# Part I - Bill calculation
subtotal = float(input("Enter the subtotal of the bill: "))
gratuity_rate = int(input("Enter the gratuity rate (in whole number): "))

# Display subtotal
print("SubTotal: ${:.2f}".format(subtotal))

# Calculate and display gratuity
gratuity_amount = subtotal * (gratuity_rate / 100)
print("Gratuity Rate: ${:.2f}".format(gratuity_amount))


# Set tax rate and calculate tax
tax_rate = 8
tax_amount = subtotal * (tax_rate / 100)
print("Tax: ${:.2f}".format(tax_amount))

# Calculate and display grand total
grand_total = subtotal + gratuity_amount + tax_amount
print("Grand Total: ${:.2f}".format(grand_total))

# Part II - Weight conversion
weight_pounds = float(input("Enter your weight in pounds: "))

# Display weight in pounds
print("Pounds: {:.2f}".format(weight_pounds))

# Calculate equivalent weight in kilograms, grams, and milligrams
weight_kilograms = weight_pounds * 0.453592
weight_grams = weight_kilograms * 1000
weight_milligrams = weight_grams * 1000

# Display converted weights
print("Kilograms: {:.2f}".format(weight_kilograms))
print("Grams: {:.2f}".format(weight_grams))
print("Milligrams: {:.2f}".format(weight_milligrams))
