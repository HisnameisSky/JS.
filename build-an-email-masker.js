function maskEmail(email) {
  const atIndex = email.indexOf("@");
  
  const username = email.slice(0, atIndex);
  const domain = email.slice(atIndex);
  
  const firstChar = username[0];
  const lastChar = username[username.length - 1];
  
  const maskLength = username.length - 2;
  const maskedMiddle = "*".repeat(maskLength);
  
  return `${firstChar}${maskedMiddle}${lastChar}${domain}`;
}

const email = "myEmail@email.com";

console.log(maskEmail(email));