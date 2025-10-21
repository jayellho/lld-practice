from stack_overflow import StackOverflow
from post import Post, Question, Answer, Comment
from user import User
from search_strategy import SearchStrategy, TagSearch, KeywordSearch, UserSearch


# Create StackOverflow system
stackOverflow = StackOverflow()


# Create users.
id1 = stackOverflow.createUser("John Adams")
id2 = stackOverflow.createUser("Scarlett")
id3 = stackOverflow.createUser("William")


# Users post questions and another user answers and another comments.
qn1 = stackOverflow.createQuestion(id1, "What is math?", "I don't really get how to add 1 plus 1.", "#lifeistough")
ans1q1 = stackOverflow.createAnswer(id2, qn1, "Math is life.")
com1q1 = stackOverflow.createComment(id3, qn1, "Lol is that why math is tough.")


# User1 upvotes the answer of user2.
stackOverflow.upVote("answer", ans1q1, True, True)
# User searchs for question.
searched_qns = stackOverflow.searchQuestion(UserSearch(id1))

# Update users' reputation scores.
stackOverflow.updateReputationScores()

print(f"answers = {stackOverflow.answers}")
print(f"comments = {stackOverflow.comments}")
print(f"questions = {stackOverflow.questions}")
print(stackOverflow.users[id1].activity)
print(stackOverflow.answers)
print(f"searched_qns = {searched_qns}")
print(f"reputationScore of user {id2}: {stackOverflow.users[id2].reputationScore}")
print(f"reputationScore of user {id1}: {stackOverflow.users[id1].reputationScore}")