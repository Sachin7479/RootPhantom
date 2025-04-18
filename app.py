from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form["target"]
    open_ports = []

    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            open_ports.append(port)
        except:
            pass
        finally:
            s.close()

    return render_template("index.html", target=target, ports=open_ports)

if __name__ == "__main__":
    app.run(debug=True)
