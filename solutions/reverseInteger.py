def reverse :
    digits = ('' + x).split('');
    isPositive = True;
    if digits[0] === '-' :
        isPositive = False;
        digits = digits.splice(1)
    # number = parseInt(digits.reverse().join(''),10);
    # return isPositive ? number : 0 - number;
