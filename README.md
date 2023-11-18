# llm-chatPDF-jocode
variable a llm example code

python 버젼 고정 : 3.9 버젼에서 에러없이 동작함

    cd ./llm-chatPDF-jocode

    pyenv local 3.9.18

    pyenv versions


해당 프로젝트를 위한 환경변수파일 생성 및 초기 설정

    python -m venv .venv

    ls -la

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore
    echo 'models/' >> .gitignore

    echo "# Project" >> readme.md

    ls -la

python 가상환경 activate

    source .venv/bin/activate

프로젝트에 필요한 라이브러리 설치

    pip3 install -r requirements.txt

    echo 'OPENAI_API_KEY=sk-SzxoT1.......' > .env

예제코드 테스트

    python3 2-8.py

    python3 3-1.py
    streamlit run 3-2.py

    # streamlit run 4-2.py (<-- 에러발생) # https://github.com/streamlit/streamlit/issues/1780
    python3 -m streamlit run 4-2.py

    python3 5-3.py
    python3 5-4.py
    python3 5-5.py
    python3 5-6.py
    python3 5-7.py

    streamlit run 5-8.py

    (pass) 5-9.py
    (pass) 6-2.py
    (pass) 7-1.py

python 가상환경 deactivate

    deactivate