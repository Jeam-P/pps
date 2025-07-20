from flask import Flask, render_template, request
import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials
from pps_utils import calculate_pps_score, get_guideline

app = Flask(__name__)

# ใช้ GOOGLE_CREDENTIALS_JSON จาก environment variable
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds_dict = json.loads(os.environ['GOOGLE_CREDENTIALS_JSON'])
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(credentials)

SHEET_ID = "1zQZhcjjX9SbKwJDicF-FDWqAeZkBkfyWF-Xb0R_LnXU"
worksheet = gc.open_by_key(SHEET_ID).sheet1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict()
    score = calculate_pps_score(data)
    guideline = get_guideline(score)

    # บันทึกลง Google Sheet
    row = list(data.values()) + [f"{score}%"]
    worksheet.append_row(row)

    return render_template("result.html", score=score, guideline=guideline)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
