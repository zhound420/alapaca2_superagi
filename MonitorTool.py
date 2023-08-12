
class MonitorInput(BaseModel):    

    class MonitorTool(BaseTool):
        name: str = "Monitor Tool"
        args_schema: Type[BaseModel] = MonitorInput
        description: str = "Tool for monitor method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.monitor()
        return result