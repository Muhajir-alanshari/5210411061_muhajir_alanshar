from Ruangan import Ruangan


class RuangVIP(Ruangan):
    def __init__(self):
        super().__init__("Ruangan VIP", "Kode Ruang A")

    def inforuangVIP1(self):
        include = "PC Dewa & AC"
        bonus = "Snacks and soft drink"
        print("Ruangan Nomor 1")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def inforuangVIP2(self):
        include = "PC Dewa & AC"
        bonus = "Snacks and soft drink"
        print("Ruangan Nomor 2")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def inforuangVIP3(self):
        include = "PC Dewa & AC"
        bonus = "Snacks and soft drink"
        print("Ruangan Nomor 3")
        print("Fitur Ruangan : ", include)
        print("Bonus yang didapat : ", bonus)
        print("Jenis Ruangan: %s \nKode Ruangan: %s" %
              (self.jenisruangan, self.koderuangan))

    def tampilharga(self):
        print("=================================")
        print("\tHarga Sewa Ruangan\n 1 jam: Rp.15.000")

    def tampilhargaVIP(self):
        print("=================================")
        print("\tHarga Sewa Ruangan\n 1 jam: Rp.15.000")
