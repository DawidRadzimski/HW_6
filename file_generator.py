import os


path = "./"


for i in range(1, 11):
    filename = f"query_{i}.sql"
    content = ""

    with open(os.path.join(path, filename), "w") as file:
        file.write(content)

print("Utworzono 10 plików o nazwie query_1.sql do query_10.sql")