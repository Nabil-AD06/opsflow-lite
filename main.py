import sys
from src.notification import approuver
from src.workflow import traiter

LOGS = [
    '2026-11-27 17:00:01 paiement INFO Service demarre',
    '2026-11-27 17:02:11 paiement ERROR timeout passerelle apres 30s card=4970123412341234',
    '2026-11-27 17:02:11 paiement ERROR timeout passerelle apres 30s card=4970123412341234',
    '2026-11-27 17:03:20 paiement ERROR timeout passerelle apres 31s',
    '2026-11-27 17:04:30 paiement ERROR timeout passerelle apres 29s',
    '2026-11-27 17:05:40 paiement ERROR timeout passerelle apres 33s',
]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    vus, erreurs, registre = set(), {}, []
    doublons = decisions = 0
    for numero, ligne in enumerate(LOGS, start=1):
        resultat = traiter(ligne, numero, vus, erreurs, registre)
        if resultat is None:
            doublons += 1
            print('>>> EVT-%04d ignore (doublon)' % numero)
            print()
            continue
        evt, ana, notif = resultat
        print('>>> %s par %s (%s)' % (notif.event_id, notif.canal, notif.destinataire))
        print(notif.contenu)
        if ana.critique:
            reponse = input('Action critique. Autoriser ? (o/n) : ')
            ok = approuver(ana, reponse)
            decisions += 1
            print('Decision :', 'AUTORISEE' if ok else 'REFUSEE', '(simulation)')
        print()
    print('%d evenements recus, %d doublon(s) ignore(s), %d notification(s), %d decision(s).'
          % (len(LOGS), doublons, len(registre), decisions))


if __name__ == '__main__':
    main()