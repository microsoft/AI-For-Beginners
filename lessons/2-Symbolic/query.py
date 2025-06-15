from rdflib import Graph

g = Graph()
g.parse("webtech.owl", format="xml")

print("All browsers and what they support:")
q1 = """
PREFIX wt: <http://example.org/webtech#>
SELECT ?browser ?label ?tech ?techlabel
WHERE {
    ?browser a wt:Browser ;
             rdfs:label ?label ;
             wt:supports ?tech .
    ?tech rdfs:label ?techlabel .
}
"""
for row in g.query(q1):
    print(f"{row.label} supports {row.techlabel}")

print("\nWhich technology does CSS3 style?")
q2 = """
PREFIX wt: <http://example.org/webtech#>
SELECT ?styled ?label
WHERE {
    wt:CSS3 wt:styles ?styled .
    ?styled rdfs:label ?label .
}
"""
for row in g.query(q2):
    print(f"CSS3 styles {row.label}")

print("\nAll programming languages in the ontology:")
q3 = """
PREFIX wt: <http://example.org/webtech#>
SELECT ?lang ?label
WHERE {
    ?lang a wt:ProgrammingLanguage ;
          rdfs:label ?label .
}
"""
for row in g.query(q3):
    print(row.label)