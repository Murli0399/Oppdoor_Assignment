# Oppdoor - Travel Application API Documentation
Oppdoor is a travel application API built with Flask and MySQL to manage travel destinations, plan itineraries, and track expenses. This documentation provides an overview of the available API endpoints and their functionalities.

Table of Contents
Getting Started
Testing the API
API Endpoints
User Registration
Destination Management
Itinerary Planning
Expense Tracking
Getting Started
Clone the Oppdoor repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/oppdoor.git
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Set up a MySQL database and configure your connection details in the Flask application:

python
Copy code
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'oppdoor'
app.config['MYSQL_HOST'] = 'localhost'
Create the necessary database tables (e.g., Users, Destination, Itineraries, Expenses) with their corresponding fields. Refer to the provided code for table creation SQL commands.

Start the Flask application:

bash
Copy code
python app.py
The API is now accessible at http://localhost:5000.

Testing the API
You can use tools like curl, Postman, or HTTPie to test the API endpoints. Make requests to the endpoints as described in the following sections.

API Endpoints
User Registration
Register a User
Endpoint: /register
Method: POST
Request Data: JSON data with username, email, and password.
Response: Registers a new user and returns a success message or an error message.
Destination Management
Create a Destination

Endpoint: /destination
Method: POST
Request Data: JSON data with name, description, and location.
Response: Creates a new destination and returns a success message or an error message.
Get all Destinations

Endpoint: /destination
Method: GET
Response: Retrieves a list of all destinations.
Get a Specific Destination by ID

Endpoint: /destination/<int:id>
Method: GET
Response: Retrieves a specific destination by its ID or returns a message if not found.
Update a Destination by ID

Endpoint: /destination/<int:id>
Method: PUT
Request Data: JSON data with name, description, and location.
Response: Updates a destination by its ID and returns a success message or an error message.
Delete a Destination by ID

Endpoint: /destination/<int:id>
Method: DELETE
Response: Deletes a destination by its ID and returns a success message or an error message.
Itinerary Planning
Create an Itinerary

Endpoint: /itineraries
Method: POST
Request Data: JSON data with user_id, destination_id, start_date, and end_date.
Response: Creates a new itinerary and returns a success message or an error message.
Get all Itineraries

Endpoint: /itineraries
Method: GET
Response: Retrieves a list of all itineraries.
Get a Specific Itinerary by ID

Endpoint: /itineraries/<int:id>
Method: GET
Response: Retrieves a specific itinerary by its ID or returns a message if not found.
Update an Itinerary by ID

Endpoint: /itineraries/<int:id>
Method: PUT
Request Data: JSON data with user_id, destination_id, start_date, and end_date.
Response: Updates an itinerary by its ID and returns a success message or an error message.
Delete an Itinerary by ID

Endpoint: /itineraries/<int:id>
Method: DELETE
Response: Deletes an itinerary by its ID and returns a success message or an error message.
Expense Tracking
Get all Expenses

Endpoint: /expenses
Method: GET
Response: Retrieves a list of all expenses.
Create an Expense

Endpoint: /expenses
Method: POST
Request Data: JSON data with user_id, itinerary_id, amount, description, date, and category_id.
Response: Creates a new expense and returns a success message or an error message.
Get a Specific Expense by ID

Endpoint: /expenses/<int:id>
Method: GET
Response: Retrieves a specific expense by its ID or returns a message if not found.
Update an Expense by ID

Endpoint: /expenses/<int:id>
Method: PUT
Request Data: JSON data with user_id, itinerary_id, amount, description, date, and category_id.
Response: Updates an expense by its ID and returns a success message or an error message.
Delete an Expense by ID

Endpoint: /expenses/<int:id>
Method: DELETE
Response: Deletes an expense by its ID and returns a success message or an error message.