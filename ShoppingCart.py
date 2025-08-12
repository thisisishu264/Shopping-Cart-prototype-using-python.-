class ShoppingList:

    def __init__(self, name, itemsList, cartNumber):
        self.name = name 
        self.itemsList = itemsList
        self.cartNumber = cartNumber 

    def itemadder(self, item, amount, cost):
        self.itemsList.update({item: [amount, cost]}) 

    def itemremover(self, item): 
        self.itemsList.pop(item) 
    
    def itemspecific(self, item):
        List = self.itemsList.get(item)
        if List is None:
            return 0
        total = List[0] * List[1] 
        return total 
    
    def item_editor(self, item, new_amount, new_cost):
        if item in self.itemsList:
            self.itemsList[item][0] = new_amount            
            self.itemsList[item][1] = new_cost
            return True
        return False
    
    def inventory_combiner(self, other):  
        for item in other.itemsList:
            if item in self.itemsList: 
                self.itemsList[item][0] += other.itemsList[item][0]  
            else:
                self.itemsList[item] = other.itemsList[item].copy()
        print("Items Merged Successfuly") 
    

    def total(self): 
        total = 0 
        for i in self.itemsList:
            List = self.itemsList.get(i)
            total = total + (List[0] * List[1])
        return total


if __name__ == "__main__": 
    cartNumbers = 1 
    ObjectList = [] 
    print("Welcome to shopping cart program.\n")
    run = True 
    while run: 
        print("1. to create cart.")
        print("2. to access created carts.")
        print("3. to delete a cart.")
        print("0. to exit program.")
        try:  
            user = int(input("Enter your number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user == 1:
            name = input("Enter Cart name: ")
            new_cart = ShoppingList(name, {}, cartNumbers)
            ObjectList.append(new_cart)
            print(f"Cart Number is {cartNumbers}")
            cartNumbers += 1
            
        elif user == 2:
            if not ObjectList:  
                print("No carts available. Please create a cart first.")
                continue
                
            try:  
                inp = int(input("Enter Cart Number: "))
            except ValueError:
                print("Please enter a valid cart number.")
                continue
                
            found = False
            for cart in ObjectList:
                if inp == cart.cartNumber:
                    found = True
                    print(f"\nAccessing Cart: {cart.name} (Number: {cart.cartNumber})")
                    while True:
                        print("\nCart Options:")
                        print("1. Add item")
                        print("2. Remove item")
                        print("3. View item total")
                        print("4. View cart total")
                        print("5. List all items")
                        print("6. Edit cart items")
                        print("7. Merge with another cart")
                        print("8. Go back to main menu")
                        try:  
                            choice = int(input("Enter your choice: "))
                        except ValueError:
                            print("Please enter a valid number.")
                            continue
                        
                        if choice == 1:
                            item = input("Enter item name: ")
                            try:
                                amount = int(input("Enter quantity: "))
                                cost = float(input("Enter unit cost: "))
                                cart.itemadder(item, amount, cost)
                                print(f"{item} added to cart.")
                            except ValueError:
                                print("Invalid quantity or cost. Please enter numbers.")
                                
                        elif choice == 2:
                            item = input("Enter item name to remove: ")
                            if item in cart.itemsList:
                                cart.itemremover(item)
                                print(f"{item} removed from cart.")
                            else:
                                print("Item not found in cart.")
                                
                        elif choice == 3:
                            item = input("Enter item name to view total: ")
                            total = cart.itemspecific(item)
                            if total > 0:
                                print(f"Total cost for {item}: {total:.2f}")
                            else:
                                print("Item not found in cart.")
                                
                        elif choice == 4:
                            total = cart.total()
                            print(f"Total cost for all items: {total:.2f}")
                            
                        elif choice == 5:
                            if not cart.itemsList:
                                print("Cart is empty.")
                            else:
                                print("\nItems in cart:")
                                for item, details in cart.itemsList.items():
                                    print(f"{item}: Quantity: {details[0]}, Unit Cost: {details[1]:.2f}")
                                    
                        elif choice == 6:  
                            item = input("Enter item name to edit: ")
                            if item in cart.itemsList:
                                try:
                                    new_amount = int(input("Enter new quantity: "))
                                    new_cost = float(input("Enter new unit cost: "))
                                    cart.item_editor(item, new_amount, new_cost)
                                    print(f"{item} updated.")
                                except ValueError:
                                    print("Invalid quantity or cost. Please enter numbers.")
                            else:
                                print("Item not found in cart.")

                        elif choice == 7: 
                            try:
                                othercart = int(input("Enter the cart number of cart you want to merge: "))
                                if 0 < othercart <= len(ObjectList):
                                    cart.inventory_combiner(ObjectList[othercart-1])
                                else:
                                    print("Invalid cart number.")
                            except ValueError:
                                print("Please enter a valid cart number.")
                                
                        elif choice == 8:
                            break
                            
                        else:
                            print("Invalid choice. Please try again.")
            
            if not found:
                print("Invalid Cart Number")
                
        elif user == 3:
            if not ObjectList:
                print("No carts available to delete.")
                continue
                
            try:
                inp = int(input("Enter Cart Number to delete: "))
                for i, cart in enumerate(ObjectList):
                    if inp == cart.cartNumber:
                        del ObjectList[i]
                        print(f"Cart {inp} deleted successfully.")
                        break
                else:
                    print("Invalid Cart Number.")
            except ValueError:
                print("Please enter a valid cart number.")
                
        elif user == 0:
            run = False
            print("Adios.")
            
        else:
            print("Use your eyes.")