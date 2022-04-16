from dbotbase import BaseCog, BotConfig

from arcacog import ArcaCogConfig


class ArcaCog(BaseCog):
    def __init__(self, bot, config: ArcaCogConfig, bot_config: BotConfig = None):
        super().__init__(bot=bot, config=config, bot_config=bot_config)
