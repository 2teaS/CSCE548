# client.py
import requests

BASE = "http://127.0.0.1:8000"

def pause():
    input("\nPress Enter to continue...")

def list_movies():
    r = requests.get(f"{BASE}/movies")
    print(r.json())

def create_movie():
    title = input("Title: ").strip()
    year = int(input("Release year: ").strip())
    runtime_raw = input("Runtime minutes (blank ok): ").strip()
    runtime = int(runtime_raw) if runtime_raw else None
    genre = input("Genre (blank ok): ").strip() or None

    r = requests.post(f"{BASE}/movies", json={
        "title": title,
        "release_year": year,
        "runtime_minutes": runtime,
        "genre": genre
    })
    print(r.status_code, r.json())
    return r.json().get("movie_id")

def get_movie():
    mid = int(input("Movie ID: ").strip())
    r = requests.get(f"{BASE}/movies/{mid}")
    print(r.status_code, r.json())

def update_movie():
    mid = int(input("Movie ID to update: ").strip())
    # get current for convenience
    cur = requests.get(f"{BASE}/movies/{mid}")
    if cur.status_code != 200:
        print(cur.status_code, cur.json())
        return
    cur = cur.json()
    print("Current:", cur)

    title = input(f"Title [{cur['title']}]: ").strip() or cur["title"]
    year_raw = input(f"Release year [{cur['release_year']}]: ").strip()
    year = int(year_raw) if year_raw else cur["release_year"]

    runtime_raw = input(f"Runtime minutes [{cur['runtime_minutes']}], blank keep, 'null' clear: ").strip()
    if runtime_raw.lower() == "null":
        runtime = None
    elif runtime_raw == "":
        runtime = cur["runtime_minutes"]
    else:
        runtime = int(runtime_raw)

    genre_raw = input(f"Genre [{cur['genre']}], blank keep, 'null' clear: ").strip()
    if genre_raw.lower() == "null":
        genre = None
    elif genre_raw == "":
        genre = cur["genre"]
    else:
        genre = genre_raw

    r = requests.put(f"{BASE}/movies/{mid}", json={
        "title": title,
        "release_year": year,
        "runtime_minutes": runtime,
        "genre": genre
    })
    print(r.status_code, r.json())
    # prove update by reading
    r2 = requests.get(f"{BASE}/movies/{mid}")
    print("After update:", r2.status_code, r2.json())

def delete_movie():
    mid = int(input("Movie ID to delete: ").strip())
    confirm = input("Type YES to confirm: ").strip()
    if confirm != "YES":
        print("Cancelled.")
        return
    r = requests.delete(f"{BASE}/movies/{mid}")
    print(r.status_code, r.json())
    # prove delete by reading
    r2 = requests.get(f"{BASE}/movies/{mid}")
    print("After delete (should be 404):", r2.status_code, r2.json())

def main():
    while True:
        print("\n=== Service Client (Project 2) ===")
        print("1) List movies (READ)")
        print("2) Create movie (CREATE)")
        print("3) Get movie by id (READ)")
        print("4) Update movie (UPDATE)")
        print("5) Delete movie (DELETE)")
        print("0) Quit")

        c = input("> ").strip()
        if c == "1":
            list_movies(); pause()
        elif c == "2":
            mid = create_movie()
            if mid:
                print("Created movie_id:", mid)
                print("Read-back:", requests.get(f"{BASE}/movies/{mid}").json())
            pause()
        elif c == "3":
            get_movie(); pause()
        elif c == "4":
            update_movie(); pause()
        elif c == "5":
            delete_movie(); pause()
        elif c == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

