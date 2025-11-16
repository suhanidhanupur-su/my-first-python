film = [input("first film name --> "), input("Second --> "), input("Third --> ")]
film1 = film.copy()
film1.reverse()

if(film == film1):
    print("its a Palidrom")
else:
    print("not Palidrom")

print(film.count("a"))
film.sort()

print(film)