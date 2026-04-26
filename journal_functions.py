class InteractiveJournal:
    """An interactive digital journal"""
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename
        self.entries = []

        def add_entry(self, text: str):
            """Adds a new line to temporary session list"""
            if text.strip():
                self.entries.append(text)

        def save_entry(self):
            """Saves all session entries to file"""
            if not self.entries:
                return False
            try:
                with open(self.filename, "a") as file:
                    for line in self.entries:
                        file.write(line + "\n")
                return True
            except Exception as e:
                print(f"Error saving your entry: {e}")
                return False

