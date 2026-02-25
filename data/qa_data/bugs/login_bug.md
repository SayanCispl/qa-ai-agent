# Bug Report: Login Failure

Bug ID: BUG_101
Title: Login fails when password contains special characters

Steps:

1. Enter valid username
2. Enter password with @#$
3. Click Login

Actual Result:
Login fails even though password is correct.

Expected Result:
User should login successfully.

Root Cause:
Password validation regex mismatch.

Severity: High
Environment: Production
