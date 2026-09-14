function addTogether(...args) {
  const [first, second] = args;

  const isNumber = (val) => typeof val === "number";

  if (!isNumber(first)) {
    return undefined;
  }

  if (args.length === 2) {
    return isNumber(second) ? first + second : undefined;
  }

  if (args.length === 1) {
    return (secondArg) => {
      return isNumber(secondArg) ? first + secondArg : undefined;
    };
  }
}