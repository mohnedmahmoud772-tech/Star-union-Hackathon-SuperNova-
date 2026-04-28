## 🔧 API Documentation

This section describes the API endpoints for user registration and authentication.

### Endpoints

#### 1. User Registration (Signup)
**Endpoint:** `POST /api/signup/`

Registers a new user and creates their profile based on the user type.

##### Request Body
```json
{
  "user_type": "provider|receiver|volunteer",
  "username": "string",
  "email": "string",
  "password": "string",
  "provider|receiver|volunteer": {
    // Profile-specific fields (see below)
  }
}
```

##### Profile Fields

**Provider:**
```json
{
  "establishment_name": "string",
  "activity_type": "restaurant|bakery|hotel|other",
  "commercial_registration_number": "string",
  "address": "string",
  "person_in_charge_full_name": "string",
  "person_in_charge_phone": "string"
}
```

**Receiver:**
```json
{
  "entity_name": "string",
  "registration_license_number": "string",
  "address": "string",
  "person_in_charge_full_name": "string",
  "person_in_charge_phone": "string"
}
```

**Volunteer:**
```json
{
  "full_name": "string",
  "national_id_number": "string",
  "means_of_transportation": "car|bike|public_transport|walking|other",
  "addresses": "string"
}
```

##### Response (Success)
```json
{
  "token": "string",
  "user": {
    "username": "string",
    "email": "string"
  }
}
```

##### Response (Error)
```json
{
  "user_type": ["This field is required."],
  "username": ["This field may not be blank."],
  // Other validation errors
}
```

#### 2. User Login
**Endpoint:** `POST /api/login/`

Authenticates an existing user and returns a token.

##### Request Body
```json
{
  "username": "string",
  "password": "string"
}
```

##### Response (Success)
```json
{
  "token": "string",
  "user": {
    "username": "string",
    "email": "string"
  }
}
```

##### Response (Error)
```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

### Authentication

For authenticated requests, include the token in the Authorization header:

```
Authorization: Token <your_token_here>
```

### Frontend Integration Examples

#### Signup Example (JavaScript)
```javascript
const signupData = {
  user_type: 'provider',
  username: 'john_doe',
  email: 'john@example.com',
  password: 'securepassword123',
  provider: {
    establishment_name: 'John\'s Restaurant',
    activity_type: 'restaurant',
    commercial_registration_number: '123456789',
    address: '123 Main St, City',
    person_in_charge_full_name: 'John Doe',
    person_in_charge_phone: '+1234567890'
  }
};

fetch('/api/signup/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(signupData)
})
.then(response => response.json())
.then(data => {
  if (data.token) {
    localStorage.setItem('authToken', data.token);
  } else {
    console.error(data);
  }
});
```

#### Login Example (JavaScript)
```javascript
const loginData = { username: 'john_doe', password: 'securepassword123' };

fetch('/api/login/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(loginData)
})
.then(response => response.json())
.then(data => {
  if (data.token) {
    localStorage.setItem('authToken', data.token);
  } else {
    console.error(data);
  }
});
```

#### Authenticated Request Example
```javascript
const token = localStorage.getItem('authToken');

fetch('/api/some-protected-endpoint/', {
  headers: { 'Authorization': `Token ${token}` }
})
.then(response => response.json());
```

### Notes

- All passwords are securely hashed.
- Tokens do not expire by default.
- Use HTTPS in production.
- API runs on `http://127.0.0.1:8000/` in development.  