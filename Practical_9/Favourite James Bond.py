def favourite_bond_actor(birth_year):
    bond_actors = {
        1973: "Roger Moore",
        1987: "Timothy Dalton",
        1995: "Pierce Brosnan",
        2006: "Daniel Craig"
    }
    
    for start_year, actor in bond_actors.items():
        if birth_year + 18 - start_year >= 0:
            return actor

#Example
birth_year = 1990
print(f"Your favourite James Bond actor is: {favourite_bond_actor(birth_year)}")