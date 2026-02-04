# core.pLibParser.py

class PLibParser:
    def __init__(self, data, language):
        self.data = data
        self.language = language
        self.current_topic = None
    
    def separation(self):
        result = {}
        for line in self.data:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("--[") and line.endswith("]--"):
                self.current_topic = line[len("--["):-len("]--")]
                result[self.current_topic] = []
            elif self.current_topic:
                
                result[self.current_topic].append(self.language_separat(line))
        return result
    
    def language_separat(self, input: str):
        data = input.split("|")
        if self.language.lower() == "all":
            # сохраняем все языки
            result = {}
            for line in data:
                if line.startswith("[") and line.endswith("]"):
                    line = line[1:-1]  # убираем скобки
                    if ":" in line:
                        lang, text = line.split(":", 1)
                        result[lang] = text
            return result
        else:
            # сохраняем только выбранный язык
            for line in data:
                if line.startswith("[") and line.endswith("]"):
                    line = line[1:-1]
                    if line.startswith(self.language + ":"):
                        return line[len(self.language + ":"):]
