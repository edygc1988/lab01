from flask import Flask, request

app = Flask(__name__)

@app.route("/log-event", methods=["POST"])
def log_event():
    event = request.get_json()
    with open('logs.txt','a') as f:
        f.write(f"Registrando evento: {event}")
    print(f"Registrando evento: {event}")
    # Implementa la lógica de almacenamiento o procesamiento de eventos
    return {"success": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
