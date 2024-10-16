import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données des fichiers CSV
data = pd.read_csv("Data/TableauxdonnéesParcelle_modifié.csv", sep=",")
data2 = pd.read_csv("Data/BiomasseMoleculaireMicrobienne.csv", sep=",")

# Créer des DataFrames pour les deux jeux de données
tableau = pd.DataFrame(data)
tableau2 = pd.DataFrame(data2)

# Afficher les colonnes des DataFrames pour vérifier la présence de 'Parcelle'
print("Colonnes de tableau:")
print(tableau.columns.tolist())
print("\nColonnes de tableau2:")
print(tableau2.columns.tolist())

# Supprimer les colonnes indésirables du premier tableau
# (Assurez-vous que cette étape ne modifie pas 'Parcelle')
colonnes_a_supprimer = [
    "Plagiolepis_pygmaea", "Messor_groupe_ibericus", "Lasius_groupe_niger", "Monomorium_monorium", 
    "Crematogaster_scutellaris", "Proformica_nasuta", "Pheidole_pallidula", "Tetramorium_sp", 
    "Tapinoma_madeirense", "Colobopsis_truncata", "Camponotus_piceus", "Campanotus_lateralis", 
    "Messor_barbarus", "Lasius_lasioides", "Temnothorax_unifasciatus", "Tapinoma_glabrella", 
    "Linepithema_humile", "Camponotus_fallax", "Camponotus_aethiops", "Temnothorax_continentalis", 
    "Formica_cunicularia", "Solenopsis_sp", "Tapinoma_erraticum", "Tapinoma_groupe_nigerrimum", 
    "Hypoponera_eduardi", "Formica_rufibarbis", "Temnothorax_lichtensteini", "Temnothorax_recedens", 
    "Themnothorax_sp", "Species", "Nb_AppatsAnt", "Nb_Appats", "Activity"
]
tableau = tableau.drop(columns=colonnes_a_supprimer, errors='ignore')  # ignore errors if column not found

# Fusionner les deux DataFrames sur 'Parcelle' et 'code echantillon'
tableau_fusionne = pd.merge(tableau, tableau2, left_on='Parcelle', right_on='code echantillon', how='inner')

# Ajouter une colonne 'Type_Emplacement' qui indique "central" ou "périphérique"
tableau_fusionne['Type_Emplacement'] = tableau_fusionne['Emplacement'].apply(lambda x: 'central' if x == 0 else 'périphérique')

# Calculer la moyenne de Moy E1_E2 par Type d'Emplacement
moyenne_par_emplacement = tableau_fusionne.groupby('Type_Emplacement')['Moy E1_E2'].mean().reset_index()

# Visualiser les moyennes de Moy E1_E2 dans un bar plot
plt.figure(figsize=(10, 6))
sns.barplot(
    data=moyenne_par_emplacement, 
    x='Type_Emplacement', 
    y='Moy E1_E2', 
)

plt.title("Moyenne de Biomasse Moléculaire Moy E1_E2 par Emplacement")
plt.xlabel("Type d'Emplacement")
plt.ylabel("Moyenne de Moy E1_E2 (µg/g sol)")
plt.xticks(rotation=0)  # Optionnel : pour garder les étiquettes horizontales
plt.show()
