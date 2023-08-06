# coding=utf-8
"""
Implementation of exporting process to CSV functionality, as proposed in article "Spreadsheet-Based Business
Process Modeling" by Kluza k. and Wisniewski P.
"""
from __future__ import print_function

import copy

import pandas as pd
import re
import six

import bpmn_python.bpmn_python_consts as consts
import bpmn_python.bpmn_diagram_exception as bpmn_exception

regex_pa_trailing_number = r'^(.*[a-z|A-Z]|[^0-9]?)([0-9]+)$'
regex_pa_trailing_letter = r'(.+)([a-z|A-Z])'
regex_pa_merge_node_finder = r'(.*?)([0-9]+[a-z|A-Z])(.*?)'
regex_pa_num_let = r'([0-9]+)([a-z,A-Z])'
regex_prefix_split_succ = r'^'
regex_suffix_split_succ = r'([a-z|A-Z]|[a-z|A-Z][1]+)$'

default_proces_id = 'process_1'
default_plane_id = 'plane_1'


def getNodeType(order, csv_line_dict):
    if order == str(0):
        return consts.Consts.start_event
    if csv_line_dict[consts.Consts.csv_terminated] == 'yes':
        return consts.Consts.end_event
    if csv_line_dict[consts.Consts.csv_subprocess] == 'yes':
        return consts.Consts.subprocess
    else:
        return consts.Consts.task


def add_node_info_to_diagram_graph(order, type, activity, process_id, diagram_graph):
    diagram_graph.add_node(order)
    diagram_graph.node[order][consts.Consts.type] = type
    diagram_graph.node[order][consts.Consts.node_name] = activity
    diagram_graph.node[order][consts.Consts.process] = process_id
    if type == consts.Consts.start_event:
        diagram_graph.node[order][consts.Consts.parallel_multiple] = "false"
        diagram_graph.node[order][consts.Consts.is_interrupting] = "true"
        diagram_graph.node[order][consts.Consts.event_definitions] = []
    if type == consts.Consts.subprocess:
        diagram_graph.node[order][consts.Consts.triggered_by_event] = "false"
        diagram_graph.node[order][consts.Consts.is_expanded] = "false"
    if type == consts.Consts.end_event:
        diagram_graph.node[order][consts.Consts.event_definitions] = []
    if type in [consts.Consts.inclusive_gateway, consts.Consts.exclusive_gateway, consts.Consts.parallel_gateway]:
        diagram_graph.node[order][consts.Consts.gateway_direction] = "Unspecified"

    # Adding some dummy constant values
    diagram_graph.node[order][consts.Consts.width] = "100"
    diagram_graph.node[order][consts.Consts.height] = "100"
    diagram_graph.node[order][consts.Consts.x] = "100"
    diagram_graph.node[order][consts.Consts.y] = "100"


def import_nodes_info(process_dict, diagram_graph):
    for order, csv_line_dict in process_dict.items():
        type = getNodeType(order, csv_line_dict)
        activity = process_dict[order][consts.Consts.csv_activity]
        process_id = default_proces_id
        add_node_info_to_diagram_graph(order, type, activity, process_id, diagram_graph)


def remove_white_spaces_in_orders(process_dict):
    for order, csv_line_dict in process_dict.items():
        del process_dict[order]
        if isinstance(order, six.string_types) and order.strip() != order:
            process_dict[order.strip()] = csv_line_dict
        else:
            process_dict[str(order)] = csv_line_dict



def get_possible_sequence_continuation_successor(node_id):
    result = re.match(regex_pa_trailing_number, node_id)
    if result:
        last_number_in_order = result.group(2)
        next_number = str(int(last_number_in_order) + 1)
        prefix = result.group(1)
        return [prefix + next_number]
    else:
        # possible if e.g. 4a
        return []


def get_possible_split_continuation_successor(node_id):
    result = re.match(regex_pa_trailing_number, node_id)
    if result:
        trailing_number = result.group(2)
        prefix = result.group(1)
        new_trailing_number = str(int(trailing_number) + 1)
        new_node_id = prefix + new_trailing_number
        return [new_node_id + 'a', new_node_id + 'a1']
    else:
        return []


