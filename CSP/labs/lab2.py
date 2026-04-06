from constraint import Problem, BacktrackingSolver


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}

    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}

    return families, rooms



if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.

    for family_name, family_data in families.items():
        valid_rooms = []

        for room_id, room_data in rooms.items():
            if room_data['capacity'] < family_data['size']:
                continue
            if not all(req in room_data['amenities'] for req in family_data['requirements']):
                continue

            valid_rooms.append(room_id)
        
        valid_rooms.append(None)

        problem.addVariable(family_name, valid_rooms)


    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.
    
    def unique_rooms(*ass):
        used = [a for a in ass if a is not None]
        return len(used) == len(set(used))
    
    problem.addConstraint(unique_rooms, list(families.keys()))

    def fair_check(family, others, valid_rooms):
        if family is not None:
            return True
        for r in valid_rooms:
            if r not in others:
                return False
        return True

    family_names = list(families.keys())

    for fam in family_names:
        other_fams = [f for f in family_names if f!= fam]

        problem.addConstraint(
            lambda fam_val, *others_val, fam = fam: fair_check(fam_val, others-vals, family_valid)
        )


    solutions = problem.getSolutions()  # Ne menuvaj! Do not modify!

    best_solution = None
    best_score = -1

    for solution in solutions:
        assigned_rooms = set(v for v in solution.values() if v is not None)
        

        valid = True
        for family_name, room_id in solution.items():
            if room_id is None:
                for r in rooms:
                    if r not in assigned_rooms:
                        room = rooms[r]
                        family = families[family_name]

                        if (room['capacity'] >= family['size'] and all(req in room['amenities'] for req in family['requirements'])):
                            valid = False
                            break
                if not valid:
                    break
        if not valid:
            continue

        score = sum(families[f]['size'] for f in solution if solution[f] is not None)
        if score > best_score:
            best_score = score
            best_solution = solution

    # Ispechatete go najdobroto reshenie vo baraniot format.
    # Print the best solution in the required format.
    
    if best_solution:
        for room, family in best_solution.items():
            if family is None:
                continue
            print(f"{room}->{family}")
