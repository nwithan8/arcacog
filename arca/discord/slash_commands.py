from discord import SlashCommandGroup


class SlashCommand:
    def __init__(self, name: str, func, group=None):
        self.name = name
        self.func = func
        self.group = group
