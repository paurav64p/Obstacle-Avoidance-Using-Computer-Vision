# path_planning.py
import heapq

def a_star(start, goal, graph):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break
        
        for neighbor, cost in graph[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current
    
    return came_from