def get_possible_merge_continuation_successors(node_id_arg):
    node_id = copy.deepcopy(node_id_arg)
    result_trailing_number = re.match(regex_pa_trailing_number, node_id)
    if result_trailing_number:
        node_id = result_trailing_number.group(1)

    result_trailing_letter = re.match(regex_pa_trailing_letter, node_id)
    if result_trailing_letter:
        possible_successors = []
        for result in re.finditer(regex_pa_merge_node_finder, node_id):
            num_let_pair = result.group(2)
            prefix = result.group(1)
            num_let_result = re.match(regex_pa_num_let, num_let_pair)
            num = num_let_result.group(1)
            inc_num = str(int(num) + 1)
            possible_successors.append(prefix + inc_num)
        return possible_successors
    else:
        return []


def is_any_possible_successor_present_in_node_ids(possible_successors, nodes_ids):
    return bool(get_possible_successors_set_present_in_node_ids(possible_successors, nodes_ids))


def get_possible_successors_set_present_in_node_ids(possible_successors, nodes_ids):
    return set(possible_successors).intersection(set(nodes_ids))


def get_possible_successor_present_in_node_ids_or_raise_excp(poissible_successors_node_id, nodes_ids):
    possible_successor_set = get_possible_successors_set_present_in_node_ids(poissible_successors_node_id, nodes_ids)
    if len(possible_successor_set) != 1:
        raise bpmn_exception.BpmnPythonError("Some error in program - there should be exactly one found successor.")
    else:
        return possible_successor_set.pop()


def get_all_split_successors(node_id, nodes_ids):
    result = re.match(regex_pa_trailing_number, node_id)
    if not result:
        raise bpmn_exception.BpmnPythonError("Something wrong in program - look for " + node_id)
    trailing_number = result.group(2)
    prefix = result.group(1)
    new_trailing_number = str(int(trailing_number) + 1)
    next_node_id = prefix + new_trailing_number

    pattern = regex_prefix_split_succ + next_node_id + regex_suffix_split_succ
    split_successors = []
    for elem in nodes_ids:
        if re.match(pattern, elem):
            split_successors.append(elem)
    return split_successors


def is_there_sequence_continuation(node_id, nodes_ids):
    possible_seq_succ = get_possible_sequence_continuation_successor(node_id)
    return is_any_possible_successor_present_in_node_ids(possible_seq_succ, nodes_ids)


def is_there_split_continuation(node_id, nodes_ids):
    possible_split_succ = get_possible_split_continuation_successor(node_id)
    return is_any_possible_successor_present_in_node_ids(possible_split_succ, nodes_ids)


def is_there_merge_continuation(node_id, nodes_ids):
    possible_merge_succ = get_possible_merge_continuation_successors(node_id)
    return is_any_possible_successor_present_in_node_ids(possible_merge_succ, nodes_ids)


def is_node_the_end_event(node_id, process_dict):
    return process_dict[node_id][consts.Consts.csv_terminated] == 'yes'


def add_outgoing_flow(node_id, successor_node_id, diagram_graph):
    if diagram_graph.node[node_id].get(consts.Consts.outgoing_flow) is None:
        diagram_graph.node[node_id][consts.Consts.outgoing_flow] = []
    diagram_graph.node[node_id][consts.Consts.outgoing_flow].append(get_flow_id(node_id, successor_node_id))


def add_incoming_flow(node_id, from_node_id, diagram_graph):
    if diagram_graph.node[node_id].get(consts.Consts.incoming_flow) is None:
        diagram_graph.node[node_id][consts.Consts.incoming_flow] = []
    diagram_graph.node[node_id][consts.Consts.incoming_flow].append(get_flow_id(from_node_id, node_id))


def get_connection_condition_if_present(from_node_id, to_node_id, process_dict):
    if to_node_id in process_dict:
        return process_dict[to_node_id].get(consts.Consts.csv_condition)


def get_flow_id(from_node_id, to_node_id):
    return from_node_id + "__" + to_node_id


