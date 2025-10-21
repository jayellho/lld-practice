from datetime import datetime

class Post:
    def __init__(self, id:str, authorId:str, text:str = ""):
        self.id = id
        self.authorId = authorId
        self.text = text
        self.postedAt = int(datetime.now().timestamp())

class Question(Post):
    def __init__(self, id: str, authorId: str, title: str, text: str, tag: str):
        super().__init__(id, authorId, text)
        self.title = title
        self.netVotes = 0
        self.linkedAnswers = set() # answerId
        self.linkedComments = set() # answerId
        self.tag = tag

class Answer(Post):
    def __init__(self, id: str, authorId: str, linkedQuestionId: str, text: str):
        super().__init__(id, authorId, text)
        self.linkedQuestionId = linkedQuestionId
        self.isAccepted = False
        self.netVotes = 0
    

class Comment(Post):
    def __init__(self, id: str, authorId: str, linkedPostId: str, text:str):
        super().__init__(id, authorId, text)
        self.linkedPostId = linkedPostId