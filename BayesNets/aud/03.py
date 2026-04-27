# =========================================================
# IMPORT LIBRARIES
# =========================================================

# DiscreteBayesianNetwork:
# This class defines the structure of the Bayesian Network,
# i.e., which variables exist and how they depend on each other.
from pgmpy.models import DiscreteBayesianNetwork

# TabularCPD:
# Used to define conditional probability tables (CPTs).
# For each node, we specify how its probabilities depend on its parents.
from pgmpy.factors.discrete import TabularCPD

# VariableElimination:
# Inference algorithm used to compute probabilities like P(X | evidence).
from pgmpy.inference import VariableElimination


# =========================================================
# VARIABLE DEFINITIONS
# =========================================================

# Variables used:
#
# HighIncome      -> H
# GoodMarketing   -> M
# Interested      -> I
# ReadsReviews    -> R
# BrowseWebsite   -> B
# Discount        -> D
# Purchase        -> P
#
# All variables are binary:
# 0 = No
# 1 = Yes


# =========================================================
# 1. DEFINE NETWORK STRUCTURE
# =========================================================

# Each tuple ("A", "B") means A -> B
# (B depends on A)
model = DiscreteBayesianNetwork([
    ("H", "I"),
    ("M", "I"),
    ("I", "R"),
    ("I", "B"),
    ("R", "P"),
    ("B", "P"),
    ("D", "P")
])


# =========================================================
# 2. DEFINE PROBABILITIES (CPTs)
# =========================================================

# ---------------------------------------------------------
# P(H)
# ---------------------------------------------------------
cpd_H = TabularCPD(
    variable="H",
    variable_card=2,
    values=[
        [0.7],  # P(H=0)
        [0.3]   # P(H=1)
    ]
)

# ---------------------------------------------------------
# P(M)
# ---------------------------------------------------------
cpd_M = TabularCPD(
    variable="M",
    variable_card=2,
    values=[
        [0.6],  # P(M=0)
        [0.4]   # P(M=1)
    ]
)

# ---------------------------------------------------------
# P(D)
# ---------------------------------------------------------
cpd_D = TabularCPD(
    variable="D",
    variable_card=2,
    values=[
        [0.75],  # P(D=0)
        [0.25]   # P(D=1)
    ]
)

# ---------------------------------------------------------
# P(I | H, M)
# ---------------------------------------------------------
# Order of columns:
# (H=0,M=0), (H=0,M=1), (H=1,M=0), (H=1,M=1)
cpd_I = TabularCPD(
    variable="I",
    variable_card=2,
    values=[
        [0.90, 0.30, 0.25, 0.05],
        [0.10, 0.70, 0.75, 0.95]
    ],
    evidence=["H", "M"],
    evidence_card=[2, 2]
)

# ---------------------------------------------------------
# P(R | I)
# ---------------------------------------------------------
cpd_R = TabularCPD(
    variable="R",
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=["I"],
    evidence_card=[2]
)

# ---------------------------------------------------------
# P(B | I)
# ---------------------------------------------------------
cpd_B = TabularCPD(
    variable="B",
    variable_card=2,
    values=[
        [0.75, 0.15],
        [0.25, 0.85]
    ],
    evidence=["I"],
    evidence_card=[2]
)

# ---------------------------------------------------------
# P(P | R, B, D)
# ---------------------------------------------------------
# Column order:
# (R=0,B=0,D=0)
# (R=0,B=0,D=1)
# (R=0,B=1,D=0)
# (R=0,B=1,D=1)
# (R=1,B=0,D=0)
# (R=1,B=0,D=1)
# (R=1,B=1,D=0)
# (R=1,B=1,D=1)
cpd_P = TabularCPD(
    variable="P",
    variable_card=2,
    values=[
        [0.95, 0.65, 0.50, 0.22, 0.45, 0.20, 0.10, 0.02],
        [0.05, 0.35, 0.50, 0.78, 0.55, 0.80, 0.90, 0.98]
    ],
    evidence=["R", "B", "D"],
    evidence_card=[2, 2, 2]
)


# =========================================================
# 3. ADD CPDs TO MODEL
# =========================================================

model.add_cpds(
    cpd_R,
    cpd_H,
    cpd_M,
    cpd_B,
    cpd_D,
    cpd_I,
    cpd_P
)

print("Model valid:", model.check_model())


# =========================================================
# 4. CREATE INFERENCE OBJECT
# =========================================================

infer = VariableElimination(model)


# =========================================================
# 5. QUERIES
# =========================================================

# ---------------------------------------------------------
# Query 1
# ---------------------------------------------------------
q1 = infer.query(
    variables=["I"],
    evidence={"H": 1, "M": 1}
)

print("\n1) P(Interested | HighIncome=1, GoodMarketing=1)")
print(q1)


# ---------------------------------------------------------
# Query 2
# ---------------------------------------------------------
q2 = infer.query(
    variables=["R"],
    evidence={"I": 1}
)

print("\n2) P(ReadsReviews | Interested=1)")
print(q2)


# ---------------------------------------------------------
# Query 3
# ---------------------------------------------------------
q3 = infer.query(
    variables=["P"],
    evidence={"R": 1, "B": 1, "D": 1}
)

print("\n3) P(Purchase | ReadsReviews=1, BrowseWebsite=1, Discount=1)")
print(q3)


# ---------------------------------------------------------
# Query 4
# ---------------------------------------------------------
q4 = infer.query(
    variables=["H"],
    evidence={"I": 1}
)

print("\n4) P(HighIncome | Interested=1)")
print(q4)


# ---------------------------------------------------------
# Query 5
# ---------------------------------------------------------
q5 = infer.query(
    variables=["M"],
    evidence={"I": 1}
)

print("\n5) P(GoodMarketing | Interested=1)")
print(q5)


# ---------------------------------------------------------
# Query 6
# ---------------------------------------------------------
q6 = infer.query(
    variables=["B"],
    evidence={"P": 1, "R": 0}
)

print(q6.values[1])

print("\n6) P(BrowseWebsite | Purchase=1, ReadsReviews=0)")
print(q6)