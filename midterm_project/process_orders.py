import json
import argparse


def process_orders():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # Read the file
    with open(args.filename, "r") as file:
        orders = json.load(file)

    customers = {}
    items = {}

    for order in orders:

        # Get the customer information
        name = order["name"]
        phone = str(order["phone"])

        phone = phone.replace("-", "")
        phone = phone.replace(" ", "")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")

        if len(phone) == 11 and phone[0] == "1":
            phone = phone[1:]

        if len(phone) != 10:
            raise ValueError("Invalid phone number: " + phone)

        phone = phone[:3] + "-" + phone[3:6] + "-" + phone[6:]

        customers[phone] = name

        # Go through every item in the order
        for item in order["items"]:
            item_name = item["name"]
            price = item["price"]

            if item_name not in items:
                items[item_name] = {
                    "price": price,
                    "orders": 1
                }
            else:
                items[item_name]["orders"] += 1

    # Save customer info
    with open("customers.json", "w") as file:
        json.dump(customers, file, indent=4)

    # Save item info
    with open("items.json", "w") as file:
        json.dump(items, file, indent=4)

    print("Files created successfully!")


process_orders()

