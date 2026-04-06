from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = int(input())
    lecture_slots_ML = int(input())
    lecture_slots_R = int(input())
    lecture_slots_BI = int(input())
    
    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13","Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13","Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13","Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]
    
    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    
    # ---Add the variables here--------------------

    ml_l = []
    ml_e = []

    vars = []
    for i in range(lecture_slots_AI):
        problem.addVariable(f"AI_lecture_{i+1}", AI_lectures_domain)
        vars.append(f"AI_lecture_{i+1}")

    for i in range(lecture_slots_R):
        problem.addVariable(f"R_lecture_{i+1}", R_lectures_domain)
        vars.append(f"R_lecture_{i+1}")
    
    for i in range(lecture_slots_BI):
        problem.addVariable(f"BI_lecture_{i+1}", BI_lectures_domain)
        vars.append(f"BI_lecture_{i+1}")

    for i in range(lecture_slots_ML):
        problem.addVariable(f"ML_lecture_{i+1}", ML_lectures_domain)
        vars.append(f"ML_lecture_{i+1}")
        ml_l.append(f"ML_lecture_{i+1}")

    problem.addVariable("ML_exercises", ML_exercises_domain)
    vars.append("ML_exercises")
    ml_e.append("ML_exercises")
    problem.addVariable("AI_exercises", AI_exercises_domain)
    vars.append("AI_exercises")
    problem.addVariable("BI_exercises", BI_exercises_domain)
    vars.append("BI_exercises")

    # ---Add the constraints here----------------
    
    def overlap(val1, val2):
        day1, time1 = val1.split("_")
        day2, time2 = val2.split("_")
        if day1 != day2:
            return True
        if abs(int(time1) - int(time2)) >= 2:
            return True
        return False
    
    for i, var in enumerate(vars):
        for j, var2 in enumerate(vars):
            if i == j:
                continue
            problem.addConstraint(overlap, [var, var2])

    def ml_check(val1, val2):
        day1, time1 = val1.split("_")
        day2, time2 = val2.split("_")
        return time1 != time2
    
    for lecture in ml_l:
        for exercise in ml_e:
            problem.addConstraint(ml_check, [lecture, exercise])


    # ----------------------------------------------------
    solution = problem.getSolution()
    
    print(solution)