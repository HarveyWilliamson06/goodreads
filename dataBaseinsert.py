import os,csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://jjkpghfnhxsfek:c741dbae64fa248b6ce5a896e7c9c3b2ea766d9e1e6d3174a56e31ecdc7d3f83@ec2-54-247-94-127.eu-west-1.compute.amazonaws.com:5432/dfejbpftufif6n')

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn": isbn,
                 "title": title,
                 "author": author,
                 "year": year})
        print(f"Added Book {isbn}, {title}, {author}, {year}\n")
    db.commit()

if __name__ == "__main__":
    main()
