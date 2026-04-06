from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    
    # Add the domains
    domain = [0, 1]
    problem.addVariable("Marija_attendance", domain)
    problem.addVariable("Simona_attendance", domain)
    problem.addVariable("Petar_attendance", domain)
    problem.addVariable("time_meeting", [13, 14, 16, 19])
    # ----------------------------------------------------

    problem.addConstraint(lambda s: s == 1, ["Simona_attendance"])

    problem.addConstraint(lambda s, m, p: m + p >= 1, ["Simona_attendance", "Marija_attendance", "Petar_attendance"])

    def simona(s, t):
        if s == 0:
            return True
        return t in (13, 14, 16, 19)
    problem.addConstraint(simona, ['Simona_attendance', 'time_meeting'])

    def maria(m, t):
        if m == 0:
            return True
        return t in [14, 15, 18]
    problem.addConstraint(maria, ['Marija_attendance', 'time_meeting'])

    def petar(p, t):
        if p == 0:
            return True
        return t in [12, 13, 16, 17, 18, 19]
    problem.addConstraint(petar, ['Petar_attendance', 'time_meeting'])


    
    # ----------------------------------------------------
    
    solutions = problem.getSolutions()
    for solution in sorted(solutions, key=lambda x: x["Marija_attendance"], reverse=True):
        print({k: solution[k] for k in ["Simona_attendance", "Marija_attendance", "Petar_attendance", "time_meeting"]})