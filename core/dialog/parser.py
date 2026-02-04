# core.dialog.parser.py

class PLibParser:
    def __init__(self, data, language):
        self.data = data
        self.language = language
        self.current_topic = None