import unittest
from src.contrat import Evenement, NIVEAUX


class TestContrat(unittest.TestCase):
    def test_etat_par_defaut(self):
        e = Evenement('EVT-0001', '2026-11-27T17:00:00Z', 'paiement', 'LOW', 'demarrage')
        self.assertEqual(e.etat, 'RECU')

    def test_niveaux_ordonnes(self):
        self.assertEqual(NIVEAUX[0], 'LOW')
        self.assertEqual(NIVEAUX[-1], 'CRITICAL')


if __name__ == '__main__':
    unittest.main()