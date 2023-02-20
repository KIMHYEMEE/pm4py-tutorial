# inductive miner
import pm4py

from path import *

file_name = path_data + '/' +file_xes

if __name__ == "__main__":
    log = pm4py.read_xes(file_name)

    process_tree = pm4py.discover_process_tree_inductive(log)
    # Process tree
    pm4py.view_process_tree(process_tree)

    # BPMN model
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)
    # error: graphviz.backend.execute.ExecutableNotFound: failed to execute WindowsPath('dot'), make sure the Graphviz executables are on your systems' PATH
    # > solve: $ conda install graphviz or $ conda install python-graphviz (in conda prompt)

    # Process map - dfg
    dfg, start_activities, end_activities = pm4py.discover_dfg(log)
    pm4py.view_dfg(dfg, start_activities, end_activities)

    # Process map - heuristic net
    map = pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(map)