import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    #tää siis ns testaa sitä et onko ees olemas tai luo sen?
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    #Mun tekemä muutos negatiivisen tilavuuden nollaantuminen?
    def test_uudella_varastolla_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    #Mun tekemä testataan et nollaantuu negatiivinen saldo:
    def test_konstruktori_negatiivisen_saldon_nollaantuminen(self):
        varasto = Varasto(10, -8)
        self.assertAlmostEqual(varasto.saldo, 0.0)
    
    #Testataan alkusaldo > tilavuus
    def test_alkusaldo_isompi_kuin_tilavuus(self):
        varasto = Varasto(5, 10)
        self.assertAlmostEqual(varasto.saldo, 5.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    #Muokataa ylempi testataa maara < 0
    def test_lisays_vahenna_saldoa(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    #testataa 
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        ota = self.varasto.ota_varastosta(-8)
        self.assertAlmostEqual(ota, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 8.0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
<<<<<<< HEAD
    
    #testaa jos ottaa enemmän
    def test_ottaa_enemman_varaston_tyhjentaminen(self):
        self.varasto.lisaa_varastoon(5)
        ota = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(ota, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    #Testataan viel str palautus
    def test_str(self):
        self.varasto.lisaa_varastoon(3)
        self.assertAlmostEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")
=======
        
>>>>>>> 14b18fad86b42ac1de0bb4444f9b335bab086903
