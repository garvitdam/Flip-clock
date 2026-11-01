from flask import Flask, jsonify, render_template
from datetime import datetime
import os
import pytz

app = Flask(__name__)


def get_ssl_context(cert_path=None, key_path=None):
    preferred_cert_path = cert_path or 'localhost+2.pem'
    preferred_key_path = key_path or 'localhost+2-key.pem'
    fallback_cert_path = cert_path or 'damclock.gd.pem'
    fallback_key_path = key_path or 'damclock.gd-key.pem'

    for candidate_cert, candidate_key in (
        (preferred_cert_path, preferred_key_path),
        (fallback_cert_path, fallback_key_path),
    ):
        if not candidate_cert or not candidate_key:
            continue
        candidate_cert = os.path.abspath(candidate_cert)
        candidate_key = os.path.abspath(candidate_key)
        if os.path.exists(candidate_cert) and os.path.exists(candidate_key):
            return (candidate_cert, candidate_key)

    return None

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/time")
def api_time():
    now_utc = datetime.now(pytz.utc)
    ny = now_utc.astimezone(pytz.timezone("America/New_York"))
    tokyo = now_utc.astimezone(pytz.timezone("Asia/Tokyo"))
    utc = now_utc.astimezone(pytz.utc)

    return jsonify({
        "local": {
            "hour": datetime.now().hour,
            "minute": datetime.now().minute,
            "second": datetime.now().second,
            "weekday": datetime.now().strftime("%A"),
            "date": datetime.now().strftime("%b %d, %Y"),
            "timezone": datetime.now().astimezone().tzname()
        },
        "utc": utc.strftime("%H:%M:%S"),
        "new_york": ny.strftime("%H:%M:%S"),
        "tokyo": tokyo.strftime("%H:%M:%S"),
        "iso": now_utc.isoformat()
    })

if __name__ == "__main__":
    ssl_context = get_ssl_context()
    port = int(os.getenv("PORT", "5000"))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
        ssl_context=ssl_context
    )
