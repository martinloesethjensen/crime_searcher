import simple_colors

from application import search


def check_value(value):
    if value == 0:
        print(simple_colors.red("Not a valid option..."))
        return False
    elif value == -1:
        print(simple_colors.red("Quiting..."))
        return True
    elif value == 1:
        search()

    # TODO: add last option when functionality is done.

    return False


def check_search_value(value: int) -> str:
    if value == 0:
        print(simple_colors.red("Not a valid option..."))
        return "0"
    elif value == -1:
        print(simple_colors.red("Going back..."))
        return "-1"
    elif value == 1:
        return "cdatetime"
    elif value == 2:
        return "address"
    elif value == 3:
        return "district"
    elif value == 4:
        return "grid"
    elif value == 5:
        return "crimedescr"
    elif value == 6:
        return "ucr_ncic_code"
    return "0"
