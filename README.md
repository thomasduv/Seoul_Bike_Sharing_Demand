# Seoul_Bike_Sharing_Demand
Projet réalisé par Thomas DUVAL, A5 IBO 2

### Fichiers du GitHub

SeoulBikeData.csv est le dataset.

NotebookProjet.ipynb est le code python.

xgbmodel.pickle est le modèle que l'on utilise dans l'API.

app.py et request.py correspondent à l'API.

PPT_Projet_DUVAL.ppt est la présentation.

# Introduction
Dans le cadre du cours de Python for Data Analysis, il a été demandé de travailler sur un dataset attribué afin de réaliser un travail qui entre dans le contexte de l'étude de ce dataset.
Le dataset qui m'avait été donné initialement était : https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction

Malheuresement, celui-ci n'étant pas disponible au téléchargement, et avec l'accord de Mr BENJBAUM et Mr JOUIN, j'ai sélectionné un autre dataset pour ce projet : https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand

Ainsi, il était attendu de :
- mener une étude cohérente avec le contexte du dataset
- explorer et visualiser les données,
- présenter notre pré-traîtement,
- entraîner différents modèles de prédiction et comparer les résultats obtenus,
- optimiser le modèle final
- le rendre disponible dans une API

Dans ce github nous pouvons retrouver, ce README.md qui apporte des indications et résume le projet, un PPT qui présente le projet plus au niveau de l'étude du problème et un notebook avec le code.

# Contexte
Actuellement, la location de vélos est adoptée dans plusieurs villes du monde pour faciliter les déplacements. Il est donc important de rendre cette location disponible et accessible au public au moment désiré et sans attente. 

Dans certaines villes, la mis à disposition de ces vélos peut devenir un problème majeur en raison de la haute demande. Ainsi la prédiction de la demande en vélos pour chaque heure de la journée est primordial pour satisfaire les habitants d'une ville.

C'est pourquoi ce dataset fournit des informations concernant les conditions métérologiques ainsi que le nombre de vélos loués par heure et par date sur 2017 et 2018.

Dataset : https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand

La source de nos données est à l'adresse suivante : http://data.seoul.go.kr/

Ainsi un article est consacré à ce problème, où les auteurs tente de trouver le meilleur modèle de prédiction pour cette problématique : https://www.tandfonline.com/doi/full/10.1080/22797254.2020.1725789

C'est pourquoi notre démarche rentre dans la démarche des auteurs : notre but dans cet étude est d'explorer les données et déterminer les facteurs expliquant la proportion de location, et également trouver un modèle de prédiction que l'on puisse comparer avec ceux de l'article.

# Exploration et Visualisation

On retrouve un total de 6 172 314 vélos loués au total entre le 01/12/2017 et le 30/11/2018.

Voici quelques éléments que l'on peut retenir de nos visualisations :

### BoxPlot selon la saison
<img width="633" alt="Capture d’écran 2021-01-08 à 17 34 44" src="https://user-images.githubusercontent.com/56085330/104040376-dea36200-51d7-11eb-9cea-72f639170f4e.png">

### BoxPlot selon les vacances
<img width="633" alt="Capture d’écran 2021-01-08 à 17 34 52" src="https://user-images.githubusercontent.com/56085330/104040421-e9f68d80-51d7-11eb-9367-2c0f4c3cdb95.png">

### BoxPlot selon le mois de l'année
<img width="633" alt="Capture d’écran 2021-01-08 à 17 34 58" src="https://user-images.githubusercontent.com/56085330/104040424-ea8f2400-51d7-11eb-9504-9c7b954acf9d.png">

# Pré-traitements

Les étapes de pré-traitements et de création de nouvelles variables sont expliquées dans le PPT et le notebook.

# Modèles

Les étapes de créations de modèles et de comparaison de performances sont expliquées dans le PPT et le notebook.

# Modèle choisi et Optimisation

Les étapes d'optimisation du modèle choisi sont expliquées dans le PPT et le notebook.

