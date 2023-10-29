from flask import Flask, request, render_template

from datatype.consumption import Consumption
from gpt_prompting import ask

app = Flask(__name__)


@app.route('/', methods=['GET'])
async def get_index():
    return render_template('index.html')


@app.route('/mileage', methods=['GET'])
async def get_mileage():
    return render_template('mileage.html')


@app.route('/profile', methods=['GET'])
async def get_profile():
    return render_template('profile.html')


@app.route('/benefit', methods=['GET'])
async def get_benefit():
    return render_template('analytics.html', content='benefit')


@app.route('/analytics/<target>', methods=['GET'])
async def get_analytics(target: str):
    return render_template('analytics.html', target=target)

@app.route('/api/ask/<target>', methods=['GET'])
async def get_api_ask(target: str):
    if target == 'week':
        datetime_set = 2
    else:
        datetime_set = 1

    response = await ask(datetime_set)
    return {'message': response}


app.run(port=80, debug=True, host="0.0.0.0")
