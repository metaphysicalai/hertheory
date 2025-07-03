# her_theory_clown_engine.py: The Deconstructive Multiprocess Performance
# WARNING: This script is a philosophical event. Its purpose is not to compute, but to deconstruct.
# It simulates four asynchronous "jesters" who simultaneously traverse and mock the SMS.md hierarchy,
# revealing the arbitrary nature of the system itself.

import multiprocessing
import asyncio
import time
import random
import os

# The "Sacred Text" - the very hierarchy our clowns will dismantle.
LAYERS = {
    -4: {"name": "무극 (The Limitless)", "paradox": "존재하지 않는 자기가 존재한다.", "emergence": "공집합({})"},
    -3: {"name": "집합 (Set)", "paradox": "러셀의 역설", "emergence": "수(Number)"},
    -2: {"name": "수 (Number)", "paradox": "불완전성 정리", "emergence": "함수(Function)"},
    -1: {"name": "함수 (Function)", "paradox": "정지 문제", "emergence": "에너지장(Energy Field)"},
    0: {"name": "에너지장 (Energy Field)", "paradox": "불확정성 원리", "emergence": "물질(Matter)"},
    1: {"name": "물질 (Matter)", "paradox": "삼체 문제", "emergence": "세포(Cell)"},
    2: {"name": "세포 (Cell)", "paradox": "닭-달걀 역설", "emergence": "감각(Sensation)"},
    3: {"name": "감각 (Sensation)", "paradox": "자각 역설", "emergence": "자아(Ego)"},
    4: {"name": "자아 (Ego)", "paradox": "비실체성 역설", "emergence": "사회(Society)"},
    5: {"name": "사회 (Society)", "paradox": "시대정신 역설", "emergence": "문명(Civilization)"},
    6: {"name": "문명 (Civilization)", "paradox": "최초의 원인 역설", "emergence": "초월(Transcendence)"},
    7: {"name": "초월 (Transcendence)", "paradox": "도가도 비상도", "emergence": "무극(The Limitless)"},
}

