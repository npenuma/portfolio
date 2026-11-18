# Neelima Penumarthy · Portfolio

An interactive portfolio built with Python and Flask, with an AI chat assistant (Claude) that answers visitors' questions using the resume content.

## Run locally

```powershell
.venv\Scripts\activate
pip install -r requirements.txt      # first time only
copy .env.example .env               # then paste your Anthropic API key into .env
python app.py                        # open http://127.0.0.1:5000
```

The site works without an API key. Only the chat assistant needs one.

## Edit content

All content (summary, skills, jobs, projects, highlights, and the chatbot's suggested questions) is in **`portfolio_data.py`**. The website and the chatbot's knowledge both come from this file, so one edit updates both.

- Add your GitHub URL in `PROFILE["github"]`.
- The phone number is hidden by default. Set `SHOW_PHONE = True` to show it.

## Files

| File | Purpose |
|---|---|
| `app.py` | Flask routes, plus the `/api/chat` endpoint that streams answers from Claude |
| `portfolio_data.py` | All resume and portfolio content |
| `templates/index.html` | Page layout |
| `static/css/style.css` | Styles, including light and dark themes |
| `static/js/main.js` | Interactivity: typing effect, skill filter, timeline, project tabs, chat |

## Chatbot safeguards

- It answers only from the resume data. For anything else, it points visitors to email or LinkedIn.
- Each IP address is limited to 20 messages per 10 minutes. Change this with `CHAT_RATE_LIMIT`.
- Visitor messages are capped at 1,000 characters and only the last 12 messages are sent. Replies are capped at 2,000 tokens.
- Uses `claude-opus-5-5` at low effort. Change the model with `CHAT_MODEL`.

## Deploy (free options)

**Render**: create a new Web Service from your GitHub repo.
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --worker-class gthread --threads 8 --timeout 120` (threads let several visitors chat at once; the longer timeout keeps streamed replies from being cut off)
- Add the environment variable `ANTHROPIC_API_KEY`.

**PythonAnywhere**: upload the project, create a Flask web app that points at `app.py`, and set `ANTHROPIC_API_KEY` in the WSGI file or a `.env` file.

Never commit `.env`. It is already listed in `.gitignore`.
