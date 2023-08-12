from .Get_large_moversTool import Get_large_moversTool
from .Get_current_priceTool import Get_current_priceTool
from .Get_account_informationTool import Get_account_informationTool
from .Get_ideasTool import Get_ideasTool
from .CloseTradeTool import CloseTradeTool
from .Add_to_watchlistTool import Add_to_watchlistTool
from .Place_tradeTool import Place_tradeTool
from .Get_positions_infoTool import Get_positions_infoTool
from .Get_sym_newsTool import Get_sym_newsTool
from .Check_price_changesTool import Check_price_changesTool
from .MonitorTool import MonitorTool
from .Get_positionsTool import Get_positionsTool
from .Is_market_openTool import Is_market_openTool
from .Get_watchlistTool import Get_watchlistTool
from .Get_day_percent_changeTool import Get_day_percent_changeTool
from .Get_market_sentimentTool import Get_market_sentimentTool

from typing import List, Type
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_toolkit import BaseToolkit

class TraderToolkit(BaseToolkit):
    name: str = "Trader Toolkit"
    description: str = "Toolkit for various trading actions using AlpacaTrader with Auto-GPT."
    version: str = "1.0.0"

    def get_tools(self) -> List[BaseTool]:
        return [CloseTradeTool, Get_account_informationTool, Get_positionsTool, Place_tradeTool, Get_positions_infoTool, Get_watchlistTool, Add_to_watchlistTool, Get_market_sentimentTool, Get_sym_newsTool, Get_large_moversTool, Get_ideasTool, MonitorTool, Check_price_changesTool, Get_current_priceTool, Get_day_percent_changeTool, Is_market_openTool]

    def get_env_keys(self) -> List[str]:
        return []
