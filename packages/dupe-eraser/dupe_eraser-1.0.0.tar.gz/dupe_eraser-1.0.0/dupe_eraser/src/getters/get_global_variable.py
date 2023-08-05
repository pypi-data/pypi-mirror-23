import json
import os


_PATH_GLOBAL_VARIABLES = "../../res/global_variables.json"


def _get_value_from_file(value):
    path = os.path.join(os.path.dirname(__file__),
                        _PATH_GLOBAL_VARIABLES)
    with open(path) as file:
        return json.load(file)[value]


def name() -> str:
    return _get_value_from_file("name")


def description() -> str:
    return _get_value_from_file("description")


def keywords() -> str:
    return _get_value_from_file("keywords")


def main_homepage() -> str:
    return _get_value_from_file("main_homepage")


def download_url() -> str:
    return _get_value_from_file("download_url")


def version() -> str:
    return _get_value_from_file("version")


def author() -> str:
    return _get_value_from_file("author")


def maintainer() -> str:
    return _get_value_from_file("maintainer")


def email() -> str:
    return _get_value_from_file("email")


def status() -> str:
    return _get_value_from_file("status")


def copyright_text() -> str:
    return _get_value_from_file("copyright")


def credits_authors() -> list:
    return _get_value_from_file("credits")


def license_used() -> str:
    return _get_value_from_file("license")


def classifiers() -> list:
    return _get_value_from_file("classifiers")


def dependencies() -> list:
    return _get_value_from_file("dependencies")


def main_entry_point() -> str:
    return _get_value_from_file("main_entry_point")


if __name__ == '__main__':
    pass
