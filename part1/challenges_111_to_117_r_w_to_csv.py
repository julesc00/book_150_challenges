import pandas as pd
import csv


def add_book_to_csv():
    """
    111
    Create a .csv file that will store the following data. Call it “Books.csv”.
    :return:
    """
    with open("docs/books.csv", "w") as f:
        f.write("To Kill A Mockingbird, Harper Lee, 1960\n")
        f.write("A Brief History of Time, Stephen Hawking, 1988\n")
        f.write("The Great Gatsby, F. Scott Fitzgerald, 1922\n")
        f.write("The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n")
        f.write("Pride and Prejudice, Jane Austen, 1813\n")

    return "Done!"


def add_record():
    """
    112
    Using the Books.csv file from program 111, ask the user to enter another record and add it to the
    end of the file. Display each row of the .csv file on a separate line.
    :return: Print book items
    """
    b_name = input("Enter book name: ").title(),
    b_author = input("Enter book author: ").title(),
    b_year = input("Enter book publishing year: "),

    entry_str = "\n" + ", ".join(b_name + b_author + b_year)
    entry_str = entry_str.rstrip(",") + "\n"

    with open("docs/books.csv", "a") as f:
        f.write(entry_str)
    with open("docs/books.csv", mode="r") as f:
        titles = f.read().split("\n")
    for title in titles:
        print(title)


def add_num_records():
    """
    113
    Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add
    that many. After all the data has been added, ask for an author and display all the books in the list by
    that author.
    If there are no books by that author in the list, display a suitable message.
    :return: books by author
    """
    # Capture and write books to csv file
    recs_to_add, recs = int(input("How many records do you want to add: ")), []
    while recs_to_add:
        recs.append(input("Enter book name, author and year separated by ',': "))
        recs_to_add -= 1
    with open("docs/books.csv", "a") as f:
        for record in recs:
            record += "\n"
            f.write(record)

    # Read books
    books, books_lst = list(csv.reader(open("docs/books.csv"))), []
    authors = set()
    for row in books:
        row = row[1].strip()
        books_lst.append(row)
        authors.add(row)

    print("Choose an author")
    [print(idx, book) for idx, book in enumerate(authors, start=1)]
    author = input("Author: ").title()

    # Enter better approach to make the below chunk of code

    if not len(authors):
        print("Choose an author")
    else:
        # NOTE: My loop doesn't work if I simplify it by breaking out of the if else statement
        for book in books:
            if author == book[1].strip():
                print(book)
            else:
                print("There are no books by that author")
                break


if __name__ == "__main__":
    print(add_num_records())
