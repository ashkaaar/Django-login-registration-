User Registration and Authentication Implementation Goals:
User Registration System:

Implement a form for users to enter their registration details, including a username, email, and password.
Upon submitting the registration form, store the user's information in a database.
Confirmation Email with Verification Link:

After successful registration, generate a unique verification token.
Send an email to the registered user's provided email address containing a link with the verification token.
The link should lead to a verification endpoint in your application.
Email Verification before Login:

When a user clicks the verification link, your application should validate the verification token.
If the token is valid, mark the user account as verified in the database.
Users should only be able to log in if their account has been verified.
Profile Page:
User Dashboard:

Create a dedicated page for registered users, commonly referred to as a user dashboard.
Users should be able to access this dashboard after successful login.
View and Edit Profiles:

Within the user dashboard, provide options for users to view and edit their profiles.
Display the user's current username and email and allow them to make changes as needed.
View All Registered Profiles:

Implement a feature to display a list of all registered profiles, accessible from the user dashboard.
This list could include usernames and other relevant information.
Password Reset:
Password Reset via Email:

Create a "Forgot Password" functionality that allows users to request a password reset.
When a user initiates a password reset, generate a secure token and send it to the user's email.
Secure Token for Password Reset:

Ensure the generated token is time-limited and can only be used for a specific reset request.
Include the token in a link that users can click to access a password reset page in your application.
Password Reset Page:

Create a page where users can enter a new password after clicking the password reset link.
Validate the reset token before allowing users to set a new password.
