# 🤖 CREWAI – Système d’agents intelligents pour la recherche, l’extraction et la synthèse d’informations

## 📌 Contexte

Dans un monde où l’information en ligne est abondante et en constante évolution, il devient indispensable de disposer d’outils capables d’aider à **rechercher**, **extraire** et **synthétiser** rapidement des données pertinentes.  
Ce projet s’inscrit dans cette logique en développant une **crew CREWAI**, composée d’agents intelligents collaboratifs, chacun spécialisé dans une étape précise du traitement de l’information.

L’objectif est de construire un système autonome qui :

- recherche des articles récents sur le web,  
- extrait leur contenu utile,  
- compare ces informations à une base documentaire PDF,  
- et génère un résumé clair, structuré et directement exploitable.

---

# 🧠 Objectif du Projet

Créer une **équipe d’agents spécialisés** capable de travailler ensemble pour automatiser tout le pipeline :

1. **Recherche web** du contenu pertinent sur un sujet donné  
2. **Extraction et nettoyage** des articles trouvés  
3. **Analyse croisée** avec un document PDF de référence  
4. **Synthèse finale** sous forme de résumé structuré

Ce système permet ainsi d’accélérer la prise de décision et la rédaction de rapports.

---

# 🏗️ Architecture du Projet

Le projet s’organise autour des fichiers principaux suivants :
📦 CREWAI-Project
┣ 📜 crew.py
┣ 📜 agent.yaml
┣ 📜 task.yaml
┣ 📜 main.py
┣ 📜 .env
┗ 📁 knowledge/
┗ 📜 Energiesrenouvelables.pd
