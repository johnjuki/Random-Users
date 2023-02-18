from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    url = "https://randomuser.me/api/?results=100&inc=name,email,dob,phone,picture&gender=male"
    response = requests.get(url)
    if response.status_code == 200:
        json_string = response.text
        data = json.loads(json_string)

        # Pass the results to the template for display
        return render_template('./home.html', results=data['results'])
    else:
        return "Error retrieving random users."


if __name__ == "__main__":
    app.run(host='0.0.0.0')
