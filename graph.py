#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


import pydot
import yaml

# code initially based off of
# http://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/


colors = {"REQUIRES": "black",
          "DEPENDSON": "red",
          "CANUSE": "grey"}


def edges(service, nodes, color):
    name = service.keys()[0]

    if service[name]:
        if color not in service[name]:
            # color isn't present
            return
        for x in service[name][color]:
            if color != "DEPENDSON":
                graph.add_edge(pydot.Edge(nodes[name],
                                          nodes[x],
                                          color=colors[color]))
                                          #label=service[name][color][x]))
            else:
                graph.add_edge(pydot.Edge(nodes[name],
                                          nodes[x],
                                          color=colors[color]))


data = yaml.load(open('openstack.yaml', 'r'))

graph = pydot.Dot(graph_type='digraph')

nodes = {}  # services

for service in data:
    name = service.keys()[0]
    nodes[name] = pydot.Node(name, style="filled")

for service in nodes:
    graph.add_node(nodes[service])

# black: a REQUIRES b THROUGH label
# blue: a CAN-USE b THROUGH label
# red: a DEPENDS-ON b


for service in data:
    edges(service, nodes, 'REQUIRES')
    edges(service, nodes, 'CANUSE')
    edges(service, nodes, 'DEPENDSON')



graph.write_png('OpenStack.png')
