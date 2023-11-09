import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_oikean_saldon(self):
        self.assertEqual(self.maksukortti.saldo, 1000)        

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)

    def test_saldo_ei_muutu_kun_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_onnistunut_otto_palauttaa_true(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_epaonnistunut_otto_palauttaa_false(self):
        self.assertFalse(self.maksukortti.ota_rahaa(20000))

    def test_saldo_euroina_palauttaa_oikean_saldon(self):
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_merkkijonoesitys_palautetaan_oikein(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")
