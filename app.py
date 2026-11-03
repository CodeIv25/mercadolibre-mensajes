from flask import Flask, requiest,
jsonify

app = Flask(__name__)
@app.route("/")
def inicio():
  return "servidor mercado libre funcionando"

@app.route("/oauth/callback")
def oauth_callback():
  code = request.args.get("code")
  if not code:
    return "No se reibio codigo de autorizacion", 400
    return jsonify({
      "mensaje": "autorizacion recibida",
      "codigo_recibido": True
    }}
                   @app.route("/notificaciones",
                              methods=["post])
                                       def notificaciones():
                                       data=
                                       request.get_json(silent=True) or {}
                                       print("Notificacion recibida:",
                                       data)
                                       return jsonify({"status": "ok"}),
                                       200
