BAD_SOURCE_PORT = "Failed to find {key} in source node outputs!\nSource node:{source}\nSource outputs: {output_set}"
BAD_USER_INPUT_KEYS = "Specified input dictionary keys must be all nodes or all strings.\nGot: {keys}"
BAD_USER_NODE_INPUT_TYPE = "Node inputs must be provided as either a dictionary of inputs for a single execution or a list of input dictionaries for multiple executions."
MISSING_ENTRY_POINT_INPUTS = "Provided input dictionary does not satisfy the number of entry point to the pipeline.\nEntry points: {entry_points}"
FAILED_NODE_RUN = "\nFailed to run node #{node_id} ({analysis_version}, execution #{run_index}) with the following exception:\n{exception}\n\nUser provided inputs:\n{user_inputs}\n\nNode inputs:\n{node_inputs}"
NODE_RUN_START = "\n{analysis_version} (#{run_index})\nInputs:\n{inputs}\n..."
NODE_RUN_FINISHED = "Outputs:\n{outputs}\n"

# Visualizers
UNREGISTERED_VISUALIZATION_PROVIDER = (
    "Unregistered provider '{provider}' for {analysis_version}!"
)
MISSING_VISUALIZATION_PROVIDER = "Please choose from the following providers for {analysis_version}: {providers}"  # noqa E501
VISUALIZER_NOT_IMPLEMENTED = (
    "No visualizer implemented for {analysis_version}!"
)

# flake8: noqa: E501
