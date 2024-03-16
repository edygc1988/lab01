import requests
from flask import Flask

app = Flask(__name__)

# Define the URL of the Sidecar service
SIDEBAR_URL = "http://sidecar:8080/log-event"


class Main:
    def process_message(self, message):
        print(f"Procesando mensaje: {message}")
        event = {"message": message}

        # Send the event to the Sidecar
        try:
            response = requests.post(SIDEBAR_URL, json=event)
            response.raise_for_status()  # Raise an exception for non-2xx response codes
            print("Event sent successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error sending event: {e}")


def handle_root_request():  # Define a function to handle requests at '/'
    main = Main()
    main.process_message("Hola, log enviado desde Main!")
    return "Main application running!"


@app.route('/')  # Associate the route with the handle_root_request function
def handle_root_request_decorated():
    return handle_root_request()  # Call the main function to process the message


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
