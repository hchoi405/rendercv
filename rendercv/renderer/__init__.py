"""
The `rendercv.renderer` package contains the necessary classes and functions for
for generating $\\LaTeX$, PDF, Markdown, HTML, and PNG files from the
`RenderCVDataModel` object.

The $\\LaTeX$ and Markdown files are generated with
[Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templates. Then, the $\\LaTeX$
file is rendered into a PDF with [TinyTeX](https://yihui.org/tinytex/), a $\\LaTeX$
distribution. The Markdown file is rendered into an HTML file with `markdown` package.
The PDF files are rendered into PNG files with `PyMuPDF`/`fitz` package.
"""

from .renderer import (
    copy_theme_files_to_output_directory,
    render_a_latex_file,
    render_a_latex_file_and_copy_theme_files,
    render_a_markdown_file,
    render_a_pdf_from_latex,
    render_an_html_from_markdown,
    render_pngs_from_pdf,
)

__all__ = [
    "copy_theme_files_to_output_directory",
    "render_a_latex_file",
    "render_a_markdown_file",
    "render_a_latex_file_and_copy_theme_files",
    "render_a_pdf_from_latex",
    "render_pngs_from_pdf",
    "render_an_html_from_markdown",
]
