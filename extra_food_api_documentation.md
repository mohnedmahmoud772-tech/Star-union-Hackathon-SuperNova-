# ExtraFood API Documentation

## Base URL
```
/api/extra-food/
```


## Endpoints

### 1. List & Create ExtraFood Items

**Endpoint:** `GET/POST /api/extra-food/`

#### GET - List all items
```http
GET /api/extra-food/
```
- **Authentication:** Not required
- **Response:** Array of ExtraFood objects

#### POST - Create new item
```http
POST /api/extra-food/
Authorization: Token <your_token>
Content-Type: application/json

{
  "description": "Fresh bread from bakery",
  "category": "Bakery",
  "price": "5.50",
  "quantity": 20,
  "quantity_unit": "pieces",
  "shelf_life": 2,
  "status": "NO_RECEIVER"  // optional (defaults to NO_RECEIVER)
}
```
- **Authentication:** Required (provider only)
- **Response:** Created ExtraFood object with 201 status

---

### 2. Retrieve, Update & Delete Single Item

**Endpoint:** `GET/PUT/PATCH/DELETE /api/extra-food/<id>/`

#### GET - Get single item
```http
GET /api/extra-food/1/
```
- **Authentication:** Not required
- **Response:** Single ExtraFood object with provider details

#### PUT - Full update
```http
PUT /api/extra-food/1/
Authorization: Token <your_token>
Content-Type: application/json

{
  "description": "Updated description",
  "category": "Bakery",
  "price": "6.00",
  "quantity": 15,
  "quantity_unit": "pieces",
  "shelf_life": 3,
  "status": "WAITING_FOR_DELIVERY"
}
```
- **Authentication:** Required (owner provider only)
- **Response:** Updated ExtraFood object

#### PATCH - Partial update
```http
PATCH /api/extra-food/1/
Authorization: Token <your_token>
Content-Type: application/json

{
  "quantity": 10,
  "status": "DONE"
}
```
- **Authentication:** Required (owner provider only)
- **Response:** Updated ExtraFood object

#### DELETE - Delete item
```http
DELETE /api/extra-food/1/
Authorization: Token <your_token>
```
- **Authentication:** Required (owner provider only)
- **Response:** 204 No Content

---

## Response Format

```json
{
  "id": 1,
  "provider": {
    "id": 5,
    "establishment_name": "Downtown Bakery",
    "address": "123 Main St, City"
  },
  "description": "Fresh bread from bakery",
  "category": "Bakery",
  "price": "5.50",
  "quantity": 20,
  "quantity_unit": "pieces",
  "shelf_life": 2,
  "status": "WAITING_FOR_DELIVERY"
}
```

---

## Status Choices

| Status | Description |
|--------|-------------|
| `NO_RECEIVER` | No receiver assigned yet (default) |
| `NO_DELIVERY` | Waiting for delivery arrangement |
| `WAITING_FOR_DELIVERY` | Receiver confirmed, awaiting delivery |
| `ON_THE_WAY_TO_RECEIVER` | Food is currently being delivered |
| `DONE` | Successfully delivered |
| `FAILED` | Delivery failed |
| `EXPIRED` | Food has expired |

---


## Example Usage

### Getting a token (from login endpoint)
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "provider_user", "password": "password123"}'
```

### Creating an ExtraFood item
```bash
curl -X POST http://localhost:8000/api/extra-food/ \
  -H "Authorization: Token abc123def456" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Leftover Pasta",
    "category": "Restaurant",
    "price": "3.00",
    "quantity": 5,
    "quantity_unit": "kg",
    "shelf_life": 1
  }'
```

### Listing all items
```bash
curl http://localhost:8000/api/extra-food/
```

### Getting single item
```bash
curl http://localhost:8000/api/extra-food/1/
```

### Updating an item
```bash
curl -X PATCH http://localhost:8000/api/extra-food/1/ \
  -H "Authorization: Token abc123def456" \
  -H "Content-Type: application/json" \
  -d '{"status": "ON_THE_WAY_TO_RECEIVER"}'
```

### Deleting an item
```bash
curl -X DELETE http://localhost:8000/api/extra-food/1/ \
  -H "Authorization: Token abc123def456"
```
