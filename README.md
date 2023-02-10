# 직장인 창업 부트캠프 {창} 클론코딩

1. `python -m venv venv` 명령어를 실행하면 venv 라는 이름의 폴더가 생성됩니다. 이는 우리가 설치하는 패키지들을 모아두는 가상환경입니다.
2. `source venv/bin/activate` (mac) `source venv/Scripts/activate` (windows) 를 실행해 가상환경을 활성화해줍니다 (매번 VS Code 를 새로 켤 때마다, 터미널을 켤 때마다 해주셔야 합니다. 그렇지 않고 아래 설치 스크립트를 실행하면 Global 환경에 패키지가 설치됩니다)
3. `pip install -r requirements.txt` 명령어를 실행해 requirements.txt 파일에 작성해둔 패키지 목록을 모두 설치해줍니다.
4. `python app.py` 명령어를 통해 서버를 실행합니다. localhost:5000 에서 서버가 돌아감을 확인할 수 있습니다
   1. mac OS Monterey 의 경우 Airplay 관련 설정을 꺼주셔야 합니다 [참고 링크](https://stackoverflow.com/questions/69818376/localhost5000-unavailable-in-macos-v12-monterey)
