import copy


def normalize_units(manifest):
    normalized = copy.copy(manifest)

    if normalized.get("unit") == "lb":
        normalized["weight"] = normalized["weight"] * 0.45
        normalized["unit"] = "kg"

    return normalized


def validate_manifest(manifest):
    result = {}

    if "containerId" not in manifest or manifest["containerId"] is None:
        result["containerId"] = "Missing"
    elif (
        not isinstance(manifest["containerId"], int)
        or isinstance(manifest["containerId"], bool)
        or manifest["containerId"] <= 0
    ):
        result["containerId"] = "Invalid"

    if "destination" not in manifest or manifest["destination"] is None:
        result["destination"] = "Missing"
    elif (
        not isinstance(manifest["destination"], str)
        or manifest["destination"].strip() == ""
    ):
        result["destination"] = "Invalid"

    if "weight" not in manifest or manifest["weight"] is None:
        result["weight"] = "Missing"
    elif (
        not isinstance(manifest["weight"], (int, float))
        or isinstance(manifest["weight"], bool)
        or manifest["weight"] <= 0
    ):
        result["weight"] = "Invalid"

    if "unit" not in manifest or manifest["unit"] is None:
        result["unit"] = "Missing"
    elif manifest["unit"] not in ["kg", "lb"]:
        result["unit"] = "Invalid"

    if "hazmat" not in manifest or manifest["hazmat"] is None:
        result["hazmat"] = "Missing"
    elif not isinstance(manifest["hazmat"], bool):
        result["hazmat"] = "Invalid"

    return result


def process_manifest(manifest):
    validation_errors = validate_manifest(manifest)
    is_valid = len(validation_errors) == 0

    if is_valid:
        print(f"Validation success: {manifest.get('containerId')}")
        normalized = normalize_units(manifest)
        print(f"Total weight: {normalized['weight']} kg")
    else:
        print(f"Validation error: {manifest.get('containerId')}")
        print(validation_errors)