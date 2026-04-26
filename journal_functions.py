class InteractiveJournal:
    """An interactive digital journal"""
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename
        self.entries = []

        