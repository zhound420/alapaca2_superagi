from alpaca_trade_api import REST, StreamConn
from TraderOriginal import TraderOriginal

from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_account_informationInput(BaseModel):


    class Get_account_informationTool(BaseTool):
        name: str = "Get_account_information Tool"
        args_schema: Type[BaseModel] = Get_account_informationInput
        description: str = "Tool for get_account_information method."

        def _execute(self, ):
            trader_instance = TraderOriginal()
            result = trader_instance.get_account_information()
            return result
