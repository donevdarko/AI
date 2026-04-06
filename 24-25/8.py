from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    movies = dict()

    n = int(input())
    for _ in range(n):
        film_info = input()
        film, genre, time = film_info.split(' ')
        movies[film] = (float(time), genre)
    
    l_days = int(input())
    
    # Tuka definirajte gi promenlivite i domenite
    vars = []

    for movie, (time, genre) in movies.items():
        vars.append(movie)

    domain = []
    for day in range(1, l_days+1):
        for hours in range(12, 24):
            for cinemaNum in range(1, 3):
                domain.append((day, hours, cinemaNum))
    
    problem.addVariables(vars, domain)

     
    # Tuka dodadete gi ogranichuvanjata
    
    def overlap_wrapper():
        for i, movie1 in enumerate(vars):
            for j, movie2 in enumerate(vars):
                if i >= j:
                    continue

                r1 = movies[movie1][0]
                r2 = movies[movie2][0]

                def not_overlap(val1, val2, r1=r1, r2=r2):
                    day1, hour1, cinema1 = val1
                    day2, hour2, cinema2 = val2

                    if cinema1 != cinema2:
                        return True
                    if day1 != day2:
                        return True

                    
                    if hour1 + r1 < hour2 or hour2 + r2 < hour1:
                        return True

                    return False

                problem.addConstraint(not_overlap, (movie1, movie2))


    overlap_wrapper()



    horros = []
    for movie, (time, genre) in movies.items():
        if genre != "horror":
            continue
        horros.append(movie)

    def horror_time(*vals):
        for val in vals:
            day, hour, cinema = val
            if hour < 21:
                return False
        return True
    if horros:
        problem.addConstraint(horror_time, horros)
    


    smol = []
    for movie, (time, genre) in movies.items():
        if time >= 2:
            continue
        smol.append(movie)

    def smol_constraint(val1, val2):
        day1, hour1, cinema1 = val1
        day2, hour2, cinema2 = val2
        if day1 == day2:
            return True
        return False

    if smol:
        for i, movie in enumerate(smol):
            for j, movie2 in enumerate(smol):
                if i == j:
                    continue
                problem.addConstraint(smol_constraint, (movie, movie2))
                
                
        
    result = problem.getSolution()
    
    # Tuka dodadete go kodot za pechatenje
    
    for name, vals in (sorted(result.items())):
        day, hour, cinema = vals
        print(f"{name}: Day {day} {hour}:00 - Cinema {cinema}")