from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]

    try:
        summary, profile_pic_url = ice_break_with(name=name)

        # Check if we got valid data
        if not summary or not profile_pic_url:
            raise ValueError("Incomplete profile data")

        return jsonify(
            {
                "summary_and_facts": {
                    "summary": summary.summary,
                    "faxxx": summary.faxxx,
                },
                "ice_breakers": {
                    "casual": summary.casual_icebreakers,
                    "formal": summary.formal_icebreakers,
                    "funny": summary.funny_icebreakers,
                },
                "photoUrl": profile_pic_url
            }
        )

    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify({"error": "Could not fetch profile info."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
