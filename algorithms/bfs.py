# BFS - O(V + E) = Vertices + Edges

from collections import deque

# Prepare the Unidirected & Unweighted Graph
graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["johnny"] = []

print(graph)

def person_is_seller(person):
  return person.endswith("m")

def breadth_first_search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []

  while search_queue:
    person = search_queue.popleft()

    if not person in searched:
      if person_is_seller(person):
        print(f"{person} is a mango seller")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)

  return False

breadth_first_search("bob")
