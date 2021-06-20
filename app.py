from flask import Flask, request
import requests
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def OnSubmit():
    from_currency = request.form.get('f_currency')
    to_currency = request.form.get('t_currency')
    print(from_currency)
    print(to_currency)
    API_ID = 'ce7ac8d2d40f4d8e89dc406468b7d302'
    
    url = f'https://openexchangerates.org/api/latest.json?app_id={ API_ID }'
    response = requests.get(url).json()
    # print(response)
    # print(requests.status_codes)

    # if from_currency == currencies['rates']['INR']:
    #     print(from_currency)

    currencies = {
        'inr' : response['rates']['INR'],
        'usd' : response['rates']['USD']
    }
    # ind = currencies['inr']
    # print(f"Indian currency 'base:usd'  {ind}")
    # print(currencies['usd_rates'])
    # print(currencies['url'])
    return render_template('index.html', currencies = currencies)


if __name__== '__main__':
    app.run(debug=True) 