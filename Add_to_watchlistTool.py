
class Add_to_watchlistInput(BaseModel):
    

class Add_to_watchlistTool(BaseTool):
    name: str = "Add_to_watchlist Tool"
    args_schema: Type[BaseModel] = Add_to_watchlistInput
    description: str = "Tool for add_to_watchlist method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.add_to_watchlist()
        return result
