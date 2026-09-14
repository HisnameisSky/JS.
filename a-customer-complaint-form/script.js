function checkFullName() {
  const val = document.getElementById("full-name").value.trim();
  return val !== "";
}

function checkEmail() {
  const val = document.getElementById("email").value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(val);
}

function checkOrderNo() {
  const val = document.getElementById("order-no").value.trim();
  const orderRegex = /^2024\d{6}$/;
  return orderRegex.test(val);
}

function checkProductCode() {
  const val = document.getElementById("product-code").value.trim();
  const codeRegex = /^[a-zA-Z]{2}\d{2}-[a-zA-Z]\d{3}-[a-zA-Z]{2}\d$/;
  return codeRegex.test(val);
}

function checkQuantity() {
  const val = document.getElementById("quantity").value;
  const num = parseInt(val, 10);
  return !isNaN(num) && num > 0;
}

function checkComplaintsGroup() {
  const checkboxes = document.querySelectorAll('#complaints-group input[type="checkbox"]');
  return Array.from(checkboxes).some((cb) => cb.checked);
}

function checkComplaintDescription() {
  const otherCb = document.getElementById("other-complaint");
  if (!otherCb || !otherCb.checked) {
    return true;
  }
  const val = document.getElementById("complaint-description").value.trim();
  return val.length >= 20;
}

function checkSolutionsGroup() {
  const radios = document.querySelectorAll('#solutions-group input[type="radio"]');
  return Array.from(radios).some((r) => r.checked);
}

function checkSolutionDescription() {
  const otherRadio = document.getElementById("other-solution");
  if (!otherRadio || !otherRadio.checked) {
    return true;
  }
  const val = document.getElementById("solution-description").value.trim();
  return val.length >= 20;
}

function validateForm() {
  return {
    "full-name": checkFullName(),
    "email": checkEmail(),
    "order-no": checkOrderNo(),
    "product-code": checkProductCode(),
    "quantity": checkQuantity(),
    "complaints-group": checkComplaintsGroup(),
    "complaint-description": checkComplaintDescription(),
    "solutions-group": checkSolutionsGroup(),
    "solution-description": checkSolutionDescription()
  };
}

function isValid(validationObj) {
  const obj = validationObj || validateForm();
  return Object.values(obj).every((val) => val === true);
}

function setBorderColor(element, isSuccess) {
  if (element) {
    element.style.borderColor = isSuccess ? "green" : "red";
  }
}

const singleFields = [
  { id: "full-name", checkFn: checkFullName },
  { id: "email", checkFn: checkEmail },
  { id: "order-no", checkFn: checkOrderNo },
  { id: "product-code", checkFn: checkProductCode },
  { id: "quantity", checkFn: checkQuantity },
  { id: "complaint-description", checkFn: checkComplaintDescription },
  { id: "solution-description", checkFn: checkSolutionDescription }
];

singleFields.forEach(({ id, checkFn }) => {
  const elem = document.getElementById(id);
  if (elem) {
    elem.addEventListener("change", () => {
      setBorderColor(elem, checkFn());
    });
  }
});

const complaintsGroup = document.getElementById("complaints-group");
if (complaintsGroup) {
  complaintsGroup.addEventListener("change", () => {
    setBorderColor(complaintsGroup, checkComplaintsGroup());
    const descElem = document.getElementById("complaint-description");
    if (descElem) {
      const otherCb = document.getElementById("other-complaint");
      if (otherCb && otherCb.checked) {
        setBorderColor(descElem, checkComplaintDescription());
      }
    }
  });
}

const solutionsGroup = document.getElementById("solutions-group");
if (solutionsGroup) {
  solutionsGroup.addEventListener("change", () => {
    setBorderColor(solutionsGroup, checkSolutionsGroup());
    const descElem = document.getElementById("solution-description");
    if (descElem) {
      const otherRadio = document.getElementById("other-solution");
      if (otherRadio && otherRadio.checked) {
        setBorderColor(descElem, checkSolutionDescription());
      }
    }
  });
}

const form = document.getElementById("form");
if (form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const results = validateForm();

    setBorderColor(document.getElementById("full-name"), results["full-name"]);
    setBorderColor(document.getElementById("email"), results["email"]);
    setBorderColor(document.getElementById("order-no"), results["order-no"]);
    setBorderColor(document.getElementById("product-code"), results["product-code"]);
    setBorderColor(document.getElementById("quantity"), results["quantity"]);
    setBorderColor(document.getElementById("complaints-group"), results["complaints-group"]);
    setBorderColor(document.getElementById("complaint-description"), results["complaint-description"]);
    setBorderColor(document.getElementById("solutions-group"), results["solutions-group"]);
    setBorderColor(document.getElementById("solution-description"), results["solution-description"]);

    if (isValid(results)) {
      const msgBox = document.getElementById("message-box");
      if (msgBox) msgBox.textContent = "Form submitted successfully!";
    }
  });
}