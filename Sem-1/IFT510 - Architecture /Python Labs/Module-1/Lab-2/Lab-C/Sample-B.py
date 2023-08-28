## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 08/20/2023

def convert_storage(value, from_unit, to_unit):
    units = {"KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4}
    return value * units[from_unit] / units[to_unit]

print(convert_storage(1, "MB", "KB"))