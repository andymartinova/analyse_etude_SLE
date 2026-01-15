# analyse_etude_SLE
# Analyse statistique des données SLE (Societas Linguistica Europaea)

Repository dédié à l'analyse quantitative des patterns d'intervention par genre lors des conférences annuelles de la SLE.

## Objectif
Étude de l'homophilie genrée dans les interventions scientifiques : corrélation négative entre taille du public et proportion d'intervenantes (Spearman ρ = -0.31, p = 0.006, N = 76 conférences).

## Contenu
- `data/sle_conferences.csv` : Données nettoyées (public_total, interv_F, prop_F_interv)
- `src/` : Scripts Python (pandas, scipy.stats) pour tests statistiques
- `notebooks/` : Exploration Jupyter (EDA, visualisations)
- `requirements.txt` : Environnement reproductible

## Résultats clés
- Femmes interviennent + dans petits publics
- Test homophilie sans panels mixtes : p = 0.0072
- Compatible Jamovi pour validation


