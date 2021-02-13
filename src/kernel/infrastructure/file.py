def write_file(file_path: str, data: str):
    with open("balance_dates.json", "w+") as file:
        file.write(data)
