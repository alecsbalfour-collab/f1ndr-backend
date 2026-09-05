class ParseUtils:
    def to_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def to_float(self, value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

parse_utils = ParseUtils()
