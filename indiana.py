def solution(string):

    #vars init
    temp = " ".join(string.split("\n"))
    args = temp.split()

    charge = int(args.pop(0))
    room_count = int(args.pop(0))
    corridor_count = int(args.pop(0))
    
    graph = []
    for i in range(room_count):
        graph.append([0] * room_count)

    for i in range(corridor_count):
        x = int(args.pop(0))
        y = int(args.pop(0))
        graph[x][y] = int(args.pop(0))
        graph[y][x] = graph[x][y]

    values = []
    for i in range(room_count):
        values.append(int(args.pop(0)))
    
    #actual func 
    def adj(v):
        res = []
        for i in range(len(graph[v])):
            if graph[v][i] != 0:
                res.append(i)
        return res
        
    def check(fr, to, visited, charge):
        visited[fr] = True
        if fr == to:
            return True

        for next in adj(fr):
            if visited[next] or charge < graph[fr][next]:
                continue
            if check(next, to, visited, charge - graph[fr][next]): return True

        return False

    res = values[0]
    
    for room in range(1, room_count):
        if check(0, room, [False] * room_count, charge) and values[room] > res:
            res = values[room]

    return res

#tests
assert solution("15 4 4 0 1 5 0 2 10 1 3 12 2 3 5 5 10 20 21") == 21
assert solution("17 8 12 0 6 12 0 2 15 2 6 5 2 5 1 6 5 3 5 3 1 6 7 15 7 3 2 3 4 88 5 4 5 5 1 11 1 4 2 5 99 10 38 102 30 1 999") == 38
