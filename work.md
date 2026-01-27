# Work notes

(Note: sections are in reverse chronological order)

- [switching to LMStudio](#switching-to-lmstudio)
- [following tutorial](#following-tutorial)
- [choosing tutorial](#choosing-tutorial)
- [skimming second skill-tutorial suggestions](#skimming-second-skill-tutorial-suggestions)
- [(start) skimming first skill-tutorials suggestions](#start-skimming-first-skill-tutorials-suggestions)

---

## example interaction

```
birkin@Brown-50021K9L agent_skills_pdev_day_code % uv run ./agent_skill_usage_example.py 
============================================================
SIMPLE TOOL-BASED SKILLS EXAMPLE
============================================================

✅ Found 1 skills:
   - pdf-processing: Extracts text from PDF files using PyPDF2.

============================================================
CHAT (type 'quit' to exit)
============================================================

You: Please parse the text out of the PDF at "/path/to/CNI_2025_slides.pdf"

============================================================
USER: Please parse the text out of the PDF at "/path/to/CNI_2025_slides.pdf"
============================================================

[Turn 1]
💭 LLM: {"function_call": {"name": "activate_skill", "arguments": {"skill_name": "pdf-processing"}}}

🔧 activate_skill({"skill_name": "pdf-processing"})
📥 {
  "success": true,
  "instructions": "---\nname: pdf-processing\ndescription: Extracts text from PDF files using PyPDF2.\n---\n\n# PDF Processing Skill\n\n## When to use this skill\nUse this skill when a user needs to extract text from a PDF file.\n\n## How to Use this Skill\nThis skill provides the `extract_text()` function from the `parse_pdf.py` script. Import it into your agent script:\n\npython\nfrom skills.pdf_parsing.parse_pdf import extract_text\n\nresult = extract_text(\n    file_path=\"/path/to/document.pdf\",\n    pages=\"all\"  # or \"1-3\" or \"1,2,3\"\n)\n\n### Parameters\n- `file_path` (str): Path to the PDF file\n- `pages` (str): Pages to extract - \"all\", \"1-3\" (range), or \"1,2,3\" (specific pages)\n\n### Returns\nJSON object with:\n- `success` (bool): Whether extraction succeeded\n- `file_path` (str): Path to the processed file\n- `total_pages` (int): Total pages in PDF\n- `extracted_pages` (int): Number of pages extracted\n- `pages` (list): Array of {page: number, text: string} objects\n\nAlternatively, you can call the script directly from the command line:\ncommand\nuv run ./skills/pdf-parsing/parse_pdf.py extract_text --file_path /path/to/file.pdf --pages all\n"
}

[Turn 2]
💭 LLM: {"function_call": {"name": "execute_skill", "arguments": {"skill_name": "pdf-processing", "action": "extract_text", "params": {"file_path": "/path/to/CNI_2025_slides.pdf", "pages": "all"}}}}

🔧 execute_skill({"skill_name": "pdf-processing", "action": "extract_text", "params": {"file_path": "/path/to/CNI_2025_slides.pdf", "pages": "all"}})
📥 {
  "success": true,
  "file_path": "/path/to/CNI_2025_slides.pdf",
  "total_pages": 18,
  "extracted_pages": 18,
  "pages": [
    {
      "page": 1,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 Hall-Hoag at Scale: \nTaming 800,000 Pages \nJustin Uhr & Birkin Diana "
    },
    {
      "page": 2,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 the BDR\n"
    },
    {
      "page": 3,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 \nhall-hoag\n(above \nthe fold) "
    },
    {
      "page": 4,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 hall-hoag\n(below \nthe fold) \n16.1-K orgs \n681.7-K items \n(so far) \n"
    },
    {
      "page": 5,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 in this talk... \n\u25cf the preparation and ingestion pipeline \n\u25cf lessons learned (scale) \n\u25cf improvements \n\u25cb discovery \n\u25cb item-organization "
    },
    {
      "page": 6,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 Pipeline \nOverview\nImages of \nScanned \nDocs from \nVendor Metadata \nFiles from \nLibrarians Preparation \nCheck inputs \nand create \noutput file \ndirectories Create \npage-level \nmetadata based \non org-level \nmetadata \nMain Pipeline \nDetect \nOrientation and \nrotate if needed Run Tesseract \nOCR and output \nALTO xml \nCreate PDF - add document image - \nwrite invisible text, using location and \nsize information to align it with the \nmatching text in the image \nWrite org- and \npage-level tracker \nfilesCreate JP2 \nDerivative Image Ingestion \nIngest metadata and content files \ninto BDR. \nFirst creating org-level \u2018parent\u2019 \nobjects and then adding pages as \n\u2018child\u2019 objects \nAdd ingestion info to tracker files Find new candidates for ingest \nbased on tracker files \nDouble-check using solr to avoid \nduplication "
    },
    {
      "page": 7,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 lessons learned... \n\u25cf the more validation that can be done up-front -- the better \n\u25cb con\ufb01rming metadata, checking vendor images \n\u25cf there are _going_ to be errors -- accept them and prepare for them as best you can \n\u25cb make sure they don\u2019t break the process \n\u25cb track them to be handled later \n\u25cf \ufb01gure out work\ufb02ows with colleagues to reduce bottlenecks "
    },
    {
      "page": 8,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 lessons learned... \n\u25cf at this scale, small things add up \n\u25cb an error that affects only 0.02% of pages occurs every week \n\u25cb extra seconds per item can add months to the total \n\u25cf it's ok to implement a best-for-now solution \n\u25cb by the time you implement a solution a better one will be available "
    },
    {
      "page": 9,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 2026..."
    },
    {
      "page": 10,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 discovery challenge \nThe question...  \nHow can we make these items discoverable, \nwithout overwhelming results \nwith possibly-offensive extremist content? "
    },
    {
      "page": 11,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 indexing ideas... \n\u25cf weight results \n\u25cf deselected-toggle \n\u25cf collection-only \n\u25cf topic/entity-extraction \n\u25cf (no snippets) "
    },
    {
      "page": 12,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 items  \u2260  documents \nimplications of scanning process... \n\u25cf no item-level metadata \n\u25cf no connection between scanned items "
    },
    {
      "page": 13,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 browse improvement \nLlama-generated summarization for an item... \nThe text describes the political battle within the US State Department during World War \nII and after. A group led by Joseph C. Grew, Eugene Dooman, Stanley Hornbeck, James C. \nDunn, and others wanted to maintain an objective attitude toward the Communists but \nwas denounced as \"fascists\" and \"champions of Munich\" by another group led by Dean \nAcheson and Alger Hiss. This group sought to drive Grew's group out...  \n(auto-summarization of extracted-text) \n(code-link )\n"
    },
    {
      "page": 14,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 \ndocs?\nhumans can tell "
    },
    {
      "page": 15,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 grouping items \nvia CLIP embedding model \n\u25cf \"embeddings\" \n\u25cf 40 out of 50 items successfully associated \n(code-link )\n"
    },
    {
      "page": 16,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 grouping items \nvia multi-modal model (gemma) "
    },
    {
      "page": 17,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 grouping items via multi-modal model (gemma) \n[\n    {\n        \"document_id\": \"1\" , \n        \"proposed_document_title\": \"House Committee Report: American Nazi Party Investigation\" , \n        \"page_number\": 1, \n        \"is_\ufb01nal_page\": false, \n        \"is_standalone\": false \n    },\n    {\n        \"document_id\": \"2\" , \n        \"proposed_document_title\": \"House Committee Report: American Nazi Party Investigation\" , \n        \"page_number\": 2, \n        \"is_\ufb01nal_page\": false, \n        \"is_standalone\": false \n    },\n    (--snip--) \n    {\n        \"document_id\": \"2\" , \n        \"proposed_document_title\": \"Committee on Un-American Activities Publication Request\" , \n        (--snip--) \n    }\n]"
    },
    {
      "page": 18,
      "text": "Brown University Library   \u2014   CNI, 2025-December-11 closing...\nWe're looking forward to 2026 work! \n\u25cf Applying these  technology improvements \n\u25cf Working with the team on policy issues \nWe'd also like to thank the other members of our team, and the Hay librarians, who helped implement this project. "
    }
  ]
}

[Turn 3]
💭 LLM: The PDF file "/path/to/CNI_2025_slides.pdf" has been successfully parsed, and the text from all 18 pages has been extracted. The extracted text includes presentations slides from a talk at the CNI conference in 2025, discussing the Brown University Library's project to process and ingest 800,000 pages of scanned documents into their digital repository. The talk covers topics such as the preparation and ingestion pipeline, lessons learned from working at scale, and improvements to discovery and item organization. 

Here is a brief summary of the content:

* The project involved scanning and ingesting a large number of documents, with a focus on validation and error handling.
* The team learned that small issues can add up at scale, and that it's essential to implement solutions that can handle errors and exceptions.
* The talk also discusses the challenge of making the ingested items discoverable without overwhelming search results with potentially offensive content.
* The team explored various solutions, including weighting search results, using collection-only searching, and applying topic and entity extraction techniques.
* The project also involved improving browse functionality, using auto-summarization and multi-modal models to group related items together.

The extracted text includes code snippets, examples, and references to specific technologies and tools used in the project. If you would like to know more about a specific aspect of the project, please let me know and I can try to provide more information.

AGENT: The PDF file "/path/to/CNI_2025_slides.pdf" has been successfully parsed, and the text from all 18 pages has been extracted. The extracted text includes presentations slides from a talk at the CNI conference in 2025, discussing the Brown University Library's project to process and ingest 800,000 pages of scanned documents into their digital repository. The talk covers topics such as the preparation and ingestion pipeline, lessons learned from working at scale, and improvements to discovery and item organization. 

Here is a brief summary of the content:

* The project involved scanning and ingesting a large number of documents, with a focus on validation and error handling.
* The team learned that small issues can add up at scale, and that it's essential to implement solutions that can handle errors and exceptions.
* The talk also discusses the challenge of making the ingested items discoverable without overwhelming search results with potentially offensive content.
* The team explored various solutions, including weighting search results, using collection-only searching, and applying topic and entity extraction techniques.
* The project also involved improving browse functionality, using auto-summarization and multi-modal models to group related items together.

The extracted text includes code snippets, examples, and references to specific technologies and tools used in the project. If you would like to know more about a specific aspect of the project, please let me know and I can try to provide more information.


You: 
```

---


## switching to LMStudio

I installed LMStudio, got familiar with it, and downloaded `qwen/qwen3-8b`. I updated the `.env` and `agent_example.py` to replace hardcoded variables with envars.

I then ran the main code: `uv run ./agent_example.py`. It found the skill, and prompted me to use it. But when I entered the standard:
```
Please parse the text out of the PDF at "/path/to/CNI_2025_slides.pdf"
```

...the results were bad -- it didn't seem to try to extract the text, and seemed to quit early.

Turns out qwen wraps a lot of its response in `<think></think>` tags -- and adding the cleaner function did the trick.

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