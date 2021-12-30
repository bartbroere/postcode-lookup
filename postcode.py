from string import digits

from flask import Flask, jsonify, request

import postcodetabel

app = Flask(__name__)


@app.route('/')
def index():
    postal_code = postcodetabel.postcodes.get(
        "".join(c for c in request.args.get('postal_code', '').strip() if c.isalnum())
    )
    if not postal_code:
        return jsonify(["", ""])
    house_number = ''.join(c for c in request.args.get('house_number', '') if c in digits)
    if request.args.get('house_number'):
        for house_number_range, street_city in postal_code.items():
            if int(house_number or '1') in range(*(int(x) for x in house_number_range.split('-'))):
                return jsonify(street_city)
    try:
        return jsonify(list(postal_code.values())[0])
    except IndexError:
        return jsonify(["", ""])


if __name__ == '__main__':
    app.run()
