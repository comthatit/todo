# 할 일 삭제 모듈
from modules.add import todo_list
from modules.view import view_tasks

def delete_task():
    view_tasks()
    task_num = int(input("삭제할 할 일 번호를 입력하세요: ")) - 1
    if 0 <= task_num < len(todo_list):
        removed_task = todo_list.pop(task_num)
        print(f"'{removed_task['task']}'가 삭제되었습니다.")
    else:
        print("올바르지 않은 번호입니다.")
