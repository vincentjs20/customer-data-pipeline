from flask import Blueprint, jsonify, request
from app.utils import load_customers

bp = Blueprint("routes", __name__)

# Health check
@bp.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# Get all customers with pagination
@bp.route("/api/customers", methods=["GET"])
def get_customers():
    customers = load_customers()

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    paginated = customers[start:end]

    return jsonify({
        "data": paginated,
        "total": len(customers),
        "page": page,
        "limit": limit
    })


@bp.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customers = load_customers()

    customer = next(
        (c for c in customers if str(c["customer_id"]) == str(customer_id)),
        None
    )

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer)