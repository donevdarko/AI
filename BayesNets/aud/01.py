import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning)

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

B = 'Bad food'
S = 'Stomach ache'
D = 'Doctor visit'

model = DiscreteBayesianNetwork([
    (B, S),
    (S, D)
])

CPD_B = TabularCPD(
    variable=B,
    variable_card=2,
    values=[
        [0.7],
        [0.3]
    ]
)

CPD_S = TabularCPD(
    variable=S,
    variable_card=2,
    values=[
        [0.9, 0.3],
        [0.1, 0.7]
    ],
    evidence=[B],
    evidence_card=[2]
)

CPD_V = TabularCPD(
    variable=D,
    variable_card=2,
    values=[
        [0.95, 0.2],
        [0.05, 0.8]
    ],
    evidence=[S],
    evidence_card=[2]
)

cpds = [CPD_B, CPD_S, CPD_V]

model.add_cpds(*cpds)

# print(model.check_model())

infer = VariableElimination(model)

q1 = infer.query(
    variables=[B, S],
    evidence={D:1}
)

print(q1)

print(q1.values)
print(q1.values[0][1])