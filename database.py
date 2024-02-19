import csv
import os
import time

productData = []

with open('product_data.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        strippedRow = []
        for item in row:
            strippedRow.append(item.strip())
        productData.append(strippedRow)


def ClearScreen():
    time.sleep(3)
    for i in range(0, 100):
        print("\n")


def AddProduct():
    newProduct = [input("New product ID: "), input("New product name: "), input("New product price: "),
                  input("New product category: ")]

    productData.append(newProduct)
    print("\'" + newProduct[1] + "' has been added to the database.")
    ClearScreen()


def ModifyProduct():
    print("Which product do you want to modify?")
    for i in range(0, len(productData)):
        print("[" + str(i + 1) + "] " + productData[i][1])

    selection = input("> ")
    isNumber = True

    try:
        selection = int(selection) - 1
    except ValueError:
        isNumber = False

    if not isNumber:
        print("ERROR: NO NUMBER DETECTED")
        ClearScreen()
        return

    if selection < 1 or selection > len(productData):
        print("ERROR: NUMBER OUT OF RANGE")
        ClearScreen()
        return

    match input("Which attribute do you want to modify?\n[1] ID\n[2] Name\n[3] Price\n[4] Category\n> "):
        case "1":
            productData[selection][0] = input("New product ID: ")
        case "2":
            productData[selection][1] = input("New product name: ")
        case "3":
            productData[selection][2] = input("New product price: ")
        case "4":
            productData[selection][3] = input("New product category: ")

    ClearScreen()


def RemoveProduct():
    print("Which product do you want to remove?")
    for i in range(0, len(productData)):
        print("[" + str(i + 1) + "] " + productData[i][1])

    selection = input("> ")
    isNumber = True

    try:
        selection = int(selection) - 1
    except ValueError:
        isNumber = False

    if not isNumber:
        print("ERROR: NO NUMBER DETECTED")
        ClearScreen()
        return

    if selection < 1 or selection > len(productData):
        print("ERROR: NUMBER OUT OF RANGE")
        ClearScreen()
        return

    print("\'" + productData[selection][1] + "\' has been deleted")
    productData.remove(productData[selection])
    ClearScreen()
    return


def SearchForProduct():
    name = input("Please enter the product name\n> ")

    found = False
    for product in productData:
        if name.lower() in product[1].lower():
            print(product)
            found = True

    if not found:
        print("ERROR: PRODUCT NOT FOUND")

    ClearScreen()


def BubbleSort():
    swapped = False
    for i in range(len(productData) - 1):
        if float(productData[i][2]) > float(productData[i + 1][2]):
            productData[i], productData[i + 1] = productData[i + 1], productData[i]
            swapped = True

    if swapped:
        BubbleSort()
        return

    for product in productData:
        print(product)

    sortTime = (time.time() * 1000) - (sortStartTime * 1000)
    print("Database sorted in " + str(sortTime) + " milliseconds")

    ClearScreen()


while True:
    os.system('cls')
    print("What do you want to do with your data?\n[1] Add new product\n[2] Modify existing product details\n[3] "
          "Remove product from database\n[4] Search for product in database\n[5] Sort by price\n[6] Leave")

    selection = input("> ")

    match selection:
        case "1":
            AddProduct()
        case "2":
            ModifyProduct()
        case "3":
            RemoveProduct()
        case "4":
            SearchForProduct()
        case "5":
            sortStartTime = time.time()
            BubbleSort()
        case _:
            break

print("Bye-bye!")
