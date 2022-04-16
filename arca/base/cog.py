from typing import List

import discord
from discord.ext.commands import Cog

from arca.base.bot_config import ArcaConfig
from arca.base.cog_config import ArcaCogConfig
from arca.discord.slash_commands import SlashCommand, SlashCommandGroup
from arca.discord.utilities import get_roles, get_users


class ArcaCog(Cog):
    def __init__(self, bot: discord.Bot, config: ArcaCogConfig, bot_config: ArcaConfig = None):
        self.bot = bot
        self.config = config
        self.bot_config = bot_config

    def register_slash_commands(self, commands: List[SlashCommand]):
        for command in commands:
            self.bot.application_command(name=command.name, cls=discord.SlashCommand, parent=command.group)(
                command.func)

    def register_slash_command_groups(self, groups: List[SlashCommandGroup]):
        for group in groups:
            self.bot.add_application_command(group)

    @property
    def admin_role_names(self) -> List[str]:
        admin_role_names = self.config.admin_role_names
        if not admin_role_names and self.bot_config:
            admin_role_names = self.bot_config.admin_role_names
        return admin_role_names

    def get_admin_roles(self, guild: discord.Guild) -> List[discord.Role]:
        return get_roles(guild=guild, role_names=self.admin_role_names)

    @property
    def admin_ids(self) -> List[int]:
        admin_ids = self.config.admin_ids
        if not admin_ids and self.bot_config:
            admin_ids = self.bot_config.admin_ids
        return admin_ids

    def get_admin_users(self, guild: discord.Guild) -> List[discord.Member]:
        return get_users(guild=guild, user_ids=self.admin_ids)
