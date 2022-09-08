from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression

class StringVal(Expression):

    def __init__(self, type: typeExpression, value) -> None:
        super().__init__()
        self.type = type
        self.value = value

    def compile(self, environment: Environment) -> Value:

        if(self.type == typeExpression.STRING):
            newTemp = self.generator.newTemp()
            self.generator.addExpression(newTemp,"H","","")

            for char in self.value:
                self.generator.addSetHeap("H",str(ord(char)))
                self.generator.addNextHeap()

            self.generator.addSetHeap("H","-1")

            return Value(str(newTemp),True,self.type)
        
        print("No se reconoce el tipo")
        return Value("0",False,typeExpression.STRING)