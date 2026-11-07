# Analyse des Risques et Gestion de Crise (ARGC)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](ARGC_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE GES4062** · École Nationale Supérieure Polytechnique de l'Université de Yaoundé I · Département de Génie Informatique · HN4 · 60 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Le risque se gère avant, la crise pendant, et l'apprentissage après.*

Ce cours prolonge la sécurité informatique (SEC3266) et l'audit des systèmes d'information (INF3226). Il apprend à décider au sujet des risques, à vérifier que le dispositif tient, à assurer la continuité et à diriger l'organisation en crise. Il traite le risque comme une incertitude sur des pertes, que l'on estime avec sa marge (EBIOS Risk Manager, FAIR, Monte-Carlo), l'audit selon l'ISO 19011, la continuité selon l'ISO 22301 et la crise selon l'ISO 22361. Quatre opérations fictives servent de fil rouge : GAROUA (le rançongiciel de mars 2026 vu par la direction), LIZBIZ (le programme de gestion des risques et l'audit), WOURI (la continuité de la BANQUE SANAGA) et MOUNGO (l'inondation d'un entrepôt de Douala). Les noms, dates et montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`ARGC_main.pdf`](ARGC_main.pdf) | Traité complet (prologue, six parties, 26 chapitres, annexes), compilé depuis [`ARGC_main.tex`](ARGC_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 31 présentations PowerPoint : vision d'ensemble et 30 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 27 fiches de 40 questions au format texte, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_ARGC.sty`](Style_ARGC.sty) | Sources du livre |

## Organisation du cours (60 heures, 30 séances de 2 heures)

| Partie | Chapitres | Séances | Fichiers |
|---|---|---|---|
| **Prologue** | Le matin du 6 mars | J01 | [`partie0/`](partie0/) |
| **I. Fondements du risque** | 1. Risque, incertitude, décision · 2. Biais et culture · 3. Gouvernance · 4. ISO 31000 et COSO ERM · 5. Obligations juridiques | J02 – J06 | [`partie1/`](partie1/) |
| **II. Analyser les risques** | 6. Identifier · 7. Échelles et matrices · 8. ISO/IEC 27005 et EBIOS RM · 9. FAIR · 10. Monte-Carlo · 11. Traiter, suivre, rendre compte | J07 – J14 | [`partie2/`](partie2/) |
| **III. Auditer le dispositif** | 12. ISO 19011 · 13. Preuves, échantillons, constats · 14. Auditer les risques et le SMSI · 15. Rapport et suivi | J15 – J18 | [`partie3/`](partie3/) |
| **IV. Incidents et continuité** | 16. Incidents · 17. Analyse d'impact · 18. Plans de continuité · 19. Reprise et résilience · 20. Exercer et tester | J19 – J23 | [`partie4/`](partie4/) |
| **V. Gestion de crise** | 21. La crise · 22. La cellule de crise · 23. Décider · 24. Communiquer · 25. Exercices de crise | J24 – J29 | [`partie5/`](partie5/) |
| **VI. Apprendre et mesurer** | 26. Retour d'expérience, résilience, OUI / NON / NEK | J30 | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes juridiques et normatifs · E. Bibliographie commentée · F. Contacts | | [`annexes/`](annexes/) |

Les chapitres 8, 9 et 22 occupent chacun deux séances. Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 60 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, des labs sur pièces et un tableau de bord de progression. Le code de cours est **GES4062**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| ARGC-LAB-01 | 7 | Matrice et registre des risques |
| ARGC-LAB-02 | 8 | EBIOS RM : menace des parties prenantes |
| ARGC-LAB-03 | 9 | FAIR : estimer la perte annuelle |
| ARGC-LAB-04 | 10 | Monte-Carlo : lire une distribution de pertes |
| ARGC-LAB-05 | 11 | Indicateurs de risque et tableau de bord |
| ARGC-LAB-06 | 13 | Échantillonnage et constats d'audit |
| ARGC-LAB-07 | 16 | Registre des incidents : classer et mesurer |
| ARGC-LAB-08 | 17 | Analyse d'impact : RTO, RPO, dépendances |
| ARGC-LAB-09 | 22 | Main courante de la cellule de crise |
| ARGC-LAB-10 | 24 | Communication de crise et retour d'expérience |

## Compiler le livre

Avec une distribution LaTeX : `pdflatex ARGC_main`, `biber ARGC_main`, `makeindex ARGC_main`, puis deux fois `pdflatex ARGC_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py ARGC all` (Python 3 et python-pptx).

## Suite du parcours

Sécurité informatique ([UE SEC3266](https://github.com/maletyon/cours-sif)), audit des systèmes d'information ([UE INF3226](https://github.com/maletyon/cours-asi)), investigation numérique ([UE SEC4031](https://github.com/maletyon/cours-iin) et [SEC4052](https://github.com/maletyon/cours-ina)), hacking éthique ([UE SEC4062](https://github.com/maletyon/cours-he2)).

## Normes et documents sous licence

Les normes ISO, ISO/IEC et IEC et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
