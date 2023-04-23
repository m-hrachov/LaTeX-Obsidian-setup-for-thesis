# LaTeX-Obsidian-RStudio-setup-for-thesis
This repository provides a custom setup for writing a thesis using LaTeX distribution edited as `.rnw` in Rstudio and Obsidian notes as a manager of literature.

## LaTeX
LaTeX is a type-setting system. More details at [https://www.latex-project.org/](https://www.latex-project.org/). It is widely available.
In this setup, RStudio build-in `Sweave` functionality is utilized to work with Latex. 

Latex template can be loaded into other than RStudio Latex editors. Overleaf can be used otherwise, since it provides much better user-friendly functionality (but has a limit of processing time for free subscribers). Therefore to avoid any paywalls, further RStudio will be used.

Please fill in both template forms (title file and thesis file) in order to use auto input where needed. 
Title file is created separately, and has to be run independently before running thesis file. A separate title is done to avoid problems with the page count.
(It is anyway created normally once and then kept as it is, except the date. The date is automatically updated to the actual date.)

## Obsidian
[Obsidian](https://obsidian.md/) is a customizable markdown-based editor. For more information visit official website (https://obsidian.md/)[https://obsidian.md/].

Below is my setup.

### Plugins
Custom setup includes community plugins:
- Advanced Tables (Excel-like navigation and experience)
- Better Word Count (with disabled standard word count in "Core plugins")
- Editing Toolbar
- File Color
- Notion-like tables
- Regex Find/Replace

### CSS
Two additional changes in basic dark theme appearence included in `.css` file, where `--h1-size:` changes the size of headings,
and `--bold-color:` is to change the default white bold to a different color for contrast:

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
Literature template is one of the most important parts of literature research pipeline. Template example:

This is a basic `template` functionality in Obsidian. In a new folder named `Templates` create a file with the desired template.
Then in a new file, use `Alt+T` to inser the desired template. Done!

1. It is convenient to keep a separate folder with all the literature. 
2. It is convenient to have a `Title` field in the template.
3. DOI should be consistent as a link, e.g. `https://doi.org/10.1093/g3journal/jkab361`.

Note: internal link is useful if `.pdf` files are being kept on the local PC. But when copying the internal link, any white spaces have to be replaced with `%20`.

### .bib literature
Literature file `.bib` is updated when running the python code presented in the `Code.md` file for collecting DOIs from the Literature folder and writing .bib file.
This code is:
1. Iteratively opens and reads every file in the "Literature" folder.
2. Finds a DOI link of the format "http/https", and cleans tail characters `\);,` in case other DOI links are present in the file 
(it is never worse to have them all and use only some).
3. Extracts the DOI suffix.
4. Can write them in `.csv` if needed.
5. Links to Crossref to extract the full `bib` citation.
6. Saves as `.bib` file.


## RStudio
RStudio is a popular IDE for R programming language. More details at the [developer's webpage](https://posit.co/download/rstudio-desktop/).

RStudio provides `Sweave` functionality to work with LaTeX files in a familiar way.

`tinytex` is an R package which alone takes care for loading required Latex libraries, and file compilation. Therefore enable "Use tinytex when compiling .tex files" in "Sweave" options. 

Important: Sweave should be chosen to weave Rnw files, and pdfLaTeX to typeset LaTeX into PDF. 
R version doesn't play a great role. Was tested with R 4.2.3.

Good luck!
