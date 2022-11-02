import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_alku_saldo_ei_voi_olla_negatiivinen(self):
        varasto = Varasto(10, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_maara_ei_muuta_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(-10)

        # vapaa tila pysyy samana
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_ei_voi_olla_negatiivinen(self):
        varasto = Varasto(-100)

        self.assertAlmostEqual(varasto.tilavuus,0)

    def test_varastoon_ei_voi_lisata_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_voi_ottaa_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(5)

        alkumaara = self.varasto.saldo

        kaikki_mita_voidaan = self.varasto.ota_varastosta(100)

        self.assertAlmostEqual(kaikki_mita_voidaan, alkumaara)

    def test_negatiivisen_tavaramaaran_noutaminen_ei_onnistu(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_tilan_tulostus(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