def add_edge(from_node_id, to_node_id, process_dict, diagram_graph, sequence_flows):
    condition = get_connection_condition_if_present(from_node_id, to_node_id, process_dict)
    diagram_graph.add_edge(from_node_id, to_node_id)
    id = get_flow_id(from_node_id, to_node_id)
    diagram_graph.edge[from_node_id][to_node_id][consts.Consts.id] = id
    diagram_graph.edge[from_node_id][to_node_id][consts.Consts.process] = default_proces_id
    diagram_graph.edge[from_node_id][to_node_id][consts.Consts.name] = ""
    diagram_graph.edge[from_node_id][to_node_id][consts.Consts.source_ref] = from_node_id
    diagram_graph.edge[from_node_id][to_node_id][consts.Consts.target_ref] = to_node_id
    if bool(condition):
        diagram_graph.edge[from_node_id][to_node_id][consts.Consts.condition_expression] = {
            consts.Consts.id: id + "_cond",
            consts.Consts.condition_expression: condition
        }
    sequence_flows[id] = {consts.Consts.name: id, consts.Consts.source_ref: from_node_id,
                          consts.Consts.target_ref: to_node_id}


def add_connection(from_node_id, to_node_id, process_dict, diagram_graph, sequence_flows):
    add_outgoing_flow(from_node_id, to_node_id, diagram_graph)
    add_incoming_flow(to_node_id, from_node_id, diagram_graph)
    add_edge(from_node_id, to_node_id, process_dict, diagram_graph, sequence_flows)


def get_node_conditions(split_successors, process_dict):
    conditions = []
    for succ in split_successors:
        conditions.append(process_dict[succ][consts.Consts.csv_condition].strip())
    return conditions


def yes_no_conditions(node_conditions):
    return set(node_conditions) == {"yes", "no"}


def sth_else_conditions(node_conditions):
    return "else" in node_conditions


def no_conditions(node_conditions):
    for node in node_conditions:
        if bool(node):
            return False
    return True


def get_gateway_type(node_id_to_add_after, nodes_ids, process_dict):
    split_successors = get_all_split_successors(node_id_to_add_after, nodes_ids)
    successors_conditions = get_node_conditions(split_successors, process_dict)
    if len(split_successors) == 2:
        if yes_no_conditions(successors_conditions) or sth_else_conditions(successors_conditions):
            return consts.Consts.exclusive_gateway
    if no_conditions(successors_conditions):
        return consts.Consts.parallel_gateway
    return consts.Consts.inclusive_gateway


def add_split_gateway(node_id_to_add_after, nodes_ids, process_dict, diagram_graph):
    split_gateway_id = node_id_to_add_after + "_split"
    process_id = default_proces_id
    type = get_gateway_type(node_id_to_add_after, nodes_ids, process_dict)
    activity = ""
    add_node_info_to_diagram_graph(split_gateway_id, type, activity, process_id, diagram_graph)
    return split_gateway_id


def get_merge_node_type(merge_successor_id, diagram_graph):
    result = re.match(regex_pa_trailing_number, merge_successor_id)
    if result:
        trailing_number = result.group(2)
        prev_prev_number = int(trailing_number) - 2
        if prev_prev_number < 0:
            raise bpmn_exception.BpmnPythonError("Something wrong in csv file syntax - look for " + merge_successor_id)
        prefix = result.group(1)
        split_node_id = prefix + str(prev_prev_number) + "_split"
        if bool(diagram_graph.has_node(split_node_id)):
            type = diagram_graph.node[split_node_id][consts.Consts.type]
            if bool(type):
                return type
        return consts.Consts.inclusive_gateway

def add_merge_gateway_if_not_exists(merge_successor_id, process_dict, diagram_graph):
    merge_gateway_id = merge_successor_id + "_join"
    if diagram_graph.has_node(merge_gateway_id):
        just_created = False
        return (merge_gateway_id, just_created)
    else:
        just_created = True
        process_id = default_proces_id
        type = get_merge_node_type(merge_successor_id, diagram_graph)
        activity = ""
        add_node_info_to_diagram_graph(merge_gateway_id, type, activity, process_id, diagram_graph)
        return (merge_gateway_id, just_created)


