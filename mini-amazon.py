inventory = {
    101: ("Keyboard",1500,10),
    102: ("Mouse",1200,15),
    103: ("Monitor",8000,5),
    104: ("Laptop",58000,7),
    105: ("USB Cable",300,20)
}
cart = []

def product_display():

    print("\n========================AVAILABLE PRODUCTS========================")
    print(f"{'ID':<8}{'Product':<15}{'Price':<12}{'Stock'}")
    for pid, details in inventory.items():                                      
       name, price, stock = details
       print(f"{pid:<8}{name:<15}₹{price:<11}{stock}")


def add_to_cart():

    product_id = int(input("\nEnter the product ID to add the product in your cart: "))
    if product_id in inventory:
        name, price, stock = inventory[product_id]
        quantity = int(input("Enter the quantity of the product: "))
        if quantity <= stock:
            cart.append((product_id,quantity))
            inventory[product_id] = (
                name,
                price,
                stock - quantity
            )
            print(f"\n{quantity} {name} added to your cart")
        else:
            print("\nNot enough stock available")
    else:
        print("\nInvalid product ID. Please check again")

def apply_cupon(total,code):
    code = code.upper()
    if code == "SHOP#20":
        discount = total * 0.20
        print("\nCoupon code applied")
        return total - discount
    elif code == "SHOP#25":
        discount = total * 0.25
        print("\nCoupon code applied")
        return total - discount
    else:
        print("\nInvalid coupon code")
        return total

def generate_reciept():
    if len(cart) == 0:
        print("\nYour cart is empty")
        return
    print("\n========= RECEIPT =========")
    total = 0
    print(f"\n{'Product':<15}{'Quantity':<15}{'Total'}")
    for item in cart:
        product_id, quantity = item
        name, price, stock = inventory[product_id]
        item_total = price * quantity
        total += item_total
        print(f"{name:<15}{quantity:<15}₹{item_total}")
    print("-----------------------------------------")
    print(f"Subtotal = ₹{total}")
    choice = input("DO YOU HAVE A COUPON CODE? (yes/no): ")
    if choice.lower() == "yes":
       code = input("Enter the coupon code: ")
       total = apply_cupon(total,code)
    print(f"\nFinal Total = ₹{total}")
    print("\nThank you for shopping!")

while True:
    print("\n========= MINI AMAZON =========")

    print("1. View Product")
    print("2. Add to cart")
    print("3. Generate Receipt")
    print("4. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
       product_display()
    elif choice == 2:
        product_display()
        add_to_cart()
    elif choice == 3:
        generate_reciept()
    elif choice == 4:
        print("\nExiting Program....")
        print("\nProgram exited successfully!!")
        break
    else:
        print("\nInvalid choice. Try again")
