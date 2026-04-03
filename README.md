# 🎓 Application de Gestion Universitaire

## 📌 Présentation

Cette application est un système de gestion universitaire permettant de gérer des matières, d’enregistrer des notes et de calculer automatiquement la moyenne pondérée des étudiants.

Le projet repose sur une architecture **full-stack** avec :

* un frontend en HTML/CSS/JavaScript
* un backend en Python (Flask)
* une base de données PostgreSQL

---

## 🎯 Objectifs du projet

* Mettre en place une architecture client / serveur
* Concevoir une API REST en Python (Flask)
* Interagir avec une base de données relationnelle (PostgreSQL)
* Manipuler des requêtes HTTP (GET, POST)
* Assurer la communication entre frontend et backend

---

## 🧱 Architecture du projet

```
WP1/
│
├── backend/
│   └── app.py          # API Flask
│
├── frontend/
│   ├── index.html      # Interface utilisateur
│   └── style.css       # Design
│
├── database/
│   └── schema.sql      # Structure de la base de données
```

---

## ⚙️ Technologies utilisées

* **Frontend**

  * HTML
  * CSS
  * JavaScript (Fetch API)

* **Backend**

  * Python
  * Flask
  * Flask-CORS

* **Base de données**

  * PostgreSQL
  * psycopg2

---

## 🚀 Fonctionnalités

* ➕ Ajouter une matière avec coefficient
* 📝 Ajouter une note associée à une matière
* 📊 Calculer la moyenne pondérée
* 🔗 Communication en temps réel avec une API REST

---

## 🔄 Fonctionnement global

1. L’utilisateur interagit avec l’interface (frontend)
2. Le JavaScript envoie une requête HTTP (`fetch`)
3. Le backend Flask reçoit et traite la requête
4. Les données sont enregistrées dans PostgreSQL
5. Une réponse JSON est renvoyée au frontend
6. Le résultat est affiché à l’utilisateur

---

## ▶️ Installation et exécution

### 🔹 1. Cloner le projet

```bash
git clone https://github.com/Yanis-JMD/Application-de-gestion-universitaire.git
cd Application-de-gestion-universitaire/WP1
```

---

### 🔹 2. Configurer la base de données

* Ouvrir PostgreSQL (pgAdmin)
* Créer une base nommée :

```
student_db
```

* Exécuter le fichier :

```
database/schema.sql
```

---

### 🔹 3. Lancer le backend

```bash
cd backend
pip install flask flask-cors psycopg2
python app.py
```

👉 Le serveur démarre sur :

```
http://127.0.0.1:5000
```

---

### 🔹 4. Lancer le frontend

**Option recommandée (VS Code) :**

* Installer l’extension **Live Server**
* Clic droit sur `index.html` → *Open with Live Server*

👉 Le site sera accessible via :

```
http://127.0.0.1:5500
```

---

## 📡 Endpoints API

### ➕ Ajouter une matière

```
POST /subjects
```

```json
{
  "name": "Maths",
  "coef": 3
}
```

---

### 📝 Ajouter une note

```
POST /grades
```

```json
{
  "subject_id": 1,
  "grade": 15
}
```

---

### 📊 Calculer la moyenne

```
GET /average
```

---

## 🧠 Compétences développées

* Développement web full-stack
* Conception d’API REST
* Gestion de base de données relationnelle
* Debugging (CORS, erreurs serveur, requêtes HTTP)
* Utilisation de Git et GitHub

---

## 📈 Améliorations possibles

* Authentification utilisateur (login/signup)
* Interface moderne (React, Vue.js)
* Ajout d’un dashboard avec visualisation
* Déploiement en ligne (Render, Railway, etc.)
* Gestion des utilisateurs (admin / étudiant)

---

## 👤 Auteur

**Yanis Brice ATEDZOE MBENG**
🔗 GitHub : https://github.com/Yanis-JMD

---

## 💬 Remarque

Ce projet a été réalisé dans un objectif d’apprentissage et de démonstration de compétences en développement web et en architecture logicielle.
