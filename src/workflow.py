from src import analyse, extraction, notification


def traiter(ligne, numero, vus, erreurs, registre):
    evt = extraction.lire_ligne(ligne, numero)
    if analyse.est_doublon(evt, vus):
        return None
    if evt.gravite in ('HIGH', 'CRITICAL'):
        erreurs[evt.service] = erreurs.get(evt.service, 0) + 1
    nb = erreurs.get(evt.service, 0)
    ana = analyse.analyser(evt, nb)
    notif = notification.notifier(evt, ana, registre)
    return evt, ana, notif