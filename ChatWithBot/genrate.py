import random
import json

# Danh sách các intent và câu hỏi mẫu
intents = {
    "greet": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "inform": ["I want [pizza](food)", "I need a [book](item)"]
}

# Danh sách các actions và câu trả lời tương ứng
responses = {
    "utter_greet": ["Hello!", "Hi there!"],
    "utter_goodbye": ["Goodbye!", "See you!"],
    "utter_inform": ["Sure, I can help you with that."]
}

# Tạo dữ liệu đào tạo cho Rasa NLU
nlu_data = {"rasa_nlu_data": {"common_examples": []}}
for intent, examples in intents.items():
    for example in examples:
        nlu_data["rasa_nlu_data"]["common_examples"].append({"text": example, "intent": intent})

# Tạo dữ liệu đào tạo cho Rasa Core
stories_data = ["## Story 1\n"]
for intent, examples in intents.items():
    for example in examples:
        action = "utter_" + intent
        stories_data.append(f"* {intent}\n  - {action}\n")

# In ra dữ liệu đào tạo
print("Rasa NLU Training Data:")
print(json.dumps(nlu_data, indent=2))

print("\nRasa Core Training Data:")
print("\n".join(stories_data))
