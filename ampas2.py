import os
import socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# ===== Warna =====
RED = "\033[91m"
DARK_RED = "\033[31m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(RED + """
========================================
   ██████╗  █████╗ ███╗   ██╗███████╗
   ██╔══██╗██╔══██╗████╗  ██║╚══███╔╝
   ██║  ██║███████║██╔██╗ ██║  ███╔╝
   ██║  ██║██╔══██║██║╚██╗██║ ███╔╝
   ██████╔╝██║  ██║██║ ╚████║███████╗
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
          Osint By DanzXploit
========================================
""" + RESET)

# ===== PHONE OSINT =====
def osint_phone():
    number = input(DARK_RED + "Masukkan nomor (+62xxxx): " + RESET)
    try:
        phone = phonenumbers.parse(number, None)
        print(RED + "\n[ PHONE OSINT RESULT ]" + RESET)
        print("Lokasi   :", geocoder.description_for_number(phone, "id"))
        print("Provider :", carrier.name_for_number(phone, "id"))
        print("Timezone :", ", ".join(timezone.time_zones_for_number(phone)))
        print("Valid    :", phonenumbers.is_valid_number(phone))
    except:
        print(DARK_RED + "Nomor tidak valid!" + RESET)

# ===== IP OSINT =====
def osint_ip():
    ip = input(DARK_RED + "Masukkan IP / Domain: " + RESET)
    try:
        target = socket.gethostbyname(ip)
        print(RED + "\n[ IP OSINT RESULT ]" + RESET)
        print("IP Address :", target)
        print("Hostname   :", socket.getfqdn(target))
    except:
        print(DARK_RED + "IP / Domain tidak valid!" + RESET)

# ===== EMAIL OSINT =====
def osint_email():
    email = input(DARK_RED + "Masukkan email: " + RESET)
    print(RED + "\n[ EMAIL OSINT RESULT ]" + RESET)

    if "@" in email:
        username, domain = email.split("@")
        print("Username :", username)
        print("Domain   :", domain)
        try:
            print("IP Domain:", socket.gethostbyname(domain))
        except:
            print("IP Domain: Tidak ditemukan")
    else:
        print(DARK_RED + "Format email tidak valid!" + RESET)

# ===== USERNAME OSINT =====
def osint_username():
    user = input(DARK_RED + "Masukkan username: " + RESET)
    print(RED + "\n[ USERNAME OSINT RESULT ]" + RESET)
    print("Cek manual di platform:")
    print(f"- https://instagram.com/{user}")
    print(f"- https://github.com/{user}")
    print(f"- https://twitter.com/{user}")
    print(f"- https://tiktok.com/@{user}")

# ===== MENU =====
def menu():
    while True:
        clear()
        banner()
        print(RED + """
[1] OSINT Phone Number
[2] OSINT IP Address
[3] OSINT Email
[4] OSINT Username
[0] Exit
""" + RESET)

        choice = input(DARK_RED + "Pilih menu: " + RESET)

        if choice == "1":
            osint_phone()
        elif choice == "2":
            osint_ip()
        elif choice == "3":
            osint_email()
        elif choice == "4":
            osint_username()
        elif choice == "0":
            print(DARK_RED + "Keluar..." + RESET)
            break
        else:
            print(DARK_RED + "Menu tidak tersedia!" + RESET)

        input(RED + "\nTekan ENTER untuk kembali ke menu..." + RESET)

# ===== RUN =====
menu()
