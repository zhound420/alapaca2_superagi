from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Typeclass 

MonitorInput(BaseModel)   
class MonitorTool(BaseTool):
    name: str = "Monitor Tool"
    args_schema: Type[BaseModel] = MonitorInput
    description: str = "Tool for monitor method."

def _execute(self, ):
    trader_instance = TraderOriginal()
    result = trader_instance.monitor()
    return result
