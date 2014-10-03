import pydot

graph = pydot.Dot(graph_type='digraph')

server_names = ['nova', 'keystone', 'glance']
s = {}  # servers

for server in server_names:
    s[server] = pydot.Node(server, style="filled")

for server in s:
    graph.add_node(s[server])

# black: a REQUIRES b THROUGH label
REQUIRES = "black"
# blue: a CAN-USE b THROUGH label
CANUSE = "blue"
# red: a DEPENDS-ON b
DEPENDSON = "red"

graph.add_edge(pydot.Edge(s['nova'],
                          s['keystone'],
                          color=REQUIRES,
                          label="keystomiddleware"))
graph.add_edge(pydot.Edge(s['nova'],
                           s['glance'],
                           color=REQUIRES,
                           label='glanceclient'))
graph.add_edge(pydot.Edge(s['nova'],
                          s['glance'],
                          color=DEPENDSON))

graph.add_edge(pydot.Edge(s['glance'],
                          s['keystone'],
                          color=REQUIRES,
                          label="keystomiddleware"))



# and we are done
graph.write_png('OpenStack.png')

# this is too good to be true!
