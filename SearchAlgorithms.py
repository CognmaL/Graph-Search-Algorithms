import time
from itertools import count
from queue import PriorityQueue
from Space import *
from Constants import *

def draw_path(g:Graph, sc:pygame.Surface, closed_set:list):
    g.start.draw_on_screen(orange, sc)
    g.goal.draw_on_screen(purple, sc)
    for cur_node in reversed(range(len(closed_set))):
        pos_1 = [closed_set[cur_node].x, closed_set[cur_node].y]
        pos_2 = [closed_set[cur_node - 1].x, closed_set[cur_node - 1].y]
        pygame.draw.line(sc, green, pos_1, pos_2)
        pygame.display.flip()
        if closed_set[cur_node - 1] == g.start:
            break
        closed_set[cur_node - 1].draw_on_screen(grey, sc)
        time.sleep(0.1)
        


def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')
    
    open_set = [g.start]
    close_set = []
    father = dict()
    father[g.start] = None
    path_found = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if len(open_set) == 0:
            raise Exception("No way Exception")
        current_node = open_set.pop()
        current_node.draw_on_screen(yellow, sc)
        time.sleep(0.01)
        close_set.append(current_node)

        # Check if node is graph.goal-node
        if current_node == g.goal:
            path_found = True
            break

        # expanding nodes
        for node in g.get_neighbors(current_node):
            if node not in close_set:
                node.draw_on_screen(red, sc)
                time.sleep(0.01) 
                open_set.append(node)
                father[node] = current_node
        close_set[-1].draw_on_screen(blue, sc)

    goal = g.goal
    path = []
    if path_found:
        path.append(goal)
        while father[goal] is not None:
            path.append(father[goal])
            goal = father[goal]
        path.reverse()
    draw_path(g, sc, path)
    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    # Dung Queue
    print('Implement BFS algorithm')
    
    open_set = [g.start]
    close_set = []
    father = dict()
    father[g.start] = None
    path_found = False
    g.start.draw_on_screen(orange,sc)
    time.sleep(0.05)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if len(open_set) == 0:
            raise Exception("No way Exception")
        current_node = open_set.pop(0)
        current_node.draw_on_screen(yellow, sc)
        time.sleep(0.05)
        close_set.append(current_node)
        close_set[-1].draw_on_screen(blue, sc)

        # Check if node is graph.goal-node
        if current_node == g.goal:
            path_found = True
            break

        # expanding nodes
        for node in g.get_neighbors(current_node):
            if node not in close_set:
                node.draw_on_screen(red, sc)
                time.sleep(0.01) 
                open_set.append(node)
                father[node] = current_node
                close_set.append(node)
        close_set[-1].draw_on_screen(blue, sc)

    goal = g.goal
    path = []
    if path_found:
        path.append(goal)
        while father[goal] is not None:
            path.append(father[goal])
            goal = father[goal]
        path.reverse()
    draw_path(g, sc, path)
    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')

#------------------------------------------------------

def Euclidean_distance(A: Node, B: Node): 
    # Euclidean fance
    return math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)

def UCS(g:Graph, sc: pygame.Surface):
    open_set = PriorityQueue()
    closed_set = []
    path_found = False
    father = dict()
    father[g.start] = None
    unique = count()
    open_set.put((0, next(unique), g.start))
    while open_set.empty() == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        current_weight, _, current_node = open_set.get()
        closed_set.append(current_node)
        current_node.draw_on_screen(yellow, sc)
        time.sleep(0.05)
        closed_set[-1].draw_on_screen(blue, sc)

        if g.is_goal(current_node):
            path_found = True
            break

        for node in g.get_neighbors(current_node):
            if node not in closed_set:
                node.draw_on_screen(red, sc)
                time.sleep(0.05)
                open_set.put((current_weight + Euclidean_distance(current_node, node), next(unique), node))
                father[node] = current_node
                closed_set.append(node)
        closed_set[-1].draw_on_screen(blue, sc)

    goal = g.goal
    path = []
    if path_found:
        path.append(goal)
        while father[goal] is not None:
            path.append(father[goal])
            goal = father[goal]
        path.reverse()

    draw_path(g, sc, path)

def Manhattan(node_start:Node, node_end:Node):
    return abs(node_start.x - node_end.x) + abs(node_start.y - node_end.y)

def AStar_Search(g:Graph, sc:pygame.Surface, open_set, closed_set, father, cost):
    temp:int = []

    total_estimate = open_set[list(open_set.keys())[0]] + cost[list(open_set.keys())[0]]
    node_low_cost = list(open_set.keys())[0]
    for value in open_set:
        temp.append(open_set[value] + cost[value])
    
    for value in open_set:
        if (open_set[value] + cost[value]) == min(temp) and open_set[value] < total_estimate:
            node_low_cost = value
            total_estimate = open_set[value] + cost[value]

    
    current_node = g.grid_cells[node_low_cost]
    current_node.set_color(yellow)
    current_node.draw(sc)
    pygame.display.flip()
    time.sleep(0.05)

    if (g.is_goal(current_node)):
        g.goal.set_color(purple)
        g.goal.draw(sc)
        g.start.set_color(orange)
        g.start.draw(sc)
        pygame.display.flip()
        time.sleep(0.05)
        return

    open_set.pop(current_node.value)
    closed_set.append(current_node.value)

    node_around = g.get_neighbors(current_node)

    for node in node_around:
        if node.value not in closed_set:
            new_cost = cost[current_node.value] + Euclidean_distance(node, current_node)
            if node.value not in list(open_set.keys()):
                open_set[node.value] = Manhattan(node, g.goal)
                cost[node.value] = new_cost
                father[node.value] = current_node.value
                node.set_color(red)
                node.draw(sc)
                pygame.display.flip()
                time.sleep(0.05)
            else:
                old_cost = cost[node.value]
                if old_cost > new_cost:
                    cost[node.value] = new_cost
                    father[node.value] = current_node.value
                    node.set_color(red)
                    node.draw(sc)
                    pygame.display.flip()
                    time.sleep(0.05)
        else:
            new_cost = cost[current_node.value] + Euclidean_distance(node, current_node)
            old_cost = cost[node.value]
            if old_cost > new_cost:
                cost[node.value] = new_cost
                father[node.value] = current_node.value
                node.set_color(red)
                node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)
    
    current_node.set_color(blue)
    current_node.draw(sc)   
    pygame.display.flip()
    time.sleep(0.01)
    
    AStar_Search(g, sc, open_set, closed_set, father, cost)

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')
    #path_found = False

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    AStar_Search(g, sc, open_set, closed_set, father, cost)
    draw_path(g, sc,closed_set )


    #TODO: Implement A* algorithm using open_set, closed_set, and father
    #raise NotImplementedError(print('Not implemented'))
