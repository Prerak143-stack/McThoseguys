

print("\n\n\t\tHello and Welcome to McThoseguys - Fast Food Restaurant")
print("-"*80)

confirm_order = False

while confirm_order != True:
    order_to_carryout = False
    name = []
    while order_to_carryout != True:
        customer_name = input("\nBefore ordering anything can we get your good name please : ")
        customer_name = customer_name.lower()
        print(customer_name)
        L_count = 0
        name = []
        length_of_string = int(len(customer_name)) + 1
        while L_count != length_of_string:
            R_count = 0
            while R_count != length_of_string:
                if customer_name[L_count:R_count] in ["mud","dirt","dust","booger","diaper"]:
                
                    print("\nYour name contains dirty name\n")
                    name = name + ["dirty"]
                    

                else:
                    name = name + ["good"]
                    
                R_count += 1
            L_count += 1
        if "dirty" in name:
            order_to_carryout = False
        else:
            order_to_carryout = True
        
    wrapper_sandwich = False
    choice_protein = False
    sauce = False

    while wrapper_sandwich != True:
        print("\n\nWhat would you like as your sandwich wrapper ?")
        print("[1]sesame seed bun")
        print("[2]soft tortilla shell\n")
        sandwich_chart = ["sesame seed bun","soft tortilla shell"]
        sandwich_wrapper = int(input("What is your choice ? "))
        if sandwich_wrapper > 3 or sandwich_wrapper < 0:
            print("I’m sorry, that isn’t a valid choice, please try again.\n")
            wrapper_sandwich = False
        else:
            wrapper_sandwich = True

    while choice_protein != True:
        print("\n\nWhat would you like as your protein choice ?")
        print("[1]chicken")
        print("[2]beef")
        print("[3]tofu\n")
        protein_choice = int(input("What is your choice ? "))
        protein_chart = ["chicken","beef","tofu"]
        if protein_choice >= 4 or protein_choice <= 0:
            print("I’m sorry, that isn’t a valid choice, please try again.\n")
            choice_protein = False
        else:
            choice_protein = True

    choices_list = []
    print_choices = []
    count = 0
    tomato_count = 0
    lettuce_count = 0
    pickles_count = 0
    cheese_count = 0
    onions_count = 0


    while count != 3:
        print("\n\nWhat would you like as your topping choice (pick 1-3 items) ?")
        print("[1]tomato")
        print("[2]lettuce")
        print("[3]pickles")
        print("[4]cheese")
        print("[5]onions\n")
        topping_choice = input("\nWhat is your choice or enter q to quit ? ")
        toppings_chart = ["tomato","lettuce","pickles","cheese","onions",""]
        topping_choice = topping_choice.lower()
        if str(topping_choice) == "q":
            if count >= 1:
                break
            elif count == 0:
                print("\nI’m sorry, you must choose at least 1 option(s).\n")
        
        if topping_choice.isdecimal():
            if int(topping_choice) > 6 or int(topping_choice) < 0:
                print("\nI’m sorry, that isn’t a valid choice, please try again.\n")

            else:
                count += 1
                
                if topping_choice in print_choices:
                    print_choices += ["6"]
                else:
                    print_choices += [topping_choice]
                choices_list += [topping_choice]

                if topping_choice in choices_list:
                    
                    if topping_choice == "1":
                        tomato_count += 1
                    if topping_choice == "2":
                        lettuce_count += 1
                    if topping_choice == "3":
                        pickles_count += 1
                    if topping_choice == "4":
                        cheese_count += 1
                    if topping_choice == "5":
                        onions_count += 1
            
            
    if count == 1 :
        print_choices += ["6"]
        print_choices += ["6"]
    if count == 2 :
        print_choices += ["6"]
    if tomato_count == 2 or tomato_count == 3 :
        toppings_chart[0] = "extra " + toppings_chart[0]
    if lettuce_count == 2 or lettuce_count == 3 :
        toppings_chart[1] = "extra " + toppings_chart[1]
    if pickles_count == 2 or pickles_count == 3:
        toppings_chart[2] = "extra " + toppings_chart[2]
    if cheese_count == 2 or cheese_count == 3:
        toppings_chart[3] = "extra " + toppings_chart[3]
    if onions_count == 2 or onions_count == 3:
        toppings_chart[4] = "extra " + toppings_chart[4]


    while sauce != True:
        print("\nWhat would you like as a sauce ?")
        print("[1]ketchup")
        print("[2]mayonaise")
        print("[3]McCalorie Secret Sauce\n")
        sauce_chart = ["ketchup","mayonise","McCalorie Secret Sauce","no sauce"]
        sauce_choice = input("\nWhat is your choice or enter q to quit ? ")
        sauce_choice = sauce_choice.lower()
        if sauce_choice == "q":
            sauce_choice = 4
            break
        else:
            sauce = True

    print("There are those who call me ... Prerak, you have chosen a " + \
          protein_chart[int(protein_choice) - 1] + \
" sandwich on a " + sandwich_chart[int(sandwich_wrapper) - 1] + ", with " \
       + toppings_chart[int(print_choices[0]) - 1] + " " + (toppings_chart[int(print_choices[1]) - 1]) \
          + " " + (toppings_chart[int(print_choices[2]) - 1]) + " and " + sauce_chart[int(sauce_choice) - 1] + ".\n\n")

    confirmation = input("\nIs this correct, yes or no ? ")
    confirmation = confirmation.lower()
    if confirmation == "yes":
        print("\nThank you for shopping at McThoseguys! Enjoy your food!\n\n")
        confirm_order = True
    else:
        confirm_order = False
        print("Sorry, let’s try again from scratch.")
    
