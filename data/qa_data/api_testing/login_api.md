# Login API Testing

Endpoint: POST /api/login

Test Cases:

1. Valid credentials
   Expected: 200 OK with token
2. Invalid password
   Expected: 401 Unauthorized
3. Missing username
   Expected: 400 Bad Request
4. SQL Injection attempt
   Expected: Input sanitized
