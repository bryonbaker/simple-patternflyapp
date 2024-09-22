from flask import request, jsonify
from .db import get_customer_by_id

def setup_routes(app):
    @app.route('/search_customer', methods=['GET'])
    def search_customer():
        cust_id = request.args.get('cust_id')
        if not cust_id:
            return jsonify({"error": "No customer ID provided"}), 400

        customer = get_customer_by_id(cust_id)
        if customer:
            return jsonify({
                "cust_id": customer[0],
                "name": customer[1],
                "address": customer[2],
                "phone": customer[3]
            }), 200
        else:
            return jsonify({"error": "Customer not found"}), 404
