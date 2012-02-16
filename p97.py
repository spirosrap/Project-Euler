Base Power Method
Every power of two 2n, mod 10m, is congruent to some power of two in the first instance of the cycle; that is, a power of two between 2m and 2(m + 4·5m – 1 – 1). You need to determine which power of two in this range it is — what I call the base power of two — and then use another method to find its ending digits.

You can find the base power of two directly: it is 2m + j, where j is an offset given by the expression n-m (mod 4·5m-1).

For example, let’s find the last digit of 22009. , so the base power of two is 21+0 = 21 = 2. Trivially, we can see the ending digit is 2.

For the last two digits of 22009, compute . The base power of two is 22+7 = 29, which is small enough to compute directly: 512. The last two digits are 12.

Finding the Last m Digits
The base power method works well for any number of ending digits, assuming n is greater than 4·5m-1.

