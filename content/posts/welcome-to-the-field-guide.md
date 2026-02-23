---
title: "Welcome to the Field Guide"
date: 2026-02-23
draft: false
tags: ["field-guide", "build-log"]
description: "What this blog is and how I use it as a robotics toolbox."
---

This blog is my robotics **field guide**: notes and tools from building robots — what worked, what broke, and what I learned.

It’s not a “perfect tutorial” blog. It’s a *lab notebook you can actually use*.

{{< video src="videos/welcome.mp4" >}}

## Why this exists
Robotics is a stack of stacks: software, physics, sensors, math, electronics, debugging, and the occasional existential crisis when Gazebo launches upside-down.

So I’m building a system that helps me (and maybe you) learn like a builder:

- **Capture** what happened (even the mistakes)
- **Extract** patterns and checklists
- **Reuse** them in the next project
- **Improve** the mental model each loop

## What you’ll find here
- **Build logs** (real progress, real mistakes, real fixes)
- **Toolbox posts** (reusable patterns, templates, checklists)
- **Clear explanations** that don’t rely on memorization

# The learning principles behind this blog
I don’t learn well by “memorize first, understand later.”
For me, learning sticks when it’s built on three principles:

### 1. Experience - (build memories you can *reuse*)
<u>Episodic memory bias:</u> You remember what you lived (or vividly imagined living) more than what you only “studied.”

<u>Mental simulation strength:</u> The “MIND strengths” often work like a scene-building engine. You take fragments of experiences and recombine them to model how systems work, predict outcomes, and solve problems.
  
  - Material Reasoning: “What object/space picture is this?”

  - Interconnected Reasoning: “What does this connect to that I already know?”

  - Narrative Reasoning: “What’s the story of failure → fix?”

  - Dynamic Reasoning: “How does it change over time if I tweak a parameter?”


### 2. Understanding - (connect it to the big picture)
Facts don’t stick in isolation. If I can’t connect an idea to why it exists, where it fits, and what it affects, it evaporates. My way of learning is meaning-first: **I build understanding by building a network, not by collecting definitions.** (That’s basically “meaningful learning” + schema building.)

So whenever I learn something in robotics, I force three anchors:
  
  - System architecture: where it lives in the stack (nodes, TF, costmaps, sensors)

  - Underlying principle: the rule underneath (control, estimation, geometry, signals)

  - Practical consequence: what breaks if I ignore it (failure modes + debugging clues)

I also start with a short roadmap before the details (big picture → then zoom in). That preview gives my brain a place to attach the new information—like adding the map before exploring the territory.

### 3. Prediction - (learning by testing models)
My strongest learning happens through prediction errors: I form a guess about what will happen next, test it, and let the mismatch (the “surprise”) teach me. The brain is basically a prediction machine that updates its internal model when reality disagrees.

When my prediction is correct, I move on. When it’s wrong, my attention spikes and the lesson sticks—because prediction error is tightly linked to the brain’s learning/reward machinery (including dopamine-based error signals).

So instead of swallowing facts like pills, I learn best when I’m shown a case, asked to infer the rule, then asked to predict what happens in a new situation—and debug my thinking when I’m wrong.

That’s why I use this loop in almost every project:

### The IDEA Loop 

I use a simple loop to make this practical:

  1. **Imagine** — simulate possible outcomes using what I already know
  
  2. **Decide** — pick the most likely outcome (my prediction)
  
  3. **Explore** — test it in the real world (or a sim / example)
  
  4. **Assess** — compare result vs prediction; if wrong, find why and update the model, then repeat

## What makes this “Field Guide” style
When I explain something, I try to do three things:

- **Start big-picture**: what problem are we solving and why?
- **Zoom into atoms**: what each part does (code, params, frames, signals)
- **End with reuse**: a checklist, template, or pattern you can copy

If a post includes code, it usually includes:
- What it does
- Why it’s structured that way
- Common failure modes & troubleshooting

## Who this is for
- People building with ROS 2, Nav2, Gazebo/Isaac, sensors, and real robots
- People who want *reasoning-first learning*
- People who like honest notes more than polished marketing

## Where to start
If you’re new here:
- Start with the **Build Logs** tag for the story of what I’m building
- Use **Toolbox** posts when you want fast reusable patterns


---

> We are not here to become repositories of facts.  
> We are here to become explorers — mental simulators who can see the terrain ahead, connect distant ideas, and chart paths into the unknown.
>
> Details matter.  
> But they serve the vision.
> <br>
> Welcome to the Field Guide...
> 
> <br>
> "Do. Fail. Learn. The rest will follow. — Tony Fadell"
