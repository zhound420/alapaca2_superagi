from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_sym_newsInput(BaseModel):


    class Get_sym_newsTool(BaseTool):
        name: str = "Get_sym_news Tool"
        args_schema: Type[BaseModel] = Get_sym_newsInput
        description: str = "Tool for get_sym_news method."

        def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_sym_news()
        return result
