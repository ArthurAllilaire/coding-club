"""<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>"""
def sum_of_squares(n):
    """Finds difference between sum of squares till n compared to sum of 1 till n squared (using formulae for nth term) so O(1) runtime"""
    summed_square = (((n+1)*n)/2)**2
    sum_squares = ((2*n+1)*(n+1)*(n))/6
    print(summed_square, sum_squares)
    return int(summed_square - sum_squares)

print(sum_of_squares(100))
print(3025-385)

