import json
import os
import random

DATA_FILE = "questions.json"


def load_data():
    """Load question and answer pairs from DATA_FILE."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(data):
    """Save question and answer pairs to DATA_FILE."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_question():
    question = input("問題を入力してください: ")
    answer = input("答えを入力してください: ")
    data = load_data()
    data.append({"question": question, "answer": answer})
    save_data(data)
    print("追加されました。")


def study():
    data = load_data()
    if not data:
        print("問題がありません。まずは問題を追加してください。")
        return
    pair = random.choice(data)
    user_answer = input(f"質問: {pair['question']}\n答え> ")
    if user_answer.strip() == pair["answer"]:
        print("正解！")
    else:
        print(f"不正解。正しい答え: {pair['answer']}")


def menu():
    while True:
        print("\n1: 問題を追加\n2: 学習する\n3: 終了")
        choice = input("選択> ")
        if choice == "1":
            add_question()
        elif choice == "2":
            study()
        elif choice == "3":
            print("終了します。")
            break
        else:
            print("無効な選択肢です。")


if __name__ == "__main__":
    menu()
