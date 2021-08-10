# Kanvas

Sistema que modela o escopo de negócios da Kenzie Academy.

## Utilização

Utilize o sistema com algum programa de requisições HTTP. Recomendamos o [Insomnia](https://insomnia.rest/download).

## Rotas

**POST /api/accounts/**

criar usuários.

```json
{
  "username": "student",
  "password": "1234",
  "is_superuser": false,
  "is_staff": false
}
```

```json
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "username": "student",
  "is_superuser": false,
  "is_staff": false
}
```

**POST /api/login/**

faz autenticação.

```json
// REQUEST
{
  "username": "student",
  "password": "1234"
}
```

```json
// RESPONSE STATUS -> HTTP 200
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

**POST /api/courses/**

criar cursos (somente instrutor).

```json
// REQUEST
// Header -> Authorization: Token <token-do-instrutor>
{
  "name": "Node"
}
```

```json
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Node",
  "users": []
}
```

**PUT /api/courses/`<int:course_id>`/registrations/**

matricular estudantes no curso do "id" passado.

```json
// REQUEST
// Header -> Authorization: Token <token-do-instrutor>
{
  "user_ids": [3, 4, 5]
}
```

```json
// RESPONSE STATUS -> HTTP 200
{
  "id": 1,
  "name": "Node",
  "users": [
    {
      "id": 3,
      "username": "student1"
    },
    {
      "id": 4,
      "username": "student2"
    },
    {
      "id": 5,
      "username": "student3"
    }
  ]
}
```

**GET /api/courses/**

listando os cursos existentes.

```json
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "Node",
    "users": [
      {
        "id": 3,
        "username": "student1"
      }
    ]
  },
  {
    "id": 2,
    "name": "Django",
    "users": []
  },
  {
    "id": 3,
    "name": "React",
    "users": []
  }
]
```

**GET /api/courses/`<int:course_id>`/**

filtrando a lista de curso com um "id" passado.

```json
// RESPONSE STATUS -> HTTP 200
{
  "id": 1,
  "name": "Node",
  "users": [
    {
      "id": 3,
      "username": "student1"
    }
  ]
}
```

**DELETE /api/courses/`<int:course_id>`/**

deletando curso filtrado pelo id passado (somente instrutor).

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT
```

**POST /api/activities/**

criando atividades (instrutor ou facilitador).

```json
// REQUEST
// Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>
{
  "title": "Kenzie Pet",
  "points": 10
}
```

```json
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "title": "Kenzie Pet",
  "points": 10,
  "submissions": []
}
```

**GET /api/activities/**

listando atividades.

```json
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "title": "Kenzie Pet",
    "points": 10,
    "submissions": [
      {
        "id": 1,
        "grade": 10,
        "repo": "http://gitlab.com/kenzie_pet",
        "user_id": 3,
        "activity_id": 1
      }
    ]
  },
  {
    "id": 2,
    "title": "Kanvas",
    "points": 10,
    "submissions": [
      {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
      }
    ]
  },
  {
    "id": 3,
    "title": "KMDb",
    "points": 9,
    "submissions": [
      {
        "id": 3,
        "grade": 4,
        "repo": "http://gitlab.com/kmdb",
        "user_id": 5,
        "activity_id": 3
      }
    ]
  }
]
```

**POST /api/activities/`<int:activity_id>`/submissions/**

fazendo a submissão de uma atividade (somente estudante).

```json
// REQUEST
// Header -> Authorization: Token <token-do-estudante>
{
  "grade": 10, // Esse campo é opcional
  "repo": "http://gitlab.com/kenzie_pet"
}
```

```json
// RESPONSE STATUS -> HTTP 201
{
  "id": 7,
  "grade": null,
  "repo": "http://gitlab.com/kenzie_pet",
  "user_id": 3,
  "activity_id": 1
}
```

**PUT /api/submissions/`<int:submission_id>`/**

editando a nota de uma submissão.

```json
// REQUEST
// Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>
{
  "grade": 10
}
```

```json
// RESPONSE STATUS -> HTTP 200
{
  "id": 3,
  "grade": 10,
  "repo": "http://gitlab.com/kenzie_pet",
  "user_id": 3,
  "activity_id": 1
}
```

**GET /api/submissions/**

listando submissões.
(estudante)

```json
//REQUEST
//Header -> Authorization: Token <token-do-estudante>

// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 2,
    "grade": 8,
    "repo": "http://gitlab.com/kanvas",
    "user_id": 4,
    "activity_id": 2
  },
  {
    "id": 5,
    "grade": null,
    "repo": "http://gitlab.com/kmdb2",
    "user_id": 4,
    "activity_id": 1
  }
]
```

(Instrutor ou Facilitador)

```json
//REQUEST
//Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>

// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
  },
  {
    "id": 2,
    "grade": 8,
    "repo": "http://gitlab.com/kanvas",
    "user_id": 4,
    "activity_id": 2
  },
  {
    "id": 3,
    "grade": 4,
    "repo": "http://gitlab.com/kmdb",
    "user_id": 5,
    "activity_id": 3
  },
  {
    "id": 4,
    "grade": null,
    "repo": "http://gitlab.com/kmdb2",
    "user_id": 5,
    "activity_id": 3
  }
]
```

## Tecnologias utilizadas

- Django
- Django Rest Framework
- SQLite
