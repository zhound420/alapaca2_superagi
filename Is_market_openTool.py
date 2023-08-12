from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Is_market_openInput(BaseModel):


    class Is_market_openTool(BaseTool):
        name: str = "Is_market_open Tool"
        args_schema: Type[BaseModel] = Is_market_openInput
        description: str = "Tool for is_market_open method."

        def _execute(self, ):
            trader_instance = TraderOriginal()
            result = trader_instance.is_market_open()
        return result
