print ("Welcome to Super Fast Fiber Optic")

#capture the number of fee of Super Fast Fiber Optic to be installed from user
feet = float(input("Please enter number of feet of fiber optic cable to be installed:"))

#caculate the total cost

cost = feet * .87

#Display the calculated information and company name
print ("The total cost for installing", feet, "feet of Super Fast Fiber Optic is $",cost)

# determine cost per foot based on bulk discount
if feet > 500:
    price_per_foot = 0.50

elif feet > 250:
    price_per_foot = 0.70
    
elif feet > 100:
    price_per_foot = 0.80
    
else:
    price_per_foot = 0.87

# Calculate total cost
total_cost = feet * price_per_foot

# Display the total cost
print(f"The total cost for installing {feet:.0f} feet of fiber optic cable is: ${total_cost:.2f}")