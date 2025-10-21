from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from post import Question

class SearchStrategy(ABC):
    @abstractmethod
    def execute(self, questions: List[Question]):
        pass

class KeywordSearch(SearchStrategy):
    def __init__(self, keyword):
        self.keyword = keyword

    def execute(self, questions: List[Question]):
        return [q for _, q in questions.items() if self.keyword in q.text]

class TagSearch(SearchStrategy):
    def __init__(self, tag):
        self.tag = tag

    def execute(self, questions: List[Question]):
        return [q for _, q in questions.items() if self.tag in q.tag]

class UserSearch(SearchStrategy):
    def __init__(self, userId):
        self.userId = userId
    def execute(self, questions: List[Question]):
        return [q for _, q in questions.items() if self.userId in q.authorId]
    

