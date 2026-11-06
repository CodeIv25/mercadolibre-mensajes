from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Servidor Mercado Libre funcionando"

@app.route("/oauth/callback")
def oauth_callback():
    code = request.args.get("code")

    if not code:
        return "No se recibio codigo de autorizacion", 400

    return jsonify({
        "mensaje": "Autorizacion recibida",
        "codigo_recibido": True
    })

@app.route("/notificaciones", methods=["POST"])
def notificaciones():
    data = request.get_json(silent=True) or {}

    print("Notificacion recibida:", data)

    return jsonify({"status": "ok"}), 200
