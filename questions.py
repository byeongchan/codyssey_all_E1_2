DEFAULT_QUESTIONS = (
    (
        "input()으로 받은 입력의 자료형은?",
        ("int", "str", "bool", "list"),
        2,
    ),
    (
        "입력 문자열의 앞뒤 공백을 제거하는 메서드는?",
        ("split()", "lower()", "replace()", "strip()"),
        4,
    ),
    (
        "len(['A', 'B', 'C', 'D'])의 결과는?",
        ("4", "3", "0", "5"),
        1,
    ),
    (
        "점수 3이 1 이상이고 4 이하인지 검사하는 조건식은?",
        ("3 < 1 or 3 > 4", "1 >= 3 >= 4", "1 <= 3 <= 4", "3 == 1 or 3 == 4"),
        3,
    ),
    (
        "유효한 번호가 들어올 때까지 입력을 반복할 때 쓰기 알맞은 문은?",
        ("while", "return", "import", "def"),
        1,
    ),
    (
        "for number in range(1, 4)에서 number에 차례로 들어가는 값은?",
        ("0, 1, 2, 3", "1, 2, 3", "1, 2, 3, 4", "2, 3, 4"),
        2,
    ),
    (
        "함수에서 계산한 값을 호출한 코드에 돌려주는 문은?",
        ("continue", "print", "break", "return"),
        4,
    ),
    (
        "Quiz 인스턴스를 만들 때 속성을 초기화하는 메서드 이름은?",
        ("__str__", "__len__", "__init__", "__name__"),
        3,
    ),
    (
        "Quiz의 인스턴스 메서드에서 self는 무엇을 가리키는가?",
        ("메서드를 호출한 Quiz 객체", "Quiz 클래스의 이름", "게임의 전체 퀴즈 목록", "정답 번호"),
        1,
    ),
    (
        "quiz가 Quiz 객체일 때 question 속성을 읽는 코드는?",
        ("quiz('question')", "Quiz['question']", "quiz.question", "question.quiz"),
        3,
    ),
    (
        "int('abc')를 실행할 때 발생하는 예외는?",
        ("EOFError", "ValueError", "FileNotFoundError", "KeyboardInterrupt"),
        2,
    ),
    (
        "저장 파일이 없어도 기본 퀴즈로 시작하려면 어떤 예외를 처리해야 하는가?",
        ("IndexError", "KeyError", "ZeroDivisionError", "FileNotFoundError"),
        4,
    ),
    (
        "UTF-8로 저장된 state.json을 텍스트로 읽기 위한 코드는?",
        (
            "open('state.json', 'w', encoding='utf-8')",
            "open('state.json', 'r', encoding='utf-8')",
            "open('state.json', 'a', encoding='utf-8')",
            "open('state.json', 'r', encoding='ascii')",
        ),
        2,
    ),
    (
        "with open(...) as file: 블록이 끝나면 파일은 어떻게 되는가?",
        ("자동으로 삭제된다", "바로 다시 열린다", "JSON으로 변환된다", "자동으로 닫힌다"),
        4,
    ),
    (
        "열린 파일에서 JSON 데이터를 읽어 Python 값으로 바꾸는 함수는?",
        ("json.load()", "json.loads()", "json.dump()", "json.dumps()"),
        1,
    ),
    (
        "Git을 사용하지 않던 프로젝트 폴더를 새 로컬 저장소로 만드는 명령은?",
        ("git status", "git pull", "git init", "git add"),
        3,
    ),
    (
        "수정한 main.py를 다음 커밋에 포함하도록 스테이징하는 명령은?",
        ("git log -- main.py", "git diff -- main.py", "git status -- main.py", "git add -- main.py"),
        4,
    ),
    (
        "스테이징한 변경을 메시지와 함께 로컬 이력에 남기는 명령은?",
        ("git push", "git commit -m '메뉴 구현'", "git pull", "git checkout main"),
        2,
    ),
    (
        "main에서 quiz-play 브랜치로 이동해 새 작업을 시작할 때, 브랜치 생성과 이동을 함께 하는 명령은?",
        ("git merge quiz-play", "git checkout main", "git checkout -b quiz-play", "git branch quiz-play"),
        3,
    ),
    (
        "원격 저장소를 새 폴더에 복제하고, 나중에 기존 작업 폴더에 원격 변경을 반영하는 명령의 순서는?",
        ("git clone → git pull", "git pull → git clone", "git init → git push", "git add → git commit"),
        1,
    ),
)
