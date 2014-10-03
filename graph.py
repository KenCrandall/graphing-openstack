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

# code initially based off of
# http://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/

graph = pydot.Dot(graph_type='digraph')

service_names = ['nova', 'keystone', 'glance']
s = {}  # services

for service in service_names:
    s[service] = pydot.Node(service, style="filled")

for service in s:
    graph.add_node(s[service])

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


graph.write_png('OpenStack.png')
