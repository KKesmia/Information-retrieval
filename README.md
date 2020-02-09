# Information-retrieval
Ce projet de TP vise à vous familiariser avec les procédures (modules) de base en recherche d&#39;information (RI) à savoir : (1) l&#39;indexation des documents, (2) la pondération des termes et (3) l&#39;appariement requête-document. Dans ce TP, on traite la collection CACM, le modèle Booléen, le modèle Vectoriel et l&#39;évaluation des formules du modèle Vectoriel, avec le langage Python.

1. **Phase indexation :**

Il existe 7 index on total, 2 index général pour tous les titres avec leurs textes, 3 index de d&#39;un fichier inversé par fréquences et 2 autres index pondérés a bases des 2 derniers FIF.

- --All titles (AT = {Num de document -\&gt; titre, …})

Fichier : All\_titles.pickle

Taille : 978 KO

Nombre d&#39;entrée : 3204

Type de structure : dictionnaire de dictionnaire sur python.

Durée d&#39;indexation de la dernière case 3.3800000000007435e-06ms

Utilité : Faciliter l&#39;affichage sur l&#39;application.

- --All textes (AR = {Num de document -\&gt; texte, …})

Fichier : All\_texts.pickle

Taille : 978 KO

Nombre d&#39;entrée : 3204

Type de structure : dictionnaire de dictionnaire sur python.

Durée d&#39;indexation de la dernière case : 4.529999999999812e-06 seconde.

Utilité : Faciliter l&#39;affichage sur l&#39;application.

- --Full Dict (FD = {Num de document -\&gt; {(Mot, fréquence), ...}, …}) :

Fichier : Full\_Dict.pickle

Taille : 882 KO

Nombre d&#39;entrée : 3204

Type de structure : dictionnaire de dictionnaire sur python.

Durée d&#39;indexation de la dernière case 4.7599999999980994e-06 seconde

Utilité : Recherche la fréquence des termes par l&#39;ID d&#39;un document.

- --Dinv1 (Dinv1 = {(Mot, Num de document) -\&gt; fréquence, …}):

Fichier : Dict\_Inv1.pickle

Taille : 1316 KO

Nombre d&#39;entrée : 67529

Type de structure : dictionnaire d&#39;entier sur python.

Durée d&#39;indexation de la dernière case 4.7599999999980994e-06 seconde.

Utilité : Faciliter l&#39;affichage sur l&#39;application.

- --Dinv2 (Dinv2 = {Mot -\&gt; [(Num de document, fréquence), ...]}) :

Fichier : Dict\_Inv2.pickle

Taille : 706 KO

Nombre d&#39;entrée : 8275

Type de structure : dictionnaire de liste sur python.

Durée d&#39;indexation de la dernière case 4.7599999999980994e-06 seconde.

Utilité : Recherche la fréquences d&#39;un terme à travers tous les documents.

- --FDpond (FDpond = {Num de document -\&gt; {(Mot, pond), ...}, …}) :

Fichier : Dict\_Inv1Pond.pickle

Taille : 1116 KO

Nombre d&#39;entrée : 3204

Type de structure : dictionnaire de liste sur python.

Durée d&#39;indexation de la dernière case 6.560000000002675e-06 seconde.

Utilité : Recherche la pondération des termes par l&#39;ID du document.

- --Dinv2pond (Dinv2pond = {Mot -\&gt; {(Num de document, pond), ...}) :

Fichier : Dict\_Inv2Pond.pickle

Taille : 1168 KO

Nombre d&#39;entrée : 8275

Type de structure : dictionnaire de liste sur python.

Durée d&#39;indexation de la dernière case 2.150000000003538e-06 seconde.

Utilité : Recherche la pondération d&#39;un terme à travers tous les documents.

Nous constatons aucun index est parfait, c&#39;est pour cela exactement nous avons utilisés autant d&#39;index que nécessaire pour gagner en temps de réponse.

La difficulté se poserai lors de la mise à jour des ces index sur tous sur l&#39;échelé massive dans le cas d&#39;un vrai moteur de recherche avec des millions de documents.

1. **Modèle booléen :**

- --Évaluation de l&#39;expression booléen :

Tous d&#39;abord, nos operateurs on les mit en majuscule et majuscule seulement, le reste de l&#39;expression peut être quoi que soit vu qu&#39;on va les transformer en minuscule (nos index sont en minuscules).

La transformation d&#39;une expression sans parenthèses se fait très normale en remplaçant les opérateurs AND par « \* », le OU avec « + » et le NOT avec « - ».

Dans le cas où il existe les parenthèses on les garde telle qu&#39;elle est.

Le reste de l&#39;expression est remplacé par leurs valeur d&#39;existence, 1 si le mot a au moins une fréquence dans un document, 0 sinon.

L&#39;évaluation se fait grâce a une fonction de python appelée « eval(expression, globals=None, locals=None) ».

Temps de réponse pour requête : &#39;NOT optimization AND system AND performance&#39; est

0.03847418000000001 seconde.

1. **Modèle Vectoriel :**

Pour ce modèle nous générons deux vecteur de la requête l&#39;un avec les pondérations de chaque mot et l&#39;autre les fréquences de chaque de ces mots et nous avons utilisé les 4 mesure de similarité :

1. -Produit interne.
2. -Coefficient de dice.
3. -Cosinus.
4. -Jaccard.

Pour l&#39;évaluation de notre modèle nous avons utilisé les deux importantes performances :

- --La précision : qui détermine la value de précision des sélectionné les documents pertinents sans inclure les non pertinents (uniquement les document pertinents).

L&#39;équation de la précision est :

précision=  (|L_q∩D_q |)/(|L_q |)


- --Le rappel : c&#39;est la valeur de la capacité de déterminer tous les documents pertinents.

L&#39;équation du rappel est :

rappel=  (|L_q∩D_q |)/(|D_q |)


 
