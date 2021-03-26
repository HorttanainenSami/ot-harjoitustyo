import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.pieni_saldoinen_kortti = Maksukortti(200)
   
    def test_luodun_kassan_raha_maara_on_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_luodun_kassan_edullisten_maara_on_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_luodun_kassan_maukkkauden_maara_on_oikea(self):
        self.assertEqual(self.kassa.maukkaat, 0)
    ## Käteisellä
    #edulliset
    def test_edullisen_osto_liian_pienella_maaralla_kateista_ei_kasvata_edullisia(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_edullisen_osto_liian_pienella_maaralla_kateista_palauttaa_oikean_maaran(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)
          
    def test_edullisen_osto_liian_pienella_maaralla_kateista_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisen_osto_kateisella_palauttaa_oikean_maaran(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
 
    def test_edullisen_osto_kateisella_kasvattaa_kassan_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    #maukkaat
    def test_maukkaan_osto_liian_pienella_maaralla_kateista_ei_kasvata_maukkaita(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_maukkaan_osto_liian_pienella_maaralla_kateista_palauttaa_oikean_maaran(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(100), 100)

    def test_maukkaan_osto_liian_pienella_maaralla_kateista_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_osto_kateisella_palauttaa_oikean_maaran(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    
    def test_maukkaan_osto_kateisella_kasvattaa_kassan_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
## Kortilla
    #edulliset
    def test_edullisen_osto_liian_pienella_maaralla_saldoa_ei_kasvata_edullisia(self):
        self.kassa.syo_edullisesti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_edullisen_osto_liian_pienella_maaralla_saldoa_epaonnistuu(self):
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.pieni_saldoinen_kortti))
          
    def test_edullisen_osto_liian_pienella_maaralla_saldoa_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisen_osto_liian_pienella_maaralla_saldoa_ei_vahenna_saldoa(self):
        self.kassa.syo_edullisesti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(str(self.pieni_saldoinen_kortti), 'saldo: 2.0')

    def test_edullisen_osto_kortilla_onnistuu(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))
 
    def test_edullisen_osto_kortilla_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisen_osto_kortilla_kasvattaa_edulliseten_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

   #maukkaat
    def test_maukkaan_osto_liian_pienella_maaralla_saldoa_ei_kasvata_maukkaita(self):
        self.kassa.syo_maukkaasti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_maukkaan_osto_liian_pienella_maaralla_saldoa_epaonnistuu(self):
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.pieni_saldoinen_kortti))
          
    def test_maukkaan_osto_liian_pienella_maaralla_saldoa_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_osto_liian_pienella_maaralla_saldoa_ei_vahenna_saldoa(self):
        self.kassa.syo_maukkaasti_kortilla(self.pieni_saldoinen_kortti)
        self.assertEqual(str(self.pieni_saldoinen_kortti), 'saldo: 2.0')
        
    def test_maukkaan_osto_kortilla_onnistuu(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))
 
    def test_maukkaan_osto_kortilla_ei_kasvata_kassan_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_osto_kortilla_kasvattaa_maukkaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    ## kortille lataus
    def test_kortille_lataus_onnistuu(self):
        self.kassa.lataa_rahaa_kortille(self.pieni_saldoinen_kortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortin_saldo_kasvaa_ladattaessa(self):
        self.kassa.lataa_rahaa_kortille(self.pieni_saldoinen_kortti, 1000)
        self.assertEqual(self.pieni_saldoinen_kortti.saldo, 1200)

    def test_kortin_lataaminen_negatiivisella_ei_muuta_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.pieni_saldoinen_kortti, -100)
        self.assertEqual(self.pieni_saldoinen_kortti.saldo, 200)

    def test_kortin_lataaminen_ei_onnistu_nollalla(self):
        self.kassa.lataa_rahaa_kortille(self.pieni_saldoinen_kortti, -100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)