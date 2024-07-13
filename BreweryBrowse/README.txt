Brewery Browse
This application allows users to manage data using a Flask-based web application.

Setup
1. Clone the repository.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt

   Routes

/ - Welcome message.
/example - Shows a list of examples.
/example/<int:id> - Shows the details of a specific example.
/auth/register - Register a new user.
/auth/login - Login and get a JWT token.
Configuration

Update your database URI in app.py.
Add your API key in app.py.
Dependencies

Flask
Flask-SQLAlchemy
Flask-Migrate
Marshmallow
Requests