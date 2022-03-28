GET /api/equipment
response [
	{
		"id": 1,
		"serialnumber": "123abc45",
		"name": "MacBookPro 2019",
		"category": {
			"id": 1,
			"category": "Laptop"
		},
		"employee": null
	},
	{
		"id": 3,
		"serialnumber": "12abc345",
		"name": "Samsung Monitor",
		"category": {
			"id": 2,
			"category": "Monitor"
		},
		"employee": null
	},
  	{
		"id": 4,
		"serialnumber": "1234abc5",
		"name": "Logitech Mouse",
		"category": {
			"id": 4,
			"category": "Mouse"
		},
		"employee": null
	},
]

POST /api/equipment
request {
	"serialnumber": "12345abc",
	"name": "Logitech Keyboard",
	"category": 3,
	"employee": null
}


DELETE /api/equipment/{id}

PATCH /api/equipment/{id}
request {
	"serialnumber": "12345abc",
	"name": "Logitech Keyboard",
	"category": 3,
	"employee": 8
}

GET /api/categories
response [
	{
		"id": 1,
		"category": "Laptop"
	},
	{
		"id": 2,
		"category": "Monitor"
	},
	{
		"id": 3,
		"category": "Keyboard"
	},
	{
		"id": 4,
		"category": "Mouse"
	},
]

POST /api/categories
request {
    "category": "Charger"
}