class User:
    def __init__(self, userId: str, name: str):
        self.userId = userId
        self.name = name
        self.reputationScore = 0
        self.activity = [] # (postedAt, postType, postId)