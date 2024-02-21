graph={
    'a':['b','e'],
    'b':['a','c','d','e'],
    'c':['b','d'],
    'd':['b','c','e'],
    'e':['a','b','d']
}
for key,val in graph.items():
    print(f"{key}-->{val}")