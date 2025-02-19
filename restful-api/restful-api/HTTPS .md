# HTTP & HTTPS

## 1 : Différences entre HTTP et HTTPS

La différence principale entre HTTP et HTTPS réside dans la sécurité.

### HTTP (Hypertext Transfer Protocol)  
HTTP est un ensemble de règles régissant le transfert de fichiers (texte, images, son, vidéo, etc.) sur le Web. Lorsqu'un utilisateur ouvre un navigateur et se connecte au Web, il utilise indirectement le protocole HTTP. C'est un protocole d'application qui s'exécute au-dessus de la suite de protocoles TCP/IP.

### HTTPS (Hyper Text Transfer Protocol Secure)  
HTTPS est une extension sécurisée de HTTP. Le « S » signifie « Secure » (sécurisé), ce qui indique que les données échangées entre le navigateur et le site web sont chiffrées et protégées contre l'espionnage ou la modification.  
Pour activer HTTPS, il faut acquérir et installer un certificat SSL/TLS auprès d’une Autorité de Certification reconnue.  

#### Niveaux d’authentification des certificats HTTPS :  
- **Domain Validation (DV)** : Authentification faible  
- **Organization Validation (OV)** : Authentification forte  
- **Extended Validation (EV)** : Authentification renforcée  

---

## 2 : Structure d'une demande et d'une réponse HTTP

### Exemple de requête HTTP GET  
```plaintext
GET /index.html HTTP/1.1  
Host: www.exemple.com  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  
Accept: text/html,application/xhtml+xml,application/xml  
Accept-Language: en-US  
Connection: keep-alive

Explications des éléments clés :

-   **GET** : Méthode HTTP utilisée (ici, GET pour récupérer des données).
-   **/index.html** : Chemin de la ressource demandée.
-   **HTTP/1.1** : Version du protocole HTTP utilisée.
-   **Host** : Nom de domaine du serveur cible.
-   **User-Agent** : Informations sur le navigateur ou l'application utilisée.
-   **Accept** : Types de contenus acceptés par le client.
-   **Connection** : Indique si la connexion doit être maintenue ouverte.
```

### Exemple de réponse HTTP:
```plaintext
-HTTP/1.1 200 OK  
-Date: Mon, 18 Feb 2025 12:34:56 GMT  
-Server: Apache/2.4.41 (Ubuntu)  
-Content-Type: text/html; charset=UTF-8  
-Content-Length: 1234  

-<!DOCTYPE html>
-<html lang="en">
-<head>
-    <title>Exemple</title>
-</head>
-<body>
 -   <h1>Bienvenue sur notre site web</h1>
-</body>
-</html>

Explications des éléments clés :

-   **HTTP/1.1 200 OK** : Code de statut et message indiquant que la requête a été traitée avec succès.
-   **Date** : Date et heure de la réponse.
-   **Server** : Informations sur le serveur web utilisé.
-   **Content-Type** : Type de contenu renvoyé (ici, HTML avec encodage UTF-8).
-   **Content-Length** : Longueur du contenu renvoyé en octets.
-   **Corps de la réponse** : Contient la ressource demandée (ici, une page HTML).
```
## 3 : Liste des méthodes HTTP courantes
-   **GET**
    
    -   **Description** : Récupère des données sans modifier l'état du serveur.
    -   **Cas d'utilisation** : Récupération d'une page Web ou de données depuis une API.
-   **POST**
    
    -   **Description** : Envoie des données au serveur pour traitement.
    -   **Cas d'utilisation** : Soumission d'un formulaire ou enregistrement de nouvelles données.
-   **PUT**
    
    -   **Description** : Remplace une ressource existante ou la crée si elle n'existe pas.
    -   **Cas d'utilisation** : Mise à jour d'un profil utilisateur.
-   **PATCH**
    
    -   **Description** : Apporte des modifications partielles à une ressource.
    -   **Cas d'utilisation** : Modification d'un champ spécifique, comme l'adresse.
-   **DELETE**
    
    -   **Description** : Supprime une ressource sur le serveur.
    -   **Cas d'utilisation** : Suppression d'un compte.
-   **HEAD**
    
    -   **Description** : Identique à GET, mais sans le corps de la réponse.
    -   **Cas d'utilisation** : Vérification de l'existence d'une ressource.
-   **OPTIONS**
    
    -   **Description** : Récupère les méthodes HTTP autorisées pour une ressource.
    -   **Cas d'utilisation** : Vérification des méthodes disponibles
 
    ## 4 : Liste des codes d'état HTTP courants
    ### Codes 2xx (Succès)

-   **200 OK** : Requête traitée avec succès.
    
    -   **Scénario** : Affichage d'une page Web ou récupération d'une réponse API correcte.
-   **201 Created** : Ressource créée avec succès.
    
    -   **Scénario** : Création d'un nouvel utilisateur.
-   **204 No Content** : Requête réussie sans contenu dans la réponse.
    
    -   **Scénario** : Suppression réussie d'une ressource.

### Codes 3xx (Redirection)

-   **301 Moved Permanently** : La ressource a été déplacée de manière permanente.
    
    -   **Scénario** : Redirection d'une ancienne URL vers une nouvelle.
-   **302 Found** : La ressource a été temporairement déplacée.
    
    -   **Scénario** : Redirection temporaire pour maintenance.
-   **304 Not Modified** : La ressource n'a pas changé depuis la dernière requête.
    
    -   **Scénario** : Utilisation de la mise en cache.

### Codes 4xx (Erreur côté client)

-   **400 Bad Request** : Requête incorrecte ou mal formée.
    
    -   **Scénario** : Syntaxe incorrecte ou données invalides.
-   **401 Unauthorized** : Authentification requise mais non fournie ou incorrecte.
    
    -   **Scénario** : Accès à une page sans être connecté.
-   **403 Forbidden** : Accès refusé, même avec authentification.
    
    -   **Scénario** : Tentative d'accès à une ressource restreinte.
-   **404 Not Found** : Ressource introuvable sur le serveur.
    
    -   **Scénario** : URL incorrecte ou suppression de la ressource.

### Codes 5xx (Erreur côté serveur)

-   **500 Internal Server Error** : Erreur générale du serveur.
    
    -   **Scénario** : Problème inattendu côté serveur.
-   **502 Bad Gateway** : Le serveur agissant en tant que passerelle a reçu une réponse invalide.
    
    -   **Scénario** : Problème de communication entre deux serveurs.
-   **503 Service Unavailable** : Service temporairement indisponible.
    
    -   **Scénario** : Serveur en surcharge ou en maintenance.

 
.
 .     _By Callacos_

