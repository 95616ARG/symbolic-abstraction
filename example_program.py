from frontend.program import Program
from domains.sign import Sign, SignAbstractState, SignDomain

program = Program("""
    x += 5
    x -= y
    y += 5
    y -= 3
    x -= 6
    z += 1
""")

domain = SignDomain(["x", "y", "z"])
input_state = SignAbstractState({
    "x": Sign.Negative,
    "y": Sign.Positive,
    "z": Sign.Negative,
})

output_state = program.transform(domain, input_state)
print(output_state)

assert output_state.sign_of("x") == Sign.Negative
assert output_state.sign_of("y") == Sign.Positive
assert output_state.sign_of("z") == Sign.Top
