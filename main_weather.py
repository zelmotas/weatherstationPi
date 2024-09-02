from flask import Flask, render_template
from sense_hat import SenseHat
import time

# Initialize Flask app and Sense HAT
app = Flask(__name__)
sense = SenseHat()

# Function to get sensor data
def get_sensor_data():
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    # Optionally round the values
    temperature = round(temperature, 2)
    humidity = round(humidity, 2)
    pressure = round(pressure, 2)
    
    return temperature, humidity, pressure

# Route for the homepage
@app.route('/')
def index():
    temperature, humidity, pressure = get_sensor_data()
    return render_template('index.html', temperature=temperature, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
