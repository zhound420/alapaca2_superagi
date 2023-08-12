from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_market_sentimentInput(BaseModel):


    class Get_market_sentimentTool(BaseTool):
        name: str = "Get_market_sentiment Tool"
        args_schema: Type[BaseModel] = Get_market_sentimentInput
        description: str = "Tool for get_market_sentiment method."

        def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_market_sentiment()
        return result
