import heapq
import tkinter as tk
from tkinter import ttk

# Define your places and their coordinates
places = {
    "School Entrance": (500, 650),
    "Mid Str-2nd Flr": (500, 600),
    
    # EAST
    "Str1": (410, 600),
    "Student Center": (280, 600),
    "Str1-2nd Flr": (100, 600),
    "ADMINISTRATION": (100, 550),
    "BOARD ROOM": (180, 550),
    "UNIVERSITY PRES": (260, 550),
    "VP ADMIN": (340, 550),
    "VP ACAD": (410, 550),
    "VP RDE": (455, 550),
    "HRMO": (500, 550),
    "REGISTRAR": (590, 550),    
    
    "2 ways": (100, 500),
    "ACCOUNTING": (100, 415),
    "CASHIER": (100, 365),
    "BUDGET": (100, 315),
    "COLLEGE PRES": (100, 265),
    "Str2-down": (165, 265),
    "CANTEEN": (165, 150),
    "Str3-2nd Flr": (100, 150),
    "CATERING": (270, 150),
    "Str4-2nd Flr": (360, 150),
 
    "USC Office": (425, 100),
    
    "LIBRARY": (500, 150),
    
    "Str1-down": (200, 500),
    "SUPPLY": (200, 450),
    "COA": (200, 380),
    "way(1)": (270, 500),
    "COA BODEGA": (270, 380),
    "ICT Office": (270, 250),
    
    "PARKING LOT": (520, 340),
    "PL1" : (560, 340),
     "PL2" : (600, 340),
      "PL3" : (640, 340),
       "PL4" : (680, 340),
    "PL5" : (520, 375),
     "PL6" : (560, 375),
       "PL7" : (600, 375),
        "PL8" : (640, 375),
         "PL9" : (680, 375),
       
    # WEST
    "Str2": (590, 600),
    "REGISTRAR": (590, 550),
    "Str2-2nd Flr": (900, 600),
    "PLANNING": (900, 550),
    "BUILDING & ESTATES": (900, 450),
    "EXIT": (900, 340),
    "NSTP Office": (900, 250),
    "DRRMO": (800, 250),
    "FITNESS STUDIO": (700, 250),
    "DANCE STUDIO": (600, 250),
    
    "Str5-2nd Flr": (640, 150),
    "CLINIC": (690, 150),
    "GUIDANCE": (740, 150),
    "PLACEMENT": (800, 150),
    "SAO": (845, 150),
    "Str6-2nd Flr": (900,150),

    
}

# Define paths between locations
paths = {
    ("School Entrance", "Mid Str-2nd Flr"):1,
    ("Mid Str-2nd Flr", "Str1"):2,
    ("Mid Str-2nd Flr", "Str2"):2,
    
    # EAST
    ("School Entrance", "Str1"):1,
    ("Str1", "Student Center"):2,
    ("Str1", "VP ACAD"):2,
    ("Student Center", "Str1-2nd Flr"):3,
    ("Str1-2nd Flr", "ADMINISTRATION"):4,
    ("ADMINISTRATION", "2 ways"):5,
    ("ADMINISTRATION", "BOARD ROOM"):5,
    ("BOARD ROOM", "UNIVERSITY PRES"):6,
    ("UNIVERSITY PRES", "VP ADMIN"):7,
    ("VP ADMIN", "VP ACAD"):7,
    ("VP ACAD", "VP RDE"):3,
    ("VP RDE", "HRMO"):4,
    ("HRMO", "REGISTRAR"):5,
    
    ("2 ways", "ACCOUNTING"):6,
    ("ACCOUNTING", "CASHIER"):7,
    ("CASHIER", "BUDGET"):8,
    ("BUDGET", "COLLEGE PRES"):9,
    ("COLLEGE PRES","Str2-down"):10,
    ("Str2-down", "CANTEEN"):11,   
    ("CANTEEN", "CATERING"):12,
    ("CANTEEN", "Str3-2nd Flr"):12,
    ("CATERING", "Str4-2nd Flr"):13,
    ("Str4-2nd Flr", "USC Office"):14,
    ("Str4-2nd Flr","LIBRARY"):14,
    ("LIBRARY", "USC Office"):11,
    
    ("2 ways", "Str1-down"):6,
    ("Str1-down", "SUPPLY"):7,
    ("SUPPLY", "COA"):8,
    ("Str1-down", "way(1)"):7,
    ("way(1)", "COA BODEGA"):8,
    ("COA BODEGA", "ICT Office"):9,
    ("COA BODEGA", "PARKING LOT"):9,
    ("ICT Office", "PARKING LOT"):10,
    ("DANCE STUDIO", "LIBRARY"):12,
    
    # WEST
    ("School Entrance", "Str2"):1,
    ("Str2", "Str2-2nd Flr"):2,
    ("Str2", "REGISTRAR"):2,
    ("REGISTRAR", "PLANNING"):3,
    ("Str2-2nd Flr", "PLANNING"):3,
    ("PLANNING", "BUILDING & ESTATES"):4,
    ("BUILDING & ESTATES", "EXIT"):5,
    ("EXIT", "NSTP Office"):6,  
    ("NSTP Office", "DRRMO"):7,
    ("DRRMO", "FITNESS STUDIO"):8,
    ("FITNESS STUDIO", "DANCE STUDIO"):9,
    
    ("DANCE STUDIO","LIBRARY"):11,
    ("EXIT", "PARKING LOT"):6,
    
    ("LIBRARY", "Str5-2nd Flr"):12,
    ("Str5-2nd Flr", "CLINIC"):13,
    ("CLINIC", "GUIDANCE"):14,
    ("GUIDANCE", "PLACEMENT"):15,
    ("PLACEMENT", "SAO"):16,
    ("SAO", "Str6-2nd Flr"):17,
}


