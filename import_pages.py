import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Page

# Discipline : Mobiliser le langage dans toutes ses dimensions
domaineDiscipline1, created = Page.objects.get_or_create(
    slug="mobiliser-le-langage-dans-toutes-ses-dimensions",
    defaults={
        'title': "Mobiliser le langage dans toutes ses dimensions",
        'content': "<p>Contenu par d\u00e9faut pour la discipline Mobiliser le langage dans toutes ses dimensions</p>",
        'published': True,
    }
)

# Discipline : Agir, s'exprimer, comprendre à travers l'activité physique
domaineDiscipline2, created = Page.objects.get_or_create(
    slug="agir-sexprimer-comprendre-\u00e0-travers-lactivit\u00e9-physique",
    defaults={
        'title': "Agir, s'exprimer, comprendre \u00e0 travers l'activit\u00e9 physique",
        'content': "<p>Contenu par d\u00e9faut pour la discipline Agir, s'exprimer, comprendre \u00e0 travers l'activit\u00e9 physique</p>",
        'published': True,
    }
)

# Discipline : Agir, s'exprimer, comprendre à travers les activités artistiques
domaineDiscipline3, created = Page.objects.get_or_create(
    slug="agir-sexprimer-comprendre-\u00e0-travers-les-activit\u00e9s-artistiques",
    defaults={
        'title': "Agir, s'exprimer, comprendre \u00e0 travers les activit\u00e9s artistiques",
        'content': "<p>Contenu par d\u00e9faut pour la discipline Agir, s'exprimer, comprendre \u00e0 travers les activit\u00e9s artistiques</p>",
        'published': True,
    }
)

# Discipline : Acquisition des premiers outils mathématiques
domaineDiscipline4, created = Page.objects.get_or_create(
    slug="acquisition-des-premiers-outils-math\u00e9matiques",
    defaults={
        'title': "Acquisition des premiers outils math\u00e9matiques",
        'content': "<p>Contenu par d\u00e9faut pour la discipline Acquisition des premiers outils math\u00e9matiques</p>",
        'published': True,
    }
)

# Discipline : Explorer le monde
domaineDiscipline5, created = Page.objects.get_or_create(
    slug="explorer-le-monde",
    defaults={
        'title': "Explorer le monde",
        'content': "<p>Contenu par d\u00e9faut pour la discipline Explorer le monde</p>",
        'published': True,
    }
)

