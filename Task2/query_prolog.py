from pyswip import Prolog

prolog = Prolog()
prolog.consult("facts.pl")

# Example query
print("Querying: parent(alice, X)")
for result in prolog.query("parent(alice, X)"):
    print(result)
