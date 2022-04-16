from typing import List

from discord import Bot, Guild, Role, Member

from arca.base.bot_config import ArcaConfig
from arca.discord.utilities import get_roles, get_users


class Arca(Bot):
    def __init__(self, config: ArcaConfig, *args, **options):
        super().__init__(*args, **options)
        self.config = config

    @property
    def server_id(self) -> int:
        return self.config.server_id

    @property
    def token(self) -> str:
        return self.config.token

    @property
    def prefix(self) -> str:
        return self.config.prefix

    @property
    def admin_role_names(self) -> List[str]:
        return self.config.admin_role_names

    def get_admin_roles(self, guild: Guild) -> List[Role]:
        return get_roles(guild=guild, role_names=self.admin_role_names)

    @property
    def admin_ids(self) -> List[int]:
        return self.config.admin_ids

    def get_admin_users(self, guild: Guild) -> List[Member]:
        return get_users(guild=guild, user_ids=self.admin_ids)
