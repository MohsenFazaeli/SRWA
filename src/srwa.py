from parser import parameter_parser
#from model import LabelPropagator
from graph_io import graph_reader
from matplotlib import pyplot as plt
import networkx as nx
from jupyterthemes import jtplot
import random
from tqdm import tqdm
from graph_io import json_dumper
from community import modularity

def create_and_run_model(args):
    G = graph_reader(args.input)
    #print G.nodes

    labels = {i: {'poslabel': i, 'negLabels': -1} for i in G.nodes}
    #print labels
    nx.set_node_attributes(G, labels)
    #print G.nodes[1]['poslabel']
    #print G.nodes[1]['poslabel']
    #print G.nodes[1]['poslabel']
    #print G.nodes[1]['negLabels']
    #print G.nodes[1]['negLabels']
    for node in G.nodes:
        print str(node)+"->"+str(G.nodes[node]['poslabel'])

    elarge = [(u,v,d) for (u,v,d) in G.edges(data=True)]
    print elarge


    """ init communities in V"""
    absdegs=dict(sorted(G.degree(weight='absweight'), key=lambda x: x[1], reverse=True))
    print type(absdegs)
    print absdegs
    posdegs=dict(sorted(G.degree(weight='posweight'), key=lambda x: x[1], reverse=True))
    print posdegs
    #print(posdegs[5])

    #Y= set off detected comunities
    Y= {}
    V={} #clustred nodes

    for v in G.nodes:
        if (absdegs[v]>=i for i in  G.neighbors(v) ) and v not in V:
            print





print __name__

if __name__ == "__main__":
    args = parameter_parser()
    create_and_run_model(args)