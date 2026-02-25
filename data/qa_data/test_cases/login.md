# Login Feature Test Cases

## Functional Test Cases

TC_LOGIN_01
Verify user can login with valid credentials.
Expected: User redirected to dashboard.

TC_LOGIN_02
Verify error message for invalid password.
Expected: "Invalid credentials" message displayed.

TC_LOGIN_03
Verify login button disabled when fields are empty.

## Edge Cases

TC_LOGIN_10
Verify login with leading/trailing spaces.
TC_LOGIN_11
Verify SQL injection attempt in username field.
TC_LOGIN_12
Verify login after 5 failed attempts (account lock).
