#Simple console line program to allow basic UI use and testing of recently defined objects and methods
#Tom Beighton 11.04.21

print("Hello World, welcome to the CMS \n Please choose what operation you would like \n 1. Create new order \n 2. View order progress \n 3. Exit")
while True
    response = input()
    print("You responded", response)

    if response == "1":
        print(" \n Creating order...")
    else if response =="2"
        print("\n Viewing progress...")
    else
        exit()


