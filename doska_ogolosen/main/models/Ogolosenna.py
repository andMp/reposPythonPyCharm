class Ogolosenna:
    def __init__(self, id, title, description, pub_date, category):
        self.id = id
        self.title = title
        self.description = description
        self.pub_date = pub_date
        self.category = category
        self.responses = []  # список откликів