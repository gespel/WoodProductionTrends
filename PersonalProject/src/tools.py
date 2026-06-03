def date_to_numerical_year(date_str: str) -> float:
    split = date_str.split("-")

    year = int(split[2])
    month = int(split[1])
    day = int(split[0])

    return year + (month - 1) / 12 + (day - 1) / 365