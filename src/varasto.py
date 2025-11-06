class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = self.test_tilavuus(tilavuus)
        self.saldo = self.test_saldo(alku_saldo)

    def test_tilavuus(self, tilavuus):
        if tilavuus > 0:
            return tilavuus
        return 0.0

    def test_saldo(self, saldo):
        if saldo < 0:
            return 0.0
        if saldo <= self.tilavuus:
            return saldo
        return self.tilavuus
    # huom: ominaisuus voidaan myös laskea. Ei tarvita
    # erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        s = f"{self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
        return f"saldo = {s}"
