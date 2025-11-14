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
# CREWAI-Project

```plaintext
CREWAI-Project
├── crew.py
├── agent.yaml
├── task.yaml
├── main.py
├── .env
└── knowledge/
    └── Energiesrenouvelables.pdf

---

## ✔️ crew.py
Définit la structure du projet via la classe `Monred` :  
- Configuration des agents  
- Définition des tâches  
- Organisation du flux de travail  
- Assignation des outils à chaque agent (SerperDevTool, ScrapeWebsiteTool, PDFSearchTool…)

## ✔️ agent.yaml
Configure chaque agent :  
- rôle  
- objectifs  
- outils  
- comportement attendu  

## ✔️ task.yaml
Décrit les tâches exécutées par la crew :  
- objectifs  
- agents responsables  
- entrées / sorties  
- workflow séquentiel  

## ✔️ main.py
Point d’entrée du projet. Contient 4 fonctions essentielles :  
- `run()` → lancer la crew avec un sujet donné  
- `train()` → entraîner la crew sur plusieurs itérations  
- `replay()` → rejouer une tâche précise  
- `test()` → évaluer la crew  

## ✔️ .env
Contient la configuration essentielle du projet :  
- `MODEL` → modèle Mistral via Ollama  
- `API_BASE` → adresse de l’API Ollama  
- `SERPER_API_KEY` → clé API pour la recherche web  
- `OPENAI_API_KEY` → clé pour les services OpenAI  


---
---
# 🤖 Agents de la Crew

### 🔍 **search_agent**
- Recherche des articles récents et pertinents  
- Utilise SerperDevTool pour effectuer la recherche web  

### 🧹 **scraper_agent**
- Extrait et nettoie le contenu textuel à partir des URLs  

### 📚 **pdf_linker_agent**
- Analyse le PDF de référence  
- Trouve les passages similaires aux articles collectés  

### 📝 **summarizer_agent**
- Produit un résumé structuré incluant :  
  - Titre  
  - Mots-clés  
  - Extraits PDF pertinents  
  - Liens vers les sources  

---

# 📋 Description des Tasks

### 🔹 **Search_task**
Recherche des articles récents et extrait les liens utiles.

### 🔹 **Scraping_task**
Récupère, nettoie et prépare le contenu textuel des articles.

### 🔹 **Pdf_linking_task**
Compare le contenu extrait avec le fichier PDF de référence pour repérer les correspondances.

### 🔹 **Summary_task**
Génère un résumé final structuré avec les éléments essentiels.

---

# 📤 Output

Le système produit un fichier contenant :  
- Un résumé clair  
- Les mots-clés  
- Les passages PDF pertinents  
- Les liens vers les sources web

---

# 👤 Réalisé par

**Salaheddine Charkati**

---


