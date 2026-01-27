Reading: <https://developers.openai.com/tracks/building-agents/>, based on `OpenAI Agents SDK: tools-as-skills + “skill files” as local instruction modules` -- from the extended-thinking answer.

Reading: <https://openai.github.io/openai-agents-python/quickstart/> based on the above.

Skimmed: <https://openai.github.io/openai-agents-python/agents/> based on the quickstart above.

---

Reading the deep-research answer: <https://chatgpt.com/share/6978d0bf-dedc-8006-a46f-2a0b88c06c17`> 

It's better, in that it more specifically addresses my question about skill-files. It notes, at the end, `All three tutorials above use the open Agent Skills standard.` (<https://agentskills.io/home>)

Going to dive into "Tutorial 1: “How to Write and Implement Agent Skills” (DigitalOcean Community)", because it focuses on parsing PDFs -- and we're actively working on PDF-accessibillity.

---

The tutorial: <https://www.digitalocean.com/community/tutorials/how-to-implement-agent-skills>

I like this overview...

```
Introduction

Agent Skills are folders of instructions, scripts, and resources that a Large Language Model (LLM) can load when relevant to perform specialized tasks in consistent, repeatable ways. They were introduced as an open framework by Claude in 2025, and the framework has been increasingly adopted by other organizations and agent developers since.

In the past, when giving an LLM a task, it was necessary to manually provide context for the LLM workflow. With Agent Skills, you’re able to separate resources and additional instructions into folders that can be accessed only when the LLM identifies it is necessary.

For example, if you’d like to have your LLM create PowerPoint presentations, rather than manually adding the style guides, graphics, and templates for your organization into the prompt each time, you can add them to a folder as a Skill and the LLM can find and use the resources independently each time you need a presentation created. You can add a large number of Skills, and LLMs can reference them like tools.

In this tutorial, you will create an Agent Skill for a PDF parser with optional folders for other reference documentation and assets.
```


