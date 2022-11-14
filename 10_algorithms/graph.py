graph = [
  [0, 1, 1, 0, 1, 0, 0],
  [1, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1, 0, 1],
  [0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 1, 0]
]

vertex_list = {
    0: "dom",
    1: "szkola",
    2: "kosciol",
    3: "bar",
    4: "szpital",
    5: "kino",
    6: "teatr"
}


for row_id, row in enumerate(graph):
    from_name_place = vertex_list[row_id]
    for col_id, _ in enumerate(row):
        to_name_place = vertex_list[col_id]
        if graph[row_id][col_id] == 1:
            print(from_name_place, "-", to_name_place)


for i in graph:
    from_name_place = vertex_list[graph.index(i)]
    for j in range(len(i)):
        to_name_place = vertex_list[j]
        #print(to_name_place, j)
        if i[j] == 1:
            print(from_name_place, "-", to_name_place)