# Convert paths to an adjacency list
adjacency_list = {}
for (start, end), cost in paths.items():
    if start not in adjacency_list:
        adjacency_list[start] = {}
    if end not in adjacency_list:
        adjacency_list[end] = {}
    adjacency_list[start][end] = cost
    adjacency_list[end][start] = cost

# Create a grid to represent the map
grid = [[0] * 800 for _ in range(800)]  # Initialize grid with zeros


# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, goal):
    # Initialize the priority queue and visited set
    queue = [(0, start, [])]  # Include a list to store the path
    visited = set()

    # While the priority queue is not empty
    while queue:
        # Dequeue the current node, cost, and path
        cost, current, path = heapq.heappop(queue)

        # If this node has not been visited yet
        if current not in visited:
            # Mark this node as visited
            visited.add(current)

            # If this is the goal node, we are done
            if current == goal:
                return cost, path + [current]  # Return the path as well

            # Otherwise, enqueue all neighbors with updated costs
            for neighbor, edge_cost in graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [current]))

    # If we get here, there is no path between the start and goal
    return None

# Define the main GUI window
root = tk.Tk()
root.title("Surigao Del Norte State University")

# Create a canvas to draw the map
canvas = tk.Canvas(root, width=1000, height=670)
canvas.pack()

# Draw paths
for (start, end), cost in paths.items():
    (x1, y1), (x2, y2) = places[start], places[end]
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(cost), fill="", tags="path_cost")

# Draw places
for place, (x, y) in places.items():
    canvas.create_rectangle(x - 20, y - 15, x + 20, y + 15, fill="red")
    canvas.create_text(x - 5, y + 11, text=place, anchor="n")

# Create a frame to hold the start and goal labels and entry fields
frame = ttk.Frame(root, padding="10")
frame.pack()

# Create labels for start and goal
start_label = ttk.Label(frame, text="Start:")
start_label.grid(row=0, column=0)

goal_label = ttk.Label(frame, text="End:")
goal_label.grid(row=1, column=0)

# Create entry widgets for selecting start and goal locations
start_var = tk.StringVar()
start_entry = ttk.Entry(frame, textvariable=start_var)
start_entry.grid(row=0, column=1)

goal_var = tk.StringVar()
goal_entry = ttk.Entry(frame, textvariable=goal_var)
goal_entry.grid(row=1, column=1)

# Create a custom dropdown for start and goal entries
def show_start_dropdown(event):
    start_dropdown.place(x=start_entry.winfo_x(), y=start_entry.winfo_y() + start_entry.winfo_height())
    start_dropdown.lift()

def show_goal_dropdown(event):
    goal_dropdown.place(x=goal_entry.winfo_x(), y=goal_entry.winfo_y() + goal_entry.winfo_height())
    goal_dropdown.lift()

# Create custom dropdown menus
start_dropdown = tk.Listbox(frame, selectmode="single")
goal_dropdown = tk.Listbox(frame, selectmode="single")

for place in places.keys():
    start_dropdown.insert(tk.END, place)
    goal_dropdown.insert(tk.END, place)

# Hide the dropdown menus initially
start_dropdown.place_forget()
goal_dropdown.place_forget()


# Create a label to display the shortest path
shortest_path_label = ttk.Label()
shortest_path_label.pack()

# Create a label to display the places of the shortest path
shortest_path_places = tk.StringVar()
shortest_path_places_label = ttk.Label(root, textvariable=shortest_path_places)
shortest_path_places_label.pack()

# Create a button to find the shortest path
def animate_path():
    start = start_var.get()
    goal = goal_var.get()

    shortest_path_label.config(text="Searching...")
    root.update()

    result = dijkstra_shortest_path(adjacency_list, start, goal)

    if result is not None:
        path_length, path = result
        shortest_path_label.config(text=f"Shortest Path Found")

        # Draw the shortest path in red
        for i in range(len(path) - 1):
            (x1, y1), (x2, y2) = places[path[i]], places[path[i + 1]]
            canvas.create_line(x1, y1, x2, y2, fill="black", tags="shortest_path", width=4)

    else:
        shortest_path_label.config(text="No path found")

# Create a button to find the shortest path
find_button = ttk.Button(frame, text="Enter", command=animate_path)
find_button.grid(row=2, columnspan=2)

# Start the GUI main loop
root.mainloop()