# Part B

## 1. Tests and production code

There are 8 test functions for the kitchen example. The addition test has two
parameter sets, so pytest runs 9 cases. A separate multiplication-by-two test
was also written earlier and removed when the reusable-input test covered it.
`kitchen.py` has 39 nonblank lines, giving a final function-to-line ratio of
8:39, or about one test function per 4.9 lines of code.

## 2. Longest red bar

The mixed-unit step in A7 needed the most consecutive fixes. After adding an
empty `add_rate`, the answer was still 201 g: the ounce had been treated as one
gram. A rate table by itself could not change that result. The converter had
to be passed into reduction, and the two sides had to be converted before
their amounts were added. This took four consecutive failing checkpoints.

## 3. The three implementation strategies

Fake It appeared in A6 when addition always returned 500 g. That was enough
for the first example, but the expression still needed a real representation.
Triangulation appeared in A2: multiplying by 2 had to give 400 instead of the
hard-coded 600. Obvious Implementation was useful for the rate table in A7,
where a dictionary under each source unit stored the target rates. The fakes
kept early changes small, and the direct dictionary implementation was easy
to follow once the failing mixed-unit example showed what was missing.

## 4. Remaining items

A8, multiplying a mixed sum, is still unchecked because it is optional. It
would be the next item to try: a sum could multiply its left and right operands
and return another sum. Hashability is only a reminder, since no current test
puts a quantity in a set or uses it as a dictionary key. That concern can be
removed from the active list until a real use case appears.

## 5. Quantity.reduce and an up-front design

An initial design might leave conversion entirely inside `Converter`.
The tests gave a reason for `Quantity.reduce` to exist: both a quantity and a
sum need to produce a quantity in a requested unit. With that shared operation,
`Converter.reduce` delegates to the source, and `Sum.reduce` can ask the
converter to handle each operand. The rate lookup stays with the converter.

## 6. Writing tests before and after code

Part 0 gave an existing function or class to check, so most of the decisions
were about useful inputs: zero weight, the 1 kg boundary, and decimal interest.
Part A required deciding how a caller should use the result before writing
the implementation. `test_scaling_can_reuse_the_original` required a returned
quantity instead of a changed input. Later, `test_combining_grams_and_ounces`
required the conversion context to reach the operands. Those tests directly
affected the structure of the code.
