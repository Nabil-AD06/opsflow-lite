from dataclasses import dataclass

NIVEAUX = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']


@dataclass
class Evenement:
    id: str
    date: str
    service: str
    gravite: str
    texte: str
    etat: str = 'RECU'   # RECU -> ANALYSE -> NOTIFIE


@dataclass
class Analyse:
    event_id: str
    niveau: str
    action: str
    critique: bool


@dataclass
class Notification:
    event_id: str
    canal: str
    destinataire: str
    contenu: str