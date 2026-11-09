DEFAULT_QUESTIONS = (
    (
        "input()에 123을 입력하면 어떤 자료형으로 반환되나요?",
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
        "숫자 n이 1 이상 4 이하인지 확인하는 조건식은 무엇인가요?",
        ("n < 1 or n > 4", "1 >= n >= 4", "1 <= n <= 4", "n == 1 or n == 4"),
        3,
    ),
    (
        "올바른 번호를 입력할 때까지 반복하기에 알맞은 문은 무엇인가요?",
        ("while", "return", "import", "def"),
        1,
    ),
    (
        "range(1, 4)가 차례로 만드는 숫자는 무엇인가요?",
        ("0, 1, 2, 3", "1, 2, 3", "1, 2, 3, 4", "2, 3, 4"),
        2,
    ),
    (
        "함수에서 계산한 값을 호출한 코드에 돌려주는 문은?",
        ("continue", "print", "break", "return"),
        4,
    ),
    (
        "새 객체의 속성을 초기화하는 메서드 이름은 무엇인가요?",
        ("__str__", "__len__", "__init__", "__name__"),
        3,
    ),
    (
        "player.check()가 인스턴스 메서드 호출이라면 self에는 무엇이 전달되나요?",
        ("player 객체", "check 메서드 이름", "player의 클래스 이름", "None"),
        1,
    ),
    (
        "book 객체의 title 속성 값을 읽는 코드는 무엇인가요?",
        ("book('title')", "book['title']", "book.title", "title.book"),
        3,
    ),
    (
        "int('abc')를 실행할 때 발생하는 예외는?",
        ("EOFError", "ValueError", "FileNotFoundError", "KeyboardInterrupt"),
        2,
    ),
    (
        "존재하지 않는 파일을 읽기 모드로 열면 어떤 예외가 발생하나요?",
        ("IndexError", "KeyError", "ZeroDivisionError", "FileNotFoundError"),
        4,
    ),
    (
        "open()에서 텍스트 파일의 인코딩을 지정하는 매개변수는 무엇인가요?",
        ("mode", "encoding", "file", "newline"),
        2,
    ),
    (
        "with open(...)으로 연 파일은 with 블록을 벗어나면 어떻게 되나요?",
        ("자동으로 삭제된다", "바로 다시 열린다", "JSON으로 변환된다", "자동으로 닫힌다"),
        4,
    ),
    (
        "열린 파일에서 JSON 데이터를 읽어 Python 값으로 바꾸는 함수는?",
        ("json.load()", "json.loads()", "json.dump()", "json.dumps()"),
        1,
    ),
    (
        "폴더에 새 Git 저장소를 만드는 명령은 무엇인가요?",
        ("git status", "git pull", "git init", "git add"),
        3,
    ),
    (
        "수정한 notes.txt를 스테이징하는 Git 명령은 무엇인가요?",
        ("git log -- notes.txt", "git diff -- notes.txt", "git status -- notes.txt", "git add -- notes.txt"),
        4,
    ),
    (
        "스테이징한 변경을 로컬 저장소에 기록하는 Git 명령은 무엇인가요?",
        ("git push", "git commit", "git pull", "git checkout"),
        2,
    ),
    (
        "새 브랜치 feature를 만들고 바로 이동하는 Git 명령은 무엇인가요?",
        ("git merge feature", "git checkout feature", "git checkout -b feature", "git branch feature"),
        3,
    ),
    (
        "원격 Git 저장소를 내 컴퓨터에 처음 복제할 때 쓰는 명령은 무엇인가요?",
        ("git clone", "git push", "git add", "git commit"),
        1,
    ),
)
