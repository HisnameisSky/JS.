import re


def validate_form(data: dict) -> dict:
    full_name_valid = bool(data.get("full-name", "").strip())

    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    email_valid = bool(re.match(email_regex, data.get("email", "").strip()))

    order_regex = r"^2024\d{6}$"
    order_valid = bool(re.match(order_regex, data.get("order-no", "").strip()))

    code_regex = r"^[a-zA-Z]{2}\d{2}-[a-zA-Z]\d{3}-[a-zA-Z]{2}\d$"
    product_code_valid = bool(
        re.match(code_regex, data.get("product-code", "").strip())
    )

    try:
        quantity_val = int(data.get("quantity", 0))
        quantity_valid = quantity_val > 0
    except ValueError:
        quantity_valid = False

    complaints = data.get("complaints", [])
    complaints_group_valid = len(complaints) > 0

    if "other" in complaints:
        complaint_desc_valid = (
            len(data.get("complaint-description", "").strip()) >= 20
        )
    else:
        complaint_desc_valid = True

    solution = data.get("solution", "")
    solutions_group_valid = bool(solution)

    if solution == "other":
        solution_desc_valid = (
            len(data.get("solution-description", "").strip()) >= 20
        )
    else:
        solution_desc_valid = True

    return {
        "full-name": full_name_valid,
        "email": email_valid,
        "order-no": order_valid,
        "product-code": product_code_valid,
        "quantity": quantity_valid,
        "complaints-group": complaints_group_valid,
        "complaint-description": complaint_desc_valid,
        "solutions-group": solutions_group_valid,
        "solution-description": solution_desc_valid,
    }


def is_valid(validation_obj: dict) -> bool:
    return all(validation_obj.values())


sample_data = {
    "full-name": "John Doe",
    "email": "john@example.com",
    "order-no": "2024123456",
    "product-code": "AB12-C345-DE6",
    "quantity": "2",
    "complaints": ["other"],
    "complaint-description": "This is a long enough description of the complaint.",
    "solution": "refund",
    "solution-description": "",
}

results = validate_form(sample_data)
print("Validation Results:", results)
print("Is Form Valid?:", is_valid(results))  # -> True