---
title: What I Learned Building a HIPAA-Aligned Patient Portal
date: 2026-12-15
summary: Lessons from designing a patient portal for a speech-therapy practice across 25 offices: encryption, audit logging, role-based access, and why security is an architecture decision.
tags: Healthcare, Security, Architecture, HIPAA
draft: true
---

> **TODO (delete this box before publishing):** This draft is built only from the facts on your resume. Add specific details and stories where marked. Before publishing, make sure you don't reveal anything confidential about your employer's systems, such as internal hostnames, vendors, schema details or security weaknesses. Describe the approach, not the exact setup. Remove `draft: true` when you're ready.

At a speech-therapy practice with 25 offices, I designed and built a patient portal from scratch. It lets therapists and staff track patient goals and progress over time. Because it handles protected health information (PHI), security couldn't be added at the end. It had to shape the design from the first day.

## Start with the data, not the screens

Before designing any pages, I mapped out what data the portal would hold and who needed to see it. That answered the most important questions early: which fields count as PHI, which roles need access to which records, and what must be logged.

> **TODO:** Add a real example, such as one decision about the data model that you'd have gotten wrong if you'd started from the screens.

## Encryption

PHI is protected both when it travels over the network and when it's stored.

> **TODO:** Describe your general approach (for example, which data is encrypted at the field level and how keys are handled), without exact configuration.

## Role-based access, enforced in more than one place

Therapists, administrators and other staff each need different access. The key lesson: **hiding a button in the interface isn't access control.** Permissions are enforced at the API and database layers, so a request that skips the interface still can't reach data it shouldn't.

> **TODO:** Give an example of a role rule that was harder than it looked, such as a therapist covering another therapist's patients.

## Audit logging

In healthcare, "who looked at this record, and when?" has to have an answer. The portal logs access to patient data so that question can always be answered.

> **TODO:** What did you log, and what did you deliberately *not* log? (Logs must not leak PHI themselves.)

## Showing progress without exposing more than needed

Therapists track patient goals through progress charts, powered by GraphQL. One advantage of GraphQL here is that each view requests exactly the fields it needs and nothing more.

> **TODO:** Describe how the charts helped therapists or families in practice.

## What I'd tell another engineer

- Treat security as part of the architecture, not a feature at the end.
- Enforce access rules on the server, as close to the data as possible.
- Design audit logging alongside the data model.
- Collect only the data you actually need. Data you don't store can't leak.

> **TODO:** Add one thing you'd do differently today.

## What's next

Healthcare is where I want to apply AI next, and building this portal taught me that any AI feature in this space has to meet the same bar. In my next post, I'll look at how I'd add AI to a portal like this one safely.
