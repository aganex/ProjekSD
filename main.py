from Owner.MenuOwner import menu_owner
from Buyer.MenuBuyer import menu_buyer

def main():
    while True:
        print("1. Masuk sebagai Owner")
        print("2. Masuk sebagai Penyewa")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            menu_owner()
        elif pilihan == '2':
            menu_buyer()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
