# 할 일 추가 모듈
todo_list = []

def add_task():
    task = input("추가할 할 일을 입력하세요: ")
    todo_list.append({"task": task, "completed": False})
    print(f"'{task}'가 할 일 목록에 추가되었습니다.")
