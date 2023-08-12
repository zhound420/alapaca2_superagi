from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_watchlistInput(BaseModel):


    class Get_watchlistTool(BaseTool):
        name: str = "Get_watchlist Tool"
        args_schema: Type[BaseModel] = Get_watchlistInput
        description: str = "Tool for get_watchlist method."

        def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_watchlist()
        return result
