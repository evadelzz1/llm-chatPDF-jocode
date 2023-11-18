echo '

python -V

pyenv local 3.9.18

pyenv versions

which python

python -m venv .venv

ls -la

echo '.env'  >> .gitignore
echo '.venv' >> .gitignore
echo 'models/' >> .gitignore

echo "# Project" >> readme.md

ls -la

# activate

python -V

source .venv/bin/activate

pip3 install -r requirements.txt

echo 'OPENAI_API_KEY=sk-SzxoT1.......' > .env

---------------------------------

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

---------------------------------

deactivate

'

