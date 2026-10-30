# src/notification.py
from src.contrat import Analyse, Evenement, Notification

def choisir_canal(niveau: str) -> str:
    raise NotImplementedError

# FOURNIE
def composer(evt: Evenement, ana: Analyse) -> str:
    return '*** %s *** Service : %s\nConstat : %s\nAction : %s' % (
        ana.niveau, evt.service, evt.texte, ana.action)

# FOURNIE
def notifier(evt: Evenement, ana: Analyse, registre: list) -> Notification:
    notif = Notification(evt.id, choisir_canal(ana.niveau), 'astreinte-ops',
                         composer(evt, ana))
    registre.append(notif)
    evt.etat = 'NOTIFIE'
    return notif

def approuver(ana: Analyse, reponse: str) -> bool:
    raise NotImplementedError