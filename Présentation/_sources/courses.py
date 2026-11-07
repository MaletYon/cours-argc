"""Métadonnées du cours ARGC (GES4062) et répartition des 30 séances de 2 heures (60 heures).

Un code de chapitre suivi de a ou b désigne la première ou la seconde moitié de
ses sections (chapitres traités en deux séances)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

ARGC = {
    "sigle": "ARGC",
    "code": "GES4062",
    "titre": "Analyse des Risques et Gestion de Crise",
    "sous_titre": "Analyser, auditer, continuer, décider : du registre des risques à la cellule de crise",
    "master": "Département de Génie Informatique · HN4",
    "bandeau": "Université de Yaoundé I",
    "ecole": "École Nationale Supérieure Polytechnique",
    "logo_g": "uy1",
    "logo_d": "enspy",
    "n_jours": 30,
    "annee": "2026-2027",
    "dossier": COURS + r"\GES4062\Présentation",
    "fil_rouge": "GAROUA, LIZBIZ, WOURI, MOUNGO",
    "parties": [
        ("Prologue", "Le matin du 6 mars", "P00"),
        ("Partie I", "Fondements du risque", "C01–C05"),
        ("Partie II", "Analyser les risques", "C06–C11"),
        ("Partie III", "Auditer le dispositif", "C12–C15"),
        ("Partie IV", "Incidents et continuité", "C16–C20"),
        ("Partie V", "Gestion de crise", "C21–C25"),
        ("Partie VI", "Apprendre et mesurer", "C26"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · Le matin du 6 mars", "Présentation + Prologue", ["P00"], []),
        2: ("Risque, incertitude et décision", "C01", ["C01"], []),
        3: ("Percevoir le risque : biais et culture", "C02", ["C02"], []),
        4: ("Gouvernance des risques", "C03", ["C03"], []),
        5: ("ISO 31000 et COSO ERM", "C04", ["C04"], []),
        6: ("Obligations juridiques et responsabilités", "C05", ["C05"], []),
        7: ("Identifier les risques", "C06", ["C06"], []),
        8: ("Échelles et matrices", "C07", ["C07"], ["LAB-01"]),
        9: ("EBIOS RM (1) : ISO/IEC 27005, socle, sources", "C08a", ["C08a"], []),
        10: ("EBIOS RM (2) : écosystème, scénarios, traitement", "C08b", ["C08b"], ["LAB-02"]),
        11: ("FAIR (1) : taxonomie et estimations", "C09a", ["C09a"], []),
        12: ("FAIR (2) : perte annuelle et options", "C09b", ["C09b"], ["LAB-03"]),
        13: ("Simuler : Monte-Carlo et sensibilité", "C10", ["C10"], ["LAB-04"]),
        14: ("Traiter, suivre, rendre compte", "C11", ["C11"], ["LAB-05"]),
        15: ("L'audit selon l'ISO 19011", "C12", ["C12"], []),
        16: ("Preuves, échantillons, constats", "C13", ["C13"], ["LAB-06"]),
        17: ("Auditer la gestion des risques et le SMSI", "C14", ["C14"], []),
        18: ("Le rapport et le suivi des actions", "C15", ["C15"], []),
        19: ("Gérer les incidents de sécurité", "C16", ["C16"], ["LAB-07"]),
        20: ("L'analyse d'impact sur l'activité", "C17", ["C17"], ["LAB-08"]),
        21: ("Stratégies et plans de continuité", "C18", ["C18"], []),
        22: ("Reprise informatique et résilience", "C19", ["C19"], []),
        23: ("Exercer et tester les plans", "C20", ["C20"], []),
        24: ("Qu'est-ce qu'une crise ?", "C21", ["C21"], []),
        25: ("La cellule de crise (1) : niveaux, rôles, main courante", "C22a", ["C22a"], []),
        26: ("La cellule de crise (2) : rythme, première heure, moyens", "C22b", ["C22b"], ["LAB-09"]),
        27: ("Décider en situation de crise", "C23", ["C23"], []),
        28: ("Communiquer en crise", "C24", ["C24"], ["LAB-10"]),
        29: ("Les exercices de crise", "C25", ["C25"], []),
        30: ("Retour d'expérience, résilience, mesure · clôture", "C26", ["C26"], []),
    },
}

ALL = {"ARGC": ARGC}
