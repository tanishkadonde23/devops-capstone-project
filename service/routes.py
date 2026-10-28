"""REST API routes for customer accounts."""
        "paths": "http://127.0.0.1:8080/accounts",
        "version": "1.0",
    })


@app.route("/accounts", methods=["POST"])
def create_account():
    """Create an account."""
    global next_id
    data = request.get_json(silent=True)

    required = [
        "name", "email", "address", "phone_number", "date_joined"
    ]
    if not data or any(not data.get(field) for field in required):
        return jsonify({"error": "Missing required account fields"}), 400

    account = {"id": next_id, **{field: data[field] for field in required}}
    accounts[next_id] = account
    next_id += 1
    return jsonify(account), 201


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all accounts."""
    return jsonify(list(accounts.values())), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Read one account."""
    account = accounts.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an account."""
    account = accounts.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json(silent=True)
    required = [
        "name", "email", "address", "phone_number", "date_joined"
    ]
    if not data or any(not data.get(field) for field in required):
        return jsonify({"error": "Missing required account fields"}), 400

    account.update({field: data[field] for field in required})
    return jsonify(account), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account."""
    if account_id not in accounts:
        return jsonify({"error": "Account not found"}), 404
    del accounts[account_id]
    return "", 204
