from pyswip import Prolog

prolog = Prolog()
prolog.consult("simpsons.pl")
# Example queries
queries = [
    "grandparent(abe, X)",
    "parent(marge, Y)",
    "grandparent(mona, X)"
]
for query in queries:
    print(f"Querying: {query}")
    for result in prolog.query(query):
        print(result)
