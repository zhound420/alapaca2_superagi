from alpaca_trade_api import REST, StreamConn
from TraderOriginal import TraderOriginal

from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class Get_current_priceInput(BaseModel):
    pass


class Get_current_priceTool(BaseTool):
    name: str = "Get_current_price Tool"
    args_schema: Type[BaseModel] = Get_current_priceInput
    description: str = "Tool for get_current_price method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_current_price()
        return result
