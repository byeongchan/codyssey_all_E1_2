import json
import random
from pathlib import Path
from tempfile import TemporaryDirectory

from questions import DEFAULT_QUESTIONS


STATE_PATH = Path(__file__).resolve().with_name("state.json")
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

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("퀴즈는 객체여야 합니다.")

        question = data.get("question")
        choices = data.get("choices")
        answer = data.get("answer")

        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있지 않은 문자열이어야 합니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if any(not isinstance(choice, str) or not choice.strip() for choice in choices):
            raise ValueError("선택지는 비어 있지 않은 문자열이어야 합니다.")
        if type(answer) is not int or not 1 <= answer <= len(choices):
            raise ValueError("정답 번호가 선택지 범위를 벗어났습니다.")

        return cls(question, choices, answer)


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


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.needs_save = False

    def load_state(self):
        try:
            with STATE_PATH.open(encoding="utf-8") as state_file:
                data = json.load(state_file)

            if not isinstance(data, dict) or not isinstance(data.get("quizzes"), list):
                raise ValueError("퀴즈 목록이 필요합니다.")
            if "best_score" not in data:
                raise ValueError("최고 점수 항목이 필요합니다.")

            best_score = data["best_score"]
            if best_score is not None and (type(best_score) is not int or best_score < 0):
                raise ValueError("최고 점수는 null 또는 0 이상의 정수여야 합니다.")

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
        except FileNotFoundError:
            return
        except (ValueError, RecursionError):
            print("저장 파일이 손상되어 기본 퀴즈로 시작합니다.")
            self.needs_save = True
            return
        except OSError:
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            return

        self.quizzes = quizzes
        self.best_score = best_score

    def save_state(self):
        if not self.needs_save:
            return

        data = {
            "quizzes": [
                {"question": quiz.question, "choices": quiz.choices, "answer": quiz.answer}
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

        try:
            # 완전히 기록한 파일로 교체하여 도중에 실패해도 기존 저장 파일을 보호합니다.
            with TemporaryDirectory(prefix=".quiz-state-", dir=STATE_PATH.parent) as directory:
                temporary_path = Path(directory) / STATE_PATH.name
                with temporary_path.open("w", encoding="utf-8") as state_file:
                    json.dump(data, state_file, ensure_ascii=False, indent=2)
                    state_file.write("\n")
                temporary_path.replace(STATE_PATH)
        except (OSError, UnicodeError):
            print("저장 파일을 쓸 수 없어 변경 사항을 저장하지 못했습니다.")
        else:
            self.needs_save = False

    def show_menu(self):
        print("\n=== 파이썬과 Git 실전 퀴즈 ===")
        for number, label in enumerate(MENU_OPTIONS, start=1):
            print(f"{number}. {label}")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        available = len(self.quizzes)
        total = read_number(f"풀 문제 수 (1~{available}): ", 1, available)
        selected_quizzes = random.sample(self.quizzes, k=total)
        correct_count = 0
        print(f"\n퀴즈를 시작합니다. 총 {total}문제입니다.")

        for number, quiz in enumerate(selected_quizzes, start=1):
            print(f"\n[문제 {number}/{total}]")
            quiz.show()
            selection = read_number("정답 입력: ", 1, len(quiz.choices))
            if quiz.is_correct(selection):
                correct_count += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n결과: {total}문제 중 {correct_count}문제 정답")
        if self.best_score is None or correct_count > self.best_score:
            self.needs_save = True
            self.best_score = correct_count
            print("새로운 최고 기록입니다!")
            self.save_state()

    def add_quiz(self):
        print("\n새 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = []
        for number in range(1, 5):
            choices.append(read_text(f"선택지 {number}: "))
        answer = read_number("정답 번호 (1~4): ", 1, len(choices))

        self.needs_save = True
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")
        self.save_state()

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}문제)")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 완료한 기록이 없습니다.")
            return

        print(f"최고 기록: {self.best_score}문제 정답")

    def run(self):
        try:
            self.load_state()
            while True:
                self.show_menu()
                selection = read_number("선택: ", 1, len(MENU_OPTIONS))

                if selection == len(MENU_OPTIONS):
                    break

                if selection == 1:
                    self.play_quiz()
                elif selection == 2:
                    self.add_quiz()
                elif selection == 3:
                    self.show_quiz_list()
                elif selection == 4:
                    self.show_best_score()

            self.save_state()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다.")
            self.save_state()

        print("퀴즈 게임을 종료합니다.")


if __name__ == "__main__":
    QuizGame().run()
