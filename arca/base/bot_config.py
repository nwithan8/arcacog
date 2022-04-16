import logging
from typing import List

from arca.internal.config_parser import ConfigParser


class ArcaConfig(ConfigParser):
    def __init__(self, bot_name: str, config_files: List[str] = None):
        if config_files is None:
            config_files = []
        super().__init__(name=bot_name, config_files=config_files)

    @property
    def log_level(self):
        level = self.get(key='Logging', default='INFO')
        return logging.getLevelName(level)

    @property
    def token(self):
        return self.get(key='BotToken', path=['Discord'], default=None)

    @property
    def prefix(self):
        return self.get(key='BotPrefix', path=['Discord'], default=None)

    @property
    def server_id(self):
        return self.get(key='ServerID', path=['Discord'], default=None)

    @property
    def admin_ids(self):
        return self.get(key='AdminIDs', path=["Discord"], default=[])

    @property
    def admin_role_names(self):
        return self.get(key='AdminRoleNames', path=['Discord'], default=[])
