import json
import os
import time
import sys

# COLOR
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[35m"

# CLEAR
def clear():
    os.system("clear")

# BANNER
def banner():
    clear()
    print("\033[1;32m")
    print(r"""
███╗   ██╗██╗██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██║██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║██║█████╔╝     ███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║██║██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║██║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """)
    print(RESET)
    print(RED + "[ SYSTEM : ACTIVE ] [ ACCESS : GRANTED ]" + RESET)
    print(CYAN + "------------------------------------------" + RESET)

# LOADING
def loading(text="Initializing"):
    print(YELLOW + text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(RESET)

# SCAN EFFECT
def scan_effect():
    text = "[ SCANNING DATABASE ]"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

    for i in range(0, 101, 20):
        print(f"{GREEN}>> {i}%{RESET}")
        time.sleep(0.1)

# LOAD DATA
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        print(RED + "[!] data.json error!" + RESET)
        return None

# PARSE NIK
def parse_nik(nik, data):
    if not nik.isdigit() or len(nik) != 16:
        print(RED + "[!] ACCESS DENIED - NIK INVALID" + RESET)
        return

    print(GREEN + "[✓] ACCESS GRANTED" + RESET)
    time.sleep(0.5)

    scan_effect()

    tanggal = nik[6:8]
    bulan = nik[8:10]
    tahun = nik[10:12]
    prov = nik[0:2]
    kab = nik[0:4]
    kec = nik[0:6]
    uniq = nik[12:16]

    cekjk = int(nik[6:8])
    jk = "LAKI-LAKI" if cekjk <= 40 else "PEREMPUAN"

    provinsi = data.get("provinsi", {}).get(prov, prov)
    kabkot = data.get("kabkot", {}).get(kab, kab)
    kecamatan_data = data.get("kecamatan", {}).get(kec, kec)

    if isinstance(kecamatan_data, str) and "--" in kecamatan_data:
        kec_name, kode_pos = kecamatan_data.split("--")
    else:
        kec_name, kode_pos = kec, "N/A"

    print("\n" + RED + "[ TARGET IDENTIFIED ]" + RESET)
    print(CYAN + "=============================" + RESET)

    print(f"{GREEN}[+] Tanggal Lahir : {tanggal}/{bulan}/{tahun}{RESET}")
    print(f"{GREEN}[+] Jenis Kelamin : {jk}{RESET}")
    print(f"{GREEN}[+] Provinsi      : {provinsi}{RESET}")
    print(f"{GREEN}[+] Kab/Kota      : {kabkot}{RESET}")
    print(f"{GREEN}[+] Kecamatan     : {kec_name.strip()}{RESET}")
    print(f"{GREEN}[+] Kode Pos      : {kode_pos.strip()}{RESET}")
    print(f"{GREEN}[+] UID           : {uniq}{RESET}")

    print(CYAN + "=============================\n" + RESET)

# MENU
def menu():
    print(YELLOW + "[1] START SCAN")
    print("[2] INFO")
    print("[0] EXIT" + RESET)

# MAIN
def main():
    data = load_data()
    if not data:
        return

    while True:
        banner()
        menu()

        pilih = input(CYAN + ">> SELECT OPTION: " + RESET)

        if pilih == "1":
            nik = input(RED + ">> INPUT NIK: " + RESET)
            loading("Processing")
            parse_nik(nik, data)
            input(YELLOW + "Press ENTER..." + RESET)

        elif pilih == "2":
            print(GREEN + "\nTool parsing NIK (edukasi).\n" + RESET)
            input(YELLOW + "Press ENTER..." + RESET)

        elif pilih == "0":
            print(RED + "EXITING..." + RESET)
            break

        else:
            print(RED + "[!] INVALID OPTION" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()
