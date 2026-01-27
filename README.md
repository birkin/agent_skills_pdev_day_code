# Goal

Experiment with the new concept of using "skill" files for agents, for a professional-development day.

[MCP][MCP] was the hot thing in early 2025, but in the Fall Anthropic [described][initial_description] a very simple lightweight "skill" architecture of plain markdown files that were extremely effective at giving LLMs useful additional abilites, without taking up lots of contextual prompt-tokens. They've since [built][more_on_skills] on that and made it a [standard-open-format][skills_spec].

A colleague and I learn about lots of this stuff together. He recently experimented with skills directly within the context of the claude-code-app, and I decided to devote my professional-development day to learning more about skills.

[MCP]: <https://en.wikipedia.org/wiki/Model_Context_Protocol>

[initial_description]: <https://claude.com/blog/skills>

[more_on_skills]: <https://claude.com/blog/skills-explained>

[skills_spec]: <https://agentskills.io/home>

---


## see work.md for details

Link: <https://github.com/birkin/agent_skills_pdev_day_code/blob/main/work.md>

---


## Usage

```bash
uv run ./agent_skill_usage_example.py
```

Then, when prompted, enter something like:

```
Please parse the text out of the PDF at "/path/to/CNI_2025_slides.pdf"
```

---