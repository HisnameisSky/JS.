function normalizeUnits(manifest) {
  const normalized = { ...manifest };

  if (normalized.unit === "lb") {
    normalized.weight = normalized.weight * 0.45;
    normalized.unit = "kg";
  }

  return normalized;
}

function validateManifest(manifest) {
  const result = {};

  if (!("containerId" in manifest) || manifest.containerId === undefined) {
    result.containerId = "Missing";
  } else if (
    typeof manifest.containerId !== "number" ||
    !Number.isInteger(manifest.containerId) ||
    manifest.containerId <= 0
  ) {
    result.containerId = "Invalid";
  }

  if (!("destination" in manifest) || manifest.destination === undefined) {
    result.destination = "Missing";
  } else if (
    typeof manifest.destination !== "string" ||
    manifest.destination.trim() === ""
  ) {
    result.destination = "Invalid";
  }

  if (!("weight" in manifest) || manifest.weight === undefined) {
    result.weight = "Missing";
  } else if (
    typeof manifest.weight !== "number" ||
    Number.isNaN(manifest.weight) ||
    manifest.weight <= 0
  ) {
    result.weight = "Invalid";
  }

  if (!("unit" in manifest) || manifest.unit === undefined) {
    result.unit = "Missing";
  } else if (manifest.unit !== "kg" && manifest.unit !== "lb") {
    result.unit = "Invalid";
  }

  if (!("hazmat" in manifest) || manifest.hazmat === undefined) {
    result.hazmat = "Missing";
  } else if (typeof manifest.hazmat !== "boolean") {
    result.hazmat = "Invalid";
  }

  return result;
}

function processManifest(manifest) {
  const validationErrors = validateManifest(manifest);
  const isValid = Object.keys(validationErrors).length === 0;

  if (isValid) {
    console.log(`Validation success: ${manifest.containerId}`);
    const normalized = normalizeUnits(manifest);
    console.log(`Total weight: ${normalized.weight} kg`);
  } else {
    console.log(`Validation error: ${manifest.containerId}`);
    console.log(validationErrors);
  }
}