class F1NDRModule:
    name: str = "f1ndr"
    version: str = "1.0.0"

    def info(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
        }


f1ndr_module = F1NDRModule()
