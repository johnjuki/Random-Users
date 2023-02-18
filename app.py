from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    url = "https://randomuser.me/api/?results=100&gender=male"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.text
        data = json.loads(json_response)

        # Extract first names from the results list
        names = []
        for result in data['results']:
            full_name = result['name']['first'] + ' ' + result['name']['last']
            names.append(full_name)

        # Pass the first names to the template for display
        return render_template('home.html', names=names)
    else:
        return "Error retrieving random users."


if __name__ == "__main__":
    app.run(host='0.0.0.0')
