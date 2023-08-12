
class Get_ideasInput(BaseModel):
    

class Get_ideasTool(BaseTool):
    name: str = "Get_ideas Tool"
    args_schema: Type[BaseModel] = Get_ideasInput
    description: str = "Tool for get_ideas method."

    def _execute(self, ):
        trader_instance = TraderOriginal()
        result = trader_instance.get_ideas()
        return result