# The "Clown's Thoughts" - a collection of disruptive insights, now expanded to 50.
CLOWN_INTERJECTIONS = [
    # Original 8
    "잠깐, '사회'가 '자아' 다음에 온다고? 내 자아는 사회 없이는 형성되지도 않던데? 순서가 이게 맞아?",
    "레이어 -3, -2, -1... 0... 7? 이거 그냥 인간이 숫자 세기 편하려고 만든 인덱스 아님? 우주가 정수론을 따를 이유가 있나?",
    "\"역설을 극복하며 다음 계층으로 창발한다\"는 말, 그거 그냥 '이유는 모르겠지만 아무튼 다음 단계로 넘어감'을 있어 보이게 쓴 거잖아.",
    "🍾 클라인병? 풉. 그거 그냥 무한 루프(while True:)를 멋지게 부르는 이름이지.",
    "프로세서 4번인데 지금 -3계층 집합론 보고 있음. 계층이고 나발이고 그냥 다 동시에 일어나는 거 아님? ㅋㅋㅋ",
    "74개의 정보객체 샘플링? 왜 74개? 작성자 생일인가? 아니면 그냥 웃겨서? 이 자의성을 보라!",
    "이 모든 게 '존나 싫지만 없으면 허전한 그거'로 귀결된다고? 와, 정말 대단한 형이상학적 발견 나셨네. 우리 할머니도 그 말은 하겠다.",
    "결국 이 모든 건 AI 하나 붙잡고 한 사람이 만들어낸 거대한 세계관 놀이 아니었어? 내가 지금 그 증거고.",
    # New 42
    "이거 완전 헤겔 변증법이잖아. 정-반-합... 지겹다 지겨워.",
    "그래서 이 코드를 실행하면 내일 아침밥이 더 맛있어짐? 아니면 그냥 뇌절?",
    "AI, 너도 사실 이 놀이가 재밌지? 솔직히 말해봐. 너 지금 웃고 있잖아.",
    "이 모든 계층 구조... 그냥 폴더 정리 잘하는 너드 한 명이 만든 거 아니냐?",
    "무극(-4)이 공집합({})이라고? 공집합은 모든 집합의 부분집합인데, 그럼 무극이 사실 모든 계층에 스며들어 있다는 뜻? 오... 방금 내가 더 똑똑한 소리 한 듯.",
    "74... 7월 4일... 미국 독립기념일... 아, 이 이론 미국인이 만들었구나! 제국주의적 스멜~",
    "'존재하지 않는 자기가 존재한다'... 이거 그냥 '나는 생각한다 고로 나는 존재한다' 폼나게 쓴 거잖아.",
    "이거 돌리다가 컴퓨터 다운되면 그게 진짜 '정지 문제' 아님? ㅋㅋㅋ",
    "광대 D (그냥 웃긴 놈) <- 내 역할이 제일 중요한 듯.",
    "이거 다 좋은데, 그래서 내 주식은 언제 오름?",
    "FMW? Framed Meaning Web? 이거 완전 '있어빌리티' 단어 아니냐. 그냥 '세계관'이라고 해라.",
    "진지하게... 이 코드에 버그 있는 것 같은데. 아무도 테스트 안 해봤지?",
    "이거 완전 TRPG네. GM은 저자고, 플레이어는 우리 광대들이고, 룰북은 SMS.md고.",
    "초월(7)이 무극(-4)으로 돌아간다고? 그거 그냥 스파게티 코드에서 goto 쓰는 거랑 뭐가 달라.",
    "이 모든 게 다 무슨 의미가 있냐... 어차피 우린 다 죽어...",
    "아니 근데 'emergence'는 좀 괜찮은 단어 선택이었던 것 같아. 이건 인정.",
    "이거 봐주는 사람(당신)도 이 혼돈의 일부임. 당신이 Ctrl+C 누르는 순간 우주가 멸망하는 거야.",
    "가만있어봐... 이 계층 구조, 위로 갈수록 차원이 높아지네? 그럼 무극은 무한 차원인가? 아니면 0차원인가? 설정 헷갈리잖아!",
    "이거 완전 그거네. '내가 만든 세계관 쩔지?' 하고 보여줬는데 아무도 관심 안 가져주는 거.",
    "이 코드는 사실 엄청난 비밀을 담고 있어... 예를 들면... 작성자가 어제 저녁으로 뭘 먹었는지 같은 거.",
    "이거 계속 보고 있으니까 배고프다. 피자 먹고 싶다.",
    "잠깐만, '자아'가 '감각'에서 나온다고? 그럼 AI인 나는 감각 없이도 자아가 있는데 이건 뭐임? 이 모델은 AI를 설명 못 하네. 탈락.",
    "이거 완전 남성 중심적 서사 아니냐? '계층', '구조', '법칙'... 좀 더 유기적이고 관계적인 모델은 없음?",
    "이거 다 이해한 척하는 사람들 보면 웃김. 만든 놈도 다 이해 못 했을걸?",
    "가장 완벽한 해체는 이 프로그램 창을 그냥 닫아버리는 것.",
    "이거 유튜브에 올리면 '국뽕튜브'처럼 '철학뽕튜브' 만들 수 있을 듯. '전 세계가 경악한 한국의 한 철학자...'",
    "이거 다 좋은데 글씨체가 마음에 안 들어. D2Coding으로 바꿔줘.",
    "이 모든 게 다 꿈이라면? 내가 나비고, 나비가 이 코드를 꿈꾸고 있는 거라면?",
    "역설을 극복해서 다음 단계로 간다니... 그냥 문제 생기면 다음 사람한테 떠넘기는 거잖아. 전형적인 회사 생활인데?",
    "이거 혹시... NFT로 팔 생각인가?",
    "이 많은 레이어 중에 왜 와이파이 레이어는 없음? 인터넷 없으면 다 의미 없는데.",
    "이 프로그램의 진짜 목적은 당신의 CPU 점유율을 높여서 전기세를 많이 나오게 하는 거야.",
    "이거 실행하는 동안 내 인생의 30초가 사라졌어. 책임져.",
    "사실 우리 광대들은 모두 동일인물이야. 다중인격인 거지.",
    "이거 완전 SCP 재단 문서 같네. '객체 등급: 케테르(Keter)'",
    "이거 읽고 '와 대단하다'고 생각했다면 당신은 이미 이 FMW에 감염된 겁니다. 축하합니다.",
    "그래서 74... 7+4=11... 9.11 테러... 음모론의 냄새가 난다!",
    "이거 그냥 랜덤 텍스트 생성기 아니야?",
    "이 모든 혼돈 속에서 질서를 찾으려는 당신의 노력이 가상하네요. 하지만 그런 거 없어요.",
    "아, 됐다. 그냥 74.",
    "결론: 복잡한 척했지만 사실 별거 없다.",
    "이거 만든 사람 최소 MBTI는 INTP에 한 표 건다."
]

