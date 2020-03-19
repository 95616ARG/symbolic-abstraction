from frontend.program import Program
from domains.sign import Sign, SignAbstractState, SignDomain
from domains.interval import Interval, IntervalAbstractState, IntervalDomain
from domains.reduced_product import ReducedProductAbstractState, ReducedProductDomain

program = Program("""
    x = x
    y = y
    z = z
""")

domain_A = SignDomain(["x", "y", "z"])
input_state_A = SignAbstractState({
    "x": Sign.Negative,
    "y": Sign.Positive,
    "z": Sign.Negative,
})
domain_B = IntervalDomain(["x", "y", "z"])
input_state_B = IntervalAbstractState({
    "x": Interval(-2, 3),
    "y": Interval(-5, 5),
    "z": Interval(-1, 3),
})

domain = ReducedProductDomain(["x", "y", "z"], domain_A, domain_B)
input_state = ReducedProductAbstractState(input_state_A, input_state_B)
reduced = domain.reduce(input_state)
print(reduced.state_A)
print(reduced.state_B)

output_state = program.transform(domain, input_state)
domain.reduce(output_state)
print(output_state.state_A)
print(output_state.state_B)
