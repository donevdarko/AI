from constraint import *

if __name__ == '__main__':
    num = int(input())
    
    papers = dict()

    subjects = {
        'AI' : 0,
        'ML' : 0,
        'NLP' : 0
    }

    presentations = {
        'AI' : [],
        'ML' : [],
        'NLP' : []
    }
    
    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        subjects[topic] = subjects[topic] + 1
        paper_info = input()
    # Define the variables
    variables = []
    for key, value in papers.items():
        variables.append(f"{key} ({value})")
        presentations[value].append(f"{key} ({value})")

     
    domain = [f'T{i + 1}' for i in range(num)]
    
    problem = Problem(BacktrackingSolver())
    
    # Change this section if necessary
    problem.addVariables(variables, domain)
    
    # Add the constraints
    
    def four_most(*vals):
        for i in range(1, num+1):
            if vals.count(f"T{i}") > 4:
                return False
        return True
    
    problem.addConstraint(four_most, variables)

    def same_term_subject(*vals):
        return len(set(vals)) == 1
    
    for subject, vars_list in presentations.items():
        if subjects[subject] == 0:
            continue
        if len(vars_list) <= 4:
            problem.addConstraint(same_term_subject, vars_list)

    result = problem.getSolution()
    
    carry = ""
    # Add the required print section
    for paper in sorted(result.keys()):
        
        term = result[paper]
        if paper[6] == "0":
            carry = (f"{paper}: {term}")
        else:
            print(f"{paper}: {term}")

    print(carry)
    
