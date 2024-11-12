# 메인 프로그램 파일
from modules.add import add_task
from modules.view import view_tasks
from modules.complete import complete_task
from modules.delete import delete_task

def show_menu():
    print("\nTODO 리스트 관리 프로그램")
    print("1. 할 일 추가")
    print("2. 할 일 보기")
    print("3. 할 일 완료 표시")
    print("4. 할 일 삭제")
    print("5. 종료")
    choice = input("원하는 작업의 번호를 선택하세요: ")
    return choice

while True:
    choice = show_menu()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
