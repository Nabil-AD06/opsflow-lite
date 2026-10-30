# src/analyse.py
from src.contrat import Analyse, Evenement

def est_doublon(evt: Evenement, vus: set) -> bool:
    raise NotImplementedError

def classer(evt: Evenement, nb_erreurs: int = 0) -> str:
    raise NotImplementedError

# FOURNIE
def analyser(evt: Evenement, nb_erreurs: int = 0) -> Analyse:
    niveau = classer(evt, nb_erreurs)
    action = 'Isoler ' + evt.service if niveau == 'CRITICAL' else 'Observer'
    evt.etat = 'ANALYSE'
    return Analyse(evt.id, niveau, action, action.startswith('Isoler'))