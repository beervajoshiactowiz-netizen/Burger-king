
def load(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        return content