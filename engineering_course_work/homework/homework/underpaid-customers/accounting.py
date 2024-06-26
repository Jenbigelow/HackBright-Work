

def get_user_data(filename):
    customer_data = []
    csv = open(filename)
    for line in csv:
        tokens = line.rstrip().split("|")
        customer_id = int(tokens[0])
        customer_name = tokens[1]
        num_melons_bought = int(tokens[2])
        customer_money_paid = float(tokens[3])
        customer_data.append((customer_id,customer_name,num_melons_bought,customer_money_paid))
    return customer_data

def varify_transaction_pay(customer_name, num_melons_bought, customer_money_paid):
    melon_cost = 1.00
    total_due = melon_cost * num_melons_bought
    if total_due > customer_money_paid:
        print(f"{customer_name} owes money.")
        print(f"{customer_name} paid ${customer_money_paid:.2f}\n")
    elif total_due < customer_money_paid:
         print(f"{customer_name} overpaid.")
         print(f"{customer_name} paid ${customer_money_paid:.2f}\n")
    else:
        print(f"{customer_name} paid the correct amount. No action needed.\n")

def main():

    customer_data = get_user_data("customer-orders.txt")
    for data in customer_data:
        customer_name = data[1]
        num_melons_bought = data[2]
        customer_money_paid = data[3]
        varify_transaction_pay(customer_name, num_melons_bought, customer_money_paid)

main()

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
