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
        rooms[int(room_id)] = {
            'floor': int(floor),
            'capacity': int(capacity),
            'amenities': amenities
        }

    return families, rooms


if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()


    family_valid_rooms = {}

    for family_name, family_data in families.items():
        valid_rooms = []

        for room_id, room_data in rooms.items():
            if room_data['capacity'] < family_data['size']:
                continue
            if not all(req in room_data['amenities'] for req in family_data['requirements']):
                continue

            valid_rooms.append(room_id)

        family_valid_rooms[family_name] = valid_rooms[:]

        valid_rooms.append(None)
        problem.addVariable(family_name, valid_rooms)



    def unique_rooms(*ass):
        used = [a for a in ass if a is not None]
        return len(used) == len(set(used))

    problem.addConstraint(unique_rooms, list(families.keys()))


    def fair_check(family_val, others_vals, valid_rooms):
        if family_val is not None:
            return True

        for r in valid_rooms:
            if r not in others_vals:
                return False  

        return True

    family_names = list(families.keys())

    for fam in family_names:
        other_fams = [f for f in family_names if f != fam]

        problem.addConstraint(
            lambda fam_val, *others_vals, fam=fam:
                fair_check(fam_val, others_vals, family_valid_rooms[fam]),
            [fam] + other_fams
        )

    
    solutions = problem.getSolutions()

    best_solution = None
    best_score = -1

    for solution in solutions:
        score = sum(
            families[f]['size']
            for f in solution
            if solution[f] is not None
        )

        if score > best_score:
            best_score = score
            best_solution = solution


    if best_solution:
        assigned = [(room, family) for family, room in best_solution.items() if room is not None]
        assigned.sort()
        print("Best assignment:")
        for room, family in assigned:
            print(f"{family}->{room}")