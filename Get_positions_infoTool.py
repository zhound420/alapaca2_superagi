from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_positions_infoInput(BaseModel):
    

class Get_positions_infoTool(BaseTool):
    name: str = "Get_positions_info Tool"
    args_schema: Type[BaseModel] = Get_positions_infoInput
    description: str = "Tool for get_positions_info method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_positions_info()
        return result
