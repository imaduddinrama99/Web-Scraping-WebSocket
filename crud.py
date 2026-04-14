import json
import os

DATA_FILE = "data.json"


if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# CREATE
def tambah_item(title, company, location, date):
    data = load_data()
    new_id = max([item["id"] for item in data], default=0) + 1

    data.append({
        "id": new_id,
        "title": title,
        "company": company,
        "location": location,
        "date": date
    })

    save_data(data)
    print("Data berhasil ditambahkan")


def lihat_semua():
    data = load_data()

    if not data:
        print("Tidak ada data")
        return

    print("\n{:<3} {:<25} {:<25} {:<20} {:<10}".format(
        "ID", "Title", "Company", "Location", "Date"
    ))
    print("=" * 90)

    for item in data:
        print("{:<3} {:<25} {:<25} {:<20} {:<10}".format(
            item["id"],
            item["title"][:24],
            item["company"][:24],
            item["location"][:19],
            item["date"]
        ))

# UPDATE
def update_item(item_id, title, company, location, date):
    data = load_data()

    for item in data:
        if item["id"] == item_id:
            item["title"] = title
            item["company"] = company
            item["location"] = location
            item["date"] = date
            save_data(data)
            print("Data berhasil diupdate")
            return

    print("ID tidak ditemukan")

# DELETE
def hapus_item(item_id):
    data = load_data()
    data = [item for item in data if item["id"] != item_id]
    save_data(data)
    print("Data berhasil dihapus")

# MENU
def menu():
    while True:
        print("\n=== MENU JOB DATA ===")
        print("1. Tambah Data")
        print("2. Lihat Data (Tabel)")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            title = input("Title: ")
            company = input("Company: ")
            location = input("Location: ")
            date = input("Date: ")
            tambah_item(title, company, location, date)

        elif pilih == "2":
            lihat_semua()

        elif pilih == "3":
            id = int(input("ID: "))
            title = input("Title baru: ")
            company = input("Company baru: ")
            location = input("Location baru: ")
            date = input("Date baru: ")
            update_item(id, title, company, location, date)

        elif pilih == "4":
            id = int(input("ID: "))
            hapus_item(id)

        elif pilih == "5":
            break

if __name__ == "__main__":
    menu()