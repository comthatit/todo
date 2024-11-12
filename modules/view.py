# 할 일 보기 모듈
from modules.add import todo_list

def view_tasks():
    if not todo_list:
        print("할 일 목록이 비어 있습니다.")
        return
    print("\n현재 TODO 리스트:")
    for idx, item in enumerate(todo_list, start=1):
        status = "완료" if item["completed"] else "미완료"
        print(f"{idx}. {item['task']} - {status}")
