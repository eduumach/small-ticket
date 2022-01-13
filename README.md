
# Small Ticket


## Link project in heroku

https://small-ticket.herokuapp.com


## API

### Users

#### Crated users

```http
POST /v1/users
```

| Parameter  | Type     | Description               |
|:-----------|:---------|:--------------------------|
| `name`     | `string` | **Obrigatório**. cpf.     |
| `email`    | `string` | **Obrigatório**. nome.    |
| `password` | `string` | **Obrigatorio**. password |

#### Update User

```http
PUT /v1/users/<id>
```

| Parameter  | Type     | Description               |
|:-----------|:---------|:--------------------------|
| `name`     | `string` | **Obrigatório**. cpf.     |
| `email`    | `string` | **Obrigatório**. nome.    |
| `password` | `string` | **Obrigatorio**. password |

#### Get Users

```http
GET /v1/users
```
Mostra todos os usuarios

#### Get User

```http
GET /v1/users/<id>
```
Mostra um usuario espesifico pelo id

#### Post Auth User

```http
POST /v1/users/auth
```
Basic Authentic

| Parameter  | Type     | Description               |
|:-----------|:---------|:--------------------------|
| `user`     | `string` | **Obrigatório**. username |
| `password` | `string` | **Obrigatorio**. password |

#### Operação deposito

```http
POST /operacao/deposito
```

| Parameter | Type     | Description                         |
|:----------|:---------|:------------------------------------|
| `conta`   | `Long`   | **Obrigatório**. Id da conta.       |
| `valor`   | `double` | **Obrigatório**. Valor do deposito. |