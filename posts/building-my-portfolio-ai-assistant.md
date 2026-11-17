---
title: How I Built an AI Assistant for My Portfolio
date: 2026-11-17
summary: A walkthrough of the chat assistant on this site: keeping answers grounded in my resume, streaming replies, and the guardrails a public AI endpoint needs.
tags: AI, Claude API, Python, Flask
---

Recruiters skim. Instead of hoping someone reads my whole resume, I added a chat assistant to this site that answers questions about my experience, like "Has she led a team?" or "What healthcare software has she built?" You can try it with the chat button in the corner.

It's a small feature, but building it well meant solving the same problems any production AI feature has: keeping answers accurate, making it feel fast and protecting a public endpoint. Here's how it works.

## The architecture

The design is deliberately simple:

- **Frontend:** plain JavaScript. It sends the conversation to my server and shows the reply as it arrives.
- **Backend:** a Flask endpoint, `/api/chat`, that checks the request, calls the Claude API and streams the answer back.
- **Knowledge:** my resume data, which already powers the rest of the site, inserted into the system prompt.

There's no database and no vector search. My whole resume fits comfortably in the prompt, so a retrieval system would add complexity without improving answers. Picking the simplest design that works is a decision too.

## Keeping answers grounded

The biggest risk with an AI assistant on a resume site is that it **makes things up**. An invented job or a wrong date would do more harm than having no assistant at all.

So the system prompt is strict. The assistant must:

- answer only from my resume, which is included in the prompt
- say it doesn't know (and suggest contacting me) for anything not covered, such as salary, visa status or availability
- never invent employers, dates, numbers or technologies
- stay on topic and politely decline unrelated requests

The resume text is generated from the same Python data that renders the website, so **the assistant can never fall out of sync with the page**. When I update a job title, both change together.

```python
SYSTEM_PROMPT = f"""You are the assistant on {data.PROFILE['name']}'s portfolio website...
- Answer only from the resume below. If something isn't covered, say you don't
  have that information and suggest contacting her directly.
- Never invent employers, dates, numbers, technologies, or achievements.

<resume>
{data.resume_as_text()}
</resume>"""
```

## Making it feel fast: streaming

Waiting several seconds for a full answer feels broken. Instead, the server streams the reply piece by piece as Claude generates it, using newline-delimited JSON, and the browser shows each piece as it arrives.

```python
def generate():
    with client.messages.stream(model=MODEL, max_tokens=2000,
                                system=SYSTEM_PROMPT, messages=messages) as stream:
        for text in stream.text_stream:
            yield json.dumps({"t": text}) + "\n"

return Response(stream_with_context(generate()), mimetype="application/x-ndjson")
```

Two smaller speed-ups help too. **Prompt caching** means the long system prompt doesn't have to be reprocessed from scratch on every message, which makes replies faster and cheaper. And a **low effort setting** suits short conversational answers that don't need deep reasoning.

## Guardrails for a public endpoint

Anyone on the internet can reach this endpoint, so I treated it like any other public API:

- **Input validation:** the server checks the shape of the conversation, limits message length and sends only the most recent turns to Claude.
- **Rate limiting:** a simple in-memory limit per visitor stops one person from running up my bill.
- **Spending limit:** replies are capped in length.
- **Friendly errors:** an invalid key, a busy API or a network problem each produce a clear message for the visitor, while the details go to the server log.
- **Safe rendering:** the browser escapes the model's output before turning simple Markdown into HTML, so a reply can never inject a script into the page.

## What I'd do differently at scale

This design is right for a personal site, but I'd change a few things for a real product:

- **Store rate limits in a shared store** like Redis, since the in-memory version resets on restart and doesn't work across several servers.
- **Track quality:** log questions the assistant couldn't answer to find gaps in the content.
- **Test the guardrails:** build a small set of tricky questions and run them automatically after every prompt change.

## Takeaways

A useful AI feature is mostly ordinary good engineering: a clear source of truth, input validation, error handling and attention to cost. The model call itself is only a few lines. Everything around it decides whether the feature can be trusted.
