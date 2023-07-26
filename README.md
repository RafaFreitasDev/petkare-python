# PARA RODAR O PROJETO 

## Requisitos ##
- Ter o Python instalado

- Ter o Django instalado

- Ter o pip instalado (gerenciador de pacotes)

## Fazer os seguintes comandos ##

pip install -r .\requirements.txt (para instalar dependencias)

python .\manage.py migrate (para rodar as migrations)

python  .\manage.py runserver (para iniciar o servidor)


## Endpoints:

| Método | Endpoint                   | Responsabilidade                                  | 
| ------ | -------------------------- | ------------------------------------------------- |
| POST   | /groups/                   | Criação de grupo                                  | 
| GET    | /groups/                   | Lista todos os grupos                             |
| POST   | /traits/                   | Criação de característica                         | 
| GET    | /traits/                   | Lista todos os características                    | 
| POST   | /pets/                     | Criação de pet                                    | 
| GET    | /pets/                     | Lista todos os pets                               |
| GET    | /pets/:id/                 | Lista pet por id                                  | 
| PATCH  | /pets/:id/                 | Atualiza um pet                                   | 
| DELETE | /pets/:id/                 | Deleta pet                                        | 



### **POST - /groups/**

**Url da requisição**: `http://127.0.0.1:8000/api/groups/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
	"scientific_name":"gatitus familiaris"
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"id": 2,
	"scientific_name": "gatitus familiaris",
	"created_at": "2023-06-06T21:07:40.545645Z"
}
```

### **GET - /groups/**

**Url da requisição**: `http://127.0.0.1:8000/api/groups/`

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">200 OK</b> |

```json
[
	{
		"id": 1,
		"scientific_name": "caninus familiaris",
		"created_at": "2023-06-06T21:07:27.140864Z"
	},
	{
		"id": 2,
		"scientific_name": "gatitus familiaris",
		"created_at": "2023-06-06T21:07:40.545645Z"
	},
	{
		"id": 3,
		"scientific_name": "canis familiaris",
		"created_at": "2023-06-07T18:52:43.210318Z"
	},
	{
		"id": 4,
		"scientific_name": "cavalus familiaris",
		"created_at": "2023-06-07T20:06:10.817260Z"
	}
]
```

### **POST - /traits/**

**Url da requisição**: `http://127.0.0.1:8000/api/traits/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
	"name":"Dark"
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"id": 2,
	"name": "Dark",
	"created_at": "2023-06-06T21:05:20.868584Z"
}
```

### **GET - /traits/**

**Url da requisição**: `http://127.0.0.1:8000/api/traits/`

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">200 OK</b> |

```json
[
	{
		"id": 1,
		"trait_name": "Hairy",
		"created_at": "2023-06-06T21:04:35.565279Z"
	},
	{
		"id": 2,
		"trait_name": "Dark",
		"created_at": "2023-06-06T21:05:20.868584Z"
	},
	{
		"id": 3,
		"trait_name": "clever",
		"created_at": "2023-06-07T18:52:43.220603Z"
	},
	{
		"id": 4,
		"trait_name": "friendly",
		"created_at": "2023-06-07T18:52:43.229313Z"
	},
	{
		"id": 5,
		"trait_name": "smart",
		"created_at": "2023-06-07T20:06:10.826886Z"
	},
	{
		"id": 6,
		"trait_name": "nervous",
		"created_at": "2023-06-07T20:07:28.034084Z"
	}
]
```

### **POST - /pets/** 

**Url da requisição**: `http://127.0.0.1:8000/api/pets/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "name": "Satanas",
  "age": 2,
  "weight": 0.5,
  "sex": "Female",
  "group": {"scientific_name": "gatitus familiaris"},
  "traits": [{"trait_name": "laizy"}, {"trait_name": "friendly"}]
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">201 CREATED</b> |

```json
{
	"id": 4,
	"name": "Satanas",
	"age": 2,
	"weight": 0.5,
	"sex": "Female",
	"group": {
		"id": 2,
		"scientific_name": "gatitus familiaris",
		"created_at": "2023-06-06T21:07:40.545645Z"
	},
	"traits": [
		{
			"id": 4,
			"trait_name": "friendly",
			"created_at": "2023-06-07T18:52:43.229313Z"
		},
		{
			"id": 7,
			"trait_name": "laizy",
			"created_at": "2023-06-07T20:16:46.473265Z"
		}
	]
}
```

### **GET - /pets/**

**Url da requisição**: `http://127.0.0.1:8000/api/pets/`

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"count": 4,
	"next": "http://127.0.0.1:8000/api/pets/?page=2&trait=clever",
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "Seraphim",
			"age": 1,
			"weight": 20.0,
			"sex": "Male",
			"group": {
				"id": 3,
				"scientific_name": "canis familiaris",
				"created_at": "2023-06-07T18:52:43.210318Z"
			},
			"traits": [
				{
					"id": 3,
					"trait_name": "clever",
					"created_at": "2023-06-07T18:52:43.220603Z"
				},
				{
					"id": 4,
					"trait_name": "friendly",
					"created_at": "2023-06-07T18:52:43.229313Z"
				}
			]
		},
		{
			"id": 2,
			"name": "Pegasus",
			"age": 7,
			"weight": 650.0,
			"sex": "Male",
			"group": {
				"id": 4,
				"scientific_name": "cavalus familiaris",
				"created_at": "2023-06-07T20:06:10.817260Z"
			},
			"traits": [
				{
					"id": 4,
					"trait_name": "friendly",
					"created_at": "2023-06-07T18:52:43.229313Z"
				},
				{
					"id": 5,
					"trait_name": "smart",
					"created_at": "2023-06-07T20:06:10.826886Z"
				}
			]
		}
	]
}
```

### **GET - /pets/:id/**

**Url da requisição**: `http://127.0.0.1:8000/api/pets/3/`

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"id": 3,
	"name": "Mary",
	"age": 100,
	"weight": 100.0,
	"sex": "Female",
	"group": {
		"id": 2,
		"scientific_name": "gatitus familiaris",
		"created_at": "2023-06-06T21:07:40.545645Z"
	},
	"traits": [
		{
			"id": 4,
			"trait_name": "friendly",
			"created_at": "2023-06-07T18:52:43.229313Z"
		},
		{
			"id": 6,
			"trait_name": "nervous",
			"created_at": "2023-06-07T20:07:28.034084Z"
		}
	]
}
```

### **PATCH - /pets/:id/**

**Url da requisição**: `http://127.0.0.1:8000/api/pets/3/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{ 
	"group": {"scientific_name": "cachorras familiaris"}
}
```

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"id": 3,
	"name": "Mary",
	"age": 100,
	"weight": 100.0,
	"sex": "Female",
	"group": {
		"id": 6,
		"scientific_name": "cachorras familiaris",
		"created_at": "2023-06-08T14:45:07.789280Z"
	},
	"traits": [
		{
			"id": 8,
			"trait_name": "wrath",
			"created_at": "2023-06-08T14:08:17.577001Z"
		}
	]
}
```

### **DELETE - /pets/:id/**

| Resposta do servidor:                                  |
| ------------------------------------------------------ |
| Body: **Nenhum body deve ser retornado**               |
| Status code: <b style="color:green">204 NO CONTENT</b> |

```json

```


