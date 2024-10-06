# Projet Web - Gestion de Produits Alimentaires

## À propos de ce projet
Ce projet est une application web de gestion de produits alimentaires qui permet aux utilisateurs de :
- Rechercher des produits.
- Visualiser des informations nutritionnelles.
- Comparer des substituts plus sains.
- Sauvegarder des produits en favoris.

Le projet intègre des fonctionnalités de gestion d'utilisateurs, d'authentification et de couverture de code pour assurer un développement rigoureux et testé.

## Fonctionnalités principales
- **Recherche de Produits** : Permet de rechercher un produit spécifique parmi les produits disponibles.
- **Comparaison de Substituts** : Affiche les substituts pour les produits avec de meilleures valeurs nutritionnelles.
- **Gestion des Favoris** : Sauvegarde des produits en favoris pour chaque utilisateur connecté.
- **Authentification des Utilisateurs** : Connexion, création de compte, déconnexion avec gestion individuelle des favoris.

## Couverture de Code avec `Coverage.py`
### À propos de la Couverture de Code
La couverture de code est une mesure utilisée pour décrire le degré auquel le code source d'un programme est exécuté lors des tests. Elle permet de découvrir les parties du code qui ne sont pas couvertes par les tests et donc potentiellement sujettes à des erreurs.

### Installation de Coverage.py
Pour utiliser `Coverage.py`, commencez par l'installer via `pip` :

- pip install coverage
- coverage run -m pytest
- coverage report

## Défis rencontrés et solutions

### 1. Gestion des Favoris pour chaque Utilisateur
- **Problème** : Initialement, tous les utilisateurs partageaient la même liste de favoris, rendant impossible la personnalisation.
- **Solution** : Mise en place d'une relation `ForeignKey` entre le modèle `Favorite` et `User` pour créer une association unique entre chaque utilisateur et ses favoris.

### 2. Affichage du Nutri-Score dynamique
- **Problème** : Lors de l'affichage du Nutri-Score, il était difficile de mettre en surbrillance uniquement la lettre correspondante au Nutri-Score réel du produit.
- **Solution** : Utilisation d'une boucle avec condition pour comparer la lettre de la boucle à celle du Nutri-Score du produit, avec application d'une classe CSS spécifique pour mettre en valeur la lettre correspondante.

### 3. Redirection en fonction de l'état de connexion
- **Problème** : Lors de la navigation sur les pages des favoris ou de déconnexion, il était nécessaire de vérifier si l'utilisateur était connecté ou non.
- **Solution** : Ajout de conditions `user.is_authenticated` dans les templates et les vues pour adapter dynamiquement les redirections en fonction de l'état de connexion de l'utilisateur.

## Structure des Fichiers
- **`models.py`** : Définit les modèles pour les produits, les utilisateurs et les favoris.
- **`views.py`** : Contient les vues pour la recherche, la gestion des favoris, et l'affichage détaillé des produits.
- **`urls.py`** : Configure les routes de l'application pour les différentes fonctionnalités.
- **`templates/`** : Dossier contenant les templates HTML pour les différentes pages de l'application.
- **`static/`** : Fichiers CSS et JS utilisés pour le rendu visuel de l'application.

## Conseils d'utilisation
- Intégrez la couverture de code dans votre pipeline CI/CD pour assurer une surveillance continue de la qualité de vos tests.
- Ne visez pas uniquement une couverture de 100%, mais concentrez-vous sur les parties critiques de votre code pour une couverture optimale.
- Utilisez les rapports HTML pour visualiser clairement les zones non couvertes de votre application et prioriser les tests.

## Comment Contribuer
Les contributions sont les bienvenues ! Si vous trouvez un bug ou avez une suggestion d'amélioration, n'hésitez pas à soumettre une `issue` ou une `pull request` avec une description claire des changements proposés.


Merci d'avoir utilisé cette application ! 
