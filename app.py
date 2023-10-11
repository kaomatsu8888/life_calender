from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Define the birth and death dates
    birth_date = datetime(1999, 3, 21)
    death_date = datetime(2062, 3, 21)
    now = datetime.now()

    # Calculate the total days, passed days, and left days
    total_days = (death_date - birth_date).days
    passed_days = (now - birth_date).days
    left_days = total_days - passed_days

    # Calculate the total yers
    total_years = int(total_days/365)

    # Calculate the total weeks, passed weeks, and left weeks
    total_weeks = int(total_days/7)
    passed_weeks = int(passed_days/7)
    left_weeks = int(left_days/7)

    # Render the template with the calculated values
    return render_template("index.html", 
                           birth_date= birth_date.strftime("%B %d, %Y"),
                           death_date= death_date.strftime("%B %d, %Y"),
                           total_years= total_years,
                           now= now.strftime("%B %d, %Y"),
                           total_days= total_days,
                           passed_days= passed_days,
                           left_days= left_days,
                           total_weeks= total_weeks,
                           passed_weeks= passed_weeks,
                           left_weeks= left_weeks)

if __name__ == '__main__':
    app.run(debug=True)