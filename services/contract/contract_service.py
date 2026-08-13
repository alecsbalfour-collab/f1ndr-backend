from engines.contract.contract_engine import ContractEngine

class ContractService:
    def __init__(self):
        self.engine = ContractEngine()

    def process(self, payload):
        return self.engine.run(payload)
