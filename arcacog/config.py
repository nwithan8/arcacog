from typing import List

from dbotbase import CogConfig


class ArcaCogConfig(CogConfig):
    def __init__(self, folder: str, name: str, config_files: List[str] = None):
        if not config_files:
            config_files = []

        adjusted_config_files = []
        for config_file in config_files:
            adjusted_config_files.append(f"cogs/{folder}/{config_file}")
        super().__init__(name=name, config_files=adjusted_config_files)
