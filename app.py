from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
    "name": "mystore",
    "item": [{

        "name": "myitem",
        "price": 12
    },
        {

        "name": "myitem1",
        "price": 121
    }]
}]


@app.route('/')
def home():
    return render_template('index.html')

 # # get store


@app.route('/store')  # 'https://127.0.0.1/store' list of store
def getstorelist():
    return jsonify({"stores": stores})


@app.route('/store', methods=['POST'])
def createstore():
    req_data = request.get_json()
    new_store = {

        "name": req_data['name'],
        "item": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')  # 'https://127.0.0.1/store/storename'
def getstore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    req_data = request.get_json()
    for store in stores:
        if name == store["name"]:
            item = {
                "name": req_data['name'],
                "price": req_data['price']
            }
            store['item'].append(item)
            return jsonify(item)
    return jsonify({"message": "no item found"})


@app.route('/store/<string:name>/item', methods=['GET', 'POST'])
def get_itemin_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"item": store["item"]})
    return jsonify({"message": "store item not found"})


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug=True)
