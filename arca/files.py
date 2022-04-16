class ArcaFilePath:
    def __init__(self, cog_name: str, file_path: str):
        self.path = f"cogs/{cog_name}/{file_path}"

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.path

    def __eq__(self, other):
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)
