from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class Get_positionsInput(BaseModel):


    class Get_positionsTool(BaseTool):
        name: str = "Get_positions Tool"
        args_schema: Type[BaseModel] = Get_positionsInput
        description: str = "Tool for get_positions method."

        def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_positions()
        return result
