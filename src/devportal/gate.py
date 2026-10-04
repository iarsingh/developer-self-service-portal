class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("template") != "python-service": failed.append("template")\n    if body.get("env") not in {"dev", "staging"}: failed.append("env")
    return {"passed": not failed, "failed": failed, "applied": False}
