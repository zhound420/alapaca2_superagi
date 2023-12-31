from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class Place_tradeInput(BaseModel):
    pass


class Place_tradeTool(BaseTool):
        name: str = "Place_trade Tool"
        args_schema: Type[BaseModel] = Place_tradeInput
        description: str = "Tool for place_trade method."

        def _execute(self, ):
            trader_instance = TraderOriginal()
            result = trader_instance.place_trade()
            return result
