from constraint import *

if __name__ == '__main__':
    
    bands = dict()
    
    band_info = input()
    while band_info != 'end':
        band, time, genre = band_info.split(' ')
        bands[band] = (time, genre)
        band_info = input()
    
    # Add the variables here
    variables=[]
    stodvaeski=[]
    mali=[]
    genres = {
        'punk' : [],
        'rock' : [],
        'metal' : []
    }


    for band, (genre, time) in bands.items():
        genres[genre].append(f"{band} (('{genre}', '{time}'))")
        variables.append(f"{band} (('{genre}', '{time}'))")
        if int(time) == 120:
            stodvaeski.append(f"{band} (('{genre}', '{time}'))")
        else:
            mali.append(f"{band} (('{genre}', '{time}'))")
        
     
    domain = [f'S{i + 1}' for i in range(3)]
    
    problem = Problem(BacktrackingSolver())
    
    # Change this section if necessary
    problem.addVariables(variables, domain)
    
    # Add the constraints here
    problem.addConstraint(AllDifferentConstraint(), stodvaeski)

    def mali_limit(*vals):
        for i in range(1, 4):
            stage=f"S{i}"
            count = 0
            for val in vals:
                if val==stage:
                    count+=1
            if count > 5:
                return False
        return True
    
    problem.addConstraint(mali_limit, mali)

    def totalTimeWrapper(gen):
        def genreTime(*vals):
            if total_time>300:
                return True
            return len(set(vals))==1

        local_vars = genres[gen]
        if len(local_vars) < 2:
            return
        total_time=0
        for band, (genre, time) in bands.items():
            if genre!=gen:
                continue
            total_time+=int(time)
        problem.addConstraint(genreTime, local_vars)
        

    for gen in genres.keys():
        totalTimeWrapper(gen)


        
    result = problem.getSolution()
    carry=""
    # Add the printing section here
    for br in sorted(result):
        if br[5]=='0':
            carry=br
            continue
        print(f'{br}: {result[br]}')
    print(f'{carry}: {result[carry]}')
