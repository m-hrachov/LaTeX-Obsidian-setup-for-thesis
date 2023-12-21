# LaTeX-Obsidian setup for thesis
This repository provides a custom setup for writing a thesis using LaTeX distribution edited as `.tex` in a LaTeX editor and Obsidian notes as a 
literature manager.

## LaTeX
LaTeX is a type-setting system. More details at [https://www.latex-project.org/](https://www.latex-project.org/). It is widely available.
Latex templates can be loaded into different LaTeX editors.

Please fill in both template forms (title file and thesis file) to use auto input where needed. 
Title file is created separately, and has to be run independently before running the thesis file. A separate title is done to avoid 
problems with the page count.
(It is created normally once and then kept as it is, except for the date. The date is automatically updated to the actual date when the file is re-run.)

## Obsidian
[Obsidian](https://obsidian.md/) is a customizable markdown-based editor. For more information visit the official website 
(https://obsidian.md/)[https://obsidian.md/].

Below is my setup.

### Plugins
Custom setup includes community plugins:
- Better Word Count (with disabled standard word count in "Core plugins")
- Editing Toolbar
- File Color
- Regex Find/Replace

### CSS
Two additional changes in basic dark theme appearence included in `.css` file, 
where `--h1-size:` changes the size of headings, and 
`--bold-color:` is to change the default white bold to a different color for contrast:

``` css
body.theme-dark { 
--bold-color: #ffb6c1 !important; 
}


body {
--h1-size: 1.92em;
--h2-size: 1.63em;
--h3-size: 1.45em;
--h4-size: 1.37em;
--h5-size: 1.32em;
--h6-size: 1.32em;
}
```

### Literature template

> [!Info]
> Update needed! A better way of templating a literature page would be setting up a proper YAML header. 
> The complete Python extraction pipeline must then also be changed, but this is worth a try
> since if the information is condensed in the YAML header, one could use the DataView plugin for in-Obsidian summaries.

A literature template is one of the most important parts of the literature research pipeline. Template example:

This is a basic `template` functionality in Obsidian. In a new folder named `Templates` create a file with the desired template.
Then in a new file, use `Alt+T` to insert the desired template. Done!

1. It is convenient to keep a separate folder with all the literature. 
2. It is convenient to have a `Title` field in the template.
3. DOI should be consistent as a link, e.g. `https://doi.org/10.1093/g3journal/jkab361`.

Note: internal link is useful if `.pdf` files are being kept on the local PC. But when copying the internal link, any white spaces 
have to be replaced with `%20`.

### .bib literature
Literature file `.bib` is updated when running the python code presented in the `Code.py` file for collecting DOIs from the Literature 
folder and writing .bib file.
This code is:
1. Iteratively opens and reads every file in the "Literature" folder.
2. Finds a DOI link of the format "http/https", and cleans tail characters `\);,`. In case other DOI links are present in the file 
it will catch them all (it is never worse to have them all and use only some).
3. Extracts the DOI suffix.
4. Can write them in `.csv` if needed.
5. Links to Crossref to extract the full `bib` citation.
6. Saves as `.bib` file.


## TeX Studio

TeX Studio is a free software for editing and compiling LaTeX files. This software is similar to the basic Overleaf but doesn't require 
Internet connection. This software allows to use `biber` backend and `apa` style for academic writing. 
You can access this software via the link [https://www.texstudio.org/](https://www.texstudio.org/).

Good luck!
