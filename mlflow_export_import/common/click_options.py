import click

# == export

def opt_output_dir(function):
    function = click.option("--output-dir",
        help="Output directory.", 
        type=str,
        required=True
    )(function)
    return function

def opt_notebook_formats(function):
    function = click.option("--notebook-formats",
        help="Databricks notebook formats. Values are SOURCE, HTML, JUPYTER or DBC (comma seperated).",
        type=str,  
        default="", 
        show_default=True
    )(function)
    return function

def opt_run_id(function):
    function = click.option("--run-id",
        help="Experiment name or ID.",
        type=str,
        required=True
    )(function)
    return function

def opt_stages(function):
    function = click.option("--stages",
        help="Stages to export (comma seperated). Default is all stages and all versions. Stages are Production, Staging, Archived and None. Mututally exclusive with option --versions.",
        type=str,
        required=False
    )(function)
    return function

# == import

def opt_input_dir(function):
    function = click.option("--input-dir",
        help="Input path - directory",
        type=str,
        required=True
    )(function)
    return function

def opt_import_source_tags(function):
    function = click.option("--import-source-tags",
        help="Import source information for registered model and its versions ad tags in destination object.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_use_src_user_id(function):
    function = click.option("--use-src-user-id",
        help= "Set the destination user ID to the source user ID. Source user ID is ignored when importing into Databricks since setting it is not allowed.",
        type=bool,
        default=False
    )(function)
    return function

def opt_dst_notebook_dir(function):
    function = click.option("--dst-notebook-dir",
        help="Databricks destination workpsace base directory for notebook. A run ID will be added to contain the run's notebook.",
        type=str,
        required=False,
        show_default=True
    )(function)
    return function

def opt_experiment_name(function):
    function = click.option("--experiment-name",
        help="Destination experiment name",
        type=str,
        required=True
    )(function)
    return function

def opt_experiment(function):
    function = click.option("--experiment",
        help="Experiment name or ID.",
        type=str,
        required=True
        )(function)
    return function

def opt_versions(function):
    function = click.option("--versions",
        help="Export specified versions (comma separated). Mututally exclusive with option --stages.",
        type=str,
        required=False)(function)
    return function

# == bulk

def opt_use_threads(function):
    click.option("--use-threads",
        help="Process export/import in parallel using threads.",
        type=bool,
        default=False,
        show_default=True)(function)
    return function

def opt_delete_model(function):
    function = click.option("--delete-model",
        help="If the model exists, first delete the model and all its versions.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

# == other

def opt_model(function):
    function = click.option("--model",
        help="Registered model name.",
        type=str,
        required=True
    )(function)
    return function

def opt_verbose(function):
    function = click.option("--verbose",
        type=bool,
        help="Verbose.",
        default=False,
        show_default=True
    )(function)
    return function