# Conclusion et Ouverture

Pour conclure, grâce à ce projet nous pouvons nous rendre compte de l'importance et de la valeur ajoutée d'un Data Analyst dans l'analyse et la prédiction de données.

En effet, notre dataset traitait de la location de vélos à Séoul, et notre rôle était d'explorer les données et de proposer une méthode de prédiction de la demande en location par heure chaque jour.

Grâce à notre exploration et nos visualisations, on peut se rendre compte rapidement que de nombreux features influence le nombre de locations. Ainsi on se rend compte de l'importance de prédire la demande afin de pouvoir répondre à un besoin utilisateur.

Après avoir tester comparer différents modèles, nous avons choisi de continuer avec XGBoost et d'optimiser ses hyperparamètres afin d'améliorer les performances de celui-ci.

Nous obtenons donc un modèle avec des scores de :
- MSE : 35437.49
- RMSE : 188.25
- MAE : 110.63
- R2 : 0.92

Avec ces performances, notre modèle s'inscrit totalement dans l'étude faites par les auteurs de l'article : https://www.tandfonline.com/doi/full/10.1080/22797254.2020.1725789

Leurs résultats : 

<img width="1300" alt="Capture d’écran 2021-01-08 à 13 57 08" src="https://user-images.githubusercontent.com/56085330/104040159-9b48f380-51d7-11eb-9ae4-278945d9485b.png">

En ouverture, il pourrait être intéressant de travailler avec un dataset qui recense les emplacements de vélos et ainsi pouvoir prédire la demande pour chaque station de vélos.

# API

Notre API est composé de 2 fichiers :

### app.py
Il s'agit du code de l'API, on charge notre modèle et on les exécute sur les données de la requête. A noté que pour faire fonctionner XGBoost, nous transformons les données d'entrée en dataframe.

### request.py
Il s'agit d'un code d'exemple de requête, on retrouve un tableau data avec 4 lignes pour 4 prédictions différentes. Pour tester vos propres prédictions vous pouvez changer les valeurs d'entrée comme bon vous semble.

Attention néanmoins à respecter le modèle :

['Hour','Temperature(C)','Humidity(%)','Wind speed (m/s)','Visibility (10m)','Dew point temperature(C)','Solar Radiation (MJ/m2)','Rainfall(mm)','Snowfall (cm)','Year','Month','Day','Seasons_id','Holiday_id','FunctioningDay_id','Day_of_Week_id']

Avec :
- Seasons_id qui vaut 1, 2, 3 ou 4 pour Hiver, Printemps, Ete, Automne
- Holiday_id qui vaut 1 ou 0 pour Oui ou Non
- FunctioningDay_id qui vaut 1 ou 0 pour Oui ou Non
- Day_of_week_id qui vaut 1, 2, 3, 4, 5, 6 ou 7 pour Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche

### Fonctionnement de l'API

Pour lancer l'API il suffit d'ouvrir un premier terminal et de faire la commande : python3 app.py

Ensuite, pour executer la requête il suffit d'ouvrir un second terminal et de faire la commande : python3 requete.py

Le output de cette deuxième commande sera la prédiction de la demande en vélos pour chaque ligne de data.

Exemple : 

data = [[4,-3.4,75,0.0,1982,-7.2,0.0,0.0,0.4,2017,6,12,1,0,1,1],
[20,26.9,49,2.1,2000,15.2,0.0,0.0,0.0,2018,1,9,4,0,1,2],
[13,10.8,44,2.0,935,-0.9,1.01,0.0,0.0,2018,11,19,4,0,1,1],
[23,18.8,73,0.8,291,13.8,0.0,0.0,0.0,2018,5,14,2,0,1,1]]

Réponse :
<img width="505" alt="Capture d’écran 2021-01-08 à 17 46 14" src="https://user-images.githubusercontent.com/56085330/104041500-6ccc1800-51d9-11eb-9fd5-c9c762e46e73.png">
