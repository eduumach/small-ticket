<div align=center>
<img height="180em" src="https://files.catbox.moe/zmeuoq.png">
</div>

# Small Ticket

With this project, I intend to make a ticket sales website, where the cinema can register and sell their tickets and 
then the user can go and buy the tickets.

## Link project in heroku

https://small-ticket.herokuapp.com

## API

### Users

#### Crated users

```http
POST /v1/users
```

| Parameter  | Type     | Description            |
|:-----------|:---------|:-----------------------|
| `name`     | `string` | **Required**. cpf.     |
| `email`    | `string` | **Required**. name.    |
| `password` | `string` | **Required**. password |

#### Update User

```http
PUT /v1/users/<id>
```

| Parameter  | Type     | Description            |
|:-----------|:---------|:-----------------------|
| `name`     | `string` | **Required**. cpf.     |
| `email`    | `string` | **Required**. name.    |
| `password` | `string` | **Required**. password |

#### Get Users

```http
GET /v1/users
```
Get all users

#### Get User

```http
GET /v1/users/<id>
```
Get user whit id

### Auth User

#### Post Auth User

```http
POST /v1/users/auth
```
Authorization - Basic Auth

| Parameter  | Type     | Description            |
|:-----------|:---------|:-----------------------|
| `user`     | `string` | **Required**. username |
| `password` | `string` | **Required**. password |

Return the token

#### Get hello

```http
POST /?token=
```
add your token, and he will say "hello {your username}"