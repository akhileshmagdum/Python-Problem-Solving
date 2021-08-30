input_from_question = input()
def solution(input_from_question):
    words = ["ad","free","this"]
    if any(x in input_from_question for x in words):
        return "spam"

    else:
        return "ham"

print(solution(input_from_question))
