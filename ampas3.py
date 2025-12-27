import subprocess
import os

# ===== Banner =====
os.system("cls")  # clear screen Windows
print("""
██╗  ██╗ █████╗  ██████╗██╗  ██╗    ██╗    ██╗██╗███████╗██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ██║    ██║██║██╔════╝██║
███████║███████║██║     █████╔╝     ██║ █╗ ██║██║█████╗  ██║
██╔══██║██╔══██║██║     ██╔═██╗     ██║███╗██║██║██╔══╝  ██║
██║  ██║██║  ██║╚██████╗██║  ██╗    ╚███╔███╔╝██║██║     ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝

        ⚡ H A C K   W I F I ⚡
              Cyber Security 
------------------------------------------------
       D A N Z X P L O I T
------------------------------------------------
Author : DanzXploit
Team   : Pasko Blackhat
Version: 2.0
""")

nama_wifi = input("Masukkan nama WiFi: ")

try:
    output = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', nama_wifi, 'key=clear'],
        stderr=subprocess.STDOUT
    ).decode('cp1252').split('\n')

    password = None
    for line in output:
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            break

    print("\n==============================")
    print(f"Nama WiFi : {nama_wifi}")

    if password:
        print(f"Password  : {password}")
    else:
        print("Password  : Tidak ditemukan")
    print("==============================")

except subprocess.CalledProcessError:
    print("\n[!] WiFi tidak ditemukan atau akses ditolak.")