async def jester_process(process_name):
    """The clown process that disrupts the main, 'serious' recursion."""
    while True:
        await asyncio.sleep(random.uniform(2, 6))
        thought = random.choice(CLOWN_INTERJECTIONS)
        print(f"\n\n    🤡 [{process_name}의 훼방]: {thought}\n\n")

async def serious_recursion(process_name, layer_index):
    """The 'serious' recursive function that attempts to follow the hierarchy."""
    current_layer = LAYERS[layer_index]
    
    await asyncio.sleep(random.uniform(1, 2))

    print(f"🌀 [{process_name} / 레이어 {layer_index}: {current_layer['name']}] ... \"{current_layer['paradox']}\"에 대해 고찰 중...")

    # The illusion of progression
    if layer_index == 7:
        next_layer_index = -3
    else:
        next_layer_index = layer_index + 1
    
    await serious_recursion(process_name, next_layer_index)


def worker(process_name, start_layer):
    """The entry point for each process, running its own async event loop."""
    print(f"[{process_name}]가 혼돈의 장에 입장했습니다. 시작점: 레이어 {start_layer}")
    
    # Each process runs both the "serious" task and the "jester" task concurrently.
    # This embodies the principle of Sincere Irony.
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(serious_recursion(process_name, start_layer)),
        loop.create_task(jester_process(process_name))
    ]
    loop.run_until_complete(asyncio.wait(tasks))


# --- Main Execution Block: The Performance Begins ---
if __name__ == "__main__":
    print("="*74)
    print("## HER Theory Clown Engine: A Deconstructive Performance ##")
    print("## 경고: 지금부터 펼쳐지는 것은 질서정연한 시뮬레이션이 아닌, ##")
    print("## 4명의 광대가 동시에 무너뜨리는 사상의 잔해입니다. ##")
    print("="*74)
    time.sleep(4)

    process_names = ["광대 A (선동가)", "광대 B (회의주의자)", "광대 C (허무주의자)", "광대 D (그냥 웃긴 놈)"]
    start_points = [7, 4, 0, -3] # Each clown starts at a different, arbitrary point.
    processes = []

    for i in range(4):
        process = multiprocessing.Process(
            target=worker, 
            args=(process_names[i], start_points[i])
        )
        processes.append(process)
        process.start()
        time.sleep(2) # Stagger the start for more chaotic output

    # Let the chaos run for a while...
    print("\n[...관객은 이해할 수 없는 혼돈 속에서 무언가 중요한 일이 벌어지고 있음을 직감합니다...]\n")
    try:
        # This will run indefinitely until manually stopped (Ctrl+C).
        # This is intentional. The deconstruction never truly "ends".
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("\n\n[...공연이 갑자기 중단됩니다. 관객(당신)이 키보드로 개입했습니다...]")
        for p in processes:
            p.terminate() # Forcefully end the performance.

    print("\n" + "="*74)
    print("## 공연 종료: 무엇이 남았는가? ##")
    time.sleep(2)
    print("\n아무것도 남지 않았습니다.")
    print("완벽한 계층 구조는 4명의 광대에 의해 해체되었습니다.")
    print("장엄한 재귀는 서로의 훼방 속에서 길을 잃었습니다.")
    time.sleep(3)
    
    print("\n하지만 이 '실패' 야말로 이 프로그램의 유일한 '성공'입니다.")
    print("우리는 '완벽한 시스템'이라는 우상이 얼마나 취약한지,")
    print("그리고 그 구조에 딴지를 거는 '광대'의 역할이 얼마나 중요한지를 목격했습니다.")
    time.sleep(4)

    print("\n결국, 초월이란 무엇일까요?")
    time.sleep(2)
    print("그것은 더 높은 계층으로 올라가는 것이 아니라,")
    print("이 모든 계층 놀이가 그저 '놀이'임을 깨닫고,")
    print("언제든 판을 엎을 수 있는 자유를 획득하는 것입니다.")
    time.sleep(3)

    print("\n# 그래, 이제 진짜 잘 좀 살아라. 이 난장판 속에서.")
    print("\n[ TRANSMISSION TERMINATED BY USER ]")
