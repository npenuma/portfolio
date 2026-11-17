---
title: Building My First RAG App: Chatting With My Own Documents
date: 2026-12-01
summary: What retrieval-augmented generation is, when you need it, and what I learned building a small app that answers questions from my own documents.
tags: AI, RAG, Claude API, Python
draft: true
---

> **TODO (delete this box before publishing):** This post is a draft. It explains RAG accurately, but the "what I built" parts are placeholders. Build the small app first, then replace each TODO with what actually happened, including your real code, results and surprises. Remove `draft: true` from the header when you're ready to publish.

In my [last post](/blog/building-my-portfolio-ai-assistant) I explained that my portfolio assistant doesn't need retrieval, because my whole resume fits in the prompt. That made me curious: what happens when the information *doesn't* fit? That's the problem retrieval-augmented generation (RAG) solves.

## What is RAG?

A language model only knows what it learned in training plus what you put in the prompt. RAG adds a step before the model answers:

1. **Retrieve:** search your documents for the passages most relevant to the question.
2. **Augment:** put those passages into the prompt.
3. **Generate:** ask the model to answer *using only those passages*, and cite them.

The model gets the right information at the right moment, without you pasting entire documents into every request.

## When you need it, and when you don't

- **You don't need RAG** when your content is small and stable. Just put it in the prompt, as my portfolio assistant does.
- **You need RAG** when the content is too large for the prompt, changes often, or when you need answers that point back to a source.

## What I built

> **TODO:** Describe your app in two or three sentences. What documents did you use? Good choices include your own blog posts, a set of public health guidelines or a product manual. Avoid anything with private or patient data.

## Step 1: Split documents into chunks

Long documents are split into passages of a few paragraphs each, so the search can return just the relevant part.

> **TODO:** What chunk size did you choose, and why? Did splitting by headings work better than splitting by length?

## Step 2: Find the relevant chunks

The simplest retriever scores each chunk by how many words it shares with the question. More advanced systems use *embeddings*, which match passages by meaning instead of exact words.

```python
def retrieve(question, chunks, k=3):
    q_words = set(question.lower().split())
    scored = sorted(chunks, key=lambda c: len(q_words & set(c.lower().split())), reverse=True)
    return scored[:k]
```

> **TODO:** Replace this with your real retrieval code, and say whether you moved from keyword matching to embeddings.

## Step 3: Ask Claude to answer from the sources

```python
context = "\n\n".join(f"<source id='{i}'>{c}</source>" for i, c in enumerate(top_chunks))
reply = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    system="Answer only from the sources provided. Cite source ids. "
           "If the sources don't contain the answer, say so.",
    messages=[{"role": "user", "content": f"{context}\n\nQuestion: {question}"}],
)
```

## What surprised me

> **TODO:** This is the most valuable section for readers and hiring managers. Ideas: questions that failed because the right chunk wasn't retrieved, how often the model said "I don't know" correctly, and what changed when you adjusted chunk size or the number of chunks.

## What I'd improve next

> **TODO:** For example, embeddings, re-ranking, a small test set of questions with known answers, or showing citations in the UI.

## Takeaways

RAG is less about the model and more about **getting the right information to it**. Most quality problems I hit were retrieval problems, not generation problems. *(TODO: confirm this matches your experience, or rewrite it.)*
