################################################################################################################
################################################################################################################
################################# IMPORTATION DES BIBLIOTHÈQUES  NÉCESSAIRES ###################################
################################################################################################################
################################################################################################################

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


################################################################################################################
################################################################################################################
################################# CONFIGURATION LA PAGE PRINCIPALE DE VOTRE APP ################################
################################################################################################################
################################################################################################################

st.title('Analyse de Corrélation et de Distribution')

# Charger les données depuis un lien CSV
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
data = pd.read_csv(link)
#data

# Liste des continents uniques avec une option "Tous les continents"
liste_continents = ['Tous les continents'] + list(data['continent'].unique())
# Sélection du continent via une liste déroulante
selected_continent = st.selectbox('Sélectionner un continent :', liste_continents)
# Filtrer les données en fonction du continent sélectionné ou afficher toutes les données si "Tous les continents" est sélectionné
if selected_continent == 'Tous les continents':
    donnees_filtrees = data
else:
    donnees_filtrees = data[data['continent'] == selected_continent]
# Supprimer la colonne 'continent' pour la heat map
colonnes_a_exclure = ['continent']
donnees_analyse = donnees_filtrees.drop(columns=colonnes_a_exclure)
# Heatmap de corrélation
st.write("Heatmap de corrélation pour le continent sélectionné :")
fig, ax = plt.subplots()
sns.heatmap(donnees_analyse.corr(), annot=True, cmap='coolwarm')
st.pyplot(fig)

# Widget pour choisir la variable pour le graphique de distribution
selected_distribution_column = st.selectbox("Choisissez une variable pour le graphique de distribution", data.columns)

# Affichage du graphique de distribution pour la variable sélectionnée
st.subheader(f"Distribution de {selected_distribution_column}")
plt.figure(figsize=(8, 6))
sns.histplot(data[selected_distribution_column], kde=True)
plt.xlabel(selected_distribution_column)
plt.ylabel("Fréquence")
st.pyplot(plt)

# Widget pour choisir les deux variables à comparer
selected_x_column = st.selectbox("Choisissez la première variable", data.columns, index=0)
selected_y_column = st.selectbox("Choisissez la deuxième variable", data.columns, index=1)

# Affichage du graphique de comparaison pour les deux variables sélectionnées
st.subheader(f"Comparaison entre {selected_x_column} et {selected_y_column}")
plt.figure(figsize=(8, 6))
sns.scatterplot(data, x=selected_x_column, y=selected_y_column)
plt.xlabel(selected_x_column)
plt.ylabel(selected_y_column)
st.pyplot(plt)
