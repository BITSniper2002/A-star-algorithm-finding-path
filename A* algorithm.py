class A_star:
    def __init__(self,graph):
        self.graph = graph

    def calculate_cost(self,pos,goal):
        #here we use Euler distance
        px,py = pos[0],pos[1]
        gx,gy = goal[0],goal[1]
        return round(math.sqrt((px-gx)**2+(py-gy)**2),2)

    def find_neighbors(self,pos):
        #assume that there are obstacles denoted by '*'
        px,py = pos[0],pos[1]
        x_max,x_min = len(self.graph)-1,0
        y_max, y_min = len(self.graph[0])-1, 0
        neighbors = []
        movement = [(1,0),(-1,0),(0,1),(0,-1)]
        for m in movement:
            nx,ny = px+m[0],py+m[1]
            if nx < x_min or nx > x_max or ny < y_min or ny > y_max or self.graph[nx][ny] == '*':
                continue
            neighbors.append((nx,ny))
        return neighbors


    def search(self,start,end):
        import queue
        q = queue.PriorityQueue()
        came_from = dict()
        cost = dict()
        came_from[start] = None
        cost[start] = 0
        q.put((0,start))

        while not q.empty():
            curr = q.get()[1]
            if curr == end:
                break
            neighbors = self.find_neighbors(curr)
            for n in neighbors:
                new_cost = cost[curr] + self.calculate_cost(n,end)
                if n not in cost or new_cost < cost[n]:
                    cost[n] = new_cost
                    q.put((new_cost,n))
                    came_from[n] = curr

        path = []
        p = end
        while p != None:
            path.append(p)
            p = came_from[p]
        path.reverse()
        return path

    def display_graph(self, graph=None):
        if graph == None:
            graph = self.graph
        dim = len(graph[0])
        print('Here is the graph:')
        print('  ', '-' * (2 * dim + 3))
        for row in graph:
            print('   |', *row, '|')
        print('  ', '-' * (2 * dim + 3))


    def display_path(self,start,end):
        path = self.search(start,end)
        tmp_graph = self.graph
        for i,p in enumerate(path):
            if i == len(path) - 1:
                tmp_graph[p[0]][p[1]] = '☺'
                break
            curr_x,curr_y = p[0],p[1]
            next_x,next_y = path[i+1][0],path[i+1][1]
            if curr_x != next_x:
                if curr_x - 1 == next_x:
                    tmp_graph[curr_x][curr_y] = '↑'
                else:
                    tmp_graph[curr_x][curr_y] = '↓'
            else:
                if curr_y - 1 == next_y:
                    tmp_graph[curr_x][curr_y] = '←'
                else:
                    tmp_graph[curr_x][curr_y] = '→'
        self.display_graph(tmp_graph)


if __name__ == '__main__':
    grid = [[' ' for _ in range(11)] for _ in range(11)]
    grid[3][3] = '*'
    grid[4][4] = '*'
    grid[5][3] = '*'
    grid[6][4] = '*'
    grid[7][4] = '*'
    grid[8][4] = '*'
    grid[9][3] = '*'
    A = A_star(grid)
    A.display_graph()
    print(A.search((9,1),(9,9)))
    A.display_path((9,1),(9,9))