def fill_graph_connections(process_dict, diagram_graph, sequence_flows):
    nodes_ids = list(diagram_graph.node.keys())
    nodes_ids_to_process = copy.deepcopy(nodes_ids)
    while (bool(nodes_ids_to_process)):
        node_id = nodes_ids_to_process.pop(0)
        if is_node_the_end_event(node_id, process_dict):
            pass
        elif is_there_sequence_continuation(node_id, nodes_ids):
            possible_sequence_successors = get_possible_sequence_continuation_successor(node_id)
            successor_node_id = get_possible_successor_present_in_node_ids_or_raise_excp(possible_sequence_successors,
                                                                                         nodes_ids)
            add_connection(node_id, successor_node_id, process_dict, diagram_graph, sequence_flows)
        elif is_there_split_continuation(node_id, nodes_ids):
            split_gateway_id = add_split_gateway(node_id, nodes_ids, process_dict, diagram_graph)
            add_connection(node_id, split_gateway_id, process_dict, diagram_graph, sequence_flows)
            for successor_node_id in get_all_split_successors(node_id, nodes_ids):
                add_connection(split_gateway_id, successor_node_id, process_dict, diagram_graph, sequence_flows)
            pass
        elif is_there_merge_continuation(node_id, nodes_ids):
            possible_merge_successors = get_possible_merge_continuation_successors(node_id)
            merge_successor_id = get_possible_successor_present_in_node_ids_or_raise_excp(possible_merge_successors,
                                                                                          nodes_ids)
            merge_gateway_id, just_created = add_merge_gateway_if_not_exists(merge_successor_id, process_dict,
                                                                             diagram_graph)
            if just_created:
                add_connection(merge_gateway_id, merge_successor_id, process_dict, diagram_graph, sequence_flows)
            add_connection(node_id, merge_gateway_id, process_dict, diagram_graph, sequence_flows)
        else:
            raise bpmn_exception.BpmnPythonError("Something wrong in csv file syntax - look for " + node_id)


def remove_outgoing_connection(base_node, diagram_graph, sequence_flows):
    outgoing_flow_id = diagram_graph.node[base_node][consts.Consts.outgoing_flow][0]
    neighbour_node = sequence_flows[outgoing_flow_id][consts.Consts.target_ref]
    diagram_graph.node[neighbour_node][consts.Consts.incoming_flow].remove(outgoing_flow_id)
    del sequence_flows[outgoing_flow_id]
    diagram_graph.remove_edge(base_node, neighbour_node)
    return neighbour_node


def remove_incoming_connection(base_node, diagram_graph, sequence_flows):
    incoming_flow_id = diagram_graph.node[base_node][consts.Consts.incoming_flow][0]
    neighbour_node = sequence_flows[incoming_flow_id][consts.Consts.source_ref]
    diagram_graph.node[neighbour_node][consts.Consts.outgoing_flow].remove(incoming_flow_id)
    del sequence_flows[incoming_flow_id]
    diagram_graph.remove_edge(neighbour_node, base_node)
    return neighbour_node


def remove_node(node_id_to_remove, process_dict, diagram_graph, sequence_flows):
    new_source_node = remove_incoming_connection(node_id_to_remove, diagram_graph, sequence_flows)
    new_target_node = remove_outgoing_connection(node_id_to_remove, diagram_graph, sequence_flows)
    diagram_graph.remove_node(node_id_to_remove)
    process_dict.pop(node_id_to_remove, None)
    # add new connection
    return new_source_node, new_target_node


def remove_unnecessary_merge_gateways(process_dict, diagram_graph, sequence_flows):
    for node in diagram_graph.nodes(True):
        type = node[1].get(consts.Consts.type)
        if type in [consts.Consts.inclusive_gateway, consts.Consts.exclusive_gateway, consts.Consts.parallel_gateway]:
            if len(node[1].get(consts.Consts.incoming_flow)) < 2 \
                    and len(node[1].get(consts.Consts.outgoing_flow)) < 2:
                new_source_node, new_target_node = remove_node(node[0], process_dict, diagram_graph, sequence_flows)
                add_connection(new_source_node, new_target_node, process_dict, diagram_graph, sequence_flows)


