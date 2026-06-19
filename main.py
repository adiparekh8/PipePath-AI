from collections import deque

# right, left, down, up
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

def get_neighbors(pos):
    # grab all adjacent squares
    return [(pos[0] + d[0], pos[1] + d[1]) for d in dirs]

class GameState:
    def __init__(self, grid, add_moat=True):
        self.grid = grid
        self.active_nodes = {}
        self.sources = {}
        self.sinks = {}
        self.colors = set()
        
        if add_moat:
            self._build_moat()
        self._scan_grid()

    def _scan_grid(self):
        # find where all the colored dots live
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                if val > 0:  
                    self.colors.add(val)
                    if val not in self.sources:
                        self.sources[val] = (r, c)
                        self.active_nodes[val] = (r, c) # start at the source
                    else:
                        self.sinks[val] = (r, c)

    def _build_moat(self):
        # surround grid with -1 so we dont have to check bounds constantly lol
        moat = -1
        w = len(self.grid[0])
        new_grid = [[moat] * (w + 2)]
        for row in self.grid:
            new_grid.append([moat] + row + [moat])
        new_grid.append([moat] * (w + 2))
        self.grid = new_grid

    def get_active_colors(self):
        # find colors that havent linked up with their sinks yet
        active = set()
        for color in self.colors:
            _, sink, curr = (self.sources[color], self.sinks[color], self.active_nodes[color])
            
            # check if we can insta-connect to the sink
            for d in dirs:
                if (curr[0] + d[0], curr[1] + d[1]) == sink:
                    curr = sink
            if sink != curr:
                active.add(color)
        return active

    def show(self):
        # pretty print with neat ansi blocks
        cmap = [
            "\033[91m", "\033[0m", "\033[32m", "\033[33m", "\033[34m", 
            "\033[35m", "\033[36m", "\033[93m", "\033[94m", "\033[95m", 
            "\033[96m", "\033[92m"
        ]
        out = []
        for row in self.grid:
            colored = [f"{cmap[0] if e < 0 else cmap[e+1] if e < len(cmap)-1 else cmap[-1]}██\033[0m" for e in row]
            out.append("".join(colored))
        print('\n'.join(out))

def is_finished(state: GameState):
    # are we done yet?
    for color in state.colors:
        _, sink, active = state.sources[color], state.sinks[color], state.active_nodes[color]
        if sink != active and (active not in get_neighbors(sink)):
            return False
    return True

def get_children(state, color):
    # find all valid places this color can step into next
    active = state.active_nodes[color]
    children = []
    for nxt in get_neighbors(active):
        if is_valid_move(nxt, state.grid, state.active_nodes, color):
            # spawn a new state with this move
            new_state = GameState([r[:] for r in state.grid], add_moat=False)
            new_state.sources = state.sources.copy()
            new_state.sinks = state.sinks.copy()
            new_state.active_nodes = state.active_nodes.copy()
            
            new_state.active_nodes[color] = nxt
            new_state.grid[nxt[0]][nxt[1]] = color
            children.append(new_state)
    return children

def next_game_states(state: GameState):
    colors = list(state.get_active_colors())
    draining = [state]
    accumulating = []
    
    while colors:
        curr_color = colors.pop()
        while draining:
            curr_state = draining.pop()
            accumulating.extend(get_children(curr_state, curr_color))
        if colors:
            draining = accumulating.copy()
            accumulating = []
            
    # filter out duplicate dead ends
    final_states = []
    for s in accumulating:
        if can_be_finished(s):
            if s not in final_states:
                final_states.append(s)
    return final_states

def is_valid_move(pos, grid, active_nodes, color):
    r, c = pos
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if grid[r][c] == 0: # space must be empty
            # make sure no other wire is sitting here
            return not any(node == pos and nc != color for nc, node in active_nodes.items())
    return False

def can_be_finished(state: GameState):
    # pathfind check to see if a color is completely boxed in
    for color in state.colors:
        if not path_exists(state.active_nodes[color], state.sinks[color], state.grid):
            return False # color is softlocked, gg
    return True

def path_exists(start, end, grid):
    if start == end: return True
    R, C = len(grid), len(grid[0])
    visited = set()
    q = deque([start])

    while q:
        curr = q.popleft()
        if curr == end: return True
        if curr in visited: continue
        visited.add(curr)

        for nxt in get_neighbors(curr):
            if nxt == end: return True
            if 0 <= nxt[0] < R and 0 <= nxt[1] < C:
                if grid[nxt[0]][nxt[1]] == 0:
                    q.append(nxt)
    return False # no path found rip

def find_solution(start_state: GameState):
    stack = [start_state]
    print("starting the solver... buckle up")
    start_state.show()
    
    steps = 0
    while stack:
        steps += 1
        curr = stack.pop(0) # dequeueing 
        
        if steps % 100 == 0:
            print(f"step {steps}...")
            curr.show()

        if not can_be_finished(curr):
            continue # skip this one, its a dead end

        if is_finished(curr):
            print("\nboom! solution found:")
            curr.show()
            return True

        # push new branched paths to the front of the stack
        stack = next_game_states(curr) + stack

    print("no solution found. tragic.")
    return False

# tiny test grid
grid = [
    [1, 0, 2],
    [0, 0, 0],
    [1, 0, 2]
]

game = GameState(grid)
found = find_solution(game)
print(f"Success status: {found}")