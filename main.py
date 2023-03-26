def hamiltonian_cycle(graph):
  n = len(graph)
  path = [-1] * n
  path[0] = 0
  if not hamiltonian_cycle_util(graph, path, 1):
    print("No Hamiltonian cycle found.")
  else:
    print("Hamiltonian cycle:")
    print(path)


def hamiltonian_cycle_util(graph, path, pos):
  if pos == len(graph):
    if graph[path[pos - 1]][path[0]] == 1:
      return True
    else:
      return False
  for v in range(1, len(graph)):
    if is_safe(v, graph, path, pos):
      path[pos] = v
      if hamiltonian_cycle_util(graph, path, pos + 1):
        return True
      path[pos] = -1
  return False


def is_safe(v, graph, path, pos):
  if graph[path[pos - 1]][v] == 0:
    return False
  for i in range(pos):
    if path[i] == v:
      return False
  return True


## Output shoub be  [0,1,2,3]
graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
hamiltonian_cycle(graph)
