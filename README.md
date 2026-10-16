# it601-midterm-project

## This python script reads example restaurant orders from a JSON file and creates two new json files called:
- 'customers.json' which contains customer phone numbers and names
- 'items.json' which contains menu items along with price and times ordered

## Script Functionality:
1. Reads the JSON file given on the command line
2. Loops through each order and collects the customer info
3. Formats the customers' phone numbers as xxx-xxx-xxxx
4. Then loops through each item and counts how many times it was ordered
5. Finally saves that information tnto the 2 files named above

## How to run:

1. Open a terminal after cloning this repo
2. run the command:

'''
python3 process_orders.py example_orders.json
'''
3. The program will create the two necessary files