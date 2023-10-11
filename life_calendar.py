from flask import Flask, render_template, request
import datetime
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import matplotlib

matplotlib.use("Agg")  # GUIを無効にする
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birth_year = int(request.form.get("birth_year"))
        birth_month = int(request.form.get("birth_month"))
        birth_day = int(request.form.get("birth_day"))
        file_path = generate_life_calendar(birth_year, birth_month, birth_day)
        return render_template("calendar.html", image_path=file_path)
    return render_template("index.html")


def generate_life_calendar(birth_year, birth_month, birth_day, expected_age=80):
    # ... [前のコードは変更なし]

    # 画像として保存する部分を追加
    file_path = "static/life_calendar.png"
    plt.savefig(file_path)
    plt.close()  # これにより、matplotlibのGUIが表示されなくなります

    return file_path  # 保存した画像のパスを返します


if __name__ == "__main__":
    app.run(debug=True, port=8000)
