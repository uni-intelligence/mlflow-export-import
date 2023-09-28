import json


def dump_mlflow_client(client, msg=""):
    print(f"MlflowClient {msg}:")
    print("  client.tracking_uri: ", client.tracking_uri)
    print("  client._registry_uri:", client._registry_uri)
    creds = client._tracking_client.store.get_host_creds()
    dump_obj(creds, "Credentials", "  ")


def dump_obj(obj, title=None, indent=""):
    if obj:
        title = title if title else type(obj).__name__
        print(f"{indent}{title}")
        for k,v in obj.__dict__.items():
            print(f"{indent}  {k}: {v}")
    else:
        title = title if title else "Object"
        title = f"{title}: None"
        print(f"{indent}{title}")


def dump_dict(dct, title=None):
    if title:
        print(f"{title}:")
    for k,v in dct.items():
        print(f"  {k}: {v}")


def dump_obj_as_json(obj, title=None):
    title = title if title else type(obj).__name__
    print(title)
    dump_as_json(obj_to_dict(obj))


def dump_as_json(dct, sort_keys=None, indent=2, title=None):
    if title:
        print(f"{title}:")
    print(dict_to_json(dct, sort_keys, indent))


def dict_to_json(dct, sort_keys=None, indent=2):
    return json.dumps(dct, sort_keys=sort_keys, indent=indent)


def obj_to_dict(obj):
    return obj.__dict__
