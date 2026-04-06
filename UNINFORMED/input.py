    
if __name__ == "__main__":
    
    


    vlezniTorki = tuple(input().split(";"))
    pillars = []
    for torka in vlezniTorki:
        if torka:
            pillars.append(tuple(map(int, torka.split(","))))
        else:
            pillars.append(())
    pillars = tuple(pillars)
    print(pillars)
    
