import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_pohjakassan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_alustaa_edullisten_myynnit_nollaksi(self):
        self.assertEqual(self.kassapaate.edulliset, 0)     

    def test_konstruktori_alustaa_maukkaiden_myynnit_nollaksi(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_negatiivinen_lataus_ei_muuta_kortin_saldoa(self):
        saldo_ennen_latausta = self.kortti.saldo
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, saldo_ennen_latausta)

    def test_negatiivinen_lataus_ei_muuta_kassaa(self):
        kassa_ennen_latausta = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassa_ennen_latausta)

    def test_onnistunut_korttilataus_kasvattaa_kortin_saldoa(self):
        saldo_ennen_latausta = self.kortti.saldo
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        saldo_latauksen_jalkeen = saldo_ennen_latausta + 1000
        self.assertEqual(self.kortti.saldo, saldo_latauksen_jalkeen)

    def test_onnistunut_korttilataus_kasvattaa_kassaa(self):
        saldo_ennen_latausta = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        saldo_latauksen_jalkeen = saldo_ennen_latausta + 1000
        self.assertEqual(self.kassapaate.kassassa_rahaa, saldo_latauksen_jalkeen)

# edullisten käteistestit
    def test_edullisen_kateismaksu_palautetaan_jos_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(150), 150)

    def test_edullisen_riittava_kateismaksu_kasvattaa_kassaa(self):
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(300)
        kassassa_pitaisi_olla = kassa_ennen_maksua + 240
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassassa_pitaisi_olla)

    def test_edullisen_riittava_kateismaksu_kasvattaa_myyntitilastoa(self):
        myydyt_ennen_maksua = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kateisella(300)
        myytyja_pitaisi_olla = myydyt_ennen_maksua + 1
        self.assertEqual(self.kassapaate.edulliset, myytyja_pitaisi_olla)

    def test_edullisen_riittava_kateismaksu_palauttaa_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

# edullisten korttitestit
    def test_edullisen_korttimaksu_hylataan_jos_ei_riittava(self):
        self.kortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

    def test_edullisen_riittava_korttimaksu_vahentaa_kortin_saldoa(self):
        kortin_saldo_ennen_maksua = self.kortti.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        kortin_saldo_pitaisi_olla = kortin_saldo_ennen_maksua - 240
        self.assertEqual(self.kortti.saldo, kortin_saldo_pitaisi_olla)

    def test_edullisen_riittava_korttimaksu_kasvattaa_myyntitilastoa(self):
        myydyt_ennen_maksua = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        myytyja_pitaisi_olla = myydyt_ennen_maksua + 1
        self.assertEqual(self.kassapaate.edulliset, myytyja_pitaisi_olla)

    def test_edullisen_riittava_korttimaksu_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

# maukkaiden käteistestit
    def test_maukkaan_kateismaksu_palautetaan_jos_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(150), 150)

    def test_maukkaan_riittava_kateismaksu_kasvattaa_kassaa(self):
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(500)
        kassassa_pitaisi_olla = kassa_ennen_maksua + 400
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassassa_pitaisi_olla)

    def test_maukkaan_riittava_kateismaksu_kasvattaa_myyntitilastoa(self):
        myydyt_ennen_maksua = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kateisella(500)
        myytyja_pitaisi_olla = myydyt_ennen_maksua + 1
        self.assertEqual(self.kassapaate.maukkaat, myytyja_pitaisi_olla)

    def test_maukkaan_riittava_kateismaksu_palauttaa_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)


# maukkaiden korttitestit
    def test_maukkaan_korttimaksu_hylataan_jos_ei_riittava(self):
        self.kortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_maukkaan_riittava_korttimaksu_vahentaa_kortin_saldoa(self):
        kortin_saldo_ennen_maksua = self.kortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        kortin_saldo_pitaisi_olla = kortin_saldo_ennen_maksua - 400
        self.assertEqual(self.kortti.saldo, kortin_saldo_pitaisi_olla)

    def test_maukkaan_riittava_korttimaksu_kasvattaa_myyntitilastoa(self):
        myydyt_ennen_maksua = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        myytyja_pitaisi_olla = myydyt_ennen_maksua + 1
        self.assertEqual(self.kassapaate.maukkaat, myytyja_pitaisi_olla)

    def test_maukkaan_riittava_korttimaksu_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))