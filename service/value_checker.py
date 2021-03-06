import simple_colors

import app


def check_value(value):
    if value == 0:
        print(simple_colors.red("Not a valid option..."))
        return False
    elif value == -1:
        print(simple_colors.red("Quiting..."))
        return True
    elif value == 1:
        app.search()
    elif value == 2:
        app.report_crime()
    elif value == 3:
        app.proximity_search(crime_list=app.get_crime_list())

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


def check_export_value(value: int):
    if value == 0:
        print(simple_colors.red("Not a valid option..."))
        return "0"
    elif value == -1:
        print(simple_colors.red("No export chosen..."))
        return "-1"
    elif value == 1:
        return "json"
    elif value == 2:
        return "html"
    return "0"


def check_proximity_option_value(value: int):
    if value == 0:
        print(simple_colors.red("Not a valid option..."))
        return "0"
    elif value == -1:
        print(simple_colors.red("No proximity option chosen..."))
        return "-1"
    elif value == 1:
        return "1"
    elif value == 2:
        return "2"
    return "0"
