Stroke data project
===================

Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.


# Prétraitement des Données

## Étapes de prétraitement

- Pour la colonne `smoking status`, on a remplacé la valeur `"Unknown"` par `"Not Specified"`.
- Pour les valeurs manquantes de la colonne `bmi` :
  - On a appliqué la médiane du `bmi` par rapport au sexe et à l'âge.
  - Comme il restait encore un `bmi` manquant, on a appliqué la médiane du `bmi` par sexe.
- On passe le nom des colonnes et le contenu des colonnes en **minuscule**.

---

## Justification des choix concernant le traitement des valeurs manquantes

- Pour `smoking status`, la valeur `"Unknown"` est remplacée par `"Not Specified"` afin d’indiquer clairement que l’information est non renseignée.
- Pour `bmi`, l’imputation par médiane permet de limiter l’influence des valeurs extrêmes. Le choix du regroupement par sexe et âge assure une estimation plus cohérente.

---

## Liste des valeurs raisonnables utilisées pour détecter les valeurs aberrantes

- `age` : entre 0 et 120

---

## Justification des choix pour traiter les valeurs aberrantes

- Nous avons fait le choix de **ne pas toucher au statut de travailleurs pour les mineurs**. En effet, on ne connaît pas le pays d'origine de la donnée (donc les lois du travail).
- Nous avons aussi fait le choix de **laisser un enfant fumeur**.
