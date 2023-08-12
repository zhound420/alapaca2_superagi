
from superagi.tools.base_toolkit import BaseToolkit

class TraderToolkit(BaseToolkit):
    name: str = "Trader Toolkit"
    description: str = "Toolkit for various trading actions using AlpacaTrader with Auto-GPT."
    version: str = "1.0.0"

    def get_tools(self) -> List[BaseTool]:
        return [CloseTradeTool, Get_account_informationTool, Get_positionsTool, Place_tradeTool, Get_positions_infoTool, Get_watchlistTool, Add_to_watchlistTool, Get_market_sentimentTool, Get_sym_newsTool, Get_large_moversTool, Get_ideasTool, MonitorTool, Check_price_changesTool, Get_current_priceTool, Get_day_percent_changeTool, Is_market_openTool()]
