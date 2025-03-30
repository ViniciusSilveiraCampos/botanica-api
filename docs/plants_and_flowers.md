### **1. Create a Plant**

**POST** `/plants/`

**Description**: Creates a new plant in the system.

**Request Body**:
- `plantSchema`: An object containing the plant information (`name`, `scientific_name`, `class`, `order`, `family`, `genus`).

**Success Response**:
```json
{
    "id": 1,
    "name": "Rosa",
    "scientific_name": "Rosa spp.",
    "class": "Magnoliopsida",
    "order": "Rosales",
    "family": "Rosaceae",
    "genus": "Rosa"
}
```

**Error Response**:
- **400 Bad Request**: If a plant with the same name already exists. ```json
{
"detail": "This plant already exists. 🍂"
} ```

---

### **2. List Plants**

**GET** `/plants/`

**Description**: Returns a list of plants, with pagination support.

**Query Parameters**:
- `limit` (int, optional): Maximum number of plants to return. Default value: `10`.
- `offset` (int, optional): Number of plants to ignore before starting to return results. Default value: `0`.

**Successful Response**:
```json
{
    "Plants": [
        {
            "id": 1,
            "name": "Rosa",
            "scientific_name": "Rosa spp.",
            "class": "Magnoliopsida",
            "order": "Rosales",
            "family": "Rosaceae",
            "genus": "Rosa"
        },
        {
            "id": 2,
            "name": "Sunflower",
            "scientific_name": "Helianthus annuus",
            "class": "Magnoliopsida",
            "order": "Asterales",
            "family": "Asteraceae",
            "genus": "Helianthus"
        }
    ]
}
```

---

### **3. Filter Plants by Attributes**

**GET** `/plants/?class={class}&order={order}&family={family}&genre={genre}`

**Description**: Filters plants based on attributes such as class, order, family, and genus.

**Query Parameters**:
- `class` (str, optional): Filter by class.
- `order` (str, optional): Filter by order.
- `family` (str, optional): Filter by family.
- `genre` (str, optional): Filter by genus.
- `limit` (int, optional): Limit of results.
- `offset` (int, optional): Offset of results.

**Successful Response**:
```json
{
    "Plants": [
        {
            "id": 3,
            "name": "Daisy",
            "scientific_name": "Bellis perennis",
            "class": "Magnoliopsida",
            "order": "Asterales",
            "family": "Asteraceae",
            "genus": "Bellis"
        }
    ]
}
```

---

### **4. Get a Specific Plant**

**GET** `/plants/{plant_id}`

**Description**: Returns the details of a specific plant based on its ID.

**Path Parameters**:
- `plant_id` (int): ID of the plant to be retrieved.

**Success Response**:
```json
{
    "id": 1,
    "name": "Rosa",
    "scientific_name": "Rosa spp.",
    "class": "Magnoliopsida",
    "order": "Rosales",
    "family": "Rosaceae",
    "genus": "Rosa"
}
```

**Error Response**:
- **404 Not Found**: If the plant with the given `plant_id` is not found. 
```json
{
    "detail": "Plant not found. 🍂"
} 
```

---

### **5. Update a Plant**

**PUT** `/plants/{plant_id}`

**Description**: Updates the information of an existing plant.

**Path Parameters**:
- `plant_id` (int): ID of the plant to be updated.

**Request Body**:
- `plantSchema`: Object containing the new values ​​for the plant (`name`, `scientific_name`, `class`, `order`, `family`, `genre`).

**Success Response**:
```json
{
    "id": 1,
    "name": "Rosa Atualizada",
    "nome_scientifico": "Rosa spp.",
    "classe": "Magnoliopsida",
    "orden": "Rosales",
    "familia": "Rosaceae",
    "genre": "Rosa"
}
```

**Error Response**:
- **404 Not Found**: If the plant with the given `plant_id` is not found.
```json
{
    "detail": "The plant does not exist, it was not found. 🍂"
}
```

---

### **6. Delete a Plant**


**DELETE** `/plants/{plant_id}`

**Description**: Deletes a specific plant from the system.

**Path Parameters**:
- `plant_id` (int): ID of the plant to be deleted.

**Success Response**:
```json
{
    "message": "The plant has been deleted 🪓🪚"
}
```

**Error Response**:
- **404 Not Found**: If the plant with the given `plant_id` is not found.
```json
{
    "detail": "Plant not found. 🍂"
}
```

---
