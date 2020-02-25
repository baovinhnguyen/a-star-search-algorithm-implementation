print(" Please enter the order of your pancakes. \n"
      " The first is the top of the stack, and the last is the bottom. \n"
      " For example:  10 8 5 6 9 3 5 1 2 4 7.")

initial = [int(m) for m in input().split()]

def heuristic(n):
    h = 0
    for i in range(len(n) - 1):
        if abs(n[i] - n[i+1]) > 1:
            h += 1
    if n[-1] < len (n) - 1:
        h += 1
    return h

class Node:
  def __init__(self, state, cost, parents):
    self.backcost = cost + 1
    self.fwcost = heuristic(state)
    self.state = state
    self.parents = parents + [state]

# List to store the frontier
q = []
# List to store visited nodes
visited = []

# Use list to check existing nodes, sort after each insertion
q.append((0, Node(initial, 0, [])))
q = sorted(q)

# While the list is not empty:
while len(q) > 0:
    current = q.pop(0)
    current_node = current[1]
    # if there is solution, return result and exit
    if current_node.state == sorted(initial, reverse=True):
        print("A* algorithm takes " + str(len(current_node.parents)-1) + " flip(s):")
        for i in range(len(current_node.parents)):
            print(current_node.parents[i])
        print('Number of nodes visited: ' + str(len(visited) + 1))
        break

    current_state = current_node.state
    for i in range(2, len(current_state) + 1): # flip range is from the second cake
        up_stack = current_state[:i]
        up_stack.reverse()
        next_state = up_stack + current_state[i:]
        next_node = Node(next_state, current_node.backcost, current_node.parents)
        cost = next_node.backcost + next_node.fwcost
        in_queue = next_state in [item[1].state for item in q]

        if (not next_state in visited) and (not in_queue): # if state is not visited and state is not in the queue
            q.append((cost, next_node))
            q = sorted(q, key=lambda ele: ele[0])
        elif in_queue: # if state is currently in queue
            ind_next_state = [item[1].state for item in q].index(next_state)
            if q[ind_next_state][0] > cost:  # if there is a new shorter path to the same node in queue
                q.pop(ind_next_state)
                q.append((cost, next_node))
                q = sorted(q, key=lambda ele: ele[0])

    visited.append(current_state)
