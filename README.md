# Raspberry Pi Weather Station

This project is a Raspberry Pi-based weather station that collects and displays real-time weather data such as temperature, humidity, and atmospheric pressure. The data is displayed on a web interface using a combination of Python, HTML, and CSS.

## Features

- **Temperature Monitoring**: Displays the current temperature with color-coded indicators (blue for cold, red for hot, orange for mild).
- **Humidity Monitoring**: Shows the current humidity level with corresponding color indicators (blue for low, red for high, green for normal).
- **Pressure Monitoring**: Displays the current atmospheric pressure with color indicators (blue for low, red for high, green for normal).
- **Responsive Design**: The web interface is designed to be responsive and visually appealing, with hover animations for better user interaction.

## Files

- `main_weather.py`: The main Python script that reads data from the sensors and serves it to the web interface.
- `index.html`: The HTML file that structures the weather data display on the web page.
- `styles.css`: The CSS file that styles the HTML elements, including color coding and animations.

## Setup

### Requirements

- Raspberry Pi with a Sense HAT
- Python 3.x
- Flask (Python web framework)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/zelmotas/weatherstationPi.git
    cd weatherstationPi
    ```

2. **Install required Python packages:**

    ```bash
    pip install flask
    ```

3. **Run the application:**

    ```bash
    python main_weather.py
    ```

4. **Access the web interface:**

    Open your web browser and navigate to `http://<your-pi-ip>:5000` to view the weather data.

## Usage

The application collects weather data in real-time and displays it on a simple web interface. You can monitor the temperature, humidity, and pressure directly from your web browser.

## Customization

- **CSS Styling**: You can customize the look and feel of the web interface by editing the `styles.css` file.
- **Python Script**: Modify `main_weather.py` if you want to add more sensors or change the data presentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Raspberry Pi Foundation
- Flask web framework
- Sense HAT library for Python
