from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    # ... その他のペアを追加
]

chat = Chat(pairs, reflections)

print("Hi, how can I help you today?")
while True:
    user_input = input(">>> ")
    if user_input == "quit":
        break
    response = chat.respond(user_input)
    print(response)