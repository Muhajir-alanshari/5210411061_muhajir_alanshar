class BookingRuangPremium:

    def __init__(self):
        print("======================================")
        self.kasir = input("Nama Petugas Kasir : ")
        self.alamatkasir = input("Alamat kasir : ")
        print("______________________________________")
        print("\n\tData diri Penyewa ")
        self.namapenyewa = input("\nMasukkan nama: ")
        self.Umurpenyewa = input("Masukkan Umur: ")
        self.alamat = input("Masukan alamat : ")
        self.nomorTelepon = input("Masukan Nomor telepon : ")
        print("Silahkan pilih lama sewa: \n 1. 1 Jam \n 2. 2 jam \n 3. 3 jam \n 4. 4 jam \n 5. 5 jam")
        self.lamasewa = input("Masukkan pilihan: ")
        if(self.lamasewa == "1"):
            print("\n\tDETAIL DATA PENYEWAAN")
            print("======================================")
            print("Nama Kasir : %s" % (self.kasir))
            print("Alamat Kasir : %s" % (self.alamatkasir))
            print("______________________________________")
            print("Nama Penyewa : %s" % (self.namapenyewa))
            print("Umur Penyewa : %s" % (self.Umurpenyewa))
            print("Alamat Penyewa : %s" % (self.alamat))
            print("Nomor Telepon Penyewa : %s" % (self.nomorTelepon))
            print("Total sewa 1 Jam: Rp.10.000")
            print("Ruangan Premium")
            print("  ")
            print("Silahkan melakukan pembayaran sekarang")
            print("======================================")
        elif(self.lamasewa == "2"):
            print("\n\tDETAIL DATA PENYEWAAN")
            print("======================================")
            print("Nama Kasir : %s" % (self.kasir))
            print("Alamat Kasir : %s" % (self.alamatkasir))
            print("______________________________________")
            print("Nama Penyewa : %s" % (self.namapenyewa))
            print("Umur Penyewa : %s" % (self.Umurpenyewa))
            print("Alamat Penyewa : %s" % (self.alamat))
            print("Nomor Telepon Penyewa : %s" % (self.nomorTelepon))
            print("Total sewa 2 Jam: Rp.20.000")
            print("Ruangan Premium")
            print("  ")
            print("Silahkan melakukan pembayaran sekarang")
            print("======================================")
        elif(self.lamasewa == "3"):
            print("\n\tDETAIL DATA PENYEWAAN")
            print("======================================")
            print("Nama Kasir : %s" % (self.kasir))
            print("Alamat Kasir : %s" % (self.alamatkasir))
            print("______________________________________")
            print("Nama Penyewa : %s" % (self.namapenyewa))
            print("Umur Penyewa : %s" % (self.Umurpenyewa))
            print("Alamat Penyewa : %s" % (self.alamat))
            print("Nomor Telepon Penyewa : %s" % (self.nomorTelepon))
            print("Total sewa 3 Jam: Rp.35.000")
            print("Ruangan Premium")
            print("  ")
            print("Silahkan melakukan pembayaran sekarang")
            print("======================================")
        elif(self.lamasewa == "4"):
            print("\n\tDETAIL DATA PENYEWAAN")
            print("======================================")
            print("Nama Kasir : %s" % (self.kasir))
            print("Alamat Kasir : %s" % (self.alamatkasir))
            print("______________________________________")
            print("Nama Penyewa : %s" % (self.namapenyewa))
            print("Umur Penyewa : %s" % (self.Umurpenyewa))
            print("Alamat Penyewa : %s" % (self.alamat))
            print("Nomor Telepon Penyewa : %s" % (self.nomorTelepon))
            print("Total sewa 4 Jam: Rp.40.000")
            print("Ruangan Premium")
            print("  ")
            print("Silahkan melakukan pembayaran sekarang")
            print("======================================")
        elif(self.lamasewa == "5"):
            print("\n\tDETAIL DATA PENYEWAAN")
            print("======================================")
            print("Nama Kasir : %s" % (self.kasir))
            print("Alamat Kasir : %s" % (self.alamatkasir))
            print("______________________________________")
            print("Nama Penyewa : %s" % (self.namapenyewa))
            print("Umur Penyewa : %s" % (self.Umurpenyewa))
            print("Alamat Penyewa : %s" % (self.alamat))
            print("Nomor Telepon Penyewa : %s" % (self.nomorTelepon))
            print("Total sewa 5 Jam: Rp.50.000")
            print("Ruangan Premium")
            print("  ")
            print("Silahkan melakukan pembayaran sekarang")
            print("======================================")
        else:
            print("Inputan anda tidak tersedia")
            exit()
