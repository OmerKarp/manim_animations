How to Do a Presentation (Manim)

This project contains animated scenes for a talk about how to present clearly.
All on-screen text is in English.

Current coverage:
- Intro statement
- Principle 1: Clarity beats complexity
- Principle 2: One thing at a time
- Two intentional break cards between sections

Setup
1. Ensure Python 3.12 is available.
2. Install dependencies:

```bash
uv sync
```

Render the scene
```bash
uv run manim -pqh main.py HowToDoAPresentation
```

Use `-pql` for a faster low-quality preview while iterating.
