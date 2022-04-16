from typing import List

from dbotbase import CogConfig

from arcacog.translations import ArcaFilePath


class ArcaCogConfig(CogConfig):
    def __init__(self, cog_name: str, cog_title: str, config_files: List[str] = None):
        if not config_files:
            config_files = []

        adjusted_config_files = []
        for config_file in config_files:
            adjusted_config_files.append(ArcaFilePath(cog_name=cog_name, file_path=config_file).path)
        super().__init__(name=cog_title, config_files=adjusted_config_files)
