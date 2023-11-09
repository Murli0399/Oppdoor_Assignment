from flask import Flask, request, jsonify
import pymysql

# Create a Flask application
app = Flask(__name__)

# Configure the MySQL connection
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'oppdoor'
app.config['MYSQL_HOST'] = 'localhost'

# Initialize the MySQL extension

mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'Welcome': 'welcome'})

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


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
