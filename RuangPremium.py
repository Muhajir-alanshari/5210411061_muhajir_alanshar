from Ruangan import Ruangan


class RuangPremium(Ruangan):
    def __init__(self):
        super().__init__("Ruangan Premium", "Kode Ruang B")

    def inforuang1(self):
        include = "PC Dewa (No AC) "
        bonus = "Snacks and soft drink"
        print("Ruangan Nomor 1")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def inforuang2(self):
        include = "PC Dewa (No AC) "
        bonus = "Snacks and soft drink"
        print("Ruangan nomor 2")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def inforuang3(self):
        include = "PC Dewa (No AC) "
        bonus = "Snacks and soft drink"
        print("Ruangan nomor 3")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def tampilharga(self):
        print("=================================")
        print("\tHarga Sewa Ruangan\n 1 jam: Rp.10.000")
