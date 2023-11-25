import pandas as pd
#import xlwt
#import csv
#from datetime import datetime
student = {
    "first name": "Adam",
    "last name" : "Haris",
    "books issued": []
}

entries_list = []
#count = 1
if len(entries_list) == 0:
    count = 1
else:
    count = len(entries_list)

def showBooks ():
    print(entries_list)

def addBook ():
    bidding = 1
    expandedDictionary = {}
    
    # entries_list.append(BooksDict)
    #print(entries_list)
    while bidding:
        expandedDictionary = {}
        author = input("What is Author?\n")
        title = input("What is Title?\n")
        publisher = input("What is your Publisher?\n")
        global count
        expandedDictionary["bookID"] = count
        expandedDictionary["Author"] = author
        expandedDictionary["Title"] = title
        expandedDictionary["Publisher"] = publisher
        expandedDictionary["issued"] = 0
        entries_list.append(expandedDictionary)
        print(entries_list)
        other_bidders = input("Are there any other books? Type 'yes' or 'no'\n")
        if other_bidders == "yes":
            print("Yes")
        else:
            bidding = 0
        count += 1

def removeBook():
    id = int(input("Enter id of the book you want to delete: "))

    if id > 0 and id <= len(entries_list):
        entries_list.pop(id - 1)
    else:
        print("Index out of range")
    # printing the updated list
    print("List after deletion of dictionary: " + str(entries_list))
    global count
    count = count -1

def issueBook():
    id = int(input("Enter id of the book you want to issue: "))
    if id > 0 and id <= len(entries_list):
        bookToIssue = entries_list[id - 1]
        if bookToIssue["issued"] == 0:
            student["books issued"].append(id)
            entries_list[id - 1]["issued"] = 1
            print("Book is issued successfully!")
            # printing the updated list
            print("List after issuing: " + str(entries_list))
        else:
            print(f"Book is already issued to {student["first name"]}!")
    else:
        print("Issue index out of range")

def returnBook():
    id = int(input("Enter id of the book you want to return: "))
    if id > 0 and id <= len(entries_list):
        bookToReturn = entries_list[id - 1]
        if bookToReturn["issued"] == 1:
            entries_list[id - 1]["issued"] = 0
            print("Book has been returned successfully!")
            print("List after return: " + str(entries_list))
        else:
            print(f"This book was not issued")
    else:
        print("Return index out of range")

def showAvailableBooks():
    i = 0
    for i, entry in enumerate(entries_list):
        if entry["issued"] == 1:
            print(f"Book {entry["bookID"]} is not available\n")
        else:
            print(f"Book {entry["bookID"]} is available\n")
    print("-------------------")

def main():
 # Pick the existing list of books in file
    df = pd.read_csv('df.csv')
    entries_list.extend(df.to_dict('records'))
    global count
    count += len(entries_list)
    #print(entries_list)
    print("Welcome to Book Management System!")
    while True:
        print("Please select your choice!")
        print("[1] -> Add Book")
        print("[2] -> Remove Book")
        print("[3] -> Issue Book")
        print("[4] -> Show Books")
        print("[5] -> Show Available Books")
        print("[6] -> Return Book")
        choice = int(input())
        if choice == 1:
            addBook()
        elif choice == 2:
            removeBook()
        elif choice == 3:
            issueBook()
        elif choice == 4:
            showBooks()
        elif choice == 5:
            showAvailableBooks()
        elif choice == 6:
            returnBook()
        else:
            df = pd.DataFrame(entries_list)
            df.to_csv('df.csv', index=False)
            break

if __name__ == "__main__":
    main()