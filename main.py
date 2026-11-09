MENU_OPTIONS = (
    "퀴즈 풀기",
    "퀴즈 추가",
    "퀴즈 목록",
    "점수 확인",
    "종료",
)


def read_number(prompt, minimum, maximum):
    while True:
        raw_input = input(prompt).strip()
        try:
            number = int(raw_input)
        except ValueError:
            print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")


def show_menu():
    print("\n=== 파이썬과 Git 실전 퀴즈 ===")
    for number, label in enumerate(MENU_OPTIONS, start=1):
        print(f"{number}. {label}")


def main():
    while True:
        show_menu()
        selection = read_number("선택: ", 1, len(MENU_OPTIONS))

        if selection == len(MENU_OPTIONS):
            print("퀴즈 게임을 종료합니다.")
            return

        print(f"{MENU_OPTIONS[selection - 1]} 기능은 준비 중입니다.")


if __name__ == "__main__":
    main()
