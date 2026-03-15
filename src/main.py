from chat import ask_vivo

if __name__ == '__main__':
    user_question = "question"   #可替换
    print("正在提问...")
    answer = ask_vivo(user_question)
    print("AI 的回答：")
    print(answer)