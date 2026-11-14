# PHYS 321: Modern Physics

Welcome to **Modern Physics** at [East Texas A&M University](https://www.etamu.edu/). These online course notes, developed by Billy Quarles, bring together physical ideas, worked examples, visualizations, and Python exercises to help you understand how relativity and quantum mechanics changed our description of nature.

PHYS 321 is a bridge from introductory physics to more advanced study. We will examine where classical models succeed, why new models became necessary, and how experimental evidence helps us decide which description to use. Along the way, you will strengthen three connected skills: solving physics problems, explaining your reasoning, and using computation to investigate physical behavior.

## What you will learn

The course develops the foundations of special relativity and quantum mechanics and explores their applications to matter and technology. By working through the material, you will practice how to:

- Connect experimental observations to the assumptions and predictions of a physical model.
- Identify when classical, relativistic, or quantum descriptions are appropriate.
- Develop symbolic solutions and interpret numerical results with appropriate units and precision.
- Use Python to check calculations, make plots, and explore how a system responds to changing parameters.
- Communicate a solution through clear prose, equations, figures, and readable code.

The notes are organized into three parts:

| Part | Main topics |
| --- | --- |
| Introduction | The origins of modern physics, special relativity, early quantum experiments, and atomic structure |
| Quantum Mechanics | Wave functions, quantum models, the hydrogen atom, atomic physics, and statistical physics |
| Applications of Modern Physics | Molecules and lasers, semiconductors, nuclei, and elementary particles |

The course schedule identifies the assigned sections and the time devoted to each topic.

## How to work through the course

Before class, read the assigned material, examine the figures, and identify a question or a step you cannot yet explain. Try the relevant example before reading its complete solution. During class, contribute to discussions and collaborative problem solving by explaining the reasoning behind your approach. After class, complete the assigned problems and revisit any ideas that remain unclear.

## Homework expectations

Write each solution as a concise scientific argument that another student—including **future-you**—can follow and check. For analytical and computational problems, use the following pattern to develop your reasoning:

| Part of the argument | Minimum length | Purpose |
| --- | --- | --- |
| **Introduction** | 2 complete sentences | Motivate the approach needed to solve the problem and identify the relevant physical ideas. Do more than restate the question. |
| **Method** | 2 complete sentences | Explain the approach, define quantities, and state assumptions. Introduce the necessary equations and describe any computational procedure. |
| **Results and Discussion** | 3 complete sentences | Develop the solution, present the results, and interpret their physical meaning. Connect consequential mathematical steps with explanations, working symbolically before substituting numerical values where appropriate. |
| **Conclusion** | 2 complete sentences | Summarize the process and main finding, and provide a specific reasonableness check using units, scale, sign, limiting behavior, or a known result. |

These are minimums for meaningful explanation, not targets to reach with filler. Equations and code do not count as complete sentences. The pattern should guide your writing; four labeled sections are not required for every problem. Use headings when they help organize a longer investigation. Related parts of a problem may share an introduction and method if every part is clearly addressed. Real papers may also discuss future directions or connections to the literature, but those are not required here.

**For short-answer questions, write one coherent paragraph of approximately five complete sentences per problem.** Address every part of the question using specific physical ideas and examples. The four-part pattern and its sentence minimums do not apply to these paragraph responses.

Include each **problem statement in bold within a blockquote**. Use Python when assigned or when it contributes meaningfully to the analysis, and place code, figures, and checks beside the explanation they support. Report numerical answers with units and justified significant figures; the digits Python prints do not determine the precision of your answer.

A complete submission consists of **two files**, a Jupyter notebook and its matching PDF, with a two-digit chapter number: `PHYS321_Chpt01_LastName.ipynb` and `PHYS321_Chpt01_LastName.pdf`. Before exporting, exit cell editing mode so all text and equations are rendered, then inspect the PDF for clipped content or unwanted source/preview columns.

Consult the [homework template](https://saturnaxis.github.io/ModernPhysics/Preamble/HW_template.html) for a worked example and guidance on saving, group work, and preparing your submission. Omit the example's colored instructional labels from your own solutions. Use the syllabus and individual assignment instructions for deadlines and grading policies.

## Developing your Python and Markdown skills

You will develop your programming skills alongside the physics. The [Introduction to Python](https://saturnaxis.github.io/ModernPhysics/Preamble/Python-basics.html) and [Introduction to Markdown](https://saturnaxis.github.io/ModernPhysics/Preamble/Markdown-basics.html) remain practical references throughout the course. Begin with the tools needed for the current assignment and return to the guides as your work becomes more demanding.

Jupyter notebooks combine the different parts of a scientific explanation in one document. Use **Markdown** for your reasoning and organization, **LaTeX** for mathematical notation, and **Python** for calculations and visualizations. Notebook chapters can be opened in Google Colab using the launch menu marked by a rocket icon, where available; save your own copy before editing.

Start by running an example and explaining what each part does. Then change a parameter, predict the outcome, and compare your prediction with the result. With practice, you should be able to adapt examples and write short calculations of your own. For instance, you might compare classical and relativistic predictions or investigate how a quantum probability distribution changes with the state.

For computational work, define variables clearly, comment on their physical meaning and units, and label plot axes. Run the notebook from the beginning before submitting it so that the results can be reproduced. Explain what the output tells you about the physics and check it against an analytical result, an estimate, or a known limiting case whenever possible.

## Background and getting started

This course draws on introductory mechanics, electricity and magnetism, waves, and calculus. Be prepared to use algebra, derivatives, and integrals and to revisit earlier ideas as they appear in new settings. Prior programming experience is helpful, but you can build the required skills through regular practice with the examples and exercises.

Begin with [Who are these notes for?](https://saturnaxis.github.io/ModernPhysics/Preamble/who-for.html), then review the Python and Markdown introductions. Open a notebook, run a code cell, and edit a text cell containing an equation. These small steps establish the workflow you will use throughout the course.

## Sources and ongoing development

These notes draw on [OpenStax: University Physics, Volume 3](https://openstax.org/books/university-physics-volume-3/pages/preface) and [Modern Physics for Scientists and Engineers](https://www.google.com/books/edition/Modern_Physics_for_Scientists_and_Engine/pWAKAAAAQBAJ?hl=en) by Thornton and Rex (2012), together with additional sources credited where used.

The book will continue to evolve as explanations, examples, and computational activities are refined. If you find an error or an unclear step, include the chapter, section, and relevant calculation when reporting it. The source files are available in the [ModernPhysics GitHub repository](https://github.com/saturnaxis/ModernPhysics).

Original material by Billy Quarles is licensed under a [Creative Commons Attribution 4.0 International License][cc-by]. Third-party material retains its own license and attribution requirements; consult the credit accompanying each item before reusing it.

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: https://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
