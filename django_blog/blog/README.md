Authentication Process
1. User Registration
Endpoint: /register/
Method: POST
Description: Users submit a form with their desired username, email, and password. Upon successful validation, the user account is created, and the user is logged in automatically.
Usage:

Fill out the registration form with a username, email, and password.
Submit the form.
On success, you will be redirected to your profile page.
2. User Login
Endpoint: /login/
Method: POST
Description: Registered users enter their username and password to authenticate and gain access to their account.
Usage:

Enter your username and password in the login form.
Submit the form.
On success, you will be redirected to your profile page.
3. User Logout
Endpoint: /logout/
Method: GET
Description: Users can log out of their accounts, which terminates their session.
Usage:

Click on the logout link in the profile page.
You will be redirected to the login page.
4. Profile Management
Endpoint: /profile/
Method: GET and POST
Description: Authenticated users can view their profile information and edit details such as email.
Usage:

Access the profile page to view your details.
Modify any fields in the profile form and submit to update your information.
On success, a message will confirm the update.
Testing the Authentication Features
1. Testing User Registration
Navigate to /register/.
Fill out the registration form with valid details and submit.
Check that the user is redirected to the profile page and a success message is displayed.
Attempt to register with an existing username or invalid email and confirm appropriate error messages are shown.
2. Testing User Login
Navigate to /login/.
Enter valid credentials and submit the form.
Confirm that you are redirected to the profile page.
Attempt to log in with invalid credentials and ensure an error message is displayed.
3. Testing User Logout
While logged in, click the logout link.
Ensure you are redirected to the login page and that your session is terminated.
4. Testing Profile Management
After logging in, navigate to /profile/.
Check that the current user information is displayed correctly.
Update the email address and submit the form.
Confirm that the changes are saved and a success message is shown.
Security Considerations
CSRF Protection: All forms include CSRF tokens to protect against cross-site request forgery attacks.
Password Handling: Passwords are securely hashed using Django’s built-in authentication system.


#question number 2
 CRUD functionality.
Instructions for authenticated users.
Notes on permissions and access control.