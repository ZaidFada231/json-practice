import json

with open(".\data\schacon.repos.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    with open(".\chacon.csv", "w", encoding="utf-8") as csv_file:
        for repo in data[:5]:
            name = repo["name"]
            html_url = repo["html_url"]
            updated_at = repo["updated_at"]
            visibility = repo["visibility"]

            line = f"{name},{html_url},{updated_at},{visibility}\n"

            csv_file.write(line)