def remove_goto_nodes(process_dict, diagram_graph, sequence_flows):
    for order, csv_line_dict in copy.deepcopy(process_dict).items():
        if csv_line_dict[consts.Consts.csv_activity].lower().startswith("goto"):
            source_node, _ = remove_node(order, process_dict, diagram_graph, sequence_flows)
            target_node = csv_line_dict[consts.Consts.csv_activity].strip().split()[1]
            add_connection(source_node, target_node, process_dict, diagram_graph, sequence_flows)




class BpmnDiagramGraphCSVImport(object):
    @staticmethod
    def load_diagram_from_csv(filepath, bpmn_diagram):
        """
        Reads an CSV file from given filepath and maps it into inner representation of BPMN diagram.
        Returns an instance of BPMNDiagramGraph class.

        :param filepath: string with output filepath,
        :param bpmn_diagram: an instance of BpmnDiagramGraph class.
        """
        diagram_graph = bpmn_diagram.diagram_graph
        sequence_flows = bpmn_diagram.sequence_flows
        process_elements_dict = bpmn_diagram.process_elements
        diagram_attributes = bpmn_diagram.diagram_attributes
        plane_attributes = bpmn_diagram.plane_attributes

        process_dict = BpmnDiagramGraphCSVImport.import_csv_file_as_dict(filepath)

        BpmnDiagramGraphCSVImport.populate_diagram_elements_dict(diagram_attributes)
        BpmnDiagramGraphCSVImport.populate_process_elements_dict(process_elements_dict, process_dict)
        BpmnDiagramGraphCSVImport.populate_plane_elements_dict(plane_attributes)

        BpmnDiagramGraphCSVImport.import_nodes(process_dict, diagram_graph, sequence_flows)
        BpmnDiagramGraphCSVImport.representation_adjustment(process_dict, diagram_graph, sequence_flows)

    @staticmethod
    def import_csv_file_as_dict(filepath):
        process_dict = pd.DataFrame.from_csv(filepath).fillna("").to_dict('index')
        remove_white_spaces_in_orders(process_dict)
        return process_dict

    @staticmethod
    def get_given_task_as_dict(csv_df, order_val):
        return csv_df.loc[csv_df[consts.Consts.csv_order] == order_val].iloc[0].to_dict()

    @staticmethod
    def import_nodes(process_dict, diagram_graph, sequence_flows):
        import_nodes_info(process_dict, diagram_graph)
        fill_graph_connections(process_dict, diagram_graph, sequence_flows)

    @staticmethod
    def populate_diagram_elements_dict(diagram_elements_dict):
        diagram_elements_dict[consts.Consts.id] = "diagram1"
        diagram_elements_dict[consts.Consts.name] = "diagram_name"

    @staticmethod
    def populate_process_elements_dict(process_elements_dict, process_dict):
        process_id = default_proces_id
        process_element_attributes = {consts.Consts.id: default_proces_id,
                                      consts.Consts.name: "",
                                      consts.Consts.is_closed: "false",
                                      consts.Consts.is_executable: "false",
                                      consts.Consts.process_type: "None",
                                      consts.Consts.node_ids: list(process_dict.keys())}
        process_elements_dict[process_id] = process_element_attributes

    @staticmethod
    def populate_plane_elements_dict(plane_elements_dict):
        plane_elements_dict[consts.Consts.id] = default_plane_id
        plane_elements_dict[consts.Consts.bpmn_element] = default_proces_id

    @staticmethod
    def legacy_adjustment(diagram_graph):
        for node in diagram_graph.nodes(True):
            if node[1].get(consts.Consts.incoming_flow) is None:
                node[1][consts.Consts.incoming_flow] = []
            if node[1].get(consts.Consts.outgoing_flow) is None:
                node[1][consts.Consts.outgoing_flow] = []
            if node[1].get(consts.Consts.event_definitions) is None:
                node[1][consts.Consts.event_definitions] = []

    @staticmethod
    def representation_adjustment(process_dict, diagram_graph, sequence_flows):
        BpmnDiagramGraphCSVImport.legacy_adjustment(diagram_graph)
        remove_goto_nodes(process_dict, diagram_graph, sequence_flows)
        remove_unnecessary_merge_gateways(process_dict, diagram_graph, sequence_flows)
