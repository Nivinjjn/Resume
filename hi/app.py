from flask import Flask, jsonify, render_template
from flask_cors import CORS
import speedtest

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
   
    return render_template("index.html")


@app.route("/speedtest")
def speedtest_api():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps

        return jsonify({
            "download": round(download_speed, 2),
            "upload": round(upload_speed, 2)
        })
    except Exception as e:
        print("Speedtest error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # disable reloader to avoid Windows socket error
    app.run(debug=True, use_reloader=False)
