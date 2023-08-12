
class Get_current_priceInput(BaseModel):
    

class Get_current_priceTool(BaseTool):
    name: str = "Get_current_price Tool"
    args_schema: Type[BaseModel] = Get_current_priceInput
    description: str = "Tool for get_current_price method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_current_price()
        return result