# Compétence : PS-Comprendre, mémoriser, réemployer les mots des corpus enseignés (2 par période)
competence1, created = Page.objects.get_or_create(
    slug="ps-comprendre-m\u00e9moriser-r\u00e9employer-les-mots-des-corpus-enseign\u00e9s-2-par-p\u00e9riode",
    defaults={
        'title': "PS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (2 par p\u00e9riode)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (2 par p\u00e9riode)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : PS-Organiser les mots en catégorie et en réseau
competence2, created = Page.objects.get_or_create(
    slug="ps-organiser-les-mots-en-cat\u00e9gorie-et-en-r\u00e9seau",
    defaults={
        'title': "PS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : MS-Comprendre, mémoriser, réemployer les mots des corpus enseignés (2 par période)
competence3, created = Page.objects.get_or_create(
    slug="ms-comprendre-m\u00e9moriser-r\u00e9employer-les-mots-des-corpus-enseign\u00e9s-2-par-p\u00e9riode",
    defaults={
        'title': "MS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (2 par p\u00e9riode)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (2 par p\u00e9riode)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : MS-Organiser les mots en catégorie et en réseau
competence4, created = Page.objects.get_or_create(
    slug="ms-organiser-les-mots-en-cat\u00e9gorie-et-en-r\u00e9seau",
    defaults={
        'title': "MS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : GS-Comprendre, mémoriser, réemployer les mots des corpus enseignés (3 par période)
competence5, created = Page.objects.get_or_create(
    slug="gs-comprendre-m\u00e9moriser-r\u00e9employer-les-mots-des-corpus-enseign\u00e9s-3-par-p\u00e9riode",
    defaults={
        'title': "GS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (3 par p\u00e9riode)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Comprendre, m\u00e9moriser, r\u00e9employer les mots des corpus enseign\u00e9s (3 par p\u00e9riode)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : GS-Organiser les mots en catégorie et en réseau
competence6, created = Page.objects.get_or_create(
    slug="gs-organiser-les-mots-en-cat\u00e9gorie-et-en-r\u00e9seau",
    defaults={
        'title': "GS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Organiser les mots en cat\u00e9gorie et en r\u00e9seau</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Enrichir son vocabulaire",
    }
)

# Compétence : PS-Diversifier les pronoms employés
competence7, created = Page.objects.get_or_create(
    slug="ps-diversifier-les-pronoms-employ\u00e9s",
    defaults={
        'title': "PS-Diversifier les pronoms employ\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Diversifier les pronoms employ\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : PS-Construire à l'oral un système de temps de plus en plus efficace
competence8, created = Page.objects.get_or_create(
    slug="ps-construire-\u00e0-loral-un-syst\u00e8me-de-temps-de-plus-en-plus-efficace",
    defaults={
        'title': "PS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : PS-Formuler des énoncés de plus en plus complexes
competence9, created = Page.objects.get_or_create(
    slug="ps-formuler-des-\u00e9nonc\u00e9s-de-plus-en-plus-complexes",
    defaults={
        'title': "PS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : MS-Diversifier les pronoms employés
competence10, created = Page.objects.get_or_create(
    slug="ms-diversifier-les-pronoms-employ\u00e9s",
    defaults={
        'title': "MS-Diversifier les pronoms employ\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Diversifier les pronoms employ\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : MS-Construire à l'oral un système de temps de plus en plus efficace
competence11, created = Page.objects.get_or_create(
    slug="ms-construire-\u00e0-loral-un-syst\u00e8me-de-temps-de-plus-en-plus-efficace",
    defaults={
        'title': "MS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : MS-Formuler des énoncés de plus en plus complexes
competence12, created = Page.objects.get_or_create(
    slug="ms-formuler-des-\u00e9nonc\u00e9s-de-plus-en-plus-complexes",
    defaults={
        'title': "MS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : GS-Construire à l'oral un système de temps de plus en plus efficace
competence13, created = Page.objects.get_or_create(
    slug="gs-construire-\u00e0-loral-un-syst\u00e8me-de-temps-de-plus-en-plus-efficace",
    defaults={
        'title': "GS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Construire \u00e0 l'oral un syst\u00e8me de temps de plus en plus efficace</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : GS-Formuler des énoncés de plus en plus complexes 
competence14, created = Page.objects.get_or_create(
    slug="gs-formuler-des-\u00e9nonc\u00e9s-de-plus-en-plus-complexes-",
    defaults={
        'title': "GS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes ",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Formuler des \u00e9nonc\u00e9s de plus en plus complexes </p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : GS-Diversifier les pronoms employés
competence15, created = Page.objects.get_or_create(
    slug="gs-diversifier-les-pronoms-employ\u00e9s",
    defaults={
        'title': "GS-Diversifier les pronoms employ\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Diversifier les pronoms employ\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "D\u00e9velopper sa syntaxe",
    }
)

# Compétence : PS-Articuler distinctement les couples de consonnes proches suivants : t/k, f/s, m/n
competence16, created = Page.objects.get_or_create(
    slug="ps-articuler-distinctement-les-couples-de-consonnes-proches-suivants-:-t/k-f/s-m/n",
    defaults={
        'title': "PS-Articuler distinctement les couples de consonnes proches suivants : t/k, f/s, m/n",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Articuler distinctement les couples de consonnes proches suivants : t/k, f/s, m/n</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Articuler distinctement",
    }
)

# Compétence : MS-Distinguer et produire correctement les nasales: é/in, a/an, o/on
competence17, created = Page.objects.get_or_create(
    slug="ms-distinguer-et-produire-correctement-les-nasales:-\u00e9/in-a/an-o/on",
    defaults={
        'title': "MS-Distinguer et produire correctement les nasales: \u00e9/in, a/an, o/on",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Distinguer et produire correctement les nasales: \u00e9/in, a/an, o/on</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Articuler distinctement",
    }
)

# Compétence : MS-Articuler distinctement les couples de consonnes proches suivants : f/v, s/z, p/b, t/d, k/g
competence18, created = Page.objects.get_or_create(
    slug="ms-articuler-distinctement-les-couples-de-consonnes-proches-suivants-:-f/v-s/z-p/b-t/d-k/g",
    defaults={
        'title': "MS-Articuler distinctement les couples de consonnes proches suivants : f/v, s/z, p/b, t/d, k/g",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Articuler distinctement les couples de consonnes proches suivants : f/v, s/z, p/b, t/d, k/g</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Articuler distinctement",
    }
)

# Compétence : GS-Prononcer correctement les couples de consonnes proches suivants: ch/s, ch/j, ch/z
competence19, created = Page.objects.get_or_create(
    slug="gs-prononcer-correctement-les-couples-de-consonnes-proches-suivants:-ch/s-ch/j-ch/z",
    defaults={
        'title': "GS-Prononcer correctement les couples de consonnes proches suivants: ch/s, ch/j, ch/z",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Prononcer correctement les couples de consonnes proches suivants: ch/s, ch/j, ch/z</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Articuler distinctement",
    }
)

# Compétence : GS-Prononcer correctement les doubles consonnes: br/cr/bl/pl/sl
competence20, created = Page.objects.get_or_create(
    slug="gs-prononcer-correctement-les-doubles-consonnes:-br/cr/bl/pl/sl",
    defaults={
        'title': "GS-Prononcer correctement les doubles consonnes: br/cr/bl/pl/sl",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Prononcer correctement les doubles consonnes: br/cr/bl/pl/sl</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Articuler distinctement",
    }
)

# Compétence : PS-Entrer en communication verbale avec un adulte ou un autre élève
competence21, created = Page.objects.get_or_create(
    slug="ps-entrer-en-communication-verbale-avec-un-adulte-ou-un-autre-\u00e9l\u00e8ve",
    defaults={
        'title': "PS-Entrer en communication verbale avec un adulte ou un autre \u00e9l\u00e8ve",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Entrer en communication verbale avec un adulte ou un autre \u00e9l\u00e8ve</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : PS-Dire ce qu'on fait
competence22, created = Page.objects.get_or_create(
    slug="ps-dire-ce-quon-fait",
    defaults={
        'title': "PS-Dire ce qu'on fait",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Dire ce qu'on fait</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : PS-Dire ce qu'on a fait et, peu à peu, ce qu'on va faire
competence23, created = Page.objects.get_or_create(
    slug="ps-dire-ce-quon-a-fait-et-peu-\u00e0-peu-ce-quon-va-faire",
    defaults={
        'title': "PS-Dire ce qu'on a fait et, peu \u00e0 peu, ce qu'on va faire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Dire ce qu'on a fait et, peu \u00e0 peu, ce qu'on va faire</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : PS-Prendre part à l'oralisation d'un court texte mémorisé
competence24, created = Page.objects.get_or_create(
    slug="ps-prendre-part-\u00e0-loralisation-dun-court-texte-m\u00e9moris\u00e9",
    defaults={
        'title': "PS-Prendre part \u00e0 l'oralisation d'un court texte m\u00e9moris\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS-Prendre part \u00e0 l'oralisation d'un court texte m\u00e9moris\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : MS-Dire ce qu'on va faire
competence25, created = Page.objects.get_or_create(
    slug="ms-dire-ce-quon-va-faire",
    defaults={
        'title': "MS-Dire ce qu'on va faire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Dire ce qu'on va faire</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : MS-Dire comment on a fait ou comment on va faire
competence26, created = Page.objects.get_or_create(
    slug="ms-dire-comment-on-a-fait-ou-comment-on-va-faire",
    defaults={
        'title': "MS-Dire comment on a fait ou comment on va faire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Dire comment on a fait ou comment on va faire</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : MS-Dire comment on a fait ou comment on va faire
competence27, created = Page.objects.get_or_create(
    slug="ms-dire-comment-on-a-fait-ou-comment-on-va-faire-1",
    defaults={
        'title': "MS-Dire comment on a fait ou comment on va faire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Dire comment on a fait ou comment on va faire</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : MS-Oraliser un court texte mémorisé
competence28, created = Page.objects.get_or_create(
    slug="ms-oraliser-un-court-texte-m\u00e9moris\u00e9",
    defaults={
        'title': "MS-Oraliser un court texte m\u00e9moris\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Oraliser un court texte m\u00e9moris\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : MS-Participer à des échanges en restant dans le propos
competence29, created = Page.objects.get_or_create(
    slug="ms-participer-\u00e0-des-\u00e9changes-en-restant-dans-le-propos",
    defaults={
        'title': "MS-Participer \u00e0 des \u00e9changes en restant dans le propos",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS-Participer \u00e0 des \u00e9changes en restant dans le propos</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : GS-Décrire une action ou une activité qui a été menée par un autre élève
competence30, created = Page.objects.get_or_create(
    slug="gs-d\u00e9crire-une-action-ou-une-activit\u00e9-qui-a-\u00e9t\u00e9-men\u00e9e-par-un-autre-\u00e9l\u00e8ve",
    defaults={
        'title': "GS-D\u00e9crire une action ou une activit\u00e9 qui a \u00e9t\u00e9 men\u00e9e par un autre \u00e9l\u00e8ve",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-D\u00e9crire une action ou une activit\u00e9 qui a \u00e9t\u00e9 men\u00e9e par un autre \u00e9l\u00e8ve</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : GS-Se faire comprendre, par le truchement du langage, d'un adulte qui ne connait rien à la situation évoquée
competence31, created = Page.objects.get_or_create(
    slug="gs-se-faire-comprendre-par-le-truchement-du-langage-dun-adulte-qui-ne-connait-rien-\u00e0-la-situation-\u00e9voqu\u00e9e",
    defaults={
        'title': "GS-Se faire comprendre, par le truchement du langage, d'un adulte qui ne connait rien \u00e0 la situation \u00e9voqu\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Se faire comprendre, par le truchement du langage, d'un adulte qui ne connait rien \u00e0 la situation \u00e9voqu\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : GS-Participer à une conversation avec un adulte ou des pairs et reformuler son propos s'il n'a pas été compris
competence32, created = Page.objects.get_or_create(
    slug="gs-participer-\u00e0-une-conversation-avec-un-adulte-ou-des-pairs-et-reformuler-son-propos-sil-na-pas-\u00e9t\u00e9-compris",
    defaults={
        'title': "GS-Participer \u00e0 une conversation avec un adulte ou des pairs et reformuler son propos s'il n'a pas \u00e9t\u00e9 compris",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-Participer \u00e0 une conversation avec un adulte ou des pairs et reformuler son propos s'il n'a pas \u00e9t\u00e9 compris</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : GS-Émettre une hypothèse
competence33, created = Page.objects.get_or_create(
    slug="gs-\u00e9mettre-une-hypoth\u00e8se",
    defaults={
        'title': "GS-\u00c9mettre une hypoth\u00e8se",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS-\u00c9mettre une hypoth\u00e8se</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Acqu\u00e9rir le langage oral",
        'competence_generale': "Produire des discours vari\u00e9s",
    }
)

# Compétence : PS Identifier les sons de la langue, lors de situations d'écoute proposées par le professeur
competence34, created = Page.objects.get_or_create(
    slug="ps-identifier-les-sons-de-la-langue-lors-de-situations-d\u00e9coute-propos\u00e9es-par-le-professeur",
    defaults={
        'title': "PS Identifier les sons de la langue, lors de situations d'\u00e9coute propos\u00e9es par le professeur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Identifier les sons de la langue, lors de situations d'\u00e9coute propos\u00e9es par le professeur</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : PS Identifier un mot donné à l'oral dans une phrase, dans un texte
competence35, created = Page.objects.get_or_create(
    slug="ps-identifier-un-mot-donn\u00e9-\u00e0-loral-dans-une-phrase-dans-un-texte",
    defaults={
        'title': "PS Identifier un mot donn\u00e9 \u00e0 l'oral dans une phrase, dans un texte",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Identifier un mot donn\u00e9 \u00e0 l'oral dans une phrase, dans un texte</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : PS Scander les syllabes d'un mot
competence36, created = Page.objects.get_or_create(
    slug="ps-scander-les-syllabes-dun-mot",
    defaults={
        'title': "PS Scander les syllabes d'un mot",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Scander les syllabes d'un mot</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : PS Dire des comptines courtes comprenant des phonèmes proches
competence37, created = Page.objects.get_or_create(
    slug="ps-dire-des-comptines-courtes-comprenant-des-phon\u00e8mes-proches",
    defaults={
        'title': "PS Dire des comptines courtes comprenant des phon\u00e8mes proches",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Dire des comptines courtes comprenant des phon\u00e8mes proches</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : PS Reconnaitre et nommer certaines lettres de son prénom écrit en capitales
competence38, created = Page.objects.get_or_create(
    slug="ps-reconnaitre-et-nommer-certaines-lettres-de-son-pr\u00e9nom-\u00e9crit-en-capitales",
    defaults={
        'title': "PS Reconnaitre et nommer certaines lettres de son pr\u00e9nom \u00e9crit en capitales",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reconnaitre et nommer certaines lettres de son pr\u00e9nom \u00e9crit en capitales</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Donner les valeurs sonores de quelques lettres de mots simples connus
competence39, created = Page.objects.get_or_create(
    slug="ms-donner-les-valeurs-sonores-de-quelques-lettres-de-mots-simples-connus",
    defaults={
        'title': "MS Donner les valeurs sonores de quelques lettres de mots simples connus",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Donner les valeurs sonores de quelques lettres de mots simples connus</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Connaitre la correspondance entre les lettres scriptes majuscules et minuscules et les lettres cursives minuscules
competence40, created = Page.objects.get_or_create(
    slug="ms-connaitre-la-correspondance-entre-les-lettres-scriptes-majuscules-et-minuscules-et-les-lettres-cursives-minuscules",
    defaults={
        'title': "MS Connaitre la correspondance entre les lettres scriptes majuscules et minuscules et les lettres cursives minuscules",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Connaitre la correspondance entre les lettres scriptes majuscules et minuscules et les lettres cursives minuscules</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Nommer les lettres de son prénom et quelques lettres de mots connus
competence41, created = Page.objects.get_or_create(
    slug="ms-nommer-les-lettres-de-son-pr\u00e9nom-et-quelques-lettres-de-mots-connus",
    defaults={
        'title': "MS Nommer les lettres de son pr\u00e9nom et quelques lettres de mots connus",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Nommer les lettres de son pr\u00e9nom et quelques lettres de mots connus</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence :  MS Dire des comptines courtes comprenant des phonèmes proches
competence42, created = Page.objects.get_or_create(
    slug="-ms-dire-des-comptines-courtes-comprenant-des-phon\u00e8mes-proches",
    defaults={
        'title': " MS Dire des comptines courtes comprenant des phon\u00e8mes proches",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence  MS Dire des comptines courtes comprenant des phon\u00e8mes proches</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Manipuler les syllabes d'un mot (ajout, suppression, permutation, répétition, fusion, substitution)
competence43, created = Page.objects.get_or_create(
    slug="ms-manipuler-les-syllabes-dun-mot-ajout-suppression-permutation-r\u00e9p\u00e9tition-fusion-substitution",
    defaults={
        'title': "MS Manipuler les syllabes d'un mot (ajout, suppression, permutation, r\u00e9p\u00e9tition, fusion, substitution)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Manipuler les syllabes d'un mot (ajout, suppression, permutation, r\u00e9p\u00e9tition, fusion, substitution)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Scander les syllabes d'un mot
competence44, created = Page.objects.get_or_create(
    slug="ms-scander-les-syllabes-dun-mot",
    defaults={
        'title': "MS Scander les syllabes d'un mot",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Scander les syllabes d'un mot</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Entendre, discriminer des phonèmes
competence45, created = Page.objects.get_or_create(
    slug="ms-entendre-discriminer-des-phon\u00e8mes",
    defaults={
        'title': "MS Entendre, discriminer des phon\u00e8mes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Entendre, discriminer des phon\u00e8mes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : MS Utiliser la voix parlée, chantée et les possibilités vocales (imitation de sons, onomatopées) afin d'expérimenter différents sons
competence46, created = Page.objects.get_or_create(
    slug="ms-utiliser-la-voix-parl\u00e9e-chant\u00e9e-et-les-possibilit\u00e9s-vocales-imitation-de-sons-onomatop\u00e9es-afin-dexp\u00e9rimenter-diff\u00e9rents-sons",
    defaults={
        'title': "MS Utiliser la voix parl\u00e9e, chant\u00e9e et les possibilit\u00e9s vocales (imitation de sons, onomatop\u00e9es) afin d'exp\u00e9rimenter diff\u00e9rents sons",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Utiliser la voix parl\u00e9e, chant\u00e9e et les possibilit\u00e9s vocales (imitation de sons, onomatop\u00e9es) afin d'exp\u00e9rimenter diff\u00e9rents sons</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Discriminer des mots auditivement proches
competence47, created = Page.objects.get_or_create(
    slug="gs-discriminer-des-mots-auditivement-proches",
    defaults={
        'title': "GS Discriminer des mots auditivement proches",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Discriminer des mots auditivement proches</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Connaitre le nom des lettres de l'alphabet et leur valeur sonore hormis les occlusives
competence48, created = Page.objects.get_or_create(
    slug="gs-connaitre-le-nom-des-lettres-de-lalphabet-et-leur-valeur-sonore-hormis-les-occlusives",
    defaults={
        'title': "GS Connaitre le nom des lettres de l'alphabet et leur valeur sonore hormis les occlusives",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Connaitre le nom des lettres de l'alphabet et leur valeur sonore hormis les occlusives</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Distinguer des lettres visuellement proches (b/d, c/e/o, p/q) grâce à leur écriture cursive et les nommer correctement
competence49, created = Page.objects.get_or_create(
    slug="gs-distinguer-des-lettres-visuellement-proches-b/d-c/e/o-p/q-gr\u00e2ce-\u00e0-leur-\u00e9criture-cursive-et-les-nommer-correctement",
    defaults={
        'title': "GS Distinguer des lettres visuellement proches (b/d, c/e/o, p/q) gr\u00e2ce \u00e0 leur \u00e9criture cursive et les nommer correctement",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Distinguer des lettres visuellement proches (b/d, c/e/o, p/q) gr\u00e2ce \u00e0 leur \u00e9criture cursive et les nommer correctement</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Connaitre les différentes graphies d'une même lettre (majuscule lettre capitale; minuscules scriptes; cursives)
competence50, created = Page.objects.get_or_create(
    slug="gs-connaitre-les-diff\u00e9rentes-graphies-dune-m\u00eame-lettre-majuscule-lettre-capitale;-minuscules-scriptes;-cursives",
    defaults={
        'title': "GS Connaitre les diff\u00e9rentes graphies d'une m\u00eame lettre (majuscule lettre capitale; minuscules scriptes; cursives)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Connaitre les diff\u00e9rentes graphies d'une m\u00eame lettre (majuscule lettre capitale; minuscules scriptes; cursives)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence :  GS Connaitre le nom des lettres de l'alphabet
competence51, created = Page.objects.get_or_create(
    slug="-gs-connaitre-le-nom-des-lettres-de-lalphabet",
    defaults={
        'title': " GS Connaitre le nom des lettres de l'alphabet",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence  GS Connaitre le nom des lettres de l'alphabet</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Entendre, discriminer, manipuler des phonèmes
competence52, created = Page.objects.get_or_create(
    slug="gs-entendre-discriminer-manipuler-des-phon\u00e8mes",
    defaults={
        'title': "GS Entendre, discriminer, manipuler des phon\u00e8mes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Entendre, discriminer, manipuler des phon\u00e8mes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Repérer et produire des rimes et des assonances
competence53, created = Page.objects.get_or_create(
    slug="gs-rep\u00e9rer-et-produire-des-rimes-et-des-assonances",
    defaults={
        'title': "GS Rep\u00e9rer et produire des rimes et des assonances",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Rep\u00e9rer et produire des rimes et des assonances</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Supprimer, ajouter, remplacer, inverser, substituer, fusionner les syllabes d'un mot
competence54, created = Page.objects.get_or_create(
    slug="gs-supprimer-ajouter-remplacer-inverser-substituer-fusionner-les-syllabes-dun-mot",
    defaults={
        'title': "GS Supprimer, ajouter, remplacer, inverser, substituer, fusionner les syllabes d'un mot",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Supprimer, ajouter, remplacer, inverser, substituer, fusionner les syllabes d'un mot</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Augmenter sa mémoire auditive et sa capacité de concentration
competence55, created = Page.objects.get_or_create(
    slug="gs-augmenter-sa-m\u00e9moire-auditive-et-sa-capacit\u00e9-de-concentration",
    defaults={
        'title': "GS Augmenter sa m\u00e9moire auditive et sa capacit\u00e9 de concentration",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Augmenter sa m\u00e9moire auditive et sa capacit\u00e9 de concentration</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : GS Utiliser les possibilités sonores de la voix
competence56, created = Page.objects.get_or_create(
    slug="gs-utiliser-les-possibilit\u00e9s-sonores-de-la-voix",
    defaults={
        'title': "GS Utiliser les possibilit\u00e9s sonores de la voix",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Utiliser les possibilit\u00e9s sonores de la voix</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "Acqu\u00e9rir les habilet\u00e9s phonologiques et le principe alphab\u00e9tique",
    }
)

# Compétence : PS Écouter des chants, des comptines, des histoires connues dans des versions en français et en langue étrangère
competence57, created = Page.objects.get_or_create(
    slug="ps-\u00e9couter-des-chants-des-comptines-des-histoires-connues-dans-des-versions-en-fran\u00e7ais-et-en-langue-\u00e9trang\u00e8re",
    defaults={
        'title': "PS \u00c9couter des chants, des comptines, des histoires connues dans des versions en fran\u00e7ais et en langue \u00e9trang\u00e8re",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS \u00c9couter des chants, des comptines, des histoires connues dans des versions en fran\u00e7ais et en langue \u00e9trang\u00e8re</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "S'\u00e9veiller \u00e0 la diversit\u00e9 linguistique",
    }
)

# Compétence : MS Participer à des jeux dans une autre langue : jeux de doigts, rondes, jeux dansés, mimes, jeux de cour, jeux de cartes
competence58, created = Page.objects.get_or_create(
    slug="ms-participer-\u00e0-des-jeux-dans-une-autre-langue-:-jeux-de-doigts-rondes-jeux-dans\u00e9s-mimes-jeux-de-cour-jeux-de-cartes",
    defaults={
        'title': "MS Participer \u00e0 des jeux dans une autre langue : jeux de doigts, rondes, jeux dans\u00e9s, mimes, jeux de cour, jeux de cartes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Participer \u00e0 des jeux dans une autre langue : jeux de doigts, rondes, jeux dans\u00e9s, mimes, jeux de cour, jeux de cartes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "S'\u00e9veiller \u00e0 la diversit\u00e9 linguistique",
    }
)

# Compétence : MS Comparer des histoires lues en français et dans une autre langue
competence59, created = Page.objects.get_or_create(
    slug="ms-comparer-des-histoires-lues-en-fran\u00e7ais-et-dans-une-autre-langue",
    defaults={
        'title': "MS Comparer des histoires lues en fran\u00e7ais et dans une autre langue",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comparer des histoires lues en fran\u00e7ais et dans une autre langue</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "S'\u00e9veiller \u00e0 la diversit\u00e9 linguistique",
    }
)

# Compétence : PS Repérer les outils fonctionnels utilisés quotidiennement en classe (étiquette du prénom, emploi du temps, affiches, etc.)
competence60, created = Page.objects.get_or_create(
    slug="ps-rep\u00e9rer-les-outils-fonctionnels-utilis\u00e9s-quotidiennement-en-classe-\u00e9tiquette-du-pr\u00e9nom-emploi-du-temps-affiches-etc.",
    defaults={
        'title': "PS Rep\u00e9rer les outils fonctionnels utilis\u00e9s quotidiennement en classe (\u00e9tiquette du pr\u00e9nom, emploi du temps, affiches, etc.)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Rep\u00e9rer les outils fonctionnels utilis\u00e9s quotidiennement en classe (\u00e9tiquette du pr\u00e9nom, emploi du temps, affiches, etc.)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : PS Reconnaitre quelques écrits utilisés et produits en classe (comptines, recettes, carnet de lecteur)
competence61, created = Page.objects.get_or_create(
    slug="ps-reconnaitre-quelques-\u00e9crits-utilis\u00e9s-et-produits-en-classe-comptines-recettes-carnet-de-lecteur",
    defaults={
        'title': "PS Reconnaitre quelques \u00e9crits utilis\u00e9s et produits en classe (comptines, recettes, carnet de lecteur)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reconnaitre quelques \u00e9crits utilis\u00e9s et produits en classe (comptines, recettes, carnet de lecteur)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : PS Reconnaitre un personnage, le nommer et le situer dans les illustrations
competence62, created = Page.objects.get_or_create(
    slug="ps-reconnaitre-un-personnage-le-nommer-et-le-situer-dans-les-illustrations",
    defaults={
        'title': "PS Reconnaitre un personnage, le nommer et le situer dans les illustrations",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reconnaitre un personnage, le nommer et le situer dans les illustrations</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : PS Comprendre des histoires où l'enchainement des actions peut être rattaché à des expériences connues de la vie quotidienne (le bain, le coucher, etc.)
competence63, created = Page.objects.get_or_create(
    slug="ps-comprendre-des-histoires-o\u00f9-lenchainement-des-actions-peut-\u00eatre-rattach\u00e9-\u00e0-des-exp\u00e9riences-connues-de-la-vie-quotidienne-le-bain-le-coucher-etc.",
    defaults={
        'title': "PS Comprendre des histoires o\u00f9 l'enchainement des actions peut \u00eatre rattach\u00e9 \u00e0 des exp\u00e9riences connues de la vie quotidienne (le bain, le coucher, etc.)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comprendre des histoires o\u00f9 l'enchainement des actions peut \u00eatre rattach\u00e9 \u00e0 des exp\u00e9riences connues de la vie quotidienne (le bain, le coucher, etc.)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : MS Reconnaitre, nommer et identifier la fonction de différents écrits rencontrés dans la vie courante
competence64, created = Page.objects.get_or_create(
    slug="ms-reconnaitre-nommer-et-identifier-la-fonction-de-diff\u00e9rents-\u00e9crits-rencontr\u00e9s-dans-la-vie-courante",
    defaults={
        'title': "MS Reconnaitre, nommer et identifier la fonction de diff\u00e9rents \u00e9crits rencontr\u00e9s dans la vie courante",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Reconnaitre, nommer et identifier la fonction de diff\u00e9rents \u00e9crits rencontr\u00e9s dans la vie courante</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : MS Prendre conscience de la notion de destinataire et de contenu de la requête adressée par un écrit
competence65, created = Page.objects.get_or_create(
    slug="ms-prendre-conscience-de-la-notion-de-destinataire-et-de-contenu-de-la-requ\u00eate-adress\u00e9e-par-un-\u00e9crit",
    defaults={
        'title': "MS Prendre conscience de la notion de destinataire et de contenu de la requ\u00eate adress\u00e9e par un \u00e9crit",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Prendre conscience de la notion de destinataire et de contenu de la requ\u00eate adress\u00e9e par un \u00e9crit</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : MS Identifier et utiliser quotidiennement des outils fonctionnels pour se repérer, s'organiser, ranger
competence66, created = Page.objects.get_or_create(
    slug="ms-identifier-et-utiliser-quotidiennement-des-outils-fonctionnels-pour-se-rep\u00e9rer-sorganiser-ranger",
    defaults={
        'title': "MS Identifier et utiliser quotidiennement des outils fonctionnels pour se rep\u00e9rer, s'organiser, ranger",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Identifier et utiliser quotidiennement des outils fonctionnels pour se rep\u00e9rer, s'organiser, ranger</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : MS Identifier et décrire le personnage principal et les personnages secondaires
competence67, created = Page.objects.get_or_create(
    slug="ms-identifier-et-d\u00e9crire-le-personnage-principal-et-les-personnages-secondaires",
    defaults={
        'title': "MS Identifier et d\u00e9crire le personnage principal et les personnages secondaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Identifier et d\u00e9crire le personnage principal et les personnages secondaires</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : MS Comprendre des histoires dont les actions sont organisées autour d'une structure répétitive (rencontres successives) et commencer à comprendre les informations implicites (émotions, états et sentiments des personnages)
competence68, created = Page.objects.get_or_create(
    slug="ms-comprendre-des-histoires-dont-les-actions-sont-organis\u00e9es-autour-dune-structure-r\u00e9p\u00e9titive-rencontres-successives-et-commencer-\u00e0-comprendre-les-informations-implicites-\u00e9motions-\u00e9tats-et-sentiments-des-personnages",
    defaults={
        'title': "MS Comprendre des histoires dont les actions sont organis\u00e9es autour d'une structure r\u00e9p\u00e9titive (rencontres successives) et commencer \u00e0 comprendre les informations implicites (\u00e9motions, \u00e9tats et sentiments des personnages)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comprendre des histoires dont les actions sont organis\u00e9es autour d'une structure r\u00e9p\u00e9titive (rencontres successives) et commencer \u00e0 comprendre les informations implicites (\u00e9motions, \u00e9tats et sentiments des personnages)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Différencier les types d'écrits et associer un écrit à un projet d'écriture ou de communication
competence69, created = Page.objects.get_or_create(
    slug="gs-diff\u00e9rencier-les-types-d\u00e9crits-et-associer-un-\u00e9crit-\u00e0-un-projet-d\u00e9criture-ou-de-communication",
    defaults={
        'title': "GS Diff\u00e9rencier les types d'\u00e9crits et associer un \u00e9crit \u00e0 un projet d'\u00e9criture ou de communication",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Diff\u00e9rencier les types d'\u00e9crits et associer un \u00e9crit \u00e0 un projet d'\u00e9criture ou de communication</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Repérer et dégager la structure et l'organisation (mise en page, typographie) de formes d'écrits fréquemment utilisés en classe (structure de la lettre, de la recette, du conte, d'un écrit documentaire, d'une notice de fabrication)
competence70, created = Page.objects.get_or_create(
    slug="gs-rep\u00e9rer-et-d\u00e9gager-la-structure-et-lorganisation-mise-en-page-typographie-de-formes-d\u00e9crits-fr\u00e9quemment-utilis\u00e9s-en-classe-structure-de-la-lettre-de-la-recette-du-conte-dun-\u00e9crit-documentaire-dune-notice-de-fabrication",
    defaults={
        'title': "GS Rep\u00e9rer et d\u00e9gager la structure et l'organisation (mise en page, typographie) de formes d'\u00e9crits fr\u00e9quemment utilis\u00e9s en classe (structure de la lettre, de la recette, du conte, d'un \u00e9crit documentaire, d'une notice de fabrication)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Rep\u00e9rer et d\u00e9gager la structure et l'organisation (mise en page, typographie) de formes d'\u00e9crits fr\u00e9quemment utilis\u00e9s en classe (structure de la lettre, de la recette, du conte, d'un \u00e9crit documentaire, d'une notice de fabrication)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Construire les caractéristiques des personnages archétypaux (loup, princesse, ogre, sorcière, renard, fée, etc.)
competence71, created = Page.objects.get_or_create(
    slug="gs-construire-les-caract\u00e9ristiques-des-personnages-arch\u00e9typaux-loup-princesse-ogre-sorci\u00e8re-renard-f\u00e9e-etc.",
    defaults={
        'title': "GS Construire les caract\u00e9ristiques des personnages arch\u00e9typaux (loup, princesse, ogre, sorci\u00e8re, renard, f\u00e9e, etc.)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Construire les caract\u00e9ristiques des personnages arch\u00e9typaux (loup, princesse, ogre, sorci\u00e8re, renard, f\u00e9e, etc.)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Comprendre des histoires où l'enchainement des actions est lié au destin de personnages centraux ou secondaires qui évoluent et interagissent, dans des lieux diversifiés
competence72, created = Page.objects.get_or_create(
    slug="gs-comprendre-des-histoires-o\u00f9-lenchainement-des-actions-est-li\u00e9-au-destin-de-personnages-centraux-ou-secondaires-qui-\u00e9voluent-et-interagissent-dans-des-lieux-diversifi\u00e9s",
    defaults={
        'title': "GS Comprendre des histoires o\u00f9 l'enchainement des actions est li\u00e9 au destin de personnages centraux ou secondaires qui \u00e9voluent et interagissent, dans des lieux diversifi\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre des histoires o\u00f9 l'enchainement des actions est li\u00e9 au destin de personnages centraux ou secondaires qui \u00e9voluent et interagissent, dans des lieux diversifi\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Comprendre les émotions, les intentions et les sentiments qui animent les personnages
competence73, created = Page.objects.get_or_create(
    slug="gs-comprendre-les-\u00e9motions-les-intentions-et-les-sentiments-qui-animent-les-personnages",
    defaults={
        'title': "GS Comprendre les \u00e9motions, les intentions et les sentiments qui animent les personnages",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre les \u00e9motions, les intentions et les sentiments qui animent les personnages</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : GS Établir un lien entre la lecture effectuée et sa propre expérience
competence74, created = Page.objects.get_or_create(
    slug="gs-\u00e9tablir-un-lien-entre-la-lecture-effectu\u00e9e-et-sa-propre-exp\u00e9rience",
    defaults={
        'title': "GS \u00c9tablir un lien entre la lecture effectu\u00e9e et sa propre exp\u00e9rience",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS \u00c9tablir un lien entre la lecture effectu\u00e9e et sa propre exp\u00e9rience</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 lire",
        'competence_generale': "\u00c9couter et comprendre diff\u00e9rentes formes d'\u00e9crits",
    }
)

# Compétence : PS Participer aux activités de motricité générale, de motricité fine et aux exercices de graphismes
competence75, created = Page.objects.get_or_create(
    slug="ps-participer-aux-activit\u00e9s-de-motricit\u00e9-g\u00e9n\u00e9rale-de-motricit\u00e9-fine-et-aux-exercices-de-graphismes",
    defaults={
        'title': "PS Participer aux activit\u00e9s de motricit\u00e9 g\u00e9n\u00e9rale, de motricit\u00e9 fine et aux exercices de graphismes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Participer aux activit\u00e9s de motricit\u00e9 g\u00e9n\u00e9rale, de motricit\u00e9 fine et aux exercices de graphismes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : PS Guider son geste par le regard lorsqu'il trace ou écrit
competence76, created = Page.objects.get_or_create(
    slug="ps-guider-son-geste-par-le-regard-lorsquil-trace-ou-\u00e9crit",
    defaults={
        'title': "PS Guider son geste par le regard lorsqu'il trace ou \u00e9crit",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Guider son geste par le regard lorsqu'il trace ou \u00e9crit</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : PS Prendre des repères spatiaux sur le support utilisé pour tracer
competence77, created = Page.objects.get_or_create(
    slug="ps-prendre-des-rep\u00e8res-spatiaux-sur-le-support-utilis\u00e9-pour-tracer",
    defaults={
        'title': "PS Prendre des rep\u00e8res spatiaux sur le support utilis\u00e9 pour tracer",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Prendre des rep\u00e8res spatiaux sur le support utilis\u00e9 pour tracer</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : MS Adopter une posture adaptée au geste d'écriture
competence78, created = Page.objects.get_or_create(
    slug="ms-adopter-une-posture-adapt\u00e9e-au-geste-d\u00e9criture",
    defaults={
        'title': "MS Adopter une posture adapt\u00e9e au geste d'\u00e9criture",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Adopter une posture adapt\u00e9e au geste d'\u00e9criture</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : MS Adopter une préhension correcte du stylo et s'entrainer à ne pas le lever en écrivant
competence79, created = Page.objects.get_or_create(
    slug="ms-adopter-une-pr\u00e9hension-correcte-du-stylo-et-sentrainer-\u00e0-ne-pas-le-lever-en-\u00e9crivant",
    defaults={
        'title': "MS Adopter une pr\u00e9hension correcte du stylo et s'entrainer \u00e0 ne pas le lever en \u00e9crivant",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Adopter une pr\u00e9hension correcte du stylo et s'entrainer \u00e0 ne pas le lever en \u00e9crivant</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : MS Utiliser de façon coordonnée les quatre articulations qui servent à tenir et guider le crayon (épaule, coude, poignet, doigts)
competence80, created = Page.objects.get_or_create(
    slug="ms-utiliser-de-fa\u00e7on-coordonn\u00e9e-les-quatre-articulations-qui-servent-\u00e0-tenir-et-guider-le-crayon-\u00e9paule-coude-poignet-doigts",
    defaults={
        'title': "MS Utiliser de fa\u00e7on coordonn\u00e9e les quatre articulations qui servent \u00e0 tenir et guider le crayon (\u00e9paule, coude, poignet, doigts)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Utiliser de fa\u00e7on coordonn\u00e9e les quatre articulations qui servent \u00e0 tenir et guider le crayon (\u00e9paule, coude, poignet, doigts)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : MS Tracer des lettres capitales
competence81, created = Page.objects.get_or_create(
    slug="ms-tracer-des-lettres-capitales",
    defaults={
        'title': "MS Tracer des lettres capitales",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Tracer des lettres capitales</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : MS S'initier aux tracés de l'écriture cursive
competence82, created = Page.objects.get_or_create(
    slug="ms-sinitier-aux-trac\u00e9s-de-l\u00e9criture-cursive",
    defaults={
        'title': "MS S'initier aux trac\u00e9s de l'\u00e9criture cursive",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS S'initier aux trac\u00e9s de l'\u00e9criture cursive</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : GS Tenir correctement son stylo par la pince des doigts et utiliser de façon coordonnée les quatre articulations (épaule, coude, poignet, doigts)
competence83, created = Page.objects.get_or_create(
    slug="gs-tenir-correctement-son-stylo-par-la-pince-des-doigts-et-utiliser-de-fa\u00e7on-coordonn\u00e9e-les-quatre-articulations-\u00e9paule-coude-poignet-doigts",
    defaults={
        'title': "GS Tenir correctement son stylo par la pince des doigts et utiliser de fa\u00e7on coordonn\u00e9e les quatre articulations (\u00e9paule, coude, poignet, doigts)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Tenir correctement son stylo par la pince des doigts et utiliser de fa\u00e7on coordonn\u00e9e les quatre articulations (\u00e9paule, coude, poignet, doigts)</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : GS Travailler la ligature entre deux lettres
competence84, created = Page.objects.get_or_create(
    slug="gs-travailler-la-ligature-entre-deux-lettres",
    defaults={
        'title': "GS Travailler la ligature entre deux lettres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Travailler la ligature entre deux lettres</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : GS Tracer des lettres en écriture cursive, les enchainer
competence85, created = Page.objects.get_or_create(
    slug="gs-tracer-des-lettres-en-\u00e9criture-cursive-les-enchainer",
    defaults={
        'title': "GS Tracer des lettres en \u00e9criture cursive, les enchainer",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Tracer des lettres en \u00e9criture cursive, les enchainer</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Apprendre le geste d'\u00e9criture",
    }
)

# Compétence : PS Percevoir que l'écrit encode l'oral
competence86, created = Page.objects.get_or_create(
    slug="ps-percevoir-que-l\u00e9crit-encode-loral",
    defaults={
        'title': "PS Percevoir que l'\u00e9crit encode l'oral",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Percevoir que l'\u00e9crit encode l'oral</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : PS Utiliser un support écrit connu
competence87, created = Page.objects.get_or_create(
    slug="ps-utiliser-un-support-\u00e9crit-connu",
    defaults={
        'title': "PS Utiliser un support \u00e9crit connu",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Utiliser un support \u00e9crit connu</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : PS Mimer la posture et les gestes d'écriture de l'adulte lors de la production de traces qui s'apparentent à de l'écriture
competence88, created = Page.objects.get_or_create(
    slug="ps-mimer-la-posture-et-les-gestes-d\u00e9criture-de-ladulte-lors-de-la-production-de-traces-qui-sapparentent-\u00e0-de-l\u00e9criture",
    defaults={
        'title': "PS Mimer la posture et les gestes d'\u00e9criture de l'adulte lors de la production de traces qui s'apparentent \u00e0 de l'\u00e9criture",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Mimer la posture et les gestes d'\u00e9criture de l'adulte lors de la production de traces qui s'apparentent \u00e0 de l'\u00e9criture</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : PS Tracer volontairement des signes abstraits dont on comprend qu'il ne s'agit pas de dessins, mais de lettres
competence89, created = Page.objects.get_or_create(
    slug="ps-tracer-volontairement-des-signes-abstraits-dont-on-comprend-quil-ne-sagit-pas-de-dessins-mais-de-lettres",
    defaults={
        'title': "PS Tracer volontairement des signes abstraits dont on comprend qu'il ne s'agit pas de dessins, mais de lettres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Tracer volontairement des signes abstraits dont on comprend qu'il ne s'agit pas de dessins, mais de lettres</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Comprendre que lorsque l'adulte lit un même écrit plusieurs fois, ce qu'il lit est toujours identique
competence90, created = Page.objects.get_or_create(
    slug="ms-comprendre-que-lorsque-ladulte-lit-un-m\u00eame-\u00e9crit-plusieurs-fois-ce-quil-lit-est-toujours-identique",
    defaults={
        'title': "MS Comprendre que lorsque l'adulte lit un m\u00eame \u00e9crit plusieurs fois, ce qu'il lit est toujours identique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comprendre que lorsque l'adulte lit un m\u00eame \u00e9crit plusieurs fois, ce qu'il lit est toujours identique</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Comprendre que l'écrit code des sons
competence91, created = Page.objects.get_or_create(
    slug="ms-comprendre-que-l\u00e9crit-code-des-sons",
    defaults={
        'title': "MS Comprendre que l'\u00e9crit code des sons",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comprendre que l'\u00e9crit code des sons</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Proposer au professeur, lors d'une activité de dictée à l'adulte, le contenu d'un court message, stabiliser un énoncé oral et le mémoriser pour pouvoir ensuite le dicter au professeur
competence92, created = Page.objects.get_or_create(
    slug="ms-proposer-au-professeur-lors-dune-activit\u00e9-de-dict\u00e9e-\u00e0-ladulte-le-contenu-dun-court-message-stabiliser-un-\u00e9nonc\u00e9-oral-et-le-m\u00e9moriser-pour-pouvoir-ensuite-le-dicter-au-professeur",
    defaults={
        'title': "MS Proposer au professeur, lors d'une activit\u00e9 de dict\u00e9e \u00e0 l'adulte, le contenu d'un court message, stabiliser un \u00e9nonc\u00e9 oral et le m\u00e9moriser pour pouvoir ensuite le dicter au professeur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Proposer au professeur, lors d'une activit\u00e9 de dict\u00e9e \u00e0 l'adulte, le contenu d'un court message, stabiliser un \u00e9nonc\u00e9 oral et le m\u00e9moriser pour pouvoir ensuite le dicter au professeur</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Comparer la longueur d'un texte écrit et la durée du texte entendu
competence93, created = Page.objects.get_or_create(
    slug="ms-comparer-la-longueur-dun-texte-\u00e9crit-et-la-dur\u00e9e-du-texte-entendu",
    defaults={
        'title': "MS Comparer la longueur d'un texte \u00e9crit et la dur\u00e9e du texte entendu",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comparer la longueur d'un texte \u00e9crit et la dur\u00e9e du texte entendu</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Savoir que le sens de la lecture est de gauche à droite et de haut en bas
competence94, created = Page.objects.get_or_create(
    slug="ms-savoir-que-le-sens-de-la-lecture-est-de-gauche-\u00e0-droite-et-de-haut-en-bas",
    defaults={
        'title': "MS Savoir que le sens de la lecture est de gauche \u00e0 droite et de haut en bas",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Savoir que le sens de la lecture est de gauche \u00e0 droite et de haut en bas</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : MS Chercher parmi les outils à sa disposition des modèles qui seront réutilisés dans un essai d'écriture
competence95, created = Page.objects.get_or_create(
    slug="ms-chercher-parmi-les-outils-\u00e0-sa-disposition-des-mod\u00e8les-qui-seront-r\u00e9utilis\u00e9s-dans-un-essai-d\u00e9criture",
    defaults={
        'title': "MS Chercher parmi les outils \u00e0 sa disposition des mod\u00e8les qui seront r\u00e9utilis\u00e9s dans un essai d'\u00e9criture",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Chercher parmi les outils \u00e0 sa disposition des mod\u00e8les qui seront r\u00e9utilis\u00e9s dans un essai d'\u00e9criture</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Segmenter l'oral en mots, les mots en syllabes, quelques syllabes en phonèmes
competence96, created = Page.objects.get_or_create(
    slug="gs-segmenter-loral-en-mots-les-mots-en-syllabes-quelques-syllabes-en-phon\u00e8mes",
    defaults={
        'title': "GS Segmenter l'oral en mots, les mots en syllabes, quelques syllabes en phon\u00e8mes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Segmenter l'oral en mots, les mots en syllabes, quelques syllabes en phon\u00e8mes</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Comprendre que l'écrit encode l'oral et que les sons de la langue sont codés par des lettres
competence97, created = Page.objects.get_or_create(
    slug="gs-comprendre-que-l\u00e9crit-encode-loral-et-que-les-sons-de-la-langue-sont-cod\u00e9s-par-des-lettres",
    defaults={
        'title': "GS Comprendre que l'\u00e9crit encode l'oral et que les sons de la langue sont cod\u00e9s par des lettres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre que l'\u00e9crit encode l'oral et que les sons de la langue sont cod\u00e9s par des lettres</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Suivre la trace écrite des yeux lors d'une relecture par l'adulte d'un message produit lors d'une dictée à l'adulte
competence98, created = Page.objects.get_or_create(
    slug="gs-suivre-la-trace-\u00e9crite-des-yeux-lors-dune-relecture-par-ladulte-dun-message-produit-lors-dune-dict\u00e9e-\u00e0-ladulte",
    defaults={
        'title': "GS Suivre la trace \u00e9crite des yeux lors d'une relecture par l'adulte d'un message produit lors d'une dict\u00e9e \u00e0 l'adulte",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Suivre la trace \u00e9crite des yeux lors d'une relecture par l'adulte d'un message produit lors d'une dict\u00e9e \u00e0 l'adulte</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Mémoriser la graphie d'un mot transparent, en s'appuyant sur la connaissance des lettres et la conscience phonologique et le retranscrire sur un support
competence99, created = Page.objects.get_or_create(
    slug="gs-m\u00e9moriser-la-graphie-dun-mot-transparent-en-sappuyant-sur-la-connaissance-des-lettres-et-la-conscience-phonologique-et-le-retranscrire-sur-un-support",
    defaults={
        'title': "GS M\u00e9moriser la graphie d'un mot transparent, en s'appuyant sur la connaissance des lettres et la conscience phonologique et le retranscrire sur un support",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS M\u00e9moriser la graphie d'un mot transparent, en s'appuyant sur la connaissance des lettres et la conscience phonologique et le retranscrire sur un support</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Réinvestir ses premières connaissances relatives au principe alphabétique pour produire un écrit
competence100, created = Page.objects.get_or_create(
    slug="gs-r\u00e9investir-ses-premi\u00e8res-connaissances-relatives-au-principe-alphab\u00e9tique-pour-produire-un-\u00e9crit",
    defaults={
        'title': "GS R\u00e9investir ses premi\u00e8res connaissances relatives au principe alphab\u00e9tique pour produire un \u00e9crit",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS R\u00e9investir ses premi\u00e8res connaissances relatives au principe alphab\u00e9tique pour produire un \u00e9crit</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Se repérer dans l'alphabet pour retrouver l'écriture d'une lettre nécessaire pour produire un écrit
competence101, created = Page.objects.get_or_create(
    slug="gs-se-rep\u00e9rer-dans-lalphabet-pour-retrouver-l\u00e9criture-dune-lettre-n\u00e9cessaire-pour-produire-un-\u00e9crit",
    defaults={
        'title': "GS Se rep\u00e9rer dans l'alphabet pour retrouver l'\u00e9criture d'une lettre n\u00e9cessaire pour produire un \u00e9crit",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Se rep\u00e9rer dans l'alphabet pour retrouver l'\u00e9criture d'une lettre n\u00e9cessaire pour produire un \u00e9crit</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Mémoriser l'écriture de mots transparents ou de syllabes connues pour les réutiliser dans une production d'écrit
competence102, created = Page.objects.get_or_create(
    slug="gs-m\u00e9moriser-l\u00e9criture-de-mots-transparents-ou-de-syllabes-connues-pour-les-r\u00e9utiliser-dans-une-production-d\u00e9crit",
    defaults={
        'title': "GS M\u00e9moriser l'\u00e9criture de mots transparents ou de syllabes connues pour les r\u00e9utiliser dans une production d'\u00e9crit",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS M\u00e9moriser l'\u00e9criture de mots transparents ou de syllabes connues pour les r\u00e9utiliser dans une production d'\u00e9crit</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Comprendre qu'il existe une norme pour écrire : ponctuation, majuscules, mise en page, etc.
competence103, created = Page.objects.get_or_create(
    slug="gs-comprendre-quil-existe-une-norme-pour-\u00e9crire-:-ponctuation-majuscules-mise-en-page-etc.",
    defaults={
        'title': "GS Comprendre qu'il existe une norme pour \u00e9crire : ponctuation, majuscules, mise en page, etc.",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre qu'il existe une norme pour \u00e9crire : ponctuation, majuscules, mise en page, etc.</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : GS Persévérer pour mener la production d'écrit à son terme : préparation, énonciation et révision
competence104, created = Page.objects.get_or_create(
    slug="gs-pers\u00e9v\u00e9rer-pour-mener-la-production-d\u00e9crit-\u00e0-son-terme-:-pr\u00e9paration-\u00e9nonciation-et-r\u00e9vision",
    defaults={
        'title': "GS Pers\u00e9v\u00e9rer pour mener la production d'\u00e9crit \u00e0 son terme : pr\u00e9paration, \u00e9nonciation et r\u00e9vision",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Pers\u00e9v\u00e9rer pour mener la production d'\u00e9crit \u00e0 son terme : pr\u00e9paration, \u00e9nonciation et r\u00e9vision</p>",
        'published': True,
        'parent': domaineDiscipline1,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Passer de l'oral \u00e0 l'\u00e9crit : se pr\u00e9parer \u00e0 apprendre \u00e0 \u00e9crire",
        'competence_generale': "Produire de premiers \u00e9crits",
    }
)

# Compétence : Courir, sauter, lancer de différentes façons, dans des espaces et avec des matériels variés, dans un but précis
competence105, created = Page.objects.get_or_create(
    slug="courir-sauter-lancer-de-diff\u00e9rentes-fa\u00e7ons-dans-des-espaces-et-avec-des-mat\u00e9riels-vari\u00e9s-dans-un-but-pr\u00e9cis",
    defaults={
        'title': "Courir, sauter, lancer de diff\u00e9rentes fa\u00e7ons, dans des espaces et avec des mat\u00e9riels vari\u00e9s, dans un but pr\u00e9cis",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Courir, sauter, lancer de diff\u00e9rentes fa\u00e7ons, dans des espaces et avec des mat\u00e9riels vari\u00e9s, dans un but pr\u00e9cis</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Ajuster et enchaîner ses actions et ses déplacements en fonction d'obstacles à franchir ou de la trajectoire d'objets sur lesquels agir
competence106, created = Page.objects.get_or_create(
    slug="ajuster-et-encha\u00eener-ses-actions-et-ses-d\u00e9placements-en-fonction-dobstacles-\u00e0-franchir-ou-de-la-trajectoire-dobjets-sur-lesquels-agir",
    defaults={
        'title': "Ajuster et encha\u00eener ses actions et ses d\u00e9placements en fonction d'obstacles \u00e0 franchir ou de la trajectoire d'objets sur lesquels agir",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Ajuster et encha\u00eener ses actions et ses d\u00e9placements en fonction d'obstacles \u00e0 franchir ou de la trajectoire d'objets sur lesquels agir</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : S'engager dans l'activité dans la durée et explorer différents possibles, à partir d'objets manipulables
competence107, created = Page.objects.get_or_create(
    slug="sengager-dans-lactivit\u00e9-dans-la-dur\u00e9e-et-explorer-diff\u00e9rents-possibles-\u00e0-partir-dobjets-manipulables",
    defaults={
        'title': "S'engager dans l'activit\u00e9 dans la dur\u00e9e et explorer diff\u00e9rents possibles, \u00e0 partir d'objets manipulables",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'engager dans l'activit\u00e9 dans la dur\u00e9e et explorer diff\u00e9rents possibles, \u00e0 partir d'objets manipulables</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Adapter son geste pour donner des trajectoires différentes à des projectiles variés et répondre aux consignes données
competence108, created = Page.objects.get_or_create(
    slug="adapter-son-geste-pour-donner-des-trajectoires-diff\u00e9rentes-\u00e0-des-projectiles-vari\u00e9s-et-r\u00e9pondre-aux-consignes-donn\u00e9es",
    defaults={
        'title': "Adapter son geste pour donner des trajectoires diff\u00e9rentes \u00e0 des projectiles vari\u00e9s et r\u00e9pondre aux consignes donn\u00e9es",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Adapter son geste pour donner des trajectoires diff\u00e9rentes \u00e0 des projectiles vari\u00e9s et r\u00e9pondre aux consignes donn\u00e9es</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Ajuster ses actions et ses déplacements en fonction de la trajectoire de l'objet qu'un autre lui envoie
competence109, created = Page.objects.get_or_create(
    slug="ajuster-ses-actions-et-ses-d\u00e9placements-en-fonction-de-la-trajectoire-de-lobjet-quun-autre-lui-envoie",
    defaults={
        'title': "Ajuster ses actions et ses d\u00e9placements en fonction de la trajectoire de l'objet qu'un autre lui envoie",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Ajuster ses actions et ses d\u00e9placements en fonction de la trajectoire de l'objet qu'un autre lui envoie</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Trouver des manières de faire efficaces pour mieux atteindre les buts proposés et chercher à progresser en fonction des effets ou des scores obtenus
competence110, created = Page.objects.get_or_create(
    slug="trouver-des-mani\u00e8res-de-faire-efficaces-pour-mieux-atteindre-les-buts-propos\u00e9s-et-chercher-\u00e0-progresser-en-fonction-des-effets-ou-des-scores-obtenus",
    defaults={
        'title': "Trouver des mani\u00e8res de faire efficaces pour mieux atteindre les buts propos\u00e9s et chercher \u00e0 progresser en fonction des effets ou des scores obtenus",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Trouver des mani\u00e8res de faire efficaces pour mieux atteindre les buts propos\u00e9s et chercher \u00e0 progresser en fonction des effets ou des scores obtenus</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Investir un espace aménagé et explorer différents cheminements ou différentes actions
competence111, created = Page.objects.get_or_create(
    slug="investir-un-espace-am\u00e9nag\u00e9-et-explorer-diff\u00e9rents-cheminements-ou-diff\u00e9rentes-actions",
    defaults={
        'title': "Investir un espace am\u00e9nag\u00e9 et explorer diff\u00e9rents cheminements ou diff\u00e9rentes actions",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Investir un espace am\u00e9nag\u00e9 et explorer diff\u00e9rents cheminements ou diff\u00e9rentes actions</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Proposer différentes solutions ou reproduire celles d'un autre, sur un parcours orienté, pour s'adapter aux obstacles rencontrés
competence112, created = Page.objects.get_or_create(
    slug="proposer-diff\u00e9rentes-solutions-ou-reproduire-celles-dun-autre-sur-un-parcours-orient\u00e9-pour-sadapter-aux-obstacles-rencontr\u00e9s",
    defaults={
        'title': "Proposer diff\u00e9rentes solutions ou reproduire celles d'un autre, sur un parcours orient\u00e9, pour s'adapter aux obstacles rencontr\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Proposer diff\u00e9rentes solutions ou reproduire celles d'un autre, sur un parcours orient\u00e9, pour s'adapter aux obstacles rencontr\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Enchainer, dans la continuité, une succession d'actions différentes en respectant les contraintes de réalisation ou les critères de réussite proposés
competence113, created = Page.objects.get_or_create(
    slug="enchainer-dans-la-continuit\u00e9-une-succession-dactions-diff\u00e9rentes-en-respectant-les-contraintes-de-r\u00e9alisation-ou-les-crit\u00e8res-de-r\u00e9ussite-propos\u00e9s",
    defaults={
        'title': "Enchainer, dans la continuit\u00e9, une succession d'actions diff\u00e9rentes en respectant les contraintes de r\u00e9alisation ou les crit\u00e8res de r\u00e9ussite propos\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Enchainer, dans la continuit\u00e9, une succession d'actions diff\u00e9rentes en respectant les contraintes de r\u00e9alisation ou les crit\u00e8res de r\u00e9ussite propos\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Anticiper et mettre en oeuvre un projet d'action en fonction des effets ou des résultats obtenus afin d'atteindre le but recherché
competence114, created = Page.objects.get_or_create(
    slug="anticiper-et-mettre-en-oeuvre-un-projet-daction-en-fonction-des-effets-ou-des-r\u00e9sultats-obtenus-afin-datteindre-le-but-recherch\u00e9",
    defaults={
        'title': "Anticiper et mettre en oeuvre un projet d'action en fonction des effets ou des r\u00e9sultats obtenus afin d'atteindre le but recherch\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Anticiper et mettre en oeuvre un projet d'action en fonction des effets ou des r\u00e9sultats obtenus afin d'atteindre le but recherch\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Agir dans l'espace, dans la dur\u00e9e et sur les objets",
    }
)

# Compétence : Ajuster et enchaîner ses actions et ses déplacements en fonction d'obstacles à franchir
competence115, created = Page.objects.get_or_create(
    slug="ajuster-et-encha\u00eener-ses-actions-et-ses-d\u00e9placements-en-fonction-dobstacles-\u00e0-franchir",
    defaults={
        'title': "Ajuster et encha\u00eener ses actions et ses d\u00e9placements en fonction d'obstacles \u00e0 franchir",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Ajuster et encha\u00eener ses actions et ses d\u00e9placements en fonction d'obstacles \u00e0 franchir</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Se déplacer avec aisance et en sécurité dans des environnements variés, naturels ou aménagés
competence116, created = Page.objects.get_or_create(
    slug="se-d\u00e9placer-avec-aisance-et-en-s\u00e9curit\u00e9-dans-des-environnements-vari\u00e9s-naturels-ou-am\u00e9nag\u00e9s",
    defaults={
        'title': "Se d\u00e9placer avec aisance et en s\u00e9curit\u00e9 dans des environnements vari\u00e9s, naturels ou am\u00e9nag\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se d\u00e9placer avec aisance et en s\u00e9curit\u00e9 dans des environnements vari\u00e9s, naturels ou am\u00e9nag\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : S'engager dans l'activité et élaborer des itinéraires ou des actions en réponse à un aménagement donné
competence117, created = Page.objects.get_or_create(
    slug="sengager-dans-lactivit\u00e9-et-\u00e9laborer-des-itin\u00e9raires-ou-des-actions-en-r\u00e9ponse-\u00e0-un-am\u00e9nagement-donn\u00e9",
    defaults={
        'title': "S'engager dans l'activit\u00e9 et \u00e9laborer des itin\u00e9raires ou des actions en r\u00e9ponse \u00e0 un am\u00e9nagement donn\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'engager dans l'activit\u00e9 et \u00e9laborer des itin\u00e9raires ou des actions en r\u00e9ponse \u00e0 un am\u00e9nagement donn\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Oser proposer, reproduire ou inventer des actions nouvelles, remettant en jeu les repères habituels


competence118, created = Page.objects.get_or_create(
    slug="oser-proposer-reproduire-ou-inventer-des-actions-nouvelles-remettant-en-jeu-les-rep\u00e8res-habituels\n\n",
    defaults={
        'title': "Oser proposer, reproduire ou inventer des actions nouvelles, remettant en jeu les rep\u00e8res habituels\n\n",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Oser proposer, reproduire ou inventer des actions nouvelles, remettant en jeu les rep\u00e8res habituels\n\n</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Se risquer à des déséquilibres afin de réaliser des « acrobaties » et montrer à d'autres ses trouvailles, ses propres « exploits »
competence119, created = Page.objects.get_or_create(
    slug="se-risquer-\u00e0-des-d\u00e9s\u00e9quilibres-afin-de-r\u00e9aliser-des-\u00ab-acrobaties-\u00bb-et-montrer-\u00e0-dautres-ses-trouvailles-ses-propres-\u00ab-exploits-\u00bb",
    defaults={
        'title': "Se risquer \u00e0 des d\u00e9s\u00e9quilibres afin de r\u00e9aliser des \u00ab acrobaties \u00bb et montrer \u00e0 d'autres ses trouvailles, ses propres \u00ab exploits \u00bb",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se risquer \u00e0 des d\u00e9s\u00e9quilibres afin de r\u00e9aliser des \u00ab acrobaties \u00bb et montrer \u00e0 d'autres ses trouvailles, ses propres \u00ab exploits \u00bb</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Anticiper, réaliser, montrer à d'autres un projet de parcours, constitué de l'enchainement d'une courte séquence d'actions, se déroulant dans un espace orienté
competence120, created = Page.objects.get_or_create(
    slug="anticiper-r\u00e9aliser-montrer-\u00e0-dautres-un-projet-de-parcours-constitu\u00e9-de-lenchainement-dune-courte-s\u00e9quence-dactions-se-d\u00e9roulant-dans-un-espace-orient\u00e9",
    defaults={
        'title': "Anticiper, r\u00e9aliser, montrer \u00e0 d'autres un projet de parcours, constitu\u00e9 de l'enchainement d'une courte s\u00e9quence d'actions, se d\u00e9roulant dans un espace orient\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Anticiper, r\u00e9aliser, montrer \u00e0 d'autres un projet de parcours, constitu\u00e9 de l'enchainement d'une courte s\u00e9quence d'actions, se d\u00e9roulant dans un espace orient\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Utiliser des engins inhabituels, en cherchant à réguler les déséquilibres que ceux-ci occasionnent
competence121, created = Page.objects.get_or_create(
    slug="utiliser-des-engins-inhabituels-en-cherchant-\u00e0-r\u00e9guler-les-d\u00e9s\u00e9quilibres-que-ceux-ci-occasionnent",
    defaults={
        'title': "Utiliser des engins inhabituels, en cherchant \u00e0 r\u00e9guler les d\u00e9s\u00e9quilibres que ceux-ci occasionnent",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des engins inhabituels, en cherchant \u00e0 r\u00e9guler les d\u00e9s\u00e9quilibres que ceux-ci occasionnent</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Trouver des moyens efficaces d'actions et de propulsion pour se déplacer dans un espace aménagé
competence122, created = Page.objects.get_or_create(
    slug="trouver-des-moyens-efficaces-dactions-et-de-propulsion-pour-se-d\u00e9placer-dans-un-espace-am\u00e9nag\u00e9",
    defaults={
        'title': "Trouver des moyens efficaces d'actions et de propulsion pour se d\u00e9placer dans un espace am\u00e9nag\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Trouver des moyens efficaces d'actions et de propulsion pour se d\u00e9placer dans un espace am\u00e9nag\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Piloter des engins, en prenant des repères sur le milieu, afin de réaliser des itinéraires précis, des trajectoires prévues
competence123, created = Page.objects.get_or_create(
    slug="piloter-des-engins-en-prenant-des-rep\u00e8res-sur-le-milieu-afin-de-r\u00e9aliser-des-itin\u00e9raires-pr\u00e9cis-des-trajectoires-pr\u00e9vues",
    defaults={
        'title': "Piloter des engins, en prenant des rep\u00e8res sur le milieu, afin de r\u00e9aliser des itin\u00e9raires pr\u00e9cis, des trajectoires pr\u00e9vues",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Piloter des engins, en prenant des rep\u00e8res sur le milieu, afin de r\u00e9aliser des itin\u00e9raires pr\u00e9cis, des trajectoires pr\u00e9vues</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Prélever des indices dans un espace plus large ou inconnu, prendre en compte des moyens de guidage ou d'orientation pour anticiper et réaliser un projet d'action
competence124, created = Page.objects.get_or_create(
    slug="pr\u00e9lever-des-indices-dans-un-espace-plus-large-ou-inconnu-prendre-en-compte-des-moyens-de-guidage-ou-dorientation-pour-anticiper-et-r\u00e9aliser-un-projet-daction",
    defaults={
        'title': "Pr\u00e9lever des indices dans un espace plus large ou inconnu, prendre en compte des moyens de guidage ou d'orientation pour anticiper et r\u00e9aliser un projet d'action",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Pr\u00e9lever des indices dans un espace plus large ou inconnu, prendre en compte des moyens de guidage ou d'orientation pour anticiper et r\u00e9aliser un projet d'action</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Entrer dans l'eau et participer aux jeux proposés
competence125, created = Page.objects.get_or_create(
    slug="entrer-dans-leau-et-participer-aux-jeux-propos\u00e9s",
    defaults={
        'title': "Entrer dans l'eau et participer aux jeux propos\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Entrer dans l'eau et participer aux jeux propos\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : S'immerger totalement et ouvrir les yeux dans l'eau
competence126, created = Page.objects.get_or_create(
    slug="simmerger-totalement-et-ouvrir-les-yeux-dans-leau",
    defaults={
        'title': "S'immerger totalement et ouvrir les yeux dans l'eau",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'immerger totalement et ouvrir les yeux dans l'eau</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Abandonner les appuis plantaires pour se déplacer par appuis manuels ou se laisser flotter
competence127, created = Page.objects.get_or_create(
    slug="abandonner-les-appuis-plantaires-pour-se-d\u00e9placer-par-appuis-manuels-ou-se-laisser-flotter",
    defaults={
        'title': "Abandonner les appuis plantaires pour se d\u00e9placer par appuis manuels ou se laisser flotter",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Abandonner les appuis plantaires pour se d\u00e9placer par appuis manuels ou se laisser flotter</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Se déplacer, tête dans l'eau, en s'aidant des bras et des jambes et explorer le volume aquatique
competence128, created = Page.objects.get_or_create(
    slug="se-d\u00e9placer-t\u00eate-dans-leau-en-saidant-des-bras-et-des-jambes-et-explorer-le-volume-aquatique",
    defaults={
        'title': "Se d\u00e9placer, t\u00eate dans l'eau, en s'aidant des bras et des jambes et explorer le volume aquatique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se d\u00e9placer, t\u00eate dans l'eau, en s'aidant des bras et des jambes et explorer le volume aquatique</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Adapter ses \u00e9quilibres et ses d\u00e9placements \u00e0 des environnements et des contraintes vari\u00e9es",
    }
)

# Compétence : Construire et conserver une séquence d'actions et de déplacements, en relation avec d'autres partenaires, avec ou sans support musical
competence129, created = Page.objects.get_or_create(
    slug="construire-et-conserver-une-s\u00e9quence-dactions-et-de-d\u00e9placements-en-relation-avec-dautres-partenaires-avec-ou-sans-support-musical",
    defaults={
        'title': "Construire et conserver une s\u00e9quence d'actions et de d\u00e9placements, en relation avec d'autres partenaires, avec ou sans support musical",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Construire et conserver une s\u00e9quence d'actions et de d\u00e9placements, en relation avec d'autres partenaires, avec ou sans support musical</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Coordonner ses gestes et ses déplacements avec ceux des autres, lors de rondes et jeux chantés
competence130, created = Page.objects.get_or_create(
    slug="coordonner-ses-gestes-et-ses-d\u00e9placements-avec-ceux-des-autres-lors-de-rondes-et-jeux-chant\u00e9s",
    defaults={
        'title': "Coordonner ses gestes et ses d\u00e9placements avec ceux des autres, lors de rondes et jeux chant\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Coordonner ses gestes et ses d\u00e9placements avec ceux des autres, lors de rondes et jeux chant\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Explorer différents possibles à partir d'inducteurs variés, matériels ou imaginaires
competence131, created = Page.objects.get_or_create(
    slug="explorer-diff\u00e9rents-possibles-\u00e0-partir-dinducteurs-vari\u00e9s-mat\u00e9riels-ou-imaginaires",
    defaults={
        'title': "Explorer diff\u00e9rents possibles \u00e0 partir d'inducteurs vari\u00e9s, mat\u00e9riels ou imaginaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Explorer diff\u00e9rents possibles \u00e0 partir d'inducteurs vari\u00e9s, mat\u00e9riels ou imaginaires</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Transformer son mouvement par l'exploration de contrastes de vitesses, d'énergies, de niveaux, de dissociations
competence132, created = Page.objects.get_or_create(
    slug="transformer-son-mouvement-par-lexploration-de-contrastes-de-vitesses-d\u00e9nergies-de-niveaux-de-dissociations",
    defaults={
        'title': "Transformer son mouvement par l'exploration de contrastes de vitesses, d'\u00e9nergies, de niveaux, de dissociations",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Transformer son mouvement par l'exploration de contrastes de vitesses, d'\u00e9nergies, de niveaux, de dissociations</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Inventer, apprendre et reproduire une courte phrase dansée, constituée d'une séquence d'actions et de déplacements qu'il a pu globalement mémoriser
competence133, created = Page.objects.get_or_create(
    slug="inventer-apprendre-et-reproduire-une-courte-phrase-dans\u00e9e-constitu\u00e9e-dune-s\u00e9quence-dactions-et-de-d\u00e9placements-quil-a-pu-globalement-m\u00e9moriser",
    defaults={
        'title': "Inventer, apprendre et reproduire une courte phrase dans\u00e9e, constitu\u00e9e d'une s\u00e9quence d'actions et de d\u00e9placements qu'il a pu globalement m\u00e9moriser",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Inventer, apprendre et reproduire une courte phrase dans\u00e9e, constitu\u00e9e d'une s\u00e9quence d'actions et de d\u00e9placements qu'il a pu globalement m\u00e9moriser</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Inscrire ses actions et ses déplacements en relation avec les autres, dans un espace scénique commun orienté, dans le cadre d'un projet présenté à des spectateurs
competence134, created = Page.objects.get_or_create(
    slug="inscrire-ses-actions-et-ses-d\u00e9placements-en-relation-avec-les-autres-dans-un-espace-sc\u00e9nique-commun-orient\u00e9-dans-le-cadre-dun-projet-pr\u00e9sent\u00e9-\u00e0-des-spectateurs",
    defaults={
        'title': "Inscrire ses actions et ses d\u00e9placements en relation avec les autres, dans un espace sc\u00e9nique commun orient\u00e9, dans le cadre d'un projet pr\u00e9sent\u00e9 \u00e0 des spectateurs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Inscrire ses actions et ses d\u00e9placements en relation avec les autres, dans un espace sc\u00e9nique commun orient\u00e9, dans le cadre d'un projet pr\u00e9sent\u00e9 \u00e0 des spectateurs</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Accorder ses gestes et ses déplacements avec ceux des autres pour évoluer collectivement selon une disposition spatiale simple
competence135, created = Page.objects.get_or_create(
    slug="accorder-ses-gestes-et-ses-d\u00e9placements-avec-ceux-des-autres-pour-\u00e9voluer-collectivement-selon-une-disposition-spatiale-simple",
    defaults={
        'title': "Accorder ses gestes et ses d\u00e9placements avec ceux des autres pour \u00e9voluer collectivement selon une disposition spatiale simple",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Accorder ses gestes et ses d\u00e9placements avec ceux des autres pour \u00e9voluer collectivement selon une disposition spatiale simple</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Synchroniser sa voix, ses frappés, ses gestes ou ses déplacements avec la pulsation, avec le tempo ou en relation avec des évènements sonores facilement perceptibles
competence136, created = Page.objects.get_or_create(
    slug="synchroniser-sa-voix-ses-frapp\u00e9s-ses-gestes-ou-ses-d\u00e9placements-avec-la-pulsation-avec-le-tempo-ou-en-relation-avec-des-\u00e9v\u00e8nements-sonores-facilement-perceptibles",
    defaults={
        'title': "Synchroniser sa voix, ses frapp\u00e9s, ses gestes ou ses d\u00e9placements avec la pulsation, avec le tempo ou en relation avec des \u00e9v\u00e8nements sonores facilement perceptibles",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Synchroniser sa voix, ses frapp\u00e9s, ses gestes ou ses d\u00e9placements avec la pulsation, avec le tempo ou en relation avec des \u00e9v\u00e8nements sonores facilement perceptibles</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Anticiper les changements d'orientation ou de mode de groupement en fonction du support musical, tout en respectant la disposition spatiale
competence137, created = Page.objects.get_or_create(
    slug="anticiper-les-changements-dorientation-ou-de-mode-de-groupement-en-fonction-du-support-musical-tout-en-respectant-la-disposition-spatiale",
    defaults={
        'title': "Anticiper les changements d'orientation ou de mode de groupement en fonction du support musical, tout en respectant la disposition spatiale",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Anticiper les changements d'orientation ou de mode de groupement en fonction du support musical, tout en respectant la disposition spatiale</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Repérer la chronologie des actions ou des rôles dans différentes danses collectives, montrées ou transmises à d'autres
competence138, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-la-chronologie-des-actions-ou-des-r\u00f4les-dans-diff\u00e9rentes-danses-collectives-montr\u00e9es-ou-transmises-\u00e0-dautres",
    defaults={
        'title': "Rep\u00e9rer la chronologie des actions ou des r\u00f4les dans diff\u00e9rentes danses collectives, montr\u00e9es ou transmises \u00e0 d'autres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer la chronologie des actions ou des r\u00f4les dans diff\u00e9rentes danses collectives, montr\u00e9es ou transmises \u00e0 d'autres</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Communiquer avec les autres au travers d'actions \u00e0 vis\u00e9e expressive ou artistique",
    }
)

# Compétence : Courir, sauter, lancer de différentes façons, dans des espaces et avec des matériels variés, dans un but précis
competence139, created = Page.objects.get_or_create(
    slug="courir-sauter-lancer-de-diff\u00e9rentes-fa\u00e7ons-dans-des-espaces-et-avec-des-mat\u00e9riels-vari\u00e9s-dans-un-but-pr\u00e9cis-1",
    defaults={
        'title': "Courir, sauter, lancer de diff\u00e9rentes fa\u00e7ons, dans des espaces et avec des mat\u00e9riels vari\u00e9s, dans un but pr\u00e9cis",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Courir, sauter, lancer de diff\u00e9rentes fa\u00e7ons, dans des espaces et avec des mat\u00e9riels vari\u00e9s, dans un but pr\u00e9cis</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Coopérer, exercer des rôles différents complémentaires, s'opposer, élaborer des stratégies pour viser un but ou un effet commun
competence140, created = Page.objects.get_or_create(
    slug="coop\u00e9rer-exercer-des-r\u00f4les-diff\u00e9rents-compl\u00e9mentaires-sopposer-\u00e9laborer-des-strat\u00e9gies-pour-viser-un-but-ou-un-effet-commun",
    defaults={
        'title': "Coop\u00e9rer, exercer des r\u00f4les diff\u00e9rents compl\u00e9mentaires, s'opposer, \u00e9laborer des strat\u00e9gies pour viser un but ou un effet commun",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Coop\u00e9rer, exercer des r\u00f4les diff\u00e9rents compl\u00e9mentaires, s'opposer, \u00e9laborer des strat\u00e9gies pour viser un but ou un effet commun</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : S'inscrire dans des règles collectives afin d'atteindre, par des actions en parallèle, un but ou un effet commun
competence141, created = Page.objects.get_or_create(
    slug="sinscrire-dans-des-r\u00e8gles-collectives-afin-datteindre-par-des-actions-en-parall\u00e8le-un-but-ou-un-effet-commun",
    defaults={
        'title': "S'inscrire dans des r\u00e8gles collectives afin d'atteindre, par des actions en parall\u00e8le, un but ou un effet commun",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'inscrire dans des r\u00e8gles collectives afin d'atteindre, par des actions en parall\u00e8le, un but ou un effet commun</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Reconnaître son appartenance à une équipe donnée et à y exercer différents rôles complémentaires
competence142, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-son-appartenance-\u00e0-une-\u00e9quipe-donn\u00e9e-et-\u00e0-y-exercer-diff\u00e9rents-r\u00f4les-compl\u00e9mentaires",
    defaults={
        'title': "Reconna\u00eetre son appartenance \u00e0 une \u00e9quipe donn\u00e9e et \u00e0 y exercer diff\u00e9rents r\u00f4les compl\u00e9mentaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre son appartenance \u00e0 une \u00e9quipe donn\u00e9e et \u00e0 y exercer diff\u00e9rents r\u00f4les compl\u00e9mentaires</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Se repérer dans un espace orienté pour s'opposer au projet d'un adversaire ou d'une équipe tenant simultanément un rôle antagoniste
competence143, created = Page.objects.get_or_create(
    slug="se-rep\u00e9rer-dans-un-espace-orient\u00e9-pour-sopposer-au-projet-dun-adversaire-ou-dune-\u00e9quipe-tenant-simultan\u00e9ment-un-r\u00f4le-antagoniste",
    defaults={
        'title': "Se rep\u00e9rer dans un espace orient\u00e9 pour s'opposer au projet d'un adversaire ou d'une \u00e9quipe tenant simultan\u00e9ment un r\u00f4le antagoniste",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se rep\u00e9rer dans un espace orient\u00e9 pour s'opposer au projet d'un adversaire ou d'une \u00e9quipe tenant simultan\u00e9ment un r\u00f4le antagoniste</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Élaborer des stratégies individuelles ou collectives pour rechercher les manières de faire les plus efficaces
competence144, created = Page.objects.get_or_create(
    slug="\u00e9laborer-des-strat\u00e9gies-individuelles-ou-collectives-pour-rechercher-les-mani\u00e8res-de-faire-les-plus-efficaces",
    defaults={
        'title': "\u00c9laborer des strat\u00e9gies individuelles ou collectives pour rechercher les mani\u00e8res de faire les plus efficaces",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9laborer des strat\u00e9gies individuelles ou collectives pour rechercher les mani\u00e8res de faire les plus efficaces</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : S'inscrire dans des formes de jeu collectives visant à déplacer, à faire glisser, à porter le corps d'un autre ou un objet lourd ou volumineux
competence145, created = Page.objects.get_or_create(
    slug="sinscrire-dans-des-formes-de-jeu-collectives-visant-\u00e0-d\u00e9placer-\u00e0-faire-glisser-\u00e0-porter-le-corps-dun-autre-ou-un-objet-lourd-ou-volumineux",
    defaults={
        'title': "S'inscrire dans des formes de jeu collectives visant \u00e0 d\u00e9placer, \u00e0 faire glisser, \u00e0 porter le corps d'un autre ou un objet lourd ou volumineux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'inscrire dans des formes de jeu collectives visant \u00e0 d\u00e9placer, \u00e0 faire glisser, \u00e0 porter le corps d'un autre ou un objet lourd ou volumineux</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Entrer en contact avec le corps d'un partenaire pour explorer différentes formes d'actions simples et mesurer les effets produits
competence146, created = Page.objects.get_or_create(
    slug="entrer-en-contact-avec-le-corps-dun-partenaire-pour-explorer-diff\u00e9rentes-formes-dactions-simples-et-mesurer-les-effets-produits",
    defaults={
        'title': "Entrer en contact avec le corps d'un partenaire pour explorer diff\u00e9rentes formes d'actions simples et mesurer les effets produits",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Entrer en contact avec le corps d'un partenaire pour explorer diff\u00e9rentes formes d'actions simples et mesurer les effets produits</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : S'opposer à un adversaire, par la médiation d'un objet que celui-ci veut s'approprier ou défendre
competence147, created = Page.objects.get_or_create(
    slug="sopposer-\u00e0-un-adversaire-par-la-m\u00e9diation-dun-objet-que-celui-ci-veut-sapproprier-ou-d\u00e9fendre",
    defaults={
        'title': "S'opposer \u00e0 un adversaire, par la m\u00e9diation d'un objet que celui-ci veut s'approprier ou d\u00e9fendre",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'opposer \u00e0 un adversaire, par la m\u00e9diation d'un objet que celui-ci veut s'approprier ou d\u00e9fendre</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Organiser ses actions et ses saisies sur le corps de l'adversaire en fonction d'une intention précise ou d'une stratégie déterminée
competence148, created = Page.objects.get_or_create(
    slug="organiser-ses-actions-et-ses-saisies-sur-le-corps-de-ladversaire-en-fonction-dune-intention-pr\u00e9cise-ou-dune-strat\u00e9gie-d\u00e9termin\u00e9e",
    defaults={
        'title': "Organiser ses actions et ses saisies sur le corps de l'adversaire en fonction d'une intention pr\u00e9cise ou d'une strat\u00e9gie d\u00e9termin\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Organiser ses actions et ses saisies sur le corps de l'adversaire en fonction d'une intention pr\u00e9cise ou d'une strat\u00e9gie d\u00e9termin\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline2,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Collaborer, coop\u00e9rer, s'opposer",
    }
)

# Compétence : Choisir différents outils, médiums, supports en fonction d'un projet ou d'une consigne et les utiliser en adaptant son geste
competence149, created = Page.objects.get_or_create(
    slug="choisir-diff\u00e9rents-outils-m\u00e9diums-supports-en-fonction-dun-projet-ou-dune-consigne-et-les-utiliser-en-adaptant-son-geste",
    defaults={
        'title': "Choisir diff\u00e9rents outils, m\u00e9diums, supports en fonction d'un projet ou d'une consigne et les utiliser en adaptant son geste",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Choisir diff\u00e9rents outils, m\u00e9diums, supports en fonction d'un projet ou d'une consigne et les utiliser en adaptant son geste</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Pratiquer le dessin pour représenter ou illustrer, en étant fidèle au réel ou à un modèle, ou en inventant
competence150, created = Page.objects.get_or_create(
    slug="pratiquer-le-dessin-pour-repr\u00e9senter-ou-illustrer-en-\u00e9tant-fid\u00e8le-au-r\u00e9el-ou-\u00e0-un-mod\u00e8le-ou-en-inventant",
    defaults={
        'title': "Pratiquer le dessin pour repr\u00e9senter ou illustrer, en \u00e9tant fid\u00e8le au r\u00e9el ou \u00e0 un mod\u00e8le, ou en inventant",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Pratiquer le dessin pour repr\u00e9senter ou illustrer, en \u00e9tant fid\u00e8le au r\u00e9el ou \u00e0 un mod\u00e8le, ou en inventant</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Réaliser une composition personnelle en reproduisant des graphismes. Créer des graphismes nouveaux
competence151, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-une-composition-personnelle-en-reproduisant-des-graphismes.-cr\u00e9er-des-graphismes-nouveaux",
    defaults={
        'title': "R\u00e9aliser une composition personnelle en reproduisant des graphismes. Cr\u00e9er des graphismes nouveaux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser une composition personnelle en reproduisant des graphismes. Cr\u00e9er des graphismes nouveaux</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Réaliser des compositions plastiques, seul ou en petit groupe, en choisissant et combinant des matériaux, en réinvestissant des techniques et des procédés
competence152, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-des-compositions-plastiques-seul-ou-en-petit-groupe-en-choisissant-et-combinant-des-mat\u00e9riaux-en-r\u00e9investissant-des-techniques-et-des-proc\u00e9d\u00e9s",
    defaults={
        'title': "R\u00e9aliser des compositions plastiques, seul ou en petit groupe, en choisissant et combinant des mat\u00e9riaux, en r\u00e9investissant des techniques et des proc\u00e9d\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser des compositions plastiques, seul ou en petit groupe, en choisissant et combinant des mat\u00e9riaux, en r\u00e9investissant des techniques et des proc\u00e9d\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Décrire une image et exprimer son ressenti ou sa compréhension en utilisant un vocabulaire adapté
competence153, created = Page.objects.get_or_create(
    slug="d\u00e9crire-une-image-et-exprimer-son-ressenti-ou-sa-compr\u00e9hension-en-utilisant-un-vocabulaire-adapt\u00e9",
    defaults={
        'title': "D\u00e9crire une image et exprimer son ressenti ou sa compr\u00e9hension en utilisant un vocabulaire adapt\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9crire une image et exprimer son ressenti ou sa compr\u00e9hension en utilisant un vocabulaire adapt\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Proposer des solutions dans des situations de projet, de création, de résolution de problèmes
competence154, created = Page.objects.get_or_create(
    slug="proposer-des-solutions-dans-des-situations-de-projet-de-cr\u00e9ation-de-r\u00e9solution-de-probl\u00e8mes",
    defaults={
        'title': "Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : S'engager spontanément dans l'exploration libre, puis guidée, de différents outils et sur des supports variés
competence155, created = Page.objects.get_or_create(
    slug="sengager-spontan\u00e9ment-dans-lexploration-libre-puis-guid\u00e9e-de-diff\u00e9rents-outils-et-sur-des-supports-vari\u00e9s",
    defaults={
        'title': "S'engager spontan\u00e9ment dans l'exploration libre, puis guid\u00e9e, de diff\u00e9rents outils et sur des supports vari\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'engager spontan\u00e9ment dans l'exploration libre, puis guid\u00e9e, de diff\u00e9rents outils et sur des supports vari\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commencer à représenter ou à illustrer ce qu'il voit, ce dont il se souvient ou ce qu'il imagine
competence156, created = Page.objects.get_or_create(
    slug="commencer-\u00e0-repr\u00e9senter-ou-\u00e0-illustrer-ce-quil-voit-ce-dont-il-se-souvient-ou-ce-quil-imagine",
    defaults={
        'title': "Commencer \u00e0 repr\u00e9senter ou \u00e0 illustrer ce qu'il voit, ce dont il se souvient ou ce qu'il imagine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commencer \u00e0 repr\u00e9senter ou \u00e0 illustrer ce qu'il voit, ce dont il se souvient ou ce qu'il imagine</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Faire des choix d'outils et de procédés en fonction d'une intention donnée
competence157, created = Page.objects.get_or_create(
    slug="faire-des-choix-doutils-et-de-proc\u00e9d\u00e9s-en-fonction-dune-intention-donn\u00e9e",
    defaults={
        'title': "Faire des choix d'outils et de proc\u00e9d\u00e9s en fonction d'une intention donn\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Faire des choix d'outils et de proc\u00e9d\u00e9s en fonction d'une intention donn\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : S'exprimer sur sa production, sur celle d'un autre ou à propos d'une oeuvre d'artiste
competence158, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-sur-celle-dun-autre-ou-\u00e0-propos-dune-oeuvre-dartiste",
    defaults={
        'title': "S'exprimer sur sa production, sur celle d'un autre ou \u00e0 propos d'une oeuvre d'artiste",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production, sur celle d'un autre ou \u00e0 propos d'une oeuvre d'artiste</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : S'exprimer sur sa production, sur celle d'un autre ou à propos d'une oeuvre d'artiste
competence159, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-sur-celle-dun-autre-ou-\u00e0-propos-dune-oeuvre-dartiste-1",
    defaults={
        'title': "S'exprimer sur sa production, sur celle d'un autre ou \u00e0 propos d'une oeuvre d'artiste",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production, sur celle d'un autre ou \u00e0 propos d'une oeuvre d'artiste</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commencer à mettre en mots ce qu'il a voulu évoquer ou représenter
competence160, created = Page.objects.get_or_create(
    slug="commencer-\u00e0-mettre-en-mots-ce-quil-a-voulu-\u00e9voquer-ou-repr\u00e9senter",
    defaults={
        'title': "Commencer \u00e0 mettre en mots ce qu'il a voulu \u00e9voquer ou repr\u00e9senter",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commencer \u00e0 mettre en mots ce qu'il a voulu \u00e9voquer ou repr\u00e9senter</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commenter les effets produits, et les situer par rapport à ses intentions initiales
competence161, created = Page.objects.get_or_create(
    slug="commenter-les-effets-produits-et-les-situer-par-rapport-\u00e0-ses-intentions-initiales",
    defaults={
        'title': "Commenter les effets produits, et les situer par rapport \u00e0 ses intentions initiales",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commenter les effets produits, et les situer par rapport \u00e0 ses intentions initiales</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Contrôler et varier l'amplitude du geste pour s'adapter au format du support, produire des tracés de plus en plus diversifiés et plus précis
competence162, created = Page.objects.get_or_create(
    slug="contr\u00f4ler-et-varier-lamplitude-du-geste-pour-sadapter-au-format-du-support-produire-des-trac\u00e9s-de-plus-en-plus-diversifi\u00e9s-et-plus-pr\u00e9cis",
    defaults={
        'title': "Contr\u00f4ler et varier l'amplitude du geste pour s'adapter au format du support, produire des trac\u00e9s de plus en plus diversifi\u00e9s et plus pr\u00e9cis",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Contr\u00f4ler et varier l'amplitude du geste pour s'adapter au format du support, produire des trac\u00e9s de plus en plus diversifi\u00e9s et plus pr\u00e9cis</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Reproduire, assembler, organiser, enchaîner des motifs graphiques puis en créer de nouveaux
competence163, created = Page.objects.get_or_create(
    slug="reproduire-assembler-organiser-encha\u00eener-des-motifs-graphiques-puis-en-cr\u00e9er-de-nouveaux",
    defaults={
        'title': "Reproduire, assembler, organiser, encha\u00eener des motifs graphiques puis en cr\u00e9er de nouveaux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reproduire, assembler, organiser, encha\u00eener des motifs graphiques puis en cr\u00e9er de nouveaux</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : S'exprimer sur ses propres tracés et nommer les éléments graphiques produits
competence164, created = Page.objects.get_or_create(
    slug="sexprimer-sur-ses-propres-trac\u00e9s-et-nommer-les-\u00e9l\u00e9ments-graphiques-produits",
    defaults={
        'title': "S'exprimer sur ses propres trac\u00e9s et nommer les \u00e9l\u00e9ments graphiques produits",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur ses propres trac\u00e9s et nommer les \u00e9l\u00e9ments graphiques produits</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Repérer des motifs graphiques sur différents supports ou dans son environnement pour constituer un répertoire
competence165, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-des-motifs-graphiques-sur-diff\u00e9rents-supports-ou-dans-son-environnement-pour-constituer-un-r\u00e9pertoire",
    defaults={
        'title': "Rep\u00e9rer des motifs graphiques sur diff\u00e9rents supports ou dans son environnement pour constituer un r\u00e9pertoire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer des motifs graphiques sur diff\u00e9rents supports ou dans son environnement pour constituer un r\u00e9pertoire</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commencer à mettre en mots ses procédures lors d'échanges entre pairs
competence166, created = Page.objects.get_or_create(
    slug="commencer-\u00e0-mettre-en-mots-ses-proc\u00e9dures-lors-d\u00e9changes-entre-pairs",
    defaults={
        'title': "Commencer \u00e0 mettre en mots ses proc\u00e9dures lors d'\u00e9changes entre pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commencer \u00e0 mettre en mots ses proc\u00e9dures lors d'\u00e9changes entre pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commencer à décrire une organisation produite ou observée
competence167, created = Page.objects.get_or_create(
    slug="commencer-\u00e0-d\u00e9crire-une-organisation-produite-ou-observ\u00e9e",
    defaults={
        'title': "Commencer \u00e0 d\u00e9crire une organisation produite ou observ\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commencer \u00e0 d\u00e9crire une organisation produite ou observ\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Explorer et s'approprier différents médiums, outils et matériaux
competence168, created = Page.objects.get_or_create(
    slug="explorer-et-sapproprier-diff\u00e9rents-m\u00e9diums-outils-et-mat\u00e9riaux",
    defaults={
        'title': "Explorer et s'approprier diff\u00e9rents m\u00e9diums, outils et mat\u00e9riaux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Explorer et s'approprier diff\u00e9rents m\u00e9diums, outils et mat\u00e9riaux</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Faire des choix de médiums (craie, encre, peinture...), de matériaux, d'outils et de supports en fonction de son intention
competence169, created = Page.objects.get_or_create(
    slug="faire-des-choix-de-m\u00e9diums-craie-encre-peinture...-de-mat\u00e9riaux-doutils-et-de-supports-en-fonction-de-son-intention",
    defaults={
        'title': "Faire des choix de m\u00e9diums (craie, encre, peinture...), de mat\u00e9riaux, d'outils et de supports en fonction de son intention",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Faire des choix de m\u00e9diums (craie, encre, peinture...), de mat\u00e9riaux, d'outils et de supports en fonction de son intention</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : S'exprimer sur sa production et / ou ses découvertes
competence170, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-et-/-ou-ses-d\u00e9couvertes",
    defaults={
        'title': "S'exprimer sur sa production et / ou ses d\u00e9couvertes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production et / ou ses d\u00e9couvertes</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Mémoriser et réinvestir un lexique approprié pour décrire les actions et / ou les effets produits
competence171, created = Page.objects.get_or_create(
    slug="m\u00e9moriser-et-r\u00e9investir-un-lexique-appropri\u00e9-pour-d\u00e9crire-les-actions-et-/-ou-les-effets-produits",
    defaults={
        'title': "M\u00e9moriser et r\u00e9investir un lexique appropri\u00e9 pour d\u00e9crire les actions et / ou les effets produits",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence M\u00e9moriser et r\u00e9investir un lexique appropri\u00e9 pour d\u00e9crire les actions et / ou les effets produits</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Observer des images fixes et animées, dire ce qu'il voit, ce qu'il imagine
competence172, created = Page.objects.get_or_create(
    slug="observer-des-images-fixes-et-anim\u00e9es-dire-ce-quil-voit-ce-quil-imagine",
    defaults={
        'title': "Observer des images fixes et anim\u00e9es, dire ce qu'il voit, ce qu'il imagine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Observer des images fixes et anim\u00e9es, dire ce qu'il voit, ce qu'il imagine</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Mettre en mots la relation entre ce qu'il a fait et ce qu'il souhaitait faire
competence173, created = Page.objects.get_or_create(
    slug="mettre-en-mots-la-relation-entre-ce-quil-a-fait-et-ce-quil-souhaitait-faire",
    defaults={
        'title': "Mettre en mots la relation entre ce qu'il a fait et ce qu'il souhaitait faire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Mettre en mots la relation entre ce qu'il a fait et ce qu'il souhaitait faire</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Comparer pour commencer à classer en repérant les différences et les ressemblances entre des images fixes et animées selon des critères simples
competence174, created = Page.objects.get_or_create(
    slug="comparer-pour-commencer-\u00e0-classer-en-rep\u00e9rant-les-diff\u00e9rences-et-les-ressemblances-entre-des-images-fixes-et-anim\u00e9es-selon-des-crit\u00e8res-simples",
    defaults={
        'title': "Comparer pour commencer \u00e0 classer en rep\u00e9rant les diff\u00e9rences et les ressemblances entre des images fixes et anim\u00e9es selon des crit\u00e8res simples",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Comparer pour commencer \u00e0 classer en rep\u00e9rant les diff\u00e9rences et les ressemblances entre des images fixes et anim\u00e9es selon des crit\u00e8res simples</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Commencer à établir et verbaliser des liens entre des images sélectionnées
competence175, created = Page.objects.get_or_create(
    slug="commencer-\u00e0-\u00e9tablir-et-verbaliser-des-liens-entre-des-images-s\u00e9lectionn\u00e9es",
    defaults={
        'title': "Commencer \u00e0 \u00e9tablir et verbaliser des liens entre des images s\u00e9lectionn\u00e9es",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Commencer \u00e0 \u00e9tablir et verbaliser des liens entre des images s\u00e9lectionn\u00e9es</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Entrer dans une lecture plus fine des images : lister les éléments narratifs et plastiques
competence176, created = Page.objects.get_or_create(
    slug="entrer-dans-une-lecture-plus-fine-des-images-:-lister-les-\u00e9l\u00e9ments-narratifs-et-plastiques",
    defaults={
        'title': "Entrer dans une lecture plus fine des images : lister les \u00e9l\u00e9ments narratifs et plastiques",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Entrer dans une lecture plus fine des images : lister les \u00e9l\u00e9ments narratifs et plastiques</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Classer des images en déterminant des critères simples
competence177, created = Page.objects.get_or_create(
    slug="classer-des-images-en-d\u00e9terminant-des-crit\u00e8res-simples",
    defaults={
        'title': "Classer des images en d\u00e9terminant des crit\u00e8res simples",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Classer des images en d\u00e9terminant des crit\u00e8res simples</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Utiliser un lexique adapté pour décrire ce qu'il voit, dire son ressenti ou traduire sa compréhension
competence178, created = Page.objects.get_or_create(
    slug="utiliser-un-lexique-adapt\u00e9-pour-d\u00e9crire-ce-quil-voit-dire-son-ressenti-ou-traduire-sa-compr\u00e9hension",
    defaults={
        'title': "Utiliser un lexique adapt\u00e9 pour d\u00e9crire ce qu'il voit, dire son ressenti ou traduire sa compr\u00e9hension",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser un lexique adapt\u00e9 pour d\u00e9crire ce qu'il voit, dire son ressenti ou traduire sa compr\u00e9hension</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Transformer des images en respectant une consigne
competence179, created = Page.objects.get_or_create(
    slug="transformer-des-images-en-respectant-une-consigne",
    defaults={
        'title': "Transformer des images en respectant une consigne",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Transformer des images en respectant une consigne</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Les productions plastiques et visuelles",
    }
)

# Compétence : Avoir mémorisé un répertoire varié de comptines et de chansons et les interpréter de manière expressive
competence180, created = Page.objects.get_or_create(
    slug="avoir-m\u00e9moris\u00e9-un-r\u00e9pertoire-vari\u00e9-de-comptines-et-de-chansons-et-les-interpr\u00e9ter-de-mani\u00e8re-expressive",
    defaults={
        'title': "Avoir m\u00e9moris\u00e9 un r\u00e9pertoire vari\u00e9 de comptines et de chansons et les interpr\u00e9ter de mani\u00e8re expressive",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Avoir m\u00e9moris\u00e9 un r\u00e9pertoire vari\u00e9 de comptines et de chansons et les interpr\u00e9ter de mani\u00e8re expressive</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Jouer avec sa voix pour explorer des variantes de timbre, d'intensité, de hauteur, de nuance
competence181, created = Page.objects.get_or_create(
    slug="jouer-avec-sa-voix-pour-explorer-des-variantes-de-timbre-dintensit\u00e9-de-hauteur-de-nuance",
    defaults={
        'title': "Jouer avec sa voix pour explorer des variantes de timbre, d'intensit\u00e9, de hauteur, de nuance",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Jouer avec sa voix pour explorer des variantes de timbre, d'intensit\u00e9, de hauteur, de nuance</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Repérer et reproduire, corporellement ou avec des instruments, des formules rythmiques simples
competence182, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-et-reproduire-corporellement-ou-avec-des-instruments-des-formules-rythmiques-simples",
    defaults={
        'title': "Rep\u00e9rer et reproduire, corporellement ou avec des instruments, des formules rythmiques simples",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer et reproduire, corporellement ou avec des instruments, des formules rythmiques simples</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Proposer des solutions dans des situations de projet, de création, de résolution de problèmes, avec son corps, sa voix ou des objets sonores
competence183, created = Page.objects.get_or_create(
    slug="proposer-des-solutions-dans-des-situations-de-projet-de-cr\u00e9ation-de-r\u00e9solution-de-probl\u00e8mes-avec-son-corps-sa-voix-ou-des-objets-sonores",
    defaults={
        'title': "Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes, avec son corps, sa voix ou des objets sonores",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes, avec son corps, sa voix ou des objets sonores</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Parler d'un extrait musical et exprimer son ressenti ou sa compréhension en utilisant un vocabulaire adapté
competence184, created = Page.objects.get_or_create(
    slug="parler-dun-extrait-musical-et-exprimer-son-ressenti-ou-sa-compr\u00e9hension-en-utilisant-un-vocabulaire-adapt\u00e9",
    defaults={
        'title': "Parler d'un extrait musical et exprimer son ressenti ou sa compr\u00e9hension en utilisant un vocabulaire adapt\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Parler d'un extrait musical et exprimer son ressenti ou sa compr\u00e9hension en utilisant un vocabulaire adapt\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Oser jouer avec sa voix seul ou en groupe pour reproduire un motif musical, une phrase (chanson, comptine)
competence185, created = Page.objects.get_or_create(
    slug="oser-jouer-avec-sa-voix-seul-ou-en-groupe-pour-reproduire-un-motif-musical-une-phrase-chanson-comptine",
    defaults={
        'title': "Oser jouer avec sa voix seul ou en groupe pour reproduire un motif musical, une phrase (chanson, comptine)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Oser jouer avec sa voix seul ou en groupe pour reproduire un motif musical, une phrase (chanson, comptine)</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Mémoriser des comptines et des chansons pour chanter en choeur avec ses pairs
competence186, created = Page.objects.get_or_create(
    slug="m\u00e9moriser-des-comptines-et-des-chansons-pour-chanter-en-choeur-avec-ses-pairs",
    defaults={
        'title': "M\u00e9moriser des comptines et des chansons pour chanter en choeur avec ses pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence M\u00e9moriser des comptines et des chansons pour chanter en choeur avec ses pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : S'exprimer sur sa production et sur celles de ses pairs
competence187, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-et-sur-celles-de-ses-pairs",
    defaults={
        'title': "S'exprimer sur sa production et sur celles de ses pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production et sur celles de ses pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : S'exprimer sur sa production et sur celles de ses pairs
competence188, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-et-sur-celles-de-ses-pairs-1",
    defaults={
        'title': "S'exprimer sur sa production et sur celles de ses pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production et sur celles de ses pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : S'exprimer sur sa production et sur celles de ses pairs
competence189, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-et-sur-celles-de-ses-pairs-2",
    defaults={
        'title': "S'exprimer sur sa production et sur celles de ses pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production et sur celles de ses pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Enrichir son bagage lexical spécifique au travers des chants et le réinvestir dans d'autres contextes
competence190, created = Page.objects.get_or_create(
    slug="enrichir-son-bagage-lexical-sp\u00e9cifique-au-travers-des-chants-et-le-r\u00e9investir-dans-dautres-contextes",
    defaults={
        'title': "Enrichir son bagage lexical sp\u00e9cifique au travers des chants et le r\u00e9investir dans d'autres contextes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Enrichir son bagage lexical sp\u00e9cifique au travers des chants et le r\u00e9investir dans d'autres contextes</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Mobiliser son attention lors de moments d'écoute
competence191, created = Page.objects.get_or_create(
    slug="mobiliser-son-attention-lors-de-moments-d\u00e9coute",
    defaults={
        'title': "Mobiliser son attention lors de moments d'\u00e9coute",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Mobiliser son attention lors de moments d'\u00e9coute</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Faire des propositions musicales enrichies par les écoutes
competence192, created = Page.objects.get_or_create(
    slug="faire-des-propositions-musicales-enrichies-par-les-\u00e9coutes",
    defaults={
        'title': "Faire des propositions musicales enrichies par les \u00e9coutes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Faire des propositions musicales enrichies par les \u00e9coutes</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Développer un vocabulaire pour nommer les paramètres du son
competence193, created = Page.objects.get_or_create(
    slug="d\u00e9velopper-un-vocabulaire-pour-nommer-les-param\u00e8tres-du-son",
    defaults={
        'title': "D\u00e9velopper un vocabulaire pour nommer les param\u00e8tres du son",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9velopper un vocabulaire pour nommer les param\u00e8tres du son</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Réinvestir le vocabulaire acquis lors des diverses activités de production
competence194, created = Page.objects.get_or_create(
    slug="r\u00e9investir-le-vocabulaire-acquis-lors-des-diverses-activit\u00e9s-de-production",
    defaults={
        'title': "R\u00e9investir le vocabulaire acquis lors des diverses activit\u00e9s de production",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9investir le vocabulaire acquis lors des diverses activit\u00e9s de production</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Explorer différents instruments de musique, des objets sonores, les trier, les catégoriser (type de timbres et durée du son...)
competence195, created = Page.objects.get_or_create(
    slug="explorer-diff\u00e9rents-instruments-de-musique-des-objets-sonores-les-trier-les-cat\u00e9goriser-type-de-timbres-et-dur\u00e9e-du-son...",
    defaults={
        'title': "Explorer diff\u00e9rents instruments de musique, des objets sonores, les trier, les cat\u00e9goriser (type de timbres et dur\u00e9e du son...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Explorer diff\u00e9rents instruments de musique, des objets sonores, les trier, les cat\u00e9goriser (type de timbres et dur\u00e9e du son...)</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Explorer son corps au travers de percussions corporelles
competence196, created = Page.objects.get_or_create(
    slug="explorer-son-corps-au-travers-de-percussions-corporelles",
    defaults={
        'title': "Explorer son corps au travers de percussions corporelles",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Explorer son corps au travers de percussions corporelles</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Faire le lien entre le geste et le son, le maîtriser en vue de produire un son attendu
competence197, created = Page.objects.get_or_create(
    slug="faire-le-lien-entre-le-geste-et-le-son-le-ma\u00eetriser-en-vue-de-produire-un-son-attendu",
    defaults={
        'title': "Faire le lien entre le geste et le son, le ma\u00eetriser en vue de produire un son attendu",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Faire le lien entre le geste et le son, le ma\u00eetriser en vue de produire un son attendu</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : S'exprimer sur sa production et sur celles de ses pairs
competence198, created = Page.objects.get_or_create(
    slug="sexprimer-sur-sa-production-et-sur-celles-de-ses-pairs-3",
    defaults={
        'title': "S'exprimer sur sa production et sur celles de ses pairs",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'exprimer sur sa production et sur celles de ses pairs</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Développer un vocabulaire musical des actions liées au geste producteur ou caractérisant les principes sonores
competence199, created = Page.objects.get_or_create(
    slug="d\u00e9velopper-un-vocabulaire-musical-des-actions-li\u00e9es-au-geste-producteur-ou-caract\u00e9risant-les-principes-sonores",
    defaults={
        'title': "D\u00e9velopper un vocabulaire musical des actions li\u00e9es au geste producteur ou caract\u00e9risant les principes sonores",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9velopper un vocabulaire musical des actions li\u00e9es au geste producteur ou caract\u00e9risant les principes sonores</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Univers sonores",
    }
)

# Compétence : Proposer des solutions dans des situations de projet, de création, de résolution de problèmes, avec son corps, sa voix ou des objets sonores
competence200, created = Page.objects.get_or_create(
    slug="proposer-des-solutions-dans-des-situations-de-projet-de-cr\u00e9ation-de-r\u00e9solution-de-probl\u00e8mes-avec-son-corps-sa-voix-ou-des-objets-sonores-1",
    defaults={
        'title': "Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes, avec son corps, sa voix ou des objets sonores",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Proposer des solutions dans des situations de projet, de cr\u00e9ation, de r\u00e9solution de probl\u00e8mes, avec son corps, sa voix ou des objets sonores</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Oser mettre en jeu son corps avec et face aux autres : en imitant ce que fait l'enseignant, un artiste ou un pair, en inventant ou en assemblant des propositions après avoir fait un choix
competence201, created = Page.objects.get_or_create(
    slug="oser-mettre-en-jeu-son-corps-avec-et-face-aux-autres-:-en-imitant-ce-que-fait-lenseignant-un-artiste-ou-un-pair-en-inventant-ou-en-assemblant-des-propositions-apr\u00e8s-avoir-fait-un-choix",
    defaults={
        'title': "Oser mettre en jeu son corps avec et face aux autres : en imitant ce que fait l'enseignant, un artiste ou un pair, en inventant ou en assemblant des propositions apr\u00e8s avoir fait un choix",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Oser mettre en jeu son corps avec et face aux autres : en imitant ce que fait l'enseignant, un artiste ou un pair, en inventant ou en assemblant des propositions apr\u00e8s avoir fait un choix</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Occuper un espace et y évoluer
competence202, created = Page.objects.get_or_create(
    slug="occuper-un-espace-et-y-\u00e9voluer",
    defaults={
        'title': "Occuper un espace et y \u00e9voluer",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Occuper un espace et y \u00e9voluer</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Transformer ses façons usuelles d'agir et de se déplacer
competence203, created = Page.objects.get_or_create(
    slug="transformer-ses-fa\u00e7ons-usuelles-dagir-et-de-se-d\u00e9placer",
    defaults={
        'title': "Transformer ses fa\u00e7ons usuelles d'agir et de se d\u00e9placer",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Transformer ses fa\u00e7ons usuelles d'agir et de se d\u00e9placer</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : S'inscrire dans l'espace et le temps d'une production collective
competence204, created = Page.objects.get_or_create(
    slug="sinscrire-dans-lespace-et-le-temps-dune-production-collective",
    defaults={
        'title': "S'inscrire dans l'espace et le temps d'une production collective",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence S'inscrire dans l'espace et le temps d'une production collective</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Devenir un spectateur actif et attentif
competence205, created = Page.objects.get_or_create(
    slug="devenir-un-spectateur-actif-et-attentif",
    defaults={
        'title': "Devenir un spectateur actif et attentif",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Devenir un spectateur actif et attentif</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Témoigner de sa sensibilité à la portée poétique et esthétique du mouvement
competence206, created = Page.objects.get_or_create(
    slug="t\u00e9moigner-de-sa-sensibilit\u00e9-\u00e0-la-port\u00e9e-po\u00e9tique-et-esth\u00e9tique-du-mouvement",
    defaults={
        'title': "T\u00e9moigner de sa sensibilit\u00e9 \u00e0 la port\u00e9e po\u00e9tique et esth\u00e9tique du mouvement",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence T\u00e9moigner de sa sensibilit\u00e9 \u00e0 la port\u00e9e po\u00e9tique et esth\u00e9tique du mouvement</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : Exprimer intentionnellement des émotions par le visage ou par le corps
competence207, created = Page.objects.get_or_create(
    slug="exprimer-intentionnellement-des-\u00e9motions-par-le-visage-ou-par-le-corps",
    defaults={
        'title': "Exprimer intentionnellement des \u00e9motions par le visage ou par le corps",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Exprimer intentionnellement des \u00e9motions par le visage ou par le corps</p>",
        'published': True,
        'parent': domaineDiscipline3,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Le spectacle vivant",
    }
)

# Compétence : PS Comprendre qu'une quantité d'objets ne dépend ni de la nature de ces objets ni de leur organisation spatiale
competence208, created = Page.objects.get_or_create(
    slug="ps-comprendre-quune-quantit\u00e9-dobjets-ne-d\u00e9pend-ni-de-la-nature-de-ces-objets-ni-de-leur-organisation-spatiale",
    defaults={
        'title': "PS Comprendre qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de la nature de ces objets ni de leur organisation spatiale",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comprendre qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de la nature de ces objets ni de leur organisation spatiale</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Comprendre que si on ajoute un objet à une collection, le nombre qui désigne sa quantité est le suivant dans la suite orale des noms des nombres
competence209, created = Page.objects.get_or_create(
    slug="ps-comprendre-que-si-on-ajoute-un-objet-\u00e0-une-collection-le-nombre-qui-d\u00e9signe-sa-quantit\u00e9-est-le-suivant-dans-la-suite-orale-des-noms-des-nombres",
    defaults={
        'title': "PS Comprendre que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comprendre que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Comprendre que dans la suite orale des noms des nombres, chaque nombre s'obtient en ajoutant un au nombre précédent
competence210, created = Page.objects.get_or_create(
    slug="ps-comprendre-que-dans-la-suite-orale-des-noms-des-nombres-chaque-nombre-sobtient-en-ajoutant-un-au-nombre-pr\u00e9c\u00e9dent",
    defaults={
        'title': "PS Comprendre que dans la suite orale des noms des nombres, chaque nombre s'obtient en ajoutant un au nombre pr\u00e9c\u00e9dent",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comprendre que dans la suite orale des noms des nombres, chaque nombre s'obtient en ajoutant un au nombre pr\u00e9c\u00e9dent</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Dénombrer une collection d'objets (jusqu'à trois, voire quatre)
competence211, created = Page.objects.get_or_create(
    slug="ps-d\u00e9nombrer-une-collection-dobjets-jusqu\u00e0-trois-voire-quatre",
    defaults={
        'title': "PS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 trois, voire quatre)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 trois, voire quatre)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Constituer une collection (jusqu'à trois, voire quatre objets) d'un cardinal donné
competence212, created = Page.objects.get_or_create(
    slug="ps-constituer-une-collection-jusqu\u00e0-trois-voire-quatre-objets-dun-cardinal-donn\u00e9",
    defaults={
        'title': "PS Constituer une collection (jusqu'\u00e0 trois, voire quatre objets) d'un cardinal donn\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Constituer une collection (jusqu'\u00e0 trois, voire quatre objets) d'un cardinal donn\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Comparer des quantités
competence213, created = Page.objects.get_or_create(
    slug="ps-comparer-des-quantit\u00e9s",
    defaults={
        'title': "PS Comparer des quantit\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comparer des quantit\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Composer et décomposer des nombres (deux, trois, voire quatre)
competence214, created = Page.objects.get_or_create(
    slug="ps-composer-et-d\u00e9composer-des-nombres-deux-trois-voire-quatre",
    defaults={
        'title': "PS Composer et d\u00e9composer des nombres (deux, trois, voire quatre)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Composer et d\u00e9composer des nombres (deux, trois, voire quatre)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Manipuler et verbaliser des compositions et des décompositions de nombres
competence215, created = Page.objects.get_or_create(
    slug="ps-manipuler-et-verbaliser-des-compositions-et-des-d\u00e9compositions-de-nombres",
    defaults={
        'title': "PS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Associer une quantité, le nom d'un nombre et une écriture chiffrée
competence216, created = Page.objects.get_or_create(
    slug="ps-associer-une-quantit\u00e9-le-nom-dun-nombre-et-une-\u00e9criture-chiffr\u00e9e",
    defaults={
        'title': "PS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Connaitre la comptine numérique de un à six
competence217, created = Page.objects.get_or_create(
    slug="ps-connaitre-la-comptine-num\u00e9rique-de-un-\u00e0-six",
    defaults={
        'title': "PS Connaitre la comptine num\u00e9rique de un \u00e0 six",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Connaitre la comptine num\u00e9rique de un \u00e0 six</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Poursuivre la compréhension qu'une quantité d'objets ne dépend ni de leur nature ni de leur organisation spatiale
competence218, created = Page.objects.get_or_create(
    slug="ms-poursuivre-la-compr\u00e9hension-quune-quantit\u00e9-dobjets-ne-d\u00e9pend-ni-de-leur-nature-ni-de-leur-organisation-spatiale",
    defaults={
        'title': "MS Poursuivre la compr\u00e9hension qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de leur nature ni de leur organisation spatiale",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Poursuivre la compr\u00e9hension qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de leur nature ni de leur organisation spatiale</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Poursuivre la compréhension que si on ajoute un objet à une collection, le nombre qui désigne sa quantité est le suivant dans la suite orale des noms des nombres
competence219, created = Page.objects.get_or_create(
    slug="ms-poursuivre-la-compr\u00e9hension-que-si-on-ajoute-un-objet-\u00e0-une-collection-le-nombre-qui-d\u00e9signe-sa-quantit\u00e9-est-le-suivant-dans-la-suite-orale-des-noms-des-nombres",
    defaults={
        'title': "MS Poursuivre la compr\u00e9hension que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Poursuivre la compr\u00e9hension que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Parcourir une collection en passant une et une seule fois par chacun de ses éléments
competence220, created = Page.objects.get_or_create(
    slug="ms-parcourir-une-collection-en-passant-une-et-une-seule-fois-par-chacun-de-ses-\u00e9l\u00e9ments",
    defaults={
        'title': "MS Parcourir une collection en passant une et une seule fois par chacun de ses \u00e9l\u00e9ments",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Parcourir une collection en passant une et une seule fois par chacun de ses \u00e9l\u00e9ments</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Dénombrer une collection d'objets (jusqu'à six)
competence221, created = Page.objects.get_or_create(
    slug="ms-d\u00e9nombrer-une-collection-dobjets-jusqu\u00e0-six",
    defaults={
        'title': "MS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 six)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 six)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Constituer une collection d'un cardinal donné (jusqu'à six objets)
competence222, created = Page.objects.get_or_create(
    slug="ms-constituer-une-collection-dun-cardinal-donn\u00e9-jusqu\u00e0-six-objets",
    defaults={
        'title': "MS Constituer une collection d'un cardinal donn\u00e9 (jusqu'\u00e0 six objets)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Constituer une collection d'un cardinal donn\u00e9 (jusqu'\u00e0 six objets)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Comparer des quantités
competence223, created = Page.objects.get_or_create(
    slug="ms-comparer-des-quantit\u00e9s",
    defaults={
        'title': "MS Comparer des quantit\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comparer des quantit\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Composer et décomposer des nombres inférieurs ou égaux à six
competence224, created = Page.objects.get_or_create(
    slug="ms-composer-et-d\u00e9composer-des-nombres-inf\u00e9rieurs-ou-\u00e9gaux-\u00e0-six",
    defaults={
        'title': "MS Composer et d\u00e9composer des nombres inf\u00e9rieurs ou \u00e9gaux \u00e0 six",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Composer et d\u00e9composer des nombres inf\u00e9rieurs ou \u00e9gaux \u00e0 six</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Manipuler et verbaliser des compositions et des décompositions de nombres
competence225, created = Page.objects.get_or_create(
    slug="ms-manipuler-et-verbaliser-des-compositions-et-des-d\u00e9compositions-de-nombres",
    defaults={
        'title': "MS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Associer une quantité, le nom d'un nombre et une écriture chiffrée
competence226, created = Page.objects.get_or_create(
    slug="ms-associer-une-quantit\u00e9-le-nom-dun-nombre-et-une-\u00e9criture-chiffr\u00e9e",
    defaults={
        'title': "MS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Écrire en chiffres les nombres de un à six
competence227, created = Page.objects.get_or_create(
    slug="ms-\u00e9crire-en-chiffres-les-nombres-de-un-\u00e0-six",
    defaults={
        'title': "MS \u00c9crire en chiffres les nombres de un \u00e0 six",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS \u00c9crire en chiffres les nombres de un \u00e0 six</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Connaitre la comptine numérique de un à douze
competence228, created = Page.objects.get_or_create(
    slug="ms-connaitre-la-comptine-num\u00e9rique-de-un-\u00e0-douze",
    defaults={
        'title': "MS Connaitre la comptine num\u00e9rique de un \u00e0 douze",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Connaitre la comptine num\u00e9rique de un \u00e0 douze</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Poursuivre la compréhension qu'une quantité d'objets ne dépend ni de la nature de ces objets ni de leur organisation spatiale
competence229, created = Page.objects.get_or_create(
    slug="gs-poursuivre-la-compr\u00e9hension-quune-quantit\u00e9-dobjets-ne-d\u00e9pend-ni-de-la-nature-de-ces-objets-ni-de-leur-organisation-spatiale",
    defaults={
        'title': "GS Poursuivre la compr\u00e9hension qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de la nature de ces objets ni de leur organisation spatiale",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Poursuivre la compr\u00e9hension qu'une quantit\u00e9 d'objets ne d\u00e9pend ni de la nature de ces objets ni de leur organisation spatiale</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Poursuivre la compréhension que si on ajoute un objet à une collection, le nombre qui désigne sa quantité est le suivant dans la suite orale des noms des nombres
competence230, created = Page.objects.get_or_create(
    slug="gs-poursuivre-la-compr\u00e9hension-que-si-on-ajoute-un-objet-\u00e0-une-collection-le-nombre-qui-d\u00e9signe-sa-quantit\u00e9-est-le-suivant-dans-la-suite-orale-des-noms-des-nombres",
    defaults={
        'title': "GS Poursuivre la compr\u00e9hension que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Poursuivre la compr\u00e9hension que si on ajoute un objet \u00e0 une collection, le nombre qui d\u00e9signe sa quantit\u00e9 est le suivant dans la suite orale des noms des nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Poursuivre la compréhension que dans la suite orale des nombres, chaque nombre s’obtient en ajoutant un au nombre précédent.
competence231, created = Page.objects.get_or_create(
    slug="gs-poursuivre-la-compr\u00e9hension-que-dans-la-suite-orale-des-nombres-chaque-nombre-sobtient-en-ajoutant-un-au-nombre-pr\u00e9c\u00e9dent.",
    defaults={
        'title': "GS Poursuivre la compr\u00e9hension que dans la suite orale des nombres, chaque nombre s\u2019obtient en ajoutant un au nombre pr\u00e9c\u00e9dent.",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Poursuivre la compr\u00e9hension que dans la suite orale des nombres, chaque nombre s\u2019obtient en ajoutant un au nombre pr\u00e9c\u00e9dent.</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Poursuivre les stratégies de parcours d'une collection en passant une et une seule fois par chacun de ses éléments
competence232, created = Page.objects.get_or_create(
    slug="gs-poursuivre-les-strat\u00e9gies-de-parcours-dune-collection-en-passant-une-et-une-seule-fois-par-chacun-de-ses-\u00e9l\u00e9ments",
    defaults={
        'title': "GS Poursuivre les strat\u00e9gies de parcours d'une collection en passant une et une seule fois par chacun de ses \u00e9l\u00e9ments",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Poursuivre les strat\u00e9gies de parcours d'une collection en passant une et une seule fois par chacun de ses \u00e9l\u00e9ments</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Dénombrer une collection d'objets (jusqu'à dix, voire au-delà)
competence233, created = Page.objects.get_or_create(
    slug="gs-d\u00e9nombrer-une-collection-dobjets-jusqu\u00e0-dix-voire-au-del\u00e0",
    defaults={
        'title': "GS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 dix, voire au-del\u00e0)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9nombrer une collection d'objets (jusqu'\u00e0 dix, voire au-del\u00e0)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Constituer une collection d'un cardinal donné (jusqu'à dix, voire au-delà)
competence234, created = Page.objects.get_or_create(
    slug="gs-constituer-une-collection-dun-cardinal-donn\u00e9-jusqu\u00e0-dix-voire-au-del\u00e0",
    defaults={
        'title': "GS Constituer une collection d'un cardinal donn\u00e9 (jusqu'\u00e0 dix, voire au-del\u00e0)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Constituer une collection d'un cardinal donn\u00e9 (jusqu'\u00e0 dix, voire au-del\u00e0)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Comparer des quantités
competence235, created = Page.objects.get_or_create(
    slug="gs-comparer-des-quantit\u00e9s",
    defaults={
        'title': "GS Comparer des quantit\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comparer des quantit\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Comparer des quantités
competence236, created = Page.objects.get_or_create(
    slug="gs-comparer-des-quantit\u00e9s-1",
    defaults={
        'title': "GS Comparer des quantit\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comparer des quantit\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Manipuler et verbaliser des compositions et des décompositions de nombres
competence237, created = Page.objects.get_or_create(
    slug="gs-manipuler-et-verbaliser-des-compositions-et-des-d\u00e9compositions-de-nombres",
    defaults={
        'title': "GS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Manipuler et verbaliser des compositions et des d\u00e9compositions de nombres</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Surcompter (c'est-à-dire compter de un en un à partir d'un nombre donné)
competence238, created = Page.objects.get_or_create(
    slug="gs-surcompter-cest-\u00e0-dire-compter-de-un-en-un-\u00e0-partir-dun-nombre-donn\u00e9",
    defaults={
        'title': "GS Surcompter (c'est-\u00e0-dire compter de un en un \u00e0 partir d'un nombre donn\u00e9)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Surcompter (c'est-\u00e0-dire compter de un en un \u00e0 partir d'un nombre donn\u00e9)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Associer une quantité, le nom d'un nombre et une écriture chiffrée
competence239, created = Page.objects.get_or_create(
    slug="gs-associer-une-quantit\u00e9-le-nom-dun-nombre-et-une-\u00e9criture-chiffr\u00e9e",
    defaults={
        'title': "GS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Associer une quantit\u00e9, le nom d'un nombre et une \u00e9criture chiffr\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Écrire en chiffres les nombres de un à dix
competence240, created = Page.objects.get_or_create(
    slug="gs-\u00e9crire-en-chiffres-les-nombres-de-un-\u00e0-dix",
    defaults={
        'title': "GS \u00c9crire en chiffres les nombres de un \u00e0 dix",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS \u00c9crire en chiffres les nombres de un \u00e0 dix</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Connaitre et utiliser la comptine numérique jusqu'à trente
competence241, created = Page.objects.get_or_create(
    slug="gs-connaitre-et-utiliser-la-comptine-num\u00e9rique-jusqu\u00e0-trente",
    defaults={
        'title': "GS Connaitre et utiliser la comptine num\u00e9rique jusqu'\u00e0 trente",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Connaitre et utiliser la comptine num\u00e9rique jusqu'\u00e0 trente</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Comprendre la notion de rang
competence242, created = Page.objects.get_or_create(
    slug="ms-comprendre-la-notion-de-rang",
    defaults={
        'title': "MS Comprendre la notion de rang",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comprendre la notion de rang</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Déterminer l'effet d'un déplacement sur une position
competence243, created = Page.objects.get_or_create(
    slug="ms-d\u00e9terminer-leffet-dun-d\u00e9placement-sur-une-position",
    defaults={
        'title': "MS D\u00e9terminer l'effet d'un d\u00e9placement sur une position",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS D\u00e9terminer l'effet d'un d\u00e9placement sur une position</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : MS Se familiariser avec le début de la bande numérique
competence244, created = Page.objects.get_or_create(
    slug="ms-se-familiariser-avec-le-d\u00e9but-de-la-bande-num\u00e9rique",
    defaults={
        'title': "MS Se familiariser avec le d\u00e9but de la bande num\u00e9rique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Se familiariser avec le d\u00e9but de la bande num\u00e9rique</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Comprendre la notion de rang d'un objet
competence245, created = Page.objects.get_or_create(
    slug="gs-comprendre-la-notion-de-rang-dun-objet",
    defaults={
        'title': "GS Comprendre la notion de rang d'un objet",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre la notion de rang d'un objet</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Déterminer l'effet d'un déplacement sur une position
competence246, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-leffet-dun-d\u00e9placement-sur-une-position",
    defaults={
        'title': "GS D\u00e9terminer l'effet d'un d\u00e9placement sur une position",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer l'effet d'un d\u00e9placement sur une position</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Comprendre le lien entre un ajout et un avancement et celui entre un retrait et un recul
competence247, created = Page.objects.get_or_create(
    slug="gs-comprendre-le-lien-entre-un-ajout-et-un-avancement-et-celui-entre-un-retrait-et-un-recul",
    defaults={
        'title': "GS Comprendre le lien entre un ajout et un avancement et celui entre un retrait et un recul",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comprendre le lien entre un ajout et un avancement et celui entre un retrait et un recul</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : GS Construire la bande numérique jusqu'à dix
competence248, created = Page.objects.get_or_create(
    slug="gs-construire-la-bande-num\u00e9rique-jusqu\u00e0-dix",
    defaults={
        'title': "GS Construire la bande num\u00e9rique jusqu'\u00e0 dix",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Construire la bande num\u00e9rique jusqu'\u00e0 dix</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir les nombres",
        'competence_generale': "Exprimer une quantit\u00e9 par un nombre",
    }
)

# Compétence : PS Recherche du tout ou d'une partie dans un problème de parties-tout
competence249, created = Page.objects.get_or_create(
    slug="ps-recherche-du-tout-ou-dune-partie-dans-un-probl\u00e8me-de-parties-tout",
    defaults={
        'title': "PS Recherche du tout ou d'une partie dans un probl\u00e8me de parties-tout",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Recherche du tout ou d'une partie dans un probl\u00e8me de parties-tout</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : MS Rechercher le tout ou une partie dans un problème de parties-tout
competence250, created = Page.objects.get_or_create(
    slug="ms-rechercher-le-tout-ou-une-partie-dans-un-probl\u00e8me-de-parties-tout",
    defaults={
        'title': "MS Rechercher le tout ou une partie dans un probl\u00e8me de parties-tout",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Rechercher le tout ou une partie dans un probl\u00e8me de parties-tout</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : MS Trouver une position finale à partir d'une position initiale et d'un déplacement sur une piste du type du jeu de l'oie ou sur la bande numérique
competence251, created = Page.objects.get_or_create(
    slug="ms-trouver-une-position-finale-\u00e0-partir-dune-position-initiale-et-dun-d\u00e9placement-sur-une-piste-du-type-du-jeu-de-loie-ou-sur-la-bande-num\u00e9rique",
    defaults={
        'title': "MS Trouver une position finale \u00e0 partir d'une position initiale et d'un d\u00e9placement sur une piste du type du jeu de l'oie ou sur la bande num\u00e9rique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Trouver une position finale \u00e0 partir d'une position initiale et d'un d\u00e9placement sur une piste du type du jeu de l'oie ou sur la bande num\u00e9rique</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : MS Rechercher le tout dans un problème de groupements
competence252, created = Page.objects.get_or_create(
    slug="ms-rechercher-le-tout-dans-un-probl\u00e8me-de-groupements",
    defaults={
        'title': "MS Rechercher le tout dans un probl\u00e8me de groupements",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Rechercher le tout dans un probl\u00e8me de groupements</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : MS Rechercher la valeur d'une part dans un problème de partage équitable
competence253, created = Page.objects.get_or_create(
    slug="ms-rechercher-la-valeur-dune-part-dans-un-probl\u00e8me-de-partage-\u00e9quitable",
    defaults={
        'title': "MS Rechercher la valeur d'une part dans un probl\u00e8me de partage \u00e9quitable",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Rechercher la valeur d'une part dans un probl\u00e8me de partage \u00e9quitable</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer le tout ou une partie dans un problème de parties-tout (d'abord deux parties, puis éventuellement trois)
competence254, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-le-tout-ou-une-partie-dans-un-probl\u00e8me-de-parties-tout-dabord-deux-parties-puis-\u00e9ventuellement-trois",
    defaults={
        'title': "GS D\u00e9terminer le tout ou une partie dans un probl\u00e8me de parties-tout (d'abord deux parties, puis \u00e9ventuellement trois)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer le tout ou une partie dans un probl\u00e8me de parties-tout (d'abord deux parties, puis \u00e9ventuellement trois)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer la quantité d'objets ayant été ajoutée ou retirée à une collection à partir de ses quantités initiale et finale
competence255, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-la-quantit\u00e9-dobjets-ayant-\u00e9t\u00e9-ajout\u00e9e-ou-retir\u00e9e-\u00e0-une-collection-\u00e0-partir-de-ses-quantit\u00e9s-initiale-et-finale",
    defaults={
        'title': "GS D\u00e9terminer la quantit\u00e9 d'objets ayant \u00e9t\u00e9 ajout\u00e9e ou retir\u00e9e \u00e0 une collection \u00e0 partir de ses quantit\u00e9s initiale et finale",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer la quantit\u00e9 d'objets ayant \u00e9t\u00e9 ajout\u00e9e ou retir\u00e9e \u00e0 une collection \u00e0 partir de ses quantit\u00e9s initiale et finale</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer la position finale (respectivement initiale) à partir de la position initiale (respectivement finale) et d'un déplacement sur une piste du type du jeu de l'oie ou sur la bande numérique
competence256, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-la-position-finale-respectivement-initiale-\u00e0-partir-de-la-position-initiale-respectivement-finale-et-dun-d\u00e9placement-sur-une-piste-du-type-du-jeu-de-loie-ou-sur-la-bande-num\u00e9rique",
    defaults={
        'title': "GS D\u00e9terminer la position finale (respectivement initiale) \u00e0 partir de la position initiale (respectivement finale) et d'un d\u00e9placement sur une piste du type du jeu de l'oie ou sur la bande num\u00e9rique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer la position finale (respectivement initiale) \u00e0 partir de la position initiale (respectivement finale) et d'un d\u00e9placement sur une piste du type du jeu de l'oie ou sur la bande num\u00e9rique</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer le cardinal d'une collection à partir de celui d'une autre collection et de l'écart entre les deux
competence257, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-le-cardinal-dune-collection-\u00e0-partir-de-celui-dune-autre-collection-et-de-l\u00e9cart-entre-les-deux",
    defaults={
        'title': "GS D\u00e9terminer le cardinal d'une collection \u00e0 partir de celui d'une autre collection et de l'\u00e9cart entre les deux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer le cardinal d'une collection \u00e0 partir de celui d'une autre collection et de l'\u00e9cart entre les deux</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer le tout dans un problème de groupement d'objets
competence258, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-le-tout-dans-un-probl\u00e8me-de-groupement-dobjets",
    defaults={
        'title': "GS D\u00e9terminer le tout dans un probl\u00e8me de groupement d'objets",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer le tout dans un probl\u00e8me de groupement d'objets</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : GS Déterminer la valeur d'une part dans un problème de partage équitable (avec éventuellement un reste)
competence259, created = Page.objects.get_or_create(
    slug="gs-d\u00e9terminer-la-valeur-dune-part-dans-un-probl\u00e8me-de-partage-\u00e9quitable-avec-\u00e9ventuellement-un-reste",
    defaults={
        'title': "GS D\u00e9terminer la valeur d'une part dans un probl\u00e8me de partage \u00e9quitable (avec \u00e9ventuellement un reste)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9terminer la valeur d'une part dans un probl\u00e8me de partage \u00e9quitable (avec \u00e9ventuellement un reste)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser les nombres pour r\u00e9soudre des probl\u00e8mes",
        'competence_generale': "R\u00e9soudre des probl\u00e8mes arithm\u00e9tiques",
    }
)

# Compétence : PS Reconnaitre, trier et classer des objets selon leur forme
competence260, created = Page.objects.get_or_create(
    slug="ps-reconnaitre-trier-et-classer-des-objets-selon-leur-forme",
    defaults={
        'title': "PS Reconnaitre, trier et classer des objets selon leur forme",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reconnaitre, trier et classer des objets selon leur forme</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : PS Percevoir l'invariance de la forme d'un objet par rapport aux déplacements qu'il peut subir
competence261, created = Page.objects.get_or_create(
    slug="ps-percevoir-linvariance-de-la-forme-dun-objet-par-rapport-aux-d\u00e9placements-quil-peut-subir",
    defaults={
        'title': "PS Percevoir l'invariance de la forme d'un objet par rapport aux d\u00e9placements qu'il peut subir",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Percevoir l'invariance de la forme d'un objet par rapport aux d\u00e9placements qu'il peut subir</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : PS Reproduire des assemblages de solides ou de formes planes
competence262, created = Page.objects.get_or_create(
    slug="ps-reproduire-des-assemblages-de-solides-ou-de-formes-planes",
    defaults={
        'title': "PS Reproduire des assemblages de solides ou de formes planes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reproduire des assemblages de solides ou de formes planes</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : MS Reconnaitre et classer des solides (cube, boule, pyramide à base carrée, cylindre) et des formes géométriques planes (triangle, carré, disque)
competence263, created = Page.objects.get_or_create(
    slug="ms-reconnaitre-et-classer-des-solides-cube-boule-pyramide-\u00e0-base-carr\u00e9e-cylindre-et-des-formes-g\u00e9om\u00e9triques-planes-triangle-carr\u00e9-disque",
    defaults={
        'title': "MS Reconnaitre et classer des solides (cube, boule, pyramide \u00e0 base carr\u00e9e, cylindre) et des formes g\u00e9om\u00e9triques planes (triangle, carr\u00e9, disque)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Reconnaitre et classer des solides (cube, boule, pyramide \u00e0 base carr\u00e9e, cylindre) et des formes g\u00e9om\u00e9triques planes (triangle, carr\u00e9, disque)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : MS Reproduire des assemblages de solides ou de formes planes (au maximum cinq)
competence264, created = Page.objects.get_or_create(
    slug="ms-reproduire-des-assemblages-de-solides-ou-de-formes-planes-au-maximum-cinq",
    defaults={
        'title': "MS Reproduire des assemblages de solides ou de formes planes (au maximum cinq)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Reproduire des assemblages de solides ou de formes planes (au maximum cinq)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : GS Décrire quelques solides simples: cube, pavé, boule, pyramides à base carrée ou triangulaire, cylindre, cône
competence265, created = Page.objects.get_or_create(
    slug="gs-d\u00e9crire-quelques-solides-simples:-cube-pav\u00e9-boule-pyramides-\u00e0-base-carr\u00e9e-ou-triangulaire-cylindre-c\u00f4ne",
    defaults={
        'title': "GS D\u00e9crire quelques solides simples: cube, pav\u00e9, boule, pyramides \u00e0 base carr\u00e9e ou triangulaire, cylindre, c\u00f4ne",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9crire quelques solides simples: cube, pav\u00e9, boule, pyramides \u00e0 base carr\u00e9e ou triangulaire, cylindre, c\u00f4ne</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : GS Reconnaitre, trier et classer des formes géométriques planes, indépendamment d'autres critères comme la couleur, la taille, l'orientation
competence266, created = Page.objects.get_or_create(
    slug="gs-reconnaitre-trier-et-classer-des-formes-g\u00e9om\u00e9triques-planes-ind\u00e9pendamment-dautres-crit\u00e8res-comme-la-couleur-la-taille-lorientation",
    defaults={
        'title': "GS Reconnaitre, trier et classer des formes g\u00e9om\u00e9triques planes, ind\u00e9pendamment d'autres crit\u00e8res comme la couleur, la taille, l'orientation",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Reconnaitre, trier et classer des formes g\u00e9om\u00e9triques planes, ind\u00e9pendamment d'autres crit\u00e8res comme la couleur, la taille, l'orientation</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : GS Décrire et nommer quelques figures géométriques simples: carré, rectangle, triangle, disque
competence267, created = Page.objects.get_or_create(
    slug="gs-d\u00e9crire-et-nommer-quelques-figures-g\u00e9om\u00e9triques-simples:-carr\u00e9-rectangle-triangle-disque",
    defaults={
        'title': "GS D\u00e9crire et nommer quelques figures g\u00e9om\u00e9triques simples: carr\u00e9, rectangle, triangle, disque",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS D\u00e9crire et nommer quelques figures g\u00e9om\u00e9triques simples: carr\u00e9, rectangle, triangle, disque</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : GS Reproduire des assemblages de solides (au maximum cinq) et de formes planes (au maximum huit)
competence268, created = Page.objects.get_or_create(
    slug="gs-reproduire-des-assemblages-de-solides-au-maximum-cinq-et-de-formes-planes-au-maximum-huit",
    defaults={
        'title': "GS Reproduire des assemblages de solides (au maximum cinq) et de formes planes (au maximum huit)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Reproduire des assemblages de solides (au maximum cinq) et de formes planes (au maximum huit)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : GS S'approprier la règle comme outil de tracé
competence269, created = Page.objects.get_or_create(
    slug="gs-sapproprier-la-r\u00e8gle-comme-outil-de-trac\u00e9",
    defaults={
        'title': "GS S'approprier la r\u00e8gle comme outil de trac\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS S'approprier la r\u00e8gle comme outil de trac\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer les solides et les formes planes",
        'competence_generale': "Explorer les formes et l'espace",
    }
)

# Compétence : PS Reconnaitre un objet de même longueur qu'un objet donné
competence270, created = Page.objects.get_or_create(
    slug="ps-reconnaitre-un-objet-de-m\u00eame-longueur-quun-objet-donn\u00e9",
    defaults={
        'title': "PS Reconnaitre un objet de m\u00eame longueur qu'un objet donn\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reconnaitre un objet de m\u00eame longueur qu'un objet donn\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : PS Comparer des objets selon leur longueur
competence271, created = Page.objects.get_or_create(
    slug="ps-comparer-des-objets-selon-leur-longueur",
    defaults={
        'title': "PS Comparer des objets selon leur longueur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Comparer des objets selon leur longueur</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : MS Comparer directement des longueurs d'objets rectilignes et verbaliser le résultat
competence272, created = Page.objects.get_or_create(
    slug="ms-comparer-directement-des-longueurs-dobjets-rectilignes-et-verbaliser-le-r\u00e9sultat",
    defaults={
        'title': "MS Comparer directement des longueurs d'objets rectilignes et verbaliser le r\u00e9sultat",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comparer directement des longueurs d'objets rectilignes et verbaliser le r\u00e9sultat</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : MS Classer des objets rectilignes selon leur longueur
competence273, created = Page.objects.get_or_create(
    slug="ms-classer-des-objets-rectilignes-selon-leur-longueur",
    defaults={
        'title': "MS Classer des objets rectilignes selon leur longueur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Classer des objets rectilignes selon leur longueur</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : MS Ordonner des objets rectilignes selon leur longueur et verbaliser le résultat
competence274, created = Page.objects.get_or_create(
    slug="ms-ordonner-des-objets-rectilignes-selon-leur-longueur-et-verbaliser-le-r\u00e9sultat",
    defaults={
        'title': "MS Ordonner des objets rectilignes selon leur longueur et verbaliser le r\u00e9sultat",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Ordonner des objets rectilignes selon leur longueur et verbaliser le r\u00e9sultat</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : GS Comparer indirectement des longueurs d'objets rectilignes
competence275, created = Page.objects.get_or_create(
    slug="gs-comparer-indirectement-des-longueurs-dobjets-rectilignes",
    defaults={
        'title': "GS Comparer indirectement des longueurs d'objets rectilignes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Comparer indirectement des longueurs d'objets rectilignes</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : GS Ordonner des objets rectilignes selon leur longueur (au maximum cinq)
competence276, created = Page.objects.get_or_create(
    slug="gs-ordonner-des-objets-rectilignes-selon-leur-longueur-au-maximum-cinq",
    defaults={
        'title': "GS Ordonner des objets rectilignes selon leur longueur (au maximum cinq)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Ordonner des objets rectilignes selon leur longueur (au maximum cinq)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : GS Produire un objet rectiligne de même longueur qu'un objet donné
competence277, created = Page.objects.get_or_create(
    slug="gs-produire-un-objet-rectiligne-de-m\u00eame-longueur-quun-objet-donn\u00e9",
    defaults={
        'title': "GS Produire un objet rectiligne de m\u00eame longueur qu'un objet donn\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Produire un objet rectiligne de m\u00eame longueur qu'un objet donn\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La longueur",
    }
)

# Compétence : MS Comparer les masses de deux objets
competence278, created = Page.objects.get_or_create(
    slug="ms-comparer-les-masses-de-deux-objets",
    defaults={
        'title': "MS Comparer les masses de deux objets",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Comparer les masses de deux objets</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La masse",
    }
)

# Compétence : GS Ordonner les masses de trois objets. Verbaliser les résultats
competence279, created = Page.objects.get_or_create(
    slug="gs-ordonner-les-masses-de-trois-objets.-verbaliser-les-r\u00e9sultats",
    defaults={
        'title': "GS Ordonner les masses de trois objets. Verbaliser les r\u00e9sultats",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Ordonner les masses de trois objets. Verbaliser les r\u00e9sultats</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La masse",
    }
)

# Compétence : GS Reconnaitre l'égalité de deux masses et verbaliser le résultat
competence280, created = Page.objects.get_or_create(
    slug="gs-reconnaitre-l\u00e9galit\u00e9-de-deux-masses-et-verbaliser-le-r\u00e9sultat",
    defaults={
        'title': "GS Reconnaitre l'\u00e9galit\u00e9 de deux masses et verbaliser le r\u00e9sultat",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Reconnaitre l'\u00e9galit\u00e9 de deux masses et verbaliser le r\u00e9sultat</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer des grandeurs : la longueur, la masse",
        'competence_generale': "La masse",
    }
)

# Compétence : PS Mémoriser un motif répétitif très simple
competence281, created = Page.objects.get_or_create(
    slug="ps-m\u00e9moriser-un-motif-r\u00e9p\u00e9titif-tr\u00e8s-simple",
    defaults={
        'title': "PS M\u00e9moriser un motif r\u00e9p\u00e9titif tr\u00e8s simple",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS M\u00e9moriser un motif r\u00e9p\u00e9titif tr\u00e8s simple</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : PS Reproduire un motif répétitif à l'identique
competence282, created = Page.objects.get_or_create(
    slug="ps-reproduire-un-motif-r\u00e9p\u00e9titif-\u00e0-lidentique",
    defaults={
        'title': "PS Reproduire un motif r\u00e9p\u00e9titif \u00e0 l'identique",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence PS Reproduire un motif r\u00e9p\u00e9titif \u00e0 l'identique</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : MS Mémoriser un motif répétitif simple
competence283, created = Page.objects.get_or_create(
    slug="ms-m\u00e9moriser-un-motif-r\u00e9p\u00e9titif-simple",
    defaults={
        'title': "MS M\u00e9moriser un motif r\u00e9p\u00e9titif simple",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS M\u00e9moriser un motif r\u00e9p\u00e9titif simple</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : MS Reconnaitre un motif répétitif à ses régularités
competence284, created = Page.objects.get_or_create(
    slug="ms-reconnaitre-un-motif-r\u00e9p\u00e9titif-\u00e0-ses-r\u00e9gularit\u00e9s",
    defaults={
        'title': "MS Reconnaitre un motif r\u00e9p\u00e9titif \u00e0 ses r\u00e9gularit\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Reconnaitre un motif r\u00e9p\u00e9titif \u00e0 ses r\u00e9gularit\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : MS Décrire oralement des motifs répétitifs simples de différentes natures, sans nécessairement recourir au vocabulaire spécialisé
competence285, created = Page.objects.get_or_create(
    slug="ms-d\u00e9crire-oralement-des-motifs-r\u00e9p\u00e9titifs-simples-de-diff\u00e9rentes-natures-sans-n\u00e9cessairement-recourir-au-vocabulaire-sp\u00e9cialis\u00e9",
    defaults={
        'title': "MS D\u00e9crire oralement des motifs r\u00e9p\u00e9titifs simples de diff\u00e9rentes natures, sans n\u00e9cessairement recourir au vocabulaire sp\u00e9cialis\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS D\u00e9crire oralement des motifs r\u00e9p\u00e9titifs simples de diff\u00e9rentes natures, sans n\u00e9cessairement recourir au vocabulaire sp\u00e9cialis\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : MS Prolonger l'amorce d'un motif répétitif et verbaliser la règle de prolongement utilisée
competence286, created = Page.objects.get_or_create(
    slug="ms-prolonger-lamorce-dun-motif-r\u00e9p\u00e9titif-et-verbaliser-la-r\u00e8gle-de-prolongement-utilis\u00e9e",
    defaults={
        'title': "MS Prolonger l'amorce d'un motif r\u00e9p\u00e9titif et verbaliser la r\u00e8gle de prolongement utilis\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence MS Prolonger l'amorce d'un motif r\u00e9p\u00e9titif et verbaliser la r\u00e8gle de prolongement utilis\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : GS Repérer et décrire oralement la structure d'un motif évolutif (par exemple relevant de la transcription formelle ABAABBAAABBB)
competence287, created = Page.objects.get_or_create(
    slug="gs-rep\u00e9rer-et-d\u00e9crire-oralement-la-structure-dun-motif-\u00e9volutif-par-exemple-relevant-de-la-transcription-formelle-abaabbaaabbb",
    defaults={
        'title': "GS Rep\u00e9rer et d\u00e9crire oralement la structure d'un motif \u00e9volutif (par exemple relevant de la transcription formelle ABAABBAAABBB)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Rep\u00e9rer et d\u00e9crire oralement la structure d'un motif \u00e9volutif (par exemple relevant de la transcription formelle ABAABBAAABBB)</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : GS Identifier la structure d'un motif répétitif ou évolutif indépendamment des éléments physiques qui le composent
competence288, created = Page.objects.get_or_create(
    slug="gs-identifier-la-structure-dun-motif-r\u00e9p\u00e9titif-ou-\u00e9volutif-ind\u00e9pendamment-des-\u00e9l\u00e9ments-physiques-qui-le-composent",
    defaults={
        'title': "GS Identifier la structure d'un motif r\u00e9p\u00e9titif ou \u00e9volutif ind\u00e9pendamment des \u00e9l\u00e9ments physiques qui le composent",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Identifier la structure d'un motif r\u00e9p\u00e9titif ou \u00e9volutif ind\u00e9pendamment des \u00e9l\u00e9ments physiques qui le composent</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : GS Créer des motifs de différentes natures
competence289, created = Page.objects.get_or_create(
    slug="gs-cr\u00e9er-des-motifs-de-diff\u00e9rentes-natures",
    defaults={
        'title': "GS Cr\u00e9er des motifs de diff\u00e9rentes natures",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence GS Cr\u00e9er des motifs de diff\u00e9rentes natures</p>",
        'published': True,
        'parent': domaineDiscipline4,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se familiariser avec les motifs organis\u00e9s",
        'competence_generale': "Motifs et algorithmes",
    }
)

# Compétence : Situer des événements vécus les uns par rapport aux autres et en les repérant dans la journée, la semaine, le mois ou une saison
competence290, created = Page.objects.get_or_create(
    slug="situer-des-\u00e9v\u00e9nements-v\u00e9cus-les-uns-par-rapport-aux-autres-et-en-les-rep\u00e9rant-dans-la-journ\u00e9e-la-semaine-le-mois-ou-une-saison",
    defaults={
        'title': "Situer des \u00e9v\u00e9nements v\u00e9cus les uns par rapport aux autres et en les rep\u00e9rant dans la journ\u00e9e, la semaine, le mois ou une saison",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer des \u00e9v\u00e9nements v\u00e9cus les uns par rapport aux autres et en les rep\u00e9rant dans la journ\u00e9e, la semaine, le mois ou une saison</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Ordonner une suite de photographies ou d'images, pour rendre compte d'une situation vécue ou d'un récit fictif entendu, en marquant de manière exacte succession et simultanéité
competence291, created = Page.objects.get_or_create(
    slug="ordonner-une-suite-de-photographies-ou-dimages-pour-rendre-compte-dune-situation-v\u00e9cue-ou-dun-r\u00e9cit-fictif-entendu-en-marquant-de-mani\u00e8re-exacte-succession-et-simultan\u00e9it\u00e9",
    defaults={
        'title': "Ordonner une suite de photographies ou d'images, pour rendre compte d'une situation v\u00e9cue ou d'un r\u00e9cit fictif entendu, en marquant de mani\u00e8re exacte succession et simultan\u00e9it\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Ordonner une suite de photographies ou d'images, pour rendre compte d'une situation v\u00e9cue ou d'un r\u00e9cit fictif entendu, en marquant de mani\u00e8re exacte succession et simultan\u00e9it\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser des marqueurs temporels adaptés (puis, pendant, avant, après...) dans des récits, descriptions ou explications
competence292, created = Page.objects.get_or_create(
    slug="utiliser-des-marqueurs-temporels-adapt\u00e9s-puis-pendant-avant-apr\u00e8s...-dans-des-r\u00e9cits-descriptions-ou-explications",
    defaults={
        'title': "Utiliser des marqueurs temporels adapt\u00e9s (puis, pendant, avant, apr\u00e8s...) dans des r\u00e9cits, descriptions ou explications",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des marqueurs temporels adapt\u00e9s (puis, pendant, avant, apr\u00e8s...) dans des r\u00e9cits, descriptions ou explications</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Associer les moments de la journée avec des activités régulières de la classe
competence293, created = Page.objects.get_or_create(
    slug="associer-les-moments-de-la-journ\u00e9e-avec-des-activit\u00e9s-r\u00e9guli\u00e8res-de-la-classe",
    defaults={
        'title': "Associer les moments de la journ\u00e9e avec des activit\u00e9s r\u00e9guli\u00e8res de la classe",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Associer les moments de la journ\u00e9e avec des activit\u00e9s r\u00e9guli\u00e8res de la classe</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Dire ce qu'on a fait avant et après une activité
competence294, created = Page.objects.get_or_create(
    slug="dire-ce-quon-a-fait-avant-et-apr\u00e8s-une-activit\u00e9",
    defaults={
        'title': "Dire ce qu'on a fait avant et apr\u00e8s une activit\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Dire ce qu'on a fait avant et apr\u00e8s une activit\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Se repérer dans les premiers éléments chronologiques sur un temps court (la demi-journée) et utiliser correctement les mots « matin », « apres-midi », « soir »
competence295, created = Page.objects.get_or_create(
    slug="se-rep\u00e9rer-dans-les-premiers-\u00e9l\u00e9ments-chronologiques-sur-un-temps-court-la-demi-journ\u00e9e-et-utiliser-correctement-les-mots-\u00ab-matin-\u00bb-\u00ab-apres-midi-\u00bb-\u00ab-soir-\u00bb",
    defaults={
        'title': "Se rep\u00e9rer dans les premiers \u00e9l\u00e9ments chronologiques sur un temps court (la demi-journ\u00e9e) et utiliser correctement les mots \u00ab matin \u00bb, \u00ab apres-midi \u00bb, \u00ab soir \u00bb",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se rep\u00e9rer dans les premiers \u00e9l\u00e9ments chronologiques sur un temps court (la demi-journ\u00e9e) et utiliser correctement les mots \u00ab matin \u00bb, \u00ab apres-midi \u00bb, \u00ab soir \u00bb</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser correctement les mots « jour » et « mois »
competence296, created = Page.objects.get_or_create(
    slug="utiliser-correctement-les-mots-\u00ab-jour-\u00bb-et-\u00ab-mois-\u00bb",
    defaults={
        'title': "Utiliser correctement les mots \u00ab jour \u00bb et \u00ab mois \u00bb",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser correctement les mots \u00ab jour \u00bb et \u00ab mois \u00bb</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Connaitre la suite des noms des jours, de la semaine et savoir dire « celui qui précède » et « celui qui suit » un jour donné
competence297, created = Page.objects.get_or_create(
    slug="connaitre-la-suite-des-noms-des-jours-de-la-semaine-et-savoir-dire-\u00ab-celui-qui-pr\u00e9c\u00e8de-\u00bb-et-\u00ab-celui-qui-suit-\u00bb-un-jour-donn\u00e9",
    defaults={
        'title': "Connaitre la suite des noms des jours, de la semaine et savoir dire \u00ab celui qui pr\u00e9c\u00e8de \u00bb et \u00ab celui qui suit \u00bb un jour donn\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Connaitre la suite des noms des jours, de la semaine et savoir dire \u00ab celui qui pr\u00e9c\u00e8de \u00bb et \u00ab celui qui suit \u00bb un jour donn\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser des marques temporelles dans le langage, notamment pour situer ce dont on parle par rapport au moment où l'on parle (hier, aujourd'hui, demain, plus tard...)
competence298, created = Page.objects.get_or_create(
    slug="utiliser-des-marques-temporelles-dans-le-langage-notamment-pour-situer-ce-dont-on-parle-par-rapport-au-moment-o\u00f9-lon-parle-hier-aujourdhui-demain-plus-tard...",
    defaults={
        'title': "Utiliser des marques temporelles dans le langage, notamment pour situer ce dont on parle par rapport au moment o\u00f9 l'on parle (hier, aujourd'hui, demain, plus tard...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des marques temporelles dans le langage, notamment pour situer ce dont on parle par rapport au moment o\u00f9 l'on parle (hier, aujourd'hui, demain, plus tard...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser les formes des verbes adaptées (présent, futur, passé) même si la conjugaison exacte fait encore défaut
competence299, created = Page.objects.get_or_create(
    slug="utiliser-les-formes-des-verbes-adapt\u00e9es-pr\u00e9sent-futur-pass\u00e9-m\u00eame-si-la-conjugaison-exacte-fait-encore-d\u00e9faut",
    defaults={
        'title': "Utiliser les formes des verbes adapt\u00e9es (pr\u00e9sent, futur, pass\u00e9) m\u00eame si la conjugaison exacte fait encore d\u00e9faut",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser les formes des verbes adapt\u00e9es (pr\u00e9sent, futur, pass\u00e9) m\u00eame si la conjugaison exacte fait encore d\u00e9faut</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser le vocabulaire adapté pour traduire une relation entre deux faits, deux moments : avant, après, pendant, bien avant, bien après, en même temps, plus tôt que, plus tard, dans deux jours
competence300, created = Page.objects.get_or_create(
    slug="utiliser-le-vocabulaire-adapt\u00e9-pour-traduire-une-relation-entre-deux-faits-deux-moments-:-avant-apr\u00e8s-pendant-bien-avant-bien-apr\u00e8s-en-m\u00eame-temps-plus-t\u00f4t-que-plus-tard-dans-deux-jours",
    defaults={
        'title': "Utiliser le vocabulaire adapt\u00e9 pour traduire une relation entre deux faits, deux moments : avant, apr\u00e8s, pendant, bien avant, bien apr\u00e8s, en m\u00eame temps, plus t\u00f4t que, plus tard, dans deux jours",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser le vocabulaire adapt\u00e9 pour traduire une relation entre deux faits, deux moments : avant, apr\u00e8s, pendant, bien avant, bien apr\u00e8s, en m\u00eame temps, plus t\u00f4t que, plus tard, dans deux jours</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Utiliser divers outils (comptage régulier, sablier, horloge...) pour comparer des durées
competence301, created = Page.objects.get_or_create(
    slug="utiliser-divers-outils-comptage-r\u00e9gulier-sablier-horloge...-pour-comparer-des-dur\u00e9es",
    defaults={
        'title': "Utiliser divers outils (comptage r\u00e9gulier, sablier, horloge...) pour comparer des dur\u00e9es",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser divers outils (comptage r\u00e9gulier, sablier, horloge...) pour comparer des dur\u00e9es</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "Se rep\u00e9rer dans le temps",
    }
)

# Compétence : Situer des objets par rapport à soi, entre eux, par rapport à des objets repères
competence302, created = Page.objects.get_or_create(
    slug="situer-des-objets-par-rapport-\u00e0-soi-entre-eux-par-rapport-\u00e0-des-objets-rep\u00e8res",
    defaults={
        'title': "Situer des objets par rapport \u00e0 soi, entre eux, par rapport \u00e0 des objets rep\u00e8res",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer des objets par rapport \u00e0 soi, entre eux, par rapport \u00e0 des objets rep\u00e8res</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Se situer par rapport à d'autres, par rapport à des objets repères
competence303, created = Page.objects.get_or_create(
    slug="se-situer-par-rapport-\u00e0-dautres-par-rapport-\u00e0-des-objets-rep\u00e8res",
    defaults={
        'title': "Se situer par rapport \u00e0 d'autres, par rapport \u00e0 des objets rep\u00e8res",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se situer par rapport \u00e0 d'autres, par rapport \u00e0 des objets rep\u00e8res</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Dans un environnement bien connu, réaliser un trajet, un parcours à partir de sa représentation (dessin ou codage)
competence304, created = Page.objects.get_or_create(
    slug="dans-un-environnement-bien-connu-r\u00e9aliser-un-trajet-un-parcours-\u00e0-partir-de-sa-repr\u00e9sentation-dessin-ou-codage",
    defaults={
        'title': "Dans un environnement bien connu, r\u00e9aliser un trajet, un parcours \u00e0 partir de sa repr\u00e9sentation (dessin ou codage)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Dans un environnement bien connu, r\u00e9aliser un trajet, un parcours \u00e0 partir de sa repr\u00e9sentation (dessin ou codage)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Élaborer des premiers essais de représentation plane, communicables (construction d'un code commun)
competence305, created = Page.objects.get_or_create(
    slug="\u00e9laborer-des-premiers-essais-de-repr\u00e9sentation-plane-communicables-construction-dun-code-commun",
    defaults={
        'title': "\u00c9laborer des premiers essais de repr\u00e9sentation plane, communicables (construction d'un code commun)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9laborer des premiers essais de repr\u00e9sentation plane, communicables (construction d'un code commun)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Orienter et utiliser correctement une feuille de papier, un livre ou autre support d'écrit, en fonction de consignes, d'un but ou d'un projet précis
competence306, created = Page.objects.get_or_create(
    slug="orienter-et-utiliser-correctement-une-feuille-de-papier-un-livre-ou-autre-support-d\u00e9crit-en-fonction-de-consignes-dun-but-ou-dun-projet-pr\u00e9cis",
    defaults={
        'title': "Orienter et utiliser correctement une feuille de papier, un livre ou autre support d'\u00e9crit, en fonction de consignes, d'un but ou d'un projet pr\u00e9cis",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Orienter et utiliser correctement une feuille de papier, un livre ou autre support d'\u00e9crit, en fonction de consignes, d'un but ou d'un projet pr\u00e9cis</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Utiliser des marqueurs spatiaux adaptés (devant, derrière, droite, gauche, dessus, dessous...) dans des récits, des descriptions ou explications
competence307, created = Page.objects.get_or_create(
    slug="utiliser-des-marqueurs-spatiaux-adapt\u00e9s-devant-derri\u00e8re-droite-gauche-dessus-dessous...-dans-des-r\u00e9cits-des-descriptions-ou-explications",
    defaults={
        'title': "Utiliser des marqueurs spatiaux adapt\u00e9s (devant, derri\u00e8re, droite, gauche, dessus, dessous...) dans des r\u00e9cits, des descriptions ou explications",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des marqueurs spatiaux adapt\u00e9s (devant, derri\u00e8re, droite, gauche, dessus, dessous...) dans des r\u00e9cits, des descriptions ou explications</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Se repérer dans l'espace de la classe
competence308, created = Page.objects.get_or_create(
    slug="se-rep\u00e9rer-dans-lespace-de-la-classe",
    defaults={
        'title': "Se rep\u00e9rer dans l'espace de la classe",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se rep\u00e9rer dans l'espace de la classe</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Identifier les espaces communs de l'école (salle de classe, salle de jeux, couloirs, dortoir, salle de restauration, cour...) et s'y déplacer en autonomie
competence309, created = Page.objects.get_or_create(
    slug="identifier-les-espaces-communs-de-l\u00e9cole-salle-de-classe-salle-de-jeux-couloirs-dortoir-salle-de-restauration-cour...-et-sy-d\u00e9placer-en-autonomie",
    defaults={
        'title': "Identifier les espaces communs de l'\u00e9cole (salle de classe, salle de jeux, couloirs, dortoir, salle de restauration, cour...) et s'y d\u00e9placer en autonomie",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Identifier les espaces communs de l'\u00e9cole (salle de classe, salle de jeux, couloirs, dortoir, salle de restauration, cour...) et s'y d\u00e9placer en autonomie</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Utiliser des locutions spatiales en particulier celles fondées sur des oppositions : sur/sous, dedans/dehors, à côté de/loin de...
competence310, created = Page.objects.get_or_create(
    slug="utiliser-des-locutions-spatiales-en-particulier-celles-fond\u00e9es-sur-des-oppositions-:-sur/sous-dedans/dehors-\u00e0-c\u00f4t\u00e9-de/loin-de...",
    defaults={
        'title': "Utiliser des locutions spatiales en particulier celles fond\u00e9es sur des oppositions : sur/sous, dedans/dehors, \u00e0 c\u00f4t\u00e9 de/loin de...",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des locutions spatiales en particulier celles fond\u00e9es sur des oppositions : sur/sous, dedans/dehors, \u00e0 c\u00f4t\u00e9 de/loin de...</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Se déplacer en respectant des règles ou consignes 
competence311, created = Page.objects.get_or_create(
    slug="se-d\u00e9placer-en-respectant-des-r\u00e8gles-ou-consignes-",
    defaults={
        'title': "Se d\u00e9placer en respectant des r\u00e8gles ou consignes ",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se d\u00e9placer en respectant des r\u00e8gles ou consignes </p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Reconnaître et utiliser des représentations d'espaces connus
competence312, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-et-utiliser-des-repr\u00e9sentations-despaces-connus",
    defaults={
        'title': "Reconna\u00eetre et utiliser des repr\u00e9sentations d'espaces connus",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre et utiliser des repr\u00e9sentations d'espaces connus</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Coder des déplacements, des emplacements sur un « plan » connu ou une photographie d'un espace vécu (salle de classe, salle de jeux, cour de récréation...)
competence313, created = Page.objects.get_or_create(
    slug="coder-des-d\u00e9placements-des-emplacements-sur-un-\u00ab-plan-\u00bb-connu-ou-une-photographie-dun-espace-v\u00e9cu-salle-de-classe-salle-de-jeux-cour-de-r\u00e9cr\u00e9ation...",
    defaults={
        'title': "Coder des d\u00e9placements, des emplacements sur un \u00ab plan \u00bb connu ou une photographie d'un espace v\u00e9cu (salle de classe, salle de jeux, cour de r\u00e9cr\u00e9ation...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Coder des d\u00e9placements, des emplacements sur un \u00ab plan \u00bb connu ou une photographie d'un espace v\u00e9cu (salle de classe, salle de jeux, cour de r\u00e9cr\u00e9ation...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Repérer sa droite et sa gauche
competence314, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-sa-droite-et-sa-gauche",
    defaults={
        'title': "Rep\u00e9rer sa droite et sa gauche",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer sa droite et sa gauche</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Décrire des positions dans l'espace : positions par rapport à soi ; positions relatives de deux objets ou deux personnes l'un(e) par rapport à l'autre
competence315, created = Page.objects.get_or_create(
    slug="d\u00e9crire-des-positions-dans-lespace-:-positions-par-rapport-\u00e0-soi-;-positions-relatives-de-deux-objets-ou-deux-personnes-lune-par-rapport-\u00e0-lautre",
    defaults={
        'title': "D\u00e9crire des positions dans l'espace : positions par rapport \u00e0 soi ; positions relatives de deux objets ou deux personnes l'un(e) par rapport \u00e0 l'autre",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9crire des positions dans l'espace : positions par rapport \u00e0 soi ; positions relatives de deux objets ou deux personnes l'un(e) par rapport \u00e0 l'autre</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Se repérer dans une page et utiliser le vocabulaire usuel (haut et bas notamment, gauche et droite)
competence316, created = Page.objects.get_or_create(
    slug="se-rep\u00e9rer-dans-une-page-et-utiliser-le-vocabulaire-usuel-haut-et-bas-notamment-gauche-et-droite",
    defaults={
        'title': "Se rep\u00e9rer dans une page et utiliser le vocabulaire usuel (haut et bas notamment, gauche et droite)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se rep\u00e9rer dans une page et utiliser le vocabulaire usuel (haut et bas notamment, gauche et droite)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Parler d'espaces lointains (hors du vécu) en employant un vocabulaire adapté pour décrire des habitats, des monuments, des paysages (en fonction de ce qui a été travaillé en classe)
competence317, created = Page.objects.get_or_create(
    slug="parler-despaces-lointains-hors-du-v\u00e9cu-en-employant-un-vocabulaire-adapt\u00e9-pour-d\u00e9crire-des-habitats-des-monuments-des-paysages-en-fonction-de-ce-qui-a-\u00e9t\u00e9-travaill\u00e9-en-classe",
    defaults={
        'title': "Parler d'espaces lointains (hors du v\u00e9cu) en employant un vocabulaire adapt\u00e9 pour d\u00e9crire des habitats, des monuments, des paysages (en fonction de ce qui a \u00e9t\u00e9 travaill\u00e9 en classe)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Parler d'espaces lointains (hors du v\u00e9cu) en employant un vocabulaire adapt\u00e9 pour d\u00e9crire des habitats, des monuments, des paysages (en fonction de ce qui a \u00e9t\u00e9 travaill\u00e9 en classe)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Se rep\u00e9rer dans le temps et l'espace",
        'competence_generale': "se rep\u00e9rer dans l'espace",
    }
)

# Compétence : Reconnaître et décrire les principales étapes du développement d'un animal ou d'un végétal, dans une situation d'observation du réel ou sur des images fixes ou animées
competence318, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-et-d\u00e9crire-les-principales-\u00e9tapes-du-d\u00e9veloppement-dun-animal-ou-dun-v\u00e9g\u00e9tal-dans-une-situation-dobservation-du-r\u00e9el-ou-sur-des-images-fixes-ou-anim\u00e9es",
    defaults={
        'title': "Reconna\u00eetre et d\u00e9crire les principales \u00e9tapes du d\u00e9veloppement d'un animal ou d'un v\u00e9g\u00e9tal, dans une situation d'observation du r\u00e9el ou sur des images fixes ou anim\u00e9es",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre et d\u00e9crire les principales \u00e9tapes du d\u00e9veloppement d'un animal ou d'un v\u00e9g\u00e9tal, dans une situation d'observation du r\u00e9el ou sur des images fixes ou anim\u00e9es</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Connaître les besoins essentiels de quelques animaux et végétaux
competence319, created = Page.objects.get_or_create(
    slug="conna\u00eetre-les-besoins-essentiels-de-quelques-animaux-et-v\u00e9g\u00e9taux",
    defaults={
        'title': "Conna\u00eetre les besoins essentiels de quelques animaux et v\u00e9g\u00e9taux",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Conna\u00eetre les besoins essentiels de quelques animaux et v\u00e9g\u00e9taux</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Situer et nommer les différentes parties du corps humain, sur soi ou sur une représentation
competence320, created = Page.objects.get_or_create(
    slug="situer-et-nommer-les-diff\u00e9rentes-parties-du-corps-humain-sur-soi-ou-sur-une-repr\u00e9sentation",
    defaults={
        'title': "Situer et nommer les diff\u00e9rentes parties du corps humain, sur soi ou sur une repr\u00e9sentation",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer et nommer les diff\u00e9rentes parties du corps humain, sur soi ou sur une repr\u00e9sentation</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Connaître et mettre en oeuvre quelques règles d'hygiène corporelle et d'une vie saine
competence321, created = Page.objects.get_or_create(
    slug="conna\u00eetre-et-mettre-en-oeuvre-quelques-r\u00e8gles-dhygi\u00e8ne-corporelle-et-dune-vie-saine",
    defaults={
        'title': "Conna\u00eetre et mettre en oeuvre quelques r\u00e8gles d'hygi\u00e8ne corporelle et d'une vie saine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Conna\u00eetre et mettre en oeuvre quelques r\u00e8gles d'hygi\u00e8ne corporelle et d'une vie saine</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Situer et nommer quelques parties du corps sur lui-même
competence322, created = Page.objects.get_or_create(
    slug="situer-et-nommer-quelques-parties-du-corps-sur-lui-m\u00eame",
    defaults={
        'title': "Situer et nommer quelques parties du corps sur lui-m\u00eame",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer et nommer quelques parties du corps sur lui-m\u00eame</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Situer et nommer quelques parties du visage et du corps sur lui-même et sur une représentation
competence323, created = Page.objects.get_or_create(
    slug="situer-et-nommer-quelques-parties-du-visage-et-du-corps-sur-lui-m\u00eame-et-sur-une-repr\u00e9sentation",
    defaults={
        'title': "Situer et nommer quelques parties du visage et du corps sur lui-m\u00eame et sur une repr\u00e9sentation",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer et nommer quelques parties du visage et du corps sur lui-m\u00eame et sur une repr\u00e9sentation</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Lister les parties du corps nécessaires à une première représentation d'un être humain (tête, corps, bras, jambes, pieds, mains)
competence324, created = Page.objects.get_or_create(
    slug="lister-les-parties-du-corps-n\u00e9cessaires-\u00e0-une-premi\u00e8re-repr\u00e9sentation-dun-\u00eatre-humain-t\u00eate-corps-bras-jambes-pieds-mains",
    defaults={
        'title': "Lister les parties du corps n\u00e9cessaires \u00e0 une premi\u00e8re repr\u00e9sentation d'un \u00eatre humain (t\u00eate, corps, bras, jambes, pieds, mains)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Lister les parties du corps n\u00e9cessaires \u00e0 une premi\u00e8re repr\u00e9sentation d'un \u00eatre humain (t\u00eate, corps, bras, jambes, pieds, mains)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Situer et nommer les parties du visage, du corps et quelques articulations (cheville, genou, coude, hanche, épaule, nuque) sur lui-même ou sur une représentation
competence325, created = Page.objects.get_or_create(
    slug="situer-et-nommer-les-parties-du-visage-du-corps-et-quelques-articulations-cheville-genou-coude-hanche-\u00e9paule-nuque-sur-lui-m\u00eame-ou-sur-une-repr\u00e9sentation",
    defaults={
        'title': "Situer et nommer les parties du visage, du corps et quelques articulations (cheville, genou, coude, hanche, \u00e9paule, nuque) sur lui-m\u00eame ou sur une repr\u00e9sentation",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Situer et nommer les parties du visage, du corps et quelques articulations (cheville, genou, coude, hanche, \u00e9paule, nuque) sur lui-m\u00eame ou sur une repr\u00e9sentation</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Évoluer de traces éparses à un dessin plus représentatif du corps humain
competence326, created = Page.objects.get_or_create(
    slug="\u00e9voluer-de-traces-\u00e9parses-\u00e0-un-dessin-plus-repr\u00e9sentatif-du-corps-humain",
    defaults={
        'title': "\u00c9voluer de traces \u00e9parses \u00e0 un dessin plus repr\u00e9sentatif du corps humain",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9voluer de traces \u00e9parses \u00e0 un dessin plus repr\u00e9sentatif du corps humain</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Dessiner un être humain complet (pieds, jambes, bassin, torse, bras, tête avec éventuellement quelques détails sur le visage)
competence327, created = Page.objects.get_or_create(
    slug="dessiner-un-\u00eatre-humain-complet-pieds-jambes-bassin-torse-bras-t\u00eate-avec-\u00e9ventuellement-quelques-d\u00e9tails-sur-le-visage",
    defaults={
        'title': "Dessiner un \u00eatre humain complet (pieds, jambes, bassin, torse, bras, t\u00eate avec \u00e9ventuellement quelques d\u00e9tails sur le visage)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Dessiner un \u00eatre humain complet (pieds, jambes, bassin, torse, bras, t\u00eate avec \u00e9ventuellement quelques d\u00e9tails sur le visage)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Dessiner un être humain complet avec des parties de son visage. Les membres commencent à prendre de l'épaisseur
competence328, created = Page.objects.get_or_create(
    slug="dessiner-un-\u00eatre-humain-complet-avec-des-parties-de-son-visage.-les-membres-commencent-\u00e0-prendre-de-l\u00e9paisseur",
    defaults={
        'title': "Dessiner un \u00eatre humain complet avec des parties de son visage. Les membres commencent \u00e0 prendre de l'\u00e9paisseur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Dessiner un \u00eatre humain complet avec des parties de son visage. Les membres commencent \u00e0 prendre de l'\u00e9paisseur</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Se représenter avec un corps articulé en mouvement (en train de courir ou de sauter...)
competence329, created = Page.objects.get_or_create(
    slug="se-repr\u00e9senter-avec-un-corps-articul\u00e9-en-mouvement-en-train-de-courir-ou-de-sauter...",
    defaults={
        'title': "Se repr\u00e9senter avec un corps articul\u00e9 en mouvement (en train de courir ou de sauter...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Se repr\u00e9senter avec un corps articul\u00e9 en mouvement (en train de courir ou de sauter...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Respecter les règles d'hygiène après invitation, avec l'aide de l'adulte
competence330, created = Page.objects.get_or_create(
    slug="respecter-les-r\u00e8gles-dhygi\u00e8ne-apr\u00e8s-invitation-avec-laide-de-ladulte",
    defaults={
        'title': "Respecter les r\u00e8gles d'hygi\u00e8ne apr\u00e8s invitation, avec l'aide de l'adulte",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Respecter les r\u00e8gles d'hygi\u00e8ne apr\u00e8s invitation, avec l'aide de l'adulte</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Réaliser les premiers gestes qui garantissent son hygiène corporelle
competence331, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-les-premiers-gestes-qui-garantissent-son-hygi\u00e8ne-corporelle",
    defaults={
        'title': "R\u00e9aliser les premiers gestes qui garantissent son hygi\u00e8ne corporelle",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser les premiers gestes qui garantissent son hygi\u00e8ne corporelle</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Demander de l'aide pour répondre à ses besoins physiologiques
competence332, created = Page.objects.get_or_create(
    slug="demander-de-laide-pour-r\u00e9pondre-\u00e0-ses-besoins-physiologiques",
    defaults={
        'title': "Demander de l'aide pour r\u00e9pondre \u00e0 ses besoins physiologiques",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Demander de l'aide pour r\u00e9pondre \u00e0 ses besoins physiologiques</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Gérer ses besoins physiologiques de façon autonome
competence333, created = Page.objects.get_or_create(
    slug="g\u00e9rer-ses-besoins-physiologiques-de-fa\u00e7on-autonome",
    defaults={
        'title': "G\u00e9rer ses besoins physiologiques de fa\u00e7on autonome",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence G\u00e9rer ses besoins physiologiques de fa\u00e7on autonome</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Réguler et anticiper ses besoins physiologiques pour ne pas arrêter les activités prévues
competence334, created = Page.objects.get_or_create(
    slug="r\u00e9guler-et-anticiper-ses-besoins-physiologiques-pour-ne-pas-arr\u00eater-les-activit\u00e9s-pr\u00e9vues",
    defaults={
        'title': "R\u00e9guler et anticiper ses besoins physiologiques pour ne pas arr\u00eater les activit\u00e9s pr\u00e9vues",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9guler et anticiper ses besoins physiologiques pour ne pas arr\u00eater les activit\u00e9s pr\u00e9vues</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Énoncer les règles d'hygiène corporelle et de vie saine
competence335, created = Page.objects.get_or_create(
    slug="\u00e9noncer-les-r\u00e8gles-dhygi\u00e8ne-corporelle-et-de-vie-saine",
    defaults={
        'title': "\u00c9noncer les r\u00e8gles d'hygi\u00e8ne corporelle et de vie saine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9noncer les r\u00e8gles d'hygi\u00e8ne corporelle et de vie saine</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Énoncer les règles d'hygiène corporelle et de vie saine
competence336, created = Page.objects.get_or_create(
    slug="\u00e9noncer-les-r\u00e8gles-dhygi\u00e8ne-corporelle-et-de-vie-saine-1",
    defaults={
        'title': "\u00c9noncer les r\u00e8gles d'hygi\u00e8ne corporelle et de vie saine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9noncer les r\u00e8gles d'hygi\u00e8ne corporelle et de vie saine</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Établir des premiers liens entre ce qu'il consomme et les conséquences possibles sur sa santé
competence337, created = Page.objects.get_or_create(
    slug="\u00e9tablir-des-premiers-liens-entre-ce-quil-consomme-et-les-cons\u00e9quences-possibles-sur-sa-sant\u00e9",
    defaults={
        'title': "\u00c9tablir des premiers liens entre ce qu'il consomme et les cons\u00e9quences possibles sur sa sant\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9tablir des premiers liens entre ce qu'il consomme et les cons\u00e9quences possibles sur sa sant\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Reconnaître et nommer les animaux observés en classe et participer à l'entretien des élevages en fournissant la « nourriture » nécessaire, en assurant le nettoyage
competence338, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-et-nommer-les-animaux-observ\u00e9s-en-classe-et-participer-\u00e0-lentretien-des-\u00e9levages-en-fournissant-la-\u00ab-nourriture-\u00bb-n\u00e9cessaire-en-assurant-le-nettoyage",
    defaults={
        'title': "Reconna\u00eetre et nommer les animaux observ\u00e9s en classe et participer \u00e0 l'entretien des \u00e9levages en fournissant la \u00ab nourriture \u00bb n\u00e9cessaire, en assurant le nettoyage",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre et nommer les animaux observ\u00e9s en classe et participer \u00e0 l'entretien des \u00e9levages en fournissant la \u00ab nourriture \u00bb n\u00e9cessaire, en assurant le nettoyage</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les animaux ont besoin de se nourrir et de boire pour vivre
competence339, created = Page.objects.get_or_create(
    slug="savoir-que-les-animaux-ont-besoin-de-se-nourrir-et-de-boire-pour-vivre",
    defaults={
        'title': "Savoir que les animaux ont besoin de se nourrir et de boire pour vivre",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les animaux ont besoin de se nourrir et de boire pour vivre</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les animaux ont besoin de boire et d'une nourriture adaptée à leur régime alimentaire
competence340, created = Page.objects.get_or_create(
    slug="savoir-que-les-animaux-ont-besoin-de-boire-et-dune-nourriture-adapt\u00e9e-\u00e0-leur-r\u00e9gime-alimentaire",
    defaults={
        'title': "Savoir que les animaux ont besoin de boire et d'une nourriture adapt\u00e9e \u00e0 leur r\u00e9gime alimentaire",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les animaux ont besoin de boire et d'une nourriture adapt\u00e9e \u00e0 leur r\u00e9gime alimentaire</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les animaux ont besoin de respirer, de dormir
competence341, created = Page.objects.get_or_create(
    slug="savoir-que-les-animaux-ont-besoin-de-respirer-de-dormir",
    defaults={
        'title': "Savoir que les animaux ont besoin de respirer, de dormir",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les animaux ont besoin de respirer, de dormir</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les animaux grandissent et se transforment
competence342, created = Page.objects.get_or_create(
    slug="savoir-que-les-animaux-grandissent-et-se-transforment",
    defaults={
        'title': "Savoir que les animaux grandissent et se transforment",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les animaux grandissent et se transforment</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Connaître les principales étapes du développement d'un animal (naissance, croissance, reproduction, vieillissement, mort)
competence343, created = Page.objects.get_or_create(
    slug="conna\u00eetre-les-principales-\u00e9tapes-du-d\u00e9veloppement-dun-animal-naissance-croissance-reproduction-vieillissement-mort",
    defaults={
        'title': "Conna\u00eetre les principales \u00e9tapes du d\u00e9veloppement d'un animal (naissance, croissance, reproduction, vieillissement, mort)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Conna\u00eetre les principales \u00e9tapes du d\u00e9veloppement d'un animal (naissance, croissance, reproduction, vieillissement, mort)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Observer et repérer les naissances dans les élevages
competence344, created = Page.objects.get_or_create(
    slug="observer-et-rep\u00e9rer-les-naissances-dans-les-\u00e9levages",
    defaults={
        'title': "Observer et rep\u00e9rer les naissances dans les \u00e9levages",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Observer et rep\u00e9rer les naissances dans les \u00e9levages</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir qu'en général, la reproduction animale nécessite un mâle et une femelle
competence345, created = Page.objects.get_or_create(
    slug="savoir-quen-g\u00e9n\u00e9ral-la-reproduction-animale-n\u00e9cessite-un-m\u00e2le-et-une-femelle",
    defaults={
        'title': "Savoir qu'en g\u00e9n\u00e9ral, la reproduction animale n\u00e9cessite un m\u00e2le et une femelle",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir qu'en g\u00e9n\u00e9ral, la reproduction animale n\u00e9cessite un m\u00e2le et une femelle</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Associer des modes de reproduction à des types d'animaux : Le bébé se développe dans le ventre de la femelle
competence346, created = Page.objects.get_or_create(
    slug="associer-des-modes-de-reproduction-\u00e0-des-types-danimaux-:-le-b\u00e9b\u00e9-se-d\u00e9veloppe-dans-le-ventre-de-la-femelle",
    defaults={
        'title': "Associer des modes de reproduction \u00e0 des types d'animaux : Le b\u00e9b\u00e9 se d\u00e9veloppe dans le ventre de la femelle",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Associer des modes de reproduction \u00e0 des types d'animaux : Le b\u00e9b\u00e9 se d\u00e9veloppe dans le ventre de la femelle</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Associer des modes de reproduction à des types d'animaux : Le bébé se développe dans un oeuf, à l'extérieur de la femelle
competence347, created = Page.objects.get_or_create(
    slug="associer-des-modes-de-reproduction-\u00e0-des-types-danimaux-:-le-b\u00e9b\u00e9-se-d\u00e9veloppe-dans-un-oeuf-\u00e0-lext\u00e9rieur-de-la-femelle",
    defaults={
        'title': "Associer des modes de reproduction \u00e0 des types d'animaux : Le b\u00e9b\u00e9 se d\u00e9veloppe dans un oeuf, \u00e0 l'ext\u00e9rieur de la femelle",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Associer des modes de reproduction \u00e0 des types d'animaux : Le b\u00e9b\u00e9 se d\u00e9veloppe dans un oeuf, \u00e0 l'ext\u00e9rieur de la femelle</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que chez certains animaux, les femelles peuvent avoir des bébés sans l'intervention d'un mâle
competence348, created = Page.objects.get_or_create(
    slug="savoir-que-chez-certains-animaux-les-femelles-peuvent-avoir-des-b\u00e9b\u00e9s-sans-lintervention-dun-m\u00e2le",
    defaults={
        'title': "Savoir que chez certains animaux, les femelles peuvent avoir des b\u00e9b\u00e9s sans l'intervention d'un m\u00e2le",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que chez certains animaux, les femelles peuvent avoir des b\u00e9b\u00e9s sans l'intervention d'un m\u00e2le</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Reconnaître et nommer les plantes observées en classe et participer à l'entretien des plantations en fournissant l'arrosage et l'entretien nécessaires
competence349, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-et-nommer-les-plantes-observ\u00e9es-en-classe-et-participer-\u00e0-lentretien-des-plantations-en-fournissant-larrosage-et-lentretien-n\u00e9cessaires",
    defaults={
        'title': "Reconna\u00eetre et nommer les plantes observ\u00e9es en classe et participer \u00e0 l'entretien des plantations en fournissant l'arrosage et l'entretien n\u00e9cessaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre et nommer les plantes observ\u00e9es en classe et participer \u00e0 l'entretien des plantations en fournissant l'arrosage et l'entretien n\u00e9cessaires</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Reconnaître et nommer les plantes observées en classe et participer à l'entretien des plantations en fournissant l'arrosage et l'entretien nécessaires
competence350, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-et-nommer-les-plantes-observ\u00e9es-en-classe-et-participer-\u00e0-lentretien-des-plantations-en-fournissant-larrosage-et-lentretien-n\u00e9cessaires-1",
    defaults={
        'title': "Reconna\u00eetre et nommer les plantes observ\u00e9es en classe et participer \u00e0 l'entretien des plantations en fournissant l'arrosage et l'entretien n\u00e9cessaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre et nommer les plantes observ\u00e9es en classe et participer \u00e0 l'entretien des plantations en fournissant l'arrosage et l'entretien n\u00e9cessaires</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les plantes ont des besoins : eau, lumière et nourriture pour se développer
competence351, created = Page.objects.get_or_create(
    slug="savoir-que-les-plantes-ont-des-besoins-:-eau-lumi\u00e8re-et-nourriture-pour-se-d\u00e9velopper",
    defaults={
        'title': "Savoir que les plantes ont des besoins : eau, lumi\u00e8re et nourriture pour se d\u00e9velopper",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les plantes ont des besoins : eau, lumi\u00e8re et nourriture pour se d\u00e9velopper</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Savoir que les végétaux sont vivants, que les plantes grandissent et se transforment
competence352, created = Page.objects.get_or_create(
    slug="savoir-que-les-v\u00e9g\u00e9taux-sont-vivants-que-les-plantes-grandissent-et-se-transforment",
    defaults={
        'title': "Savoir que les v\u00e9g\u00e9taux sont vivants, que les plantes grandissent et se transforment",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Savoir que les v\u00e9g\u00e9taux sont vivants, que les plantes grandissent et se transforment</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Reconnaître les principales étapes du développement d'un végétal
competence353, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-les-principales-\u00e9tapes-du-d\u00e9veloppement-dun-v\u00e9g\u00e9tal",
    defaults={
        'title': "Reconna\u00eetre les principales \u00e9tapes du d\u00e9veloppement d'un v\u00e9g\u00e9tal",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre les principales \u00e9tapes du d\u00e9veloppement d'un v\u00e9g\u00e9tal</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Établir des premiers liens entre fleur, fruit et graine
competence354, created = Page.objects.get_or_create(
    slug="\u00e9tablir-des-premiers-liens-entre-fleur-fruit-et-graine",
    defaults={
        'title': "\u00c9tablir des premiers liens entre fleur, fruit et graine",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence \u00c9tablir des premiers liens entre fleur, fruit et graine</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "D\u00e9couvrir le monde du vivant",
    }
)

# Compétence : Choisir, utiliser et savoir désigner des outils et des matériaux adaptés à une situation, à des actions techniques spécifiques (plier, couper, coller, assembler, actionner...)
competence355, created = Page.objects.get_or_create(
    slug="choisir-utiliser-et-savoir-d\u00e9signer-des-outils-et-des-mat\u00e9riaux-adapt\u00e9s-\u00e0-une-situation-\u00e0-des-actions-techniques-sp\u00e9cifiques-plier-couper-coller-assembler-actionner...",
    defaults={
        'title': "Choisir, utiliser et savoir d\u00e9signer des outils et des mat\u00e9riaux adapt\u00e9s \u00e0 une situation, \u00e0 des actions techniques sp\u00e9cifiques (plier, couper, coller, assembler, actionner...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Choisir, utiliser et savoir d\u00e9signer des outils et des mat\u00e9riaux adapt\u00e9s \u00e0 une situation, \u00e0 des actions techniques sp\u00e9cifiques (plier, couper, coller, assembler, actionner...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Identifier quelques matériaux et les différencier en grandes familles (les papiers, les cartons, les tissus, les pâtes...)
competence356, created = Page.objects.get_or_create(
    slug="identifier-quelques-mat\u00e9riaux-et-les-diff\u00e9rencier-en-grandes-familles-les-papiers-les-cartons-les-tissus-les-p\u00e2tes...",
    defaults={
        'title': "Identifier quelques mat\u00e9riaux et les diff\u00e9rencier en grandes familles (les papiers, les cartons, les tissus, les p\u00e2tes...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Identifier quelques mat\u00e9riaux et les diff\u00e9rencier en grandes familles (les papiers, les cartons, les tissus, les p\u00e2tes...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Découvrir et manipuler des matériaux existants ou fabriqués en classe (ex : pâte à sel, pâte à tarte...) 
competence357, created = Page.objects.get_or_create(
    slug="d\u00e9couvrir-et-manipuler-des-mat\u00e9riaux-existants-ou-fabriqu\u00e9s-en-classe-ex-:-p\u00e2te-\u00e0-sel-p\u00e2te-\u00e0-tarte...-",
    defaults={
        'title': "D\u00e9couvrir et manipuler des mat\u00e9riaux existants ou fabriqu\u00e9s en classe (ex : p\u00e2te \u00e0 sel, p\u00e2te \u00e0 tarte...) ",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9couvrir et manipuler des mat\u00e9riaux existants ou fabriqu\u00e9s en classe (ex : p\u00e2te \u00e0 sel, p\u00e2te \u00e0 tarte...) </p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Trier, comparer des matériaux en fonction de caractéristiques physiques accessibles par les 5 sens (couleur, forme, taille, odeur, bruit, masse, texture, dureté) ou d'autres propriétés physiques (opaque, transparent, translucide ; attiré ou non par l'aimant ; perméable, imperméable...)
competence358, created = Page.objects.get_or_create(
    slug="trier-comparer-des-mat\u00e9riaux-en-fonction-de-caract\u00e9ristiques-physiques-accessibles-par-les-5-sens-couleur-forme-taille-odeur-bruit-masse-texture-duret\u00e9-ou-dautres-propri\u00e9t\u00e9s-physiques-opaque-transparent-translucide-;-attir\u00e9-ou-non-par-laimant-;-perm\u00e9able-imperm\u00e9able...",
    defaults={
        'title': "Trier, comparer des mat\u00e9riaux en fonction de caract\u00e9ristiques physiques accessibles par les 5 sens (couleur, forme, taille, odeur, bruit, masse, texture, duret\u00e9) ou d'autres propri\u00e9t\u00e9s physiques (opaque, transparent, translucide ; attir\u00e9 ou non par l'aimant ; perm\u00e9able, imperm\u00e9able...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Trier, comparer des mat\u00e9riaux en fonction de caract\u00e9ristiques physiques accessibles par les 5 sens (couleur, forme, taille, odeur, bruit, masse, texture, duret\u00e9) ou d'autres propri\u00e9t\u00e9s physiques (opaque, transparent, translucide ; attir\u00e9 ou non par l'aimant ; perm\u00e9able, imperm\u00e9able...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Connaître d'autres propriétés physiques des matériaux (perméabilité, magnétisme, transparence...)
competence359, created = Page.objects.get_or_create(
    slug="conna\u00eetre-dautres-propri\u00e9t\u00e9s-physiques-des-mat\u00e9riaux-perm\u00e9abilit\u00e9-magn\u00e9tisme-transparence...",
    defaults={
        'title': "Conna\u00eetre d'autres propri\u00e9t\u00e9s physiques des mat\u00e9riaux (perm\u00e9abilit\u00e9, magn\u00e9tisme, transparence...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Conna\u00eetre d'autres propri\u00e9t\u00e9s physiques des mat\u00e9riaux (perm\u00e9abilit\u00e9, magn\u00e9tisme, transparence...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Classer des objets selon le matériau qui les compose (manipulation) selon une propriété commune (formes, goût, texture...), selon leurs usages
competence360, created = Page.objects.get_or_create(
    slug="classer-des-objets-selon-le-mat\u00e9riau-qui-les-compose-manipulation-selon-une-propri\u00e9t\u00e9-commune-formes-go\u00fbt-texture...-selon-leurs-usages",
    defaults={
        'title': "Classer des objets selon le mat\u00e9riau qui les compose (manipulation) selon une propri\u00e9t\u00e9 commune (formes, go\u00fbt, texture...), selon leurs usages",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Classer des objets selon le mat\u00e9riau qui les compose (manipulation) selon une propri\u00e9t\u00e9 commune (formes, go\u00fbt, texture...), selon leurs usages</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Repérer des transformations de matériaux sous l'effet de la chaleur (sécher, durcir, fondre...), de l'eau (mouiller, dissoudre...), de l'air (déplacer, gonfler...), d'actions mécaniques avec des mains (froisser, plier...) et avec des outils (découper, percer...)
competence361, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-des-transformations-de-mat\u00e9riaux-sous-leffet-de-la-chaleur-s\u00e9cher-durcir-fondre...-de-leau-mouiller-dissoudre...-de-lair-d\u00e9placer-gonfler...-dactions-m\u00e9caniques-avec-des-mains-froisser-plier...-et-avec-des-outils-d\u00e9couper-percer...",
    defaults={
        'title': "Rep\u00e9rer des transformations de mat\u00e9riaux sous l'effet de la chaleur (s\u00e9cher, durcir, fondre...), de l'eau (mouiller, dissoudre...), de l'air (d\u00e9placer, gonfler...), d'actions m\u00e9caniques avec des mains (froisser, plier...) et avec des outils (d\u00e9couper, percer...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer des transformations de mat\u00e9riaux sous l'effet de la chaleur (s\u00e9cher, durcir, fondre...), de l'eau (mouiller, dissoudre...), de l'air (d\u00e9placer, gonfler...), d'actions m\u00e9caniques avec des mains (froisser, plier...) et avec des outils (d\u00e9couper, percer...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Agir de manière raisonnée sur un matériau, choisir le bon matériau en fonction d'un besoin, d'un effet attendu, d'un projet
competence362, created = Page.objects.get_or_create(
    slug="agir-de-mani\u00e8re-raisonn\u00e9e-sur-un-mat\u00e9riau-choisir-le-bon-mat\u00e9riau-en-fonction-dun-besoin-dun-effet-attendu-dun-projet",
    defaults={
        'title': "Agir de mani\u00e8re raisonn\u00e9e sur un mat\u00e9riau, choisir le bon mat\u00e9riau en fonction d'un besoin, d'un effet attendu, d'un projet",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Agir de mani\u00e8re raisonn\u00e9e sur un mat\u00e9riau, choisir le bon mat\u00e9riau en fonction d'un besoin, d'un effet attendu, d'un projet</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Modifier une procédure si nécessaire pour l'adapter au résultat attendu
competence363, created = Page.objects.get_or_create(
    slug="modifier-une-proc\u00e9dure-si-n\u00e9cessaire-pour-ladapter-au-r\u00e9sultat-attendu",
    defaults={
        'title': "Modifier une proc\u00e9dure si n\u00e9cessaire pour l'adapter au r\u00e9sultat attendu",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Modifier une proc\u00e9dure si n\u00e9cessaire pour l'adapter au r\u00e9sultat attendu</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Prendre conscience du caractère réversible (ou non) de certaines actions
competence364, created = Page.objects.get_or_create(
    slug="prendre-conscience-du-caract\u00e8re-r\u00e9versible-ou-non-de-certaines-actions",
    defaults={
        'title': "Prendre conscience du caract\u00e8re r\u00e9versible (ou non) de certaines actions",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Prendre conscience du caract\u00e8re r\u00e9versible (ou non) de certaines actions</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Lister les actions et l'ordre de réalisation, les transformations accomplies et les outils nécessaires
competence365, created = Page.objects.get_or_create(
    slug="lister-les-actions-et-lordre-de-r\u00e9alisation-les-transformations-accomplies-et-les-outils-n\u00e9cessaires",
    defaults={
        'title': "Lister les actions et l'ordre de r\u00e9alisation, les transformations accomplies et les outils n\u00e9cessaires",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Lister les actions et l'ordre de r\u00e9alisation, les transformations accomplies et les outils n\u00e9cessaires</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Explorer la mati\u00e8re",
    }
)

# Compétence : Réaliser des constructions ; construire des maquettes simples en fonction de plans ou d'instructions de montage
competence366, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-des-constructions-;-construire-des-maquettes-simples-en-fonction-de-plans-ou-dinstructions-de-montage",
    defaults={
        'title': "R\u00e9aliser des constructions ; construire des maquettes simples en fonction de plans ou d'instructions de montage",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser des constructions ; construire des maquettes simples en fonction de plans ou d'instructions de montage</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser des montages de plus en plus complexes avec une intention repérable
competence367, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-des-montages-de-plus-en-plus-complexes-avec-une-intention-rep\u00e9rable",
    defaults={
        'title': "R\u00e9aliser des montages de plus en plus complexes avec une intention rep\u00e9rable",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser des montages de plus en plus complexes avec une intention rep\u00e9rable</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Prendre en compte les risques de l'environnement familier proche (objets et comportements dangereux, produits toxiques) 
competence368, created = Page.objects.get_or_create(
    slug="prendre-en-compte-les-risques-de-lenvironnement-familier-proche-objets-et-comportements-dangereux-produits-toxiques-",
    defaults={
        'title': "Prendre en compte les risques de l'environnement familier proche (objets et comportements dangereux, produits toxiques) ",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Prendre en compte les risques de l'environnement familier proche (objets et comportements dangereux, produits toxiques) </p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser des montages de plus en plus complexes avec une intention formulée
competence369, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-des-montages-de-plus-en-plus-complexes-avec-une-intention-formul\u00e9e",
    defaults={
        'title': "R\u00e9aliser des montages de plus en plus complexes avec une intention formul\u00e9e",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser des montages de plus en plus complexes avec une intention formul\u00e9e</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser une construction, reconstituer un objet en disposant d'un modèle de référence qu'il peut manipuler ou observer
competence370, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-une-construction-reconstituer-un-objet-en-disposant-dun-mod\u00e8le-de-r\u00e9f\u00e9rence-quil-peut-manipuler-ou-observer",
    defaults={
        'title': "R\u00e9aliser une construction, reconstituer un objet en disposant d'un mod\u00e8le de r\u00e9f\u00e9rence qu'il peut manipuler ou observer",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser une construction, reconstituer un objet en disposant d'un mod\u00e8le de r\u00e9f\u00e9rence qu'il peut manipuler ou observer</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser une construction, reconstituer un objet à partir d'un modèle représenté (photographie, dessin, schéma)
competence371, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-une-construction-reconstituer-un-objet-\u00e0-partir-dun-mod\u00e8le-repr\u00e9sent\u00e9-photographie-dessin-sch\u00e9ma",
    defaults={
        'title': "R\u00e9aliser une construction, reconstituer un objet \u00e0 partir d'un mod\u00e8le repr\u00e9sent\u00e9 (photographie, dessin, sch\u00e9ma)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser une construction, reconstituer un objet \u00e0 partir d'un mod\u00e8le repr\u00e9sent\u00e9 (photographie, dessin, sch\u00e9ma)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser une construction, reconstituer un objet à partir d'illustrations des étapes de la construction, de représentations avec différentes vues (en éclaté, en perspective, de plusieurs points de vue...)
competence372, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-une-construction-reconstituer-un-objet-\u00e0-partir-dillustrations-des-\u00e9tapes-de-la-construction-de-repr\u00e9sentations-avec-diff\u00e9rentes-vues-en-\u00e9clat\u00e9-en-perspective-de-plusieurs-points-de-vue...",
    defaults={
        'title': "R\u00e9aliser une construction, reconstituer un objet \u00e0 partir d'illustrations des \u00e9tapes de la construction, de repr\u00e9sentations avec diff\u00e9rentes vues (en \u00e9clat\u00e9, en perspective, de plusieurs points de vue...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser une construction, reconstituer un objet \u00e0 partir d'illustrations des \u00e9tapes de la construction, de repr\u00e9sentations avec diff\u00e9rentes vues (en \u00e9clat\u00e9, en perspective, de plusieurs points de vue...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Représenter par le dessin/schéma un montage qu'il a réalisé
competence373, created = Page.objects.get_or_create(
    slug="repr\u00e9senter-par-le-dessin/sch\u00e9ma-un-montage-quil-a-r\u00e9alis\u00e9",
    defaults={
        'title': "Repr\u00e9senter par le dessin/sch\u00e9ma un montage qu'il a r\u00e9alis\u00e9",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Repr\u00e9senter par le dessin/sch\u00e9ma un montage qu'il a r\u00e9alis\u00e9</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Réaliser des photographies caractéristiques des différentes étapes du montage
competence374, created = Page.objects.get_or_create(
    slug="r\u00e9aliser-des-photographies-caract\u00e9ristiques-des-diff\u00e9rentes-\u00e9tapes-du-montage",
    defaults={
        'title': "R\u00e9aliser des photographies caract\u00e9ristiques des diff\u00e9rentes \u00e9tapes du montage",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence R\u00e9aliser des photographies caract\u00e9ristiques des diff\u00e9rentes \u00e9tapes du montage</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Reconnaître les différents systèmes de fermeture des vêtements ou des chaussures (bouton, bouton-pression, fermeture éclair, lacets, bande autoagrippante...)
competence375, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-les-diff\u00e9rents-syst\u00e8mes-de-fermeture-des-v\u00eatements-ou-des-chaussures-bouton-bouton-pression-fermeture-\u00e9clair-lacets-bande-autoagrippante...",
    defaults={
        'title': "Reconna\u00eetre les diff\u00e9rents syst\u00e8mes de fermeture des v\u00eatements ou des chaussures (bouton, bouton-pression, fermeture \u00e9clair, lacets, bande autoagrippante...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre les diff\u00e9rents syst\u00e8mes de fermeture des v\u00eatements ou des chaussures (bouton, bouton-pression, fermeture \u00e9clair, lacets, bande autoagrippante...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Découvrir la fonction d'usage (boutonner, attacher, fermer, fixer...) et réaliser les gestes adaptés (utiliser efficacement une fermeture à glissière, un boutonpression, etc.)
competence376, created = Page.objects.get_or_create(
    slug="d\u00e9couvrir-la-fonction-dusage-boutonner-attacher-fermer-fixer...-et-r\u00e9aliser-les-gestes-adapt\u00e9s-utiliser-efficacement-une-fermeture-\u00e0-glissi\u00e8re-un-boutonpression-etc.",
    defaults={
        'title': "D\u00e9couvrir la fonction d'usage (boutonner, attacher, fermer, fixer...) et r\u00e9aliser les gestes adapt\u00e9s (utiliser efficacement une fermeture \u00e0 glissi\u00e8re, un boutonpression, etc.)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence D\u00e9couvrir la fonction d'usage (boutonner, attacher, fermer, fixer...) et r\u00e9aliser les gestes adapt\u00e9s (utiliser efficacement une fermeture \u00e0 glissi\u00e8re, un boutonpression, etc.)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Reconnaître, identifier et nommer quelques objets parmi une famille d'objets
competence377, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-identifier-et-nommer-quelques-objets-parmi-une-famille-dobjets",
    defaults={
        'title': "Reconna\u00eetre, identifier et nommer quelques objets parmi une famille d'objets",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre, identifier et nommer quelques objets parmi une famille d'objets</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Trier, comparer en fonction des usages
competence378, created = Page.objects.get_or_create(
    slug="trier-comparer-en-fonction-des-usages",
    defaults={
        'title': "Trier, comparer en fonction des usages",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Trier, comparer en fonction des usages</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Utiliser de manière raisonnée, choisir le bon outil en fonction d'un besoin, d'un effet attendu, d'un contexte d'utilisation
competence379, created = Page.objects.get_or_create(
    slug="utiliser-de-mani\u00e8re-raisonn\u00e9e-choisir-le-bon-outil-en-fonction-dun-besoin-dun-effet-attendu-dun-contexte-dutilisation",
    defaults={
        'title': "Utiliser de mani\u00e8re raisonn\u00e9e, choisir le bon outil en fonction d'un besoin, d'un effet attendu, d'un contexte d'utilisation",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser de mani\u00e8re raisonn\u00e9e, choisir le bon outil en fonction d'un besoin, d'un effet attendu, d'un contexte d'utilisation</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Identifier et nommer les risques liés à certaines activités ou à certains outils utilisés (chuter, se pincer, se couper, s'étouffer, s'électrocuter, se brûler...)
competence380, created = Page.objects.get_or_create(
    slug="identifier-et-nommer-les-risques-li\u00e9s-\u00e0-certaines-activit\u00e9s-ou-\u00e0-certains-outils-utilis\u00e9s-chuter-se-pincer-se-couper-s\u00e9touffer-s\u00e9lectrocuter-se-br\u00fbler...",
    defaults={
        'title': "Identifier et nommer les risques li\u00e9s \u00e0 certaines activit\u00e9s ou \u00e0 certains outils utilis\u00e9s (chuter, se pincer, se couper, s'\u00e9touffer, s'\u00e9lectrocuter, se br\u00fbler...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Identifier et nommer les risques li\u00e9s \u00e0 certaines activit\u00e9s ou \u00e0 certains outils utilis\u00e9s (chuter, se pincer, se couper, s'\u00e9touffer, s'\u00e9lectrocuter, se br\u00fbler...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Adapter et justifier son comportement en fonction des risques identifiés
competence381, created = Page.objects.get_or_create(
    slug="adapter-et-justifier-son-comportement-en-fonction-des-risques-identifi\u00e9s",
    defaults={
        'title': "Adapter et justifier son comportement en fonction des risques identifi\u00e9s",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Adapter et justifier son comportement en fonction des risques identifi\u00e9s</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Reconnaître certains produits toxiques ou dangereux et le justifier grâce aux indications visuelles présentes
competence382, created = Page.objects.get_or_create(
    slug="reconna\u00eetre-certains-produits-toxiques-ou-dangereux-et-le-justifier-gr\u00e2ce-aux-indications-visuelles-pr\u00e9sentes",
    defaults={
        'title': "Reconna\u00eetre certains produits toxiques ou dangereux et le justifier gr\u00e2ce aux indications visuelles pr\u00e9sentes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Reconna\u00eetre certains produits toxiques ou dangereux et le justifier gr\u00e2ce aux indications visuelles pr\u00e9sentes</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Alerter un adulte en cas de danger pour lui-même ou pour un camarade
competence383, created = Page.objects.get_or_create(
    slug="alerter-un-adulte-en-cas-de-danger-pour-lui-m\u00eame-ou-pour-un-camarade",
    defaults={
        'title': "Alerter un adulte en cas de danger pour lui-m\u00eame ou pour un camarade",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Alerter un adulte en cas de danger pour lui-m\u00eame ou pour un camarade</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser, fabriquer, manipuler des objets",
    }
)

# Compétence : Utiliser des objets numériques : appareil photo, tablette, ordinateur
competence384, created = Page.objects.get_or_create(
    slug="utiliser-des-objets-num\u00e9riques-:-appareil-photo-tablette-ordinateur",
    defaults={
        'title': "Utiliser des objets num\u00e9riques : appareil photo, tablette, ordinateur",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser des objets num\u00e9riques : appareil photo, tablette, ordinateur</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Agir sur une tablette numérique (allumer, éteindre, choisir une application : l'ouvrir, l'utiliser et la fermer)
competence385, created = Page.objects.get_or_create(
    slug="agir-sur-une-tablette-num\u00e9rique-allumer-\u00e9teindre-choisir-une-application-:-louvrir-lutiliser-et-la-fermer",
    defaults={
        'title': "Agir sur une tablette num\u00e9rique (allumer, \u00e9teindre, choisir une application : l'ouvrir, l'utiliser et la fermer)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Agir sur une tablette num\u00e9rique (allumer, \u00e9teindre, choisir une application : l'ouvrir, l'utiliser et la fermer)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Choisir l'outil numérique qui convient en fonction d'un besoin (photographier, filmer, enregistrer la voix, copier du texte...)
competence386, created = Page.objects.get_or_create(
    slug="choisir-loutil-num\u00e9rique-qui-convient-en-fonction-dun-besoin-photographier-filmer-enregistrer-la-voix-copier-du-texte...",
    defaults={
        'title': "Choisir l'outil num\u00e9rique qui convient en fonction d'un besoin (photographier, filmer, enregistrer la voix, copier du texte...)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Choisir l'outil num\u00e9rique qui convient en fonction d'un besoin (photographier, filmer, enregistrer la voix, copier du texte...)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Manipuler une souris d'ordinateur pour pointer un élément, cliquer sur un élément, déplacer un élément
competence387, created = Page.objects.get_or_create(
    slug="manipuler-une-souris-dordinateur-pour-pointer-un-\u00e9l\u00e9ment-cliquer-sur-un-\u00e9l\u00e9ment-d\u00e9placer-un-\u00e9l\u00e9ment",
    defaults={
        'title': "Manipuler une souris d'ordinateur pour pointer un \u00e9l\u00e9ment, cliquer sur un \u00e9l\u00e9ment, d\u00e9placer un \u00e9l\u00e9ment",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Manipuler une souris d'ordinateur pour pointer un \u00e9l\u00e9ment, cliquer sur un \u00e9l\u00e9ment, d\u00e9placer un \u00e9l\u00e9ment</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Repérer des lettres sur un clavier (ordinateur ou tablette)
competence388, created = Page.objects.get_or_create(
    slug="rep\u00e9rer-des-lettres-sur-un-clavier-ordinateur-ou-tablette",
    defaults={
        'title': "Rep\u00e9rer des lettres sur un clavier (ordinateur ou tablette)",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Rep\u00e9rer des lettres sur un clavier (ordinateur ou tablette)</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Copier, écrire à l'aide d'un clavier (ordinateur ou tablette) : son prénom, des mots, le titre d'un livre, des phrases, de courts textes
competence389, created = Page.objects.get_or_create(
    slug="copier-\u00e9crire-\u00e0-laide-dun-clavier-ordinateur-ou-tablette-:-son-pr\u00e9nom-des-mots-le-titre-dun-livre-des-phrases-de-courts-textes",
    defaults={
        'title': "Copier, \u00e9crire \u00e0 l'aide d'un clavier (ordinateur ou tablette) : son pr\u00e9nom, des mots, le titre d'un livre, des phrases, de courts textes",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Copier, \u00e9crire \u00e0 l'aide d'un clavier (ordinateur ou tablette) : son pr\u00e9nom, des mots, le titre d'un livre, des phrases, de courts textes</p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

# Compétence : Utiliser les touches de direction (haut, bas, gauche, droite) pour déplacer un personnage dans un jeu éducatif 
competence390, created = Page.objects.get_or_create(
    slug="utiliser-les-touches-de-direction-haut-bas-gauche-droite-pour-d\u00e9placer-un-personnage-dans-un-jeu-\u00e9ducatif-",
    defaults={
        'title': "Utiliser les touches de direction (haut, bas, gauche, droite) pour d\u00e9placer un personnage dans un jeu \u00e9ducatif ",
        'content': "<p>Contenu par d\u00e9faut pour la comp\u00e9tence Utiliser les touches de direction (haut, bas, gauche, droite) pour d\u00e9placer un personnage dans un jeu \u00e9ducatif </p>",
        'published': True,
        'parent': domaineDiscipline5,
        'cycle_enseignement': "cycle 1",
        'objectifs_generaux': "Utiliser des outils num\u00e9riques",
    }
)

