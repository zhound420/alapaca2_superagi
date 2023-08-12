
class Get_large_moversInput(BaseModel):
    

class Get_large_moversTool(BaseTool):
    name: str = "Get_large_movers Tool"
    args_schema: Type[BaseModel] = Get_large_moversInput
    description: str = "Tool for get_large_movers method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_large_movers()
        return result
