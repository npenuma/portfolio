---
title: If I Added AI to a Patient Portal Today, Here's How I'd Do It Safely
date: 2027-01-05
summary: A design walkthrough for adding AI to a healthcare app: picking the right first feature, protecting patient data, keeping clinicians in control, and planning for mistakes.
tags: Healthcare, AI, Architecture, Security
draft: true
---

> **TODO (delete this box before publishing):** This is a design-thinking post: how you *would* approach the problem, not a description of a system you built. Keep that framing honest. Read every recommendation and change anything you disagree with, because readers will take these as your views. Check current HIPAA and vendor requirements before publishing, since this post isn't legal advice. Remove `draft: true` when you're ready.

In my [last post](/blog/building-a-hipaa-aligned-patient-portal) I wrote about building a HIPAA-aligned patient portal for a speech-therapy practice. Since then, I've been learning how to build with AI, and I keep coming back to one question: if I were adding AI to that portal today, how would I do it responsibly?

Here's how I'd approach it.

## 1. Pick a first feature where mistakes are cheap

The worst way to start is with AI making clinical decisions. A better first feature **saves clinicians time while they stay in control**:

- **Drafting session-note summaries** for the therapist to review and edit.
- **Turning progress data into a plain-language update** for families, approved by the therapist before it's sent.
- **Helping staff search policies and documentation**, which involves no patient data at all.

That last option is the safest pilot: it builds trust and experience before any PHI is involved.

> **TODO:** Which of these would you pick first for the practice you worked with, and why?

## 2. Keep a human in the loop

For anything involving a patient, the AI **drafts** and a clinician **decides**. The interface should make that clear: label AI-generated text, make editing easy and require explicit approval before anything is saved or sent.

## 3. Protect patient data at every step

- Use an AI provider that will sign a **Business Associate Agreement (BAA)** and offers appropriate data-retention terms.
- Send the **minimum necessary** information. Not every task needs names or dates of birth.
- Apply the portal's existing **role-based access** to AI features too. The AI should never see records the user couldn't see themselves.
- Keep PHI out of application logs and analytics, including the prompts and responses themselves.

## 4. Log everything an auditor would ask about

Extend the portal's audit log to AI actions: who requested an AI draft, for which record, which model produced it and whether a clinician approved, edited or rejected it. This also gives you the data to measure whether the feature is actually helping.

## 5. Plan for the AI being wrong

AI models can produce confident, incorrect text. Design for that:

- Ground outputs in the patient's actual records, and show where each statement came from.
- Build a test set of realistic, **de-identified** cases and check outputs before every change.
- Watch the rejection and edit rate. If clinicians rewrite most drafts, the feature isn't working.
- Provide a simple way to report a bad output.

## 6. Roll out gradually

Start with a few volunteer clinicians at one or two offices, gather feedback, fix what breaks and only then expand. Across 25 offices, a slow rollout is much cheaper than a fast mistake.

## Takeaways

Adding AI to healthcare software is mostly about the same things that made the original portal trustworthy: access control, audit trails, data minimization and respect for clinicians' judgment. The model is the easy part. Earning trust is the real work.

> **TODO:** Close with a sentence in your own words about why this work matters to you.
