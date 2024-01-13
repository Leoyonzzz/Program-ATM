class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Saldo Anda saat ini: ${self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Anda telah menarik ${amount}. Saldo Anda saat ini: ${self.balance}")
        else:
            print("Jumlah penarikan tidak valid atau melebihi saldo.")

def main():
    # Inisialisasi ATM dengan PIN dan saldo awal
    atm = ATM(pin="1234", balance=1000)

    # Meminta pengguna untuk memasukkan PIN
    entered_pin = input("Masukkan nomor PIN Anda: ")

    # Memeriksa kecocokan PIN
    if entered_pin == atm.pin:
        print("PIN benar. Selamat datang di ATM.")
        
        while True:
            # Menampilkan menu ATM
            print("\nMenu ATM:")
            print("1. Cek Saldo")
            print("2. Tarik Uang")
            print("3. Keluar")

            # Meminta pengguna untuk memilih opsi
            choice = input("Pilih nomor menu: ")

            # Proses pilihan pengguna
            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                amount = float(input("Masukkan jumlah yang ingin ditarik: $"))
                atm.withdraw(amount)
            elif choice == "3":
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
    else:
        print("PIN salah. Program berakhir.")

if __name__ == "__main__":
    main()
