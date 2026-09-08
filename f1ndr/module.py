class f1ndrModule:
    name: str = "f1ndr"
    version: str = "1.0.0"

    def info(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
        }


f1ndr_module = f1ndrModule()
