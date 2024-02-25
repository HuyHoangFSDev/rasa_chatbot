import yaml

def create_nlu_data():
    nlu_data = {"version": "3.0", "nlu": []}

    while True:
        intent = input("Nhập intent (nhập 'exit' để thoát): ")
        if intent.lower() == 'exit':
            break

        examples = []
        while True:
            example = input(f"Nhập ví dụ cho intent '{intent}' (nhập 'done' để kết thúc): ")
            if example.lower() == 'done':
                break
            examples.append(example)

        nlu_data["nlu"].append({"intent": intent, "examples": examples})

    return nlu_data

def create_stories_data():
    stories_data = {"version": "3.1", "stories": []}

    while True:
        story_name = input("Nhập tên story (nhập 'exit' để thoát): ")
        if story_name.lower() == 'exit':
            break

        story = {"story": story_name, "steps": []}
        while True:
            intent = input("Nhập intent: ")
            if intent.lower() == 'exit':
                break

            action = input("Nhập action: ")
            story["steps"].append({"intent": intent, "action": action})

        stories_data["stories"].append(story)

    return stories_data

def save_to_yaml(data, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        if "nlu" in data:
            file.write(f"version: {data['version']}\n\n")
            for item in data["nlu"]:
                file.write(f"- intent: {item['intent']}\n")
                file.write("  examples: |\n")
                for example in item['examples']:
                    file.write(f"    - {example}\n")
        elif "stories" in data:
            file.write(f"version: {data['version']}\n\n")
            for item in data["stories"]:
                file.write(f"- story: {item['story']}\n")
                file.write("  steps:\n")
                for step in item['steps']:
                    file.write(f"  - intent: {step['intent']}\n")
                    file.write(f"    - {step['action']}\n")

if __name__ == "__main__":
    nlu_data = create_nlu_data()
    stories_data = create_stories_data()

    # Ghi nối tiếp vào file YAML
    save_to_yaml(nlu_data, 'nlu_data.yml')
    save_to_yaml(stories_data, 'stories_data.yml')

    print("Dữ liệu đã được ghi nối tiếp vào file YAML.")
