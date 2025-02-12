def mapToJson(raw_data, columns):
    if not raw_data:
        return []

    return [dict(zip(columns, row)) for row in raw_data]