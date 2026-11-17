---
title: AI for Beginners: What I Learned from Claude 101
date: 2026-11-17
summary: My notes from Anthropic's free Claude 101 course: what an AI assistant is, how to ask it better questions, and the features that make it useful for everyday work.
tags: AI, Claude, Learning
---

I've spent years building software, but using AI well is a skill of its own. To learn it properly, I started at the beginning with **Claude 101**, a free beginner course from Anthropic Academy. These are my notes, written for anyone who's just getting started too.

## What is an AI assistant, really?

Claude is a *large language model* (LLM). It learned patterns from a huge amount of text, and it uses those patterns to understand what you write and respond in natural language. You can ask it to explain a concept, draft an email, summarize a document or think through a problem with you.

Two things helped me set the right expectations early:

- **It's a collaborator, not a search engine.** It's best when you work back and forth with it, not when you ask one question and leave.
- **It can be wrong.** It sometimes states things confidently that aren't true. For anything that matters, check the facts.

## Your first conversation

The course starts simply: open a chat and ask something. The lesson that stuck with me is that **a conversation builds on itself**. If the first answer isn't quite right, you don't start over. You reply with "make it shorter," "explain it like I'm new to this," or "what did you assume here?"

## Getting better results

This was the most useful part for me. Better answers come from better instructions:

1. **Give context.** Say who you are, what you're working on and who the result is for.
2. **Be specific about the output.** Say the length, the format (bullets, a table, an email) and the tone.
3. **Share examples.** Show it a sample of what "good" looks like.
4. **Break big tasks into steps.** Outline first, then draft, then review.
5. **Ask it to check its own work.** For example: "What might be wrong or missing in this answer?"

Here's a before-and-after:

> **Before:** "Write about my project."
>
> **After:** "I'm a software engineer writing a two-paragraph summary of a patient-portal project for my portfolio. The audience is hiring managers. Focus on the security design and the impact on staff time, and keep the tone confident but plain."

The second prompt takes 30 seconds longer to write and saves several rounds of edits.

## Organizing your work: Projects

**Projects** let you group related chats and give Claude shared background, like documents and standing instructions, so you don't repeat yourself in every conversation. I think of a Project as a workspace for one goal, like "job search" or "learning RAG."

## Creating with Artifacts

When Claude produces something substantial, like a document, a piece of code or a small interactive page, it can appear as an **Artifact**: a separate panel you can view, edit and keep improving. That makes it feel less like chatting and more like building something together.

## Skills and connected tools

Later modules cover how Claude can do more than answer from what it already knows:

- **Skills** are packaged instructions and resources that teach Claude how to do a particular kind of task consistently.
- **Connectors** link Claude to tools you already use, so it can work with your real files and information, with your permission.
- **Research** lets it search across many sources for deeper questions and come back with a summary of what it found.

## What I'm taking away

- Treat AI as a teammate you have to brief well.
- Clear context and specific requests matter more than clever wording.
- Verify anything important, especially facts and numbers.
- Start with everyday tasks, then explore Projects, Artifacts and connected tools as you get comfortable.

## What's next

Next, I want to go beyond using AI to building with it: calling the Claude API from code, and learning how retrieval-augmented generation (RAG) works. I'll write about that in my next post.

*If you're starting your own AI learning journey, Claude 101 is a good, gentle first step. It's free on Anthropic Academy.*
