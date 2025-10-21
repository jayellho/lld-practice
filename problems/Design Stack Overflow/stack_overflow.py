from __future__ import annotations
from user import User
from post import Question, Answer, Comment
import uuid
from search_strategy import SearchStrategy, UserSearch, TagSearch, KeywordSearch

def get_unique_id():
    """Generates a random, universally unique ID."""
    return str(uuid.uuid4())
class StackOverflow:
    _instance = None
    def __init__(self):
        if StackOverflow._instance is not None:
            raise Exception("This class is a singleton!")
        StackOverflow._instance = self
        self.users = {} # key = id, val = User
        self.questions = {} # key = id, val = Question
        self.answers = {} # key = id, val = Answer
        self.comments = {} # key = id, val = Comment
    
    def createUser(self, name: str) -> None:
        userId = self._getUniqueId()
        newUser = User(userId, name)
        if userId in self.users:
            raise Exception(f"Trying to create user {userId} that already exists.")
        self.users[userId] = newUser

    def createQuestion(self, authorId: str, title: str, text: str, tag: str):
        if authorId not in self.users:
            raise Exception(f"user {authorId} does not exist.")
        questionId = self._getUniqueId()
        newQuestion = Question(questionId, authorId, title, text)
        if questionId in self.questions:
            raise Exception(f"Trying to create question with id {questionId} that already exists.") 
        self.questions[questionId] = newQuestion
        user = self.users[authorId]
        user.activity.append((newQuestion.postedAt, "question", questionId))

    def createAnswer(self, authorId: str, questionId: str, text: str):
        if authorId not in self.users:
            raise Exception(f"user {authorId} does not exist.")
        answerId = self._getUniqueId()
        newAnswer = Answer(answerId, authorId, questionId, text)
        if answerId in self.answers:
            raise Exception(f"Trying to create answer with id {answerId} that already exists.")
        self.answers[answerId] = newAnswer
        user = self.users[authorId]
        user.activity.append((newAnswer.postedAt, "answer", answerId))
        

    def createComment(self, authorId: str, postId: str, text:str):
        if authorId not in self.users:
            raise Exception(f"user {authorId} does not exist.")
        commentId = self._getUniqueId()
        newComment = Comment(commentId, authorId, postId, text)
        if commentId in self.comments:
            raise Exception(f"Trying to create comment with id {commentId} that already exists.")
        self.comments[commentId] = newComment
        user = self.users[authorId]
        user.activity.append((newComment.postedAt, "answer", commentId))

    def searchQuestion(self, searchType: UserSearch | TagSearch | KeywordSearch, searchTerm: str):
        searchStrategy = SearchStrategy(searchType(searchTerm))
        return searchStrategy.execute()
        
    
    def updateReputationScore(self, user: User):
        '''
        reputation score formula:
        number of posts / (last timestamp - first timestamp) * sum of all votes.
        '''
        (firstTimestamp, _, _), (lastTimestamp, _,  _) = self.activity[0], self.activity[-1]
        timeRange = lastTimestamp[0] - firstTimestamp[0] + 0.1 # to avoid divide by zero error.
        numPosts = len(user.activity)
        sumVotes = 0

        for timestamp, postType, postId in user.activity: # TODO: to optimize? seems like bad time complexity + many branches.
            if postId not in self.questions or postId not in self.answers:
                raise Exception(f"Id {postId} does not exist.")   
            if postType == "question":
                sumVotes += self.questions[postId].netVotes
            elif postType == "answer":
                answer = self.answers[postId]
                sumVotes += answer.netVotes * (int(answer.isAccepted) + 2) # arbitrary multiplier for accepted answers.
        
        return numPosts / timeRange * sumVotes

    def _getUniqueId():
        return str(uuid.uuid4())
    
    def upVote(self, postType: str, postId: str, voteBool: bool, acceptedAns: bool = False):
        if postType == "question": # TODO: maybe try not to branch?
            if postId not in self.questions:
                raise Exception(f"Trying to vote on question with id {postId} that does not exist.")
            else:
                post = self.questions[postId]
        else:
            if postId not in self.answers:
                raise Exception(f"Trying to vote on answer with id {postId} that does not exist.")
            else:
                post = self.answers[postId]
                post.isAccepted = acceptedAns
        
        if voteBool:
            post.netVotes += 1
        else:
            post.netVotes -= 1


    

