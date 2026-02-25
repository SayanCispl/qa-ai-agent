Requirement ID: REQ-LOGIN-001

Feature: User Login

Description:
The system shall allow registered users to log in using
a valid email and password.

Rules:
- Email must be registered
- Password must be encrypted
- Login failures must show proper error messages
- Account locks after 5 failed attempts

Non-Functional:
- Login response time < 2 seconds
- Supports Chrome, Firefox, Safari
