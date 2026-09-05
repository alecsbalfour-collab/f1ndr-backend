from typing import Any, Dict

class RuleEngine:
    """
    Lightweight rule engine for API-level validation or transformation.
    Extend this later as needed.
    """

    def apply_rules(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply API-level rules to incoming data.
        Currently a passthrough — expand later.
        """
        return data

rule_engine = RuleEngine()
