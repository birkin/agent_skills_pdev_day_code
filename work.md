# Work notes

(Note: sections are in reverse chronological order)

- [switching to LMStudio](#switching-to-lmstudio)
- [following tutorial](#following-tutorial)
- [choosing tutorial](#choosing-tutorial)
- [skimming second skill-tutorial suggestions](#skimming-second-skill-tutorial-suggestions)
- [(start) skimming first skill-tutorials suggestions](#start-skimming-first-skill-tutorials-suggestions)

---

## switching to LMStudio

here

---


## following tutorial

Ok -- fully implemented the tutorial.

Got a "model-access-key" from D.O.

Set up a dotenv envar for the key.

So the main initial work seems to be in setting up the script -- implementing the structure of the `skills/pdf-parsing/` folder, and the two files in it, `parse_pdf.py` and `SKILL.md`.

I was able to verify the code via successfully running:
```
% uv run ./skills/pdf-parsing/parse_pdf.py extract_text --file_path "/path/to/CNI_2025_slides.pdf"
```

(...which runs the script -- no llm interaction)

Then the second main piece of work is to instruct the llm to use the skill, via `agent_example.py`.

---


## choosing tutorial

The tutorial: <https://www.digitalocean.com/community/tutorials/how-to-implement-agent-skills>

I like this overview...

```
Introduction

Agent Skills are folders of instructions, scripts, and resources that a Large Language Model (LLM) can load when relevant to perform specialized tasks in consistent, repeatable ways. They were introduced as an open framework by Claude in 2025, and the framework has been increasingly adopted by other organizations and agent developers since.

In the past, when giving an LLM a task, it was necessary to manually provide context for the LLM workflow. With Agent Skills, you’re able to separate resources and additional instructions into folders that can be accessed only when the LLM identifies it is necessary.

For example, if you’d like to have your LLM create PowerPoint presentations, rather than manually adding the style guides, graphics, and templates for your organization into the prompt each time, you can add them to a folder as a Skill and the LLM can find and use the resources independently each time you need a presentation created. You can add a large number of Skills, and LLMs can reference them like tools.

In this tutorial, you will create an Agent Skill for a PDF parser with optional folders for other reference documentation and assets.
```

I'm using a modified version of the example scripts at:
<https://github.com/adugan-do/Agent-Skills/blob/main/skills/pdf-parsing/>

...so I can use `uv`.

---


## skimming second skill-tutorial suggestions

Reading the deep-research answer: <https://chatgpt.com/share/6978d0bf-dedc-8006-a46f-2a0b88c06c17`> 

It's better, in that it more specifically addresses my question about skill-files. It notes, at the end, `All three tutorials above use the open Agent Skills standard.` (<https://agentskills.io/home>)

Going to dive into "Tutorial 1: “How to Write and Implement Agent Skills” (DigitalOcean Community)", because it focuses on parsing PDFs -- and we're actively working on PDF-accessibillity.

---


## (start) skimming first skill-tutorials suggestions

Skimmed: <https://openai.github.io/openai-agents-python/agents/> based on the quickstart reading.

Reading: <https://openai.github.io/openai-agents-python/quickstart/> based on the building-agents reading.

Reading: <https://developers.openai.com/tracks/building-agents/>, based on `OpenAI Agents SDK: tools-as-skills + “skill files” as local instruction modules` -- from the extended-thinking answer.



---


---