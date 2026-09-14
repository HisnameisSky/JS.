function bouncer(arr) {
    return arr.filter(Boolean);
}

/*
false == false
0(-0) == 0
"" == ""||''
null == null
unidefined == unidefined
NaN == NaN

*/

if (userName !== "" && userName !== null && userName !== undefined) {
    console.log("Has a name!");
}

if (userName) {
    console.log("Has a name.");
}