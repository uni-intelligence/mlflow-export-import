from mlflow_export_import.common.iterators import SearchRegisteredModelsIterator
from mlflow_export_import.common.iterators import SearchExperimentsIterator


def _get_list(names, func_list):
    """
    Returns a list of entities specified by the 'names' filter.
    :param names: Filter of desired list of entities. Can be: "all", comma-delimited string, list of entities or trailing wildcard "*".
    :param func_list: Function that lists the entities primary keys - for experiments it is experiment_id, for registered models it is model name.
    :return: List of entities.
    """
    if isinstance(names, str):
        if names == "all":
            return func_list()
        elif names.endswith("*"):
            prefix = names[:-1]
            return [ x for x in func_list() if x.startswith(prefix) ] 
        else:
            return names.split(",")
    else:
        return names


def get_experiment_ids(mlflow_client, experiment_ids):
    def list_entities():
        return [ exp.experiment_id for exp in SearchExperimentsIterator(mlflow_client) ]
    return _get_list(experiment_ids, list_entities)


def get_model_names(mlflow_client, model_names):
    def list_entities():
        return [ model.name for model in SearchRegisteredModelsIterator(mlflow_client) ]
    return _get_list(model_names, list_entities)


def read_name_replacements_file(path):
    with open(path, "r", encoding="utf-8") as f:
        dct = {} 
        for line in f:
            toks = line.rstrip().split(",")
            dct[toks[0]] = toks[1]
    return dct


def replace_name(name, replacements):
    if not replacements:
        return name
    for k,v in replacements.items():
        if name.startswith(k):
            return name.replace(k,v)
    return name
