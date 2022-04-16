import logging
from typing import List

from arca import ArcaFilePath
from arca.internal.config_parser import ConfigParser


class ArcaCogConfig(ConfigParser):
    def __init__(self, cog_name: str, config_files: List[str] = None):
        if not config_files:
            config_files = []

        adjusted_config_files = []
        for config_file in config_files:
            adjusted_config_files.append(ArcaFilePath(cog_name=cog_name, file_path=config_file).path)
        super().__init__(name=cog_name, config_files=config_files)

    @property
    def log_level(self):
        level = self.get(key='Logging', default='INFO')
        return logging.getLevelName(level)

    @property
    def admin_ids(self):
        return self.get(key='AdminIDs', path=["Discord"], default=[])

    @property
    def admin_role_names(self):
        return self.get(key='AdminRoleNames', path=["Discord"], default=[])
