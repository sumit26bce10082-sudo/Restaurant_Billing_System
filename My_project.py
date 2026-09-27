# Python lists for menu data

foods = ["Paneer Butter Masala", "Dal Tadka", "Butter Naan", "Jeera Rice", "Veg Biryani"]
foods_price = [220, 150, 40, 120, 180]
item_No = [101, 102, 103, 104, 105]
Qty_ordered = [0,0,0,0,0]

# Logic 
name = str(input("Enter Customer Name: "))

print("~" * 50)
print ("                Family Restaurant           ")
print("~" * 50)

for i in range(0,5) :
    print ('[', item_No[i], ']',foods[i],'-',"Rs.",foods_price[i] )
    
print ("-"*50)    

while True:
    choice = input("Enter Items No to add (or 0 to complete order): ")

    if choice == "0":
        break

    if not choice.isdigit():
        print("Please enter a valid Item number.")
        continue

    code = int(choice)

    key = -1
    for i in range(0,5):
        if item_No[i] == code :
            key = i
            break

    if key == -1:
        print ("Incorrect item number! Please check again the menu.")   
        continue

    while True :
        qty_input = input("Enter quantity for "+ foods[key] + " : ")

        if not qty_input.isdigit():
            print("Please enter a valid quantity.")
            continue

        qty = int(qty_input)
        
        if qty <= 0:
            print("Please enter Quantity properly.")
            continue

        break

    Qty_ordered[key] += qty
    print("Added to cart: " + foods[key] + " x " + str(qty) )    


# Bill Calculation

subtotal = 0

print("~"*50)
print("                   FINAL BILL        ")
print("~"*50)
print ("Customer Name: "+ name )
print("-"*50)

for i in range (0,5):
    if Qty_ordered[i] > 0:
        cost = Qty_ordered[i] * foods_price[i]
        subtotal += cost
        print(foods[i] + " x " + str(Qty_ordered[i]) + " = Rs" + str(cost))

print ("-"*50)        


discount = 0
if subtotal >= 2000:
    discount = subtotal * 0.15
elif subtotal >= 1000:
    discount = subtotal * 0.10   
elif subtotal >= 500:    
    discount = subtotal * 0.05

Gst = (subtotal-discount)*0.05
final_payment = subtotal-discount + Gst   

print ("Subtotal:      Rs." + str(subtotal))
print ("Discount:      Rs." + str(discount))
print("GST (5%):      Rs." + str(Gst))
print("~"*50)
print("Total Payable Amount: Rs." + str(final_payment))
print("~"*50)
print("            Thank you! Visit again!           ")