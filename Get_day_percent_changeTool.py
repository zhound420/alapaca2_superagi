from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_day_percent_changeInput(BaseModel):
    

class Get_day_percent_changeTool(BaseTool):
    name: str = "Get_day_percent_change Tool"
    args_schema: Type[BaseModel] = Get_day_percent_changeInput
    description: str = "Tool for get_day_percent_change method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_day_percent_change()
        return result
