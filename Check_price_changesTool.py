
class Check_price_changesInput(BaseModel):
    

class Check_price_changesTool(BaseTool):
    name: str = "Check_price_changes Tool"
    args_schema: Type[BaseModel] = Check_price_changesInput
    description: str = "Tool for check_price_changes method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.check_price_changes()
        return result
