import pandas as pd  # Construire et manipuler le tableau de données
import numpy as np   # Générer des valeurs numériques aléatoires

# Fixer la graine aléatoire pour garantir la reproductibilité
np.random.seed(42)

# Nombre de clients fictifs à générer
n = 500

# Création du jeu de données avec les caractéristiques (features)
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    # Âge compris entre 18 et 69 ans

    "salaire": np.random.randint(1200, 8000, n),
    # Salaire mensuel simulé

    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),
    # Type d'abonnement

    "anciennete": np.random.randint(0, 15, n),
    # Ancienneté comprise entre 0 et 14 ans

    "consommation": np.random.randint(0, 100, n),
    # Score de consommation du service, entre 0 et 99
})

# Création de la variable cible (target) : churn
# Un client est considéré comme à risque si :
# - sa consommation est inférieure à 30 ;
# - son ancienneté est inférieure à 2 ans.

data["churn"] = (
    (data["consommation"] < 30)
    & (data["anciennete"] < 2)
).astype(int)  # Conversion de True/False en 1/0

# Sauvegarde du jeu de données au format CSV
# Le fichier est enregistré dans le répertoire de travail courant.
data.to_csv("churn_data.csv", index=False)

# Affichage des cinq premières lignes du tableau
print(data.head())

# Calcul et affichage du taux de churn
print(f"Taux de churn : {data['churn'].mean():.1%}")