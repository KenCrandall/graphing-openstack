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

import argparse

import pydot
import yaml

# code initially based off of
# http://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/


colors = {"REQUIRES": "black",
          "DEPENDSON": "red",
          "CANUSE": "grey"}


def edges(graph, service, nodes, color):
    """Add edges from service to nodes."""
    name = service.keys()[0]

    if service[name]:
        if color is None:
            # service specific graph
            for x in service[name]:
                graph.add_edge(pydot.Edge(nodes[name],
                                          nodes[x]))
        if color not in service[name]:
            # color isn't present
            return
        for x in service[name][color]:
            if color != "DEPENDSON":
                graph.add_edge(pydot.Edge(nodes[name],
                                          nodes[x],
                                          color=colors[color]))
            else:
                graph.add_edge(pydot.Edge(nodes[name],
                                          nodes[x],
                                          color=colors[color]))


def plot_all_services(graph, verbose=False):
    # TODO(jogo): if verbose, break out each service
    data = yaml.load(open('openstack.yaml', 'r'))

    nodes = {}  # services

    for service in sorted(data):
        name = service.keys()[0]
        nodes[name] = pydot.Node(name)
        graph.add_node(nodes[name])

    for service in data:
        edges(graph, service, nodes, 'REQUIRES')
        edges(graph, service, nodes, 'CANUSE')
        edges(graph, service, nodes, 'DEPENDSON')


def plot_service(graph, service):
    nodes = {}
    data = yaml.load(open('services/%s.yaml' % service, 'r'))
    for server in sorted(data):
        name = server.keys()[0]
        nodes[name] = pydot.Node(name)
        graph.add_node(nodes[name])

    for server in data:
        edges(graph, server, nodes, None)


def main(service=None):
    graph = pydot.Dot(graph_type='digraph')
    graph.set_node_defaults(style='filled')

    if service is None:
        plot_all_services(graph)
    else:
        plot_service(graph, service)

    graph.write_raw('OpenStack.dot')
    graph.write_png('OpenStack.png')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--service", help="Graph a single service")
    args = parser.parse_args()
    main(service=args.service)
