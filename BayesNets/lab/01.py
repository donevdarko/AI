from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("B", "I"),
    ("M", "I"),
    ("I", "R"),
    ("I", "T"),
    ("R", "C"),
    ("T", "C"),
    ("D", "C")
])

cpd_B = TabularCPD(
    variable="B",
    variable_card=2,
    values=[
        [1-0.35],
        [0.35]
    ]
)

cpd_M = TabularCPD(
    variable="M",
    variable_card=2,
    values=[
        [1-0.45],
        [0.45]
    ]
)

cpd_D = TabularCPD(
    variable="D",
    variable_card=2,
    values=[
        [1-0.25],
        [0.25]
    ]
)

cpd_I = TabularCPD(
    variable="I",
    variable_card=2,
    values=[
        [1-0.12, 1-0.65, 1-0.72, 1-0.93],
        [0.12, 0.65, 0.72, 0.93]
    ],
    evidence=["B", "M"],
    evidence_card=[2, 2]
)

cpd_R = TabularCPD(
    variable="R",
    variable_card=2,
    values=[
        [1-0.2, 1-0.8],
        [0.2, 0.8]
    ],
    evidence=["I"],
    evidence_card=[2]
)

cpd_T = TabularCPD(
    variable="T",
    variable_card=2,
    values=[
        [1-0.3, 1-0.85],
        [0.3, 0.85]
    ],
    evidence=["I"],
    evidence_card=[2]
)

cpd_C = TabularCPD(
    variable="C",
    variable_card=2,
    values=[
        [1-0.04, 1-0.32, 1-0.48, 1-0.75, 1-0.55, 1-0.78, 1-0.88, 1-0.97],
        [0.04, 0.32, 0.48, 0.75, 0.55, 0.78, 0.88, 0.97]
    ],
    evidence=["R", "T", "D"],
    evidence_card=[2, 2, 2]
)

model.add_cpds(
    cpd_B,
    cpd_M,
    cpd_D,
    cpd_I,
    cpd_R,
    cpd_T,
    cpd_C
)

print(model.check_model())

infer = VariableElimination(model)

q1 = infer.query(
    variables=["I"],
    evidence={"B": 1, "M": 1}
)
print("\n1) P(I | B=1, M=1)")
print(q1)

q2 = infer.query(
    variables=["R"],
    evidence={"I": 1}
)
print("\n1) P(R | I=1)")
print(q2)

q3 = infer.query(
    variables=["C"],
    evidence={"T": 1}
)
print("\n1) P(C | T=1)")
print(q3)

q4 = infer.query(
    variables=["B"],
    evidence={"I": 1}
)
print("\n1) P(B | I=1)")
print(q4)

q5 = infer.query(
    variables=["M"],
    evidence={"I": 1}
)
print("\n1) P(M | I=1)")
print(q5)

q6 = infer.query(
    variables=["T"],
    evidence={"C": 1, "R": 0}
)
print("\n1) P(T | C=1, R=0)")
print(q6)