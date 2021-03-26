import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikea(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')

    def test_kortin_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.2')

    def test_rahan_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.08')

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')

    def test_kortilta_voi_ottaa_rahaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_kortilta_ei_voi_ottaa_liikaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(20))
