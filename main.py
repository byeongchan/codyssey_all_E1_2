from questions import DEFAULT_QUESTIONS


MENU_OPTIONS = (
    "퀴즈 풀기",
    "퀴즈 추가",
    "퀴즈 목록",
    "점수 확인",
    "종료",
)


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selection):
        return selection == self.answer


def create_default_quizzes():
    return [
        Quiz(question, list(choices), answer)
        for question, choices, answer in DEFAULT_QUESTIONS
    ]


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


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("내용을 입력하세요.")


def show_menu():
    print("\n=== 파이썬과 Git 실전 퀴즈 ===")
    for number, label in enumerate(MENU_OPTIONS, start=1):
        print(f"{number}. {label}")


def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return None

    total = len(quizzes)
    correct_count = 0
    print(f"\n퀴즈를 시작합니다. 총 {total}문제입니다.")

    for number, quiz in enumerate(quizzes, start=1):
        print(f"\n[문제 {number}/{total}]")
        quiz.show()
        selection = read_number("정답 입력: ", 1, len(quiz.choices))
        if quiz.is_correct(selection):
            correct_count += 1
            print("정답입니다!")
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    print(f"\n결과: {total}문제 중 {correct_count}문제 정답")
    return correct_count


def add_quiz(quizzes):
    print("\n새 퀴즈를 추가합니다.")
    question = read_text("문제: ")
    choices = []
    for number in range(1, 5):
        choices.append(read_text(f"선택지 {number}: "))
    answer = read_number("정답 번호 (1~4): ", 1, len(choices))

    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다.")


def show_quiz_list(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    print(f"\n등록된 퀴즈 목록 (총 {len(quizzes)}문제)")
    for number, quiz in enumerate(quizzes, start=1):
        print(f"{number}. {quiz.question}")


def show_best_score(best_score):
    if best_score is None:
        print("아직 퀴즈를 완료한 기록이 없습니다.")
        return

    print(f"최고 기록: {best_score}문제 정답")


def main():
    quizzes = create_default_quizzes()
    best_score = None
    while True:
        show_menu()
        selection = read_number("선택: ", 1, len(MENU_OPTIONS))

        if selection == len(MENU_OPTIONS):
            print("퀴즈 게임을 종료합니다.")
            return

        if selection == 1:
            score = play_quiz(quizzes)
            if score is not None and (best_score is None or score > best_score):
                best_score = score
                print("새로운 최고 기록입니다!")
        elif selection == 2:
            add_quiz(quizzes)
        elif selection == 3:
            show_quiz_list(quizzes)
        elif selection == 4:
            show_best_score(best_score)


if __name__ == "__main__":
    main()
