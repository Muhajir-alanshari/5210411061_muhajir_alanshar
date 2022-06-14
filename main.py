# from Ruangan import Ruangan
from RuangVIP import RuangVIP
from RuangPremium import RuangPremium
from BookingVIP import BookingVIP
from BookingPremium import BookingRuangPremium


def choiceRuanganVIP():
    choice = input(str("\nApakah ingin melanjutkan Penyewaan? [L/T]"))
    if choice == "L":
        f = BookingVIP()
        exit()
    elif choice == "T":
        exit()
    else:
        print("Pilihan kamu salah!")
        exit()


def choiceRuanganPremium():
    choice = input(str("\nApakah ingin melanjutkan Penyewaan? [L/T]"))
    if choice == "L":
        f = BookingRuangPremium()
        exit()
    elif choice == "T":
        exit()
    else:
        print("Pilihan kamu salah!")
        exit()


def RuanganVIP():
    print("\nSilahkan pilih Ruangan VIP yang tersedia \n 1.Ruangan 1 \n 2.Ruangan 2 \n 3.Ruangan 3")


def RuanganPremium():
    print("\nSilahkan pilih Ruangan Premium yang tersedia \n 1.Ruangan 1 \n 2.Ruangan 2 \n 3.Ruangan 3")


def formpesan():
    print("Silahkan isi form penyewaan")


def show_menu():
    print("************************************")
    print("--------Program Warnet Elits--------")
    print("--------------- Menu ---------------")
    print("~~~~~~` Silakan Pilih Ruangan `~~~~~\n")
    print("[1] Ruangan VIP")
    print("[2] Ruangan Premium")
    print("[0] Exit \n")
    print("====================================")
    pilih_menu = input("Pilih menu> ")
    if(pilih_menu == "1"):
        RuanganVIP()
        Ruangan = input("Pilih menu> ")
        if(Ruangan == "1"):
            a = RuangVIP()
            a.inforuangVIP1()
            a.tampilharga()
            choiceRuanganVIP()
        elif(Ruangan == "2"):
            i = RuangVIP()
            i.inforuangVIP2()
            i.tampilharga()
            choiceRuanganVIP()
        elif(Ruangan == "3"):
            i = RuangVIP()
            i.inforuangVIP3()
            i.tampilharga()
            choiceRuanganVIP()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "2"):
        RuanganPremium()
        Ruangan = input("Pilih menu> ")
        if(Ruangan == "1"):
            ay = RuangPremium()
            ay.inforuang1()
            ay.tampilharga()
            choiceRuanganPremium()
        elif(pilih_menu == "2"):
            br = RuangPremium()
            br.inforuang2()
            br.tampilharga()
            choiceRuanganPremium()
        elif(pilih_menu == "3"):
            br = RuangPremium()
            br.inforuang3()
            br.tampilharga()
            choiceRuanganPremium()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "0"):
        print("Terimakasih & Sampai Jumpa")
        exit()
    else:
        print("error")


if __name__ == "__main__":
    while True:
        show_menu()
