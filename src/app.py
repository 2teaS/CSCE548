from db import ping
from dal.movies_dao import MoviesDAO
from dal.lists_dao import ListsDAO

movies = MoviesDAO()
lists = ListsDAO()

def print_rows(rows):
    if not rows:
        print("(none)")
        return
    for r in rows:
        print(r)

def main():
    if not ping():
        print("DB connection failed. Check db.py credentials + that MySQL is running.")
        return

    while True:
        print("\n== Movie Watchlist ==")
        print("1) List all movies")
        print("2) Add a movie")
        print("3) Show user lists")
        print("4) Show items in a list")
        print("0) Quit")
        choice = input("> ").strip()

        if choice == "1":
            print_rows(movies.list_all())

        elif choice == "2":
            title = input("Title: ").strip()
            year = int(input("Release year: ").strip())
            runtime_raw = input("Runtime minutes (blank ok): ").strip()
            runtime = int(runtime_raw) if runtime_raw else None
            genre = input("Genre (blank ok): ").strip() or None
            mid = movies.create(title, year, runtime, genre)
            print(f"Inserted movie_id={mid}")

        elif choice == "3":
            uid = int(input("User ID (1-10 seeded): ").strip())
            print_rows(lists.list_by_user(uid))

        elif choice == "4":
            lid = int(input("List ID: ").strip())
            print_rows(lists.list_items_for_list(lid))

        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

