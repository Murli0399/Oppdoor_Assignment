from flask import Flask, request, jsonify
import pymysql

# Create a Flask application
app = Flask(__name__)

# Configure the MySQL connection
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'oppdoor'
app.config['MYSQL_HOST'] = 'localhost'

mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)


# Testing API 
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'Welcome': 'welcome'})


@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json  
        username = data['username']
        email = data['email']
        password = data['password']

        cursor = mysql.cursor()
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        mysql.commit()
        cursor.close()

        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Create a new destination
@app.route('/destination', methods=['POST'])
def create_data():
    try:
        data = request.json  
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO Destination (name, description, location) VALUES (%s, %s, %s)",
                       (data['name'], data['description'], data['location']))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Destination created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Get all Destination
@app.route('/destination', methods=['GET'])
def get_data():
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Destination")
        data = cursor.fetchall()
        cursor.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


# Get a specific Des Itination byD
@app.route('/destination/<int:id>', methods=['GET'])
def get_destination_by_id(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Destination WHERE id = %s", (id))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify(data)
        else:
            return jsonify({'message': 'Destination not found'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Update an Destination by ID
@app.route('/destination/<int:id>', methods=['PUT'])
def update_destination(id):
    try:
        data = request.json
        cursor = mysql.cursor()
        cursor.execute("UPDATE Destination SET name=%s, description=%s, location=%s WHERE id=%s",
                       (data['name'], data['description'], data['location'], id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Destination updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Delete an Destination by ID
@app.route('/destination/<int:id>', methods=['DELETE'])
def delete_data(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("DELETE FROM Destination WHERE id = %s", (id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Destination deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Create a new itinerary
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    try:
        data = request.json
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO Itineraries (user_id, destination_id, start_date, end_date) VALUES (%s, %s, %s, %s)",
                       (data['user_id'], data['destination_id'], data['start_date'], data['end_date']))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Itinerary created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Get all itineraries
@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Itineraries")
        itineraries = cursor.fetchall()
        cursor.close()
        return jsonify(itineraries)
    except Exception as e:
        return jsonify({'error': str(e)})

# Get a specific itinerary by ID
@app.route('/itineraries/<int:id>', methods=['GET'])
def get_itinerary(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Itineraries WHERE id = %s", (id,))
        itinerary = cursor.fetchone()
        cursor.close()
        if itinerary:
            return jsonify(itinerary)
        else:
            return jsonify({'message': 'Itinerary not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Update an itinerary by ID
@app.route('/itineraries/<int:id>', methods=['PUT'])
def update_itinerary(id):
    try:
        data = request.json
        cursor = mysql.cursor()
        cursor.execute("UPDATE Itineraries SET user_id=%s, destination_id=%s, start_date=%s, end_date=%s WHERE id=%s",
                       (data['user_id'], data['destination_id'], data['start_date'], data['end_date'], id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Itinerary updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Delete an itinerary by ID
@app.route('/itineraries/<int:id>', methods=['DELETE'])
def delete_itinerary(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("DELETE FROM Itineraries WHERE id = %s", (id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Itinerary deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Get all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Expenses")
        expenses = cursor.fetchall()
        cursor.close()
        return jsonify(expenses)
    except Exception as e:
        return jsonify({'error': str(e)})

# Create a new expense
@app.route('/expenses', methods=['POST'])
def create_expense():
    try:
        data = request.json  
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO Expenses (user_id, itinerary_id, amount, description, date, category_id) "
                       "VALUES (%s, %s, %s, %s, %s, %s)",
                       (data['user_id'], data['itinerary_id'], data['amount'], data['description'], data['date'], data['category_id']))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Expense created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Get a specific expense by ID
@app.route('/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM Expenses WHERE id = %s", (id))
        expense = cursor.fetchone()
        cursor.close()
        if expense:
            return jsonify(expense)
        else:
            return jsonify({'message': 'Expense not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Update an expense by ID
@app.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    try:
        data = request.json  
        cursor = mysql.cursor()
        cursor.execute("UPDATE Expenses SET user_id=%s, itinerary_id=%s, amount=%s, description=%s, date=%s, category_id=%s "
                       "WHERE id=%s",
                       (data['user_id'], data['itinerary_id'], data['amount'], data['description'], data['date'], data['category_id'], id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Expense updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Delete an expense by ID
@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    try:
        cursor = mysql.cursor()
        cursor.execute("DELETE FROM Expenses WHERE id = %s", (id))
        mysql.commit()
        cursor.close()
        return jsonify({'message': 'Expense deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
