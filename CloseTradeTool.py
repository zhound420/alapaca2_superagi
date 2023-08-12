
class CloseTradeInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the trade to close")

class CloseTradeTool(BaseTool):
    name: str = "Close Trade Tool"
    args_schema: Type[BaseModel] = CloseTradeInput
    description: str = "Tool to close a specific trade by its symbol."

    def _execute(self, symbol):
        # Fetch environment keys using get_tool_config
        config = self.get_tool_config()
        APCA_API_KEY_ID = config.get("APCA_API_KEY_ID")
        APCA_API_SECRET_KEY = config.get("APCA_API_SECRET_KEY")
        APCA_PAPER = config.get("APCA_PAPER")
        
        # Initialize the Trader with the environment keys (this step will vary based on how the original code uses these keys)
        trader_instance = TraderOriginal(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_PAPER)
        
        # Execute the original method
        result = trader_instance.close_trade(symbol)
        return result
