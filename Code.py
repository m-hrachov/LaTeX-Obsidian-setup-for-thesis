# ----------------------------------------------------------------
#             DOI to .bib references from Obsidian notes.
# Custom scrip created by m-hrachov.
# Version 0.0.1. 
# Created 05.04.2023.
# Designed to be an external addition to the Obsidian workflow.
# 
#                            DESCRIPTION
# Extracts doi of doi-links from a Literature folder (standartized
# and not-standardized notes), and compile BibTeX citations into
# a .bib file which is saved in "Python projects" folder.
# doi-links supposed to be of a format (reges expression):
# https?://doi.org/(\d+\.\d+\/.+)
# that is equal, e.g., 
# ----------------------------------------------------------------

import os
import re
import csv
import requests
from habanero import Crossref 
from habanero import cn

# extract doi
note_dir = "D:/Obsidian vaults/Masters thesis/Literature"  # replace with the path to your vault directory

dois = []

for filename in os.listdir(os.path.abspath(note_dir)):
    if filename.endswith(".md"):  # assuming the notes are in markdown format
        with open(os.path.join(note_dir, filename), "r") as f:
            lines = f.readlines()
            # search for DOI links and extract the DOI suffix
            for line in lines:
            # searches for links, stops with a space or a newline
            # patenthesis, dots or commas are deleted later on
                match = re.search(r"https?://doi\.org/(\S+?)[\s\n;,)]*(\n|\s|$)", line)
                if match:
                # delete a dot in the end, delete ", ) ;" which are
                # character often following a link in the text
                    doi_suffix = re.sub(r"[\);,]", "", match.group(1).rstrip("."))
                    dois.append(doi_suffix)

# write the DOIs to a CSV file
with open("D:/Python projects/Citations/dois.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows([[doi] for doi in dois])

# if you want to check that the code still works fine for one doi
# print(cn.content_negotiation(ids = "10.3389/fpls.2022.932512", format = "bibtex"))


# write the DOIs to a CSV file if needed
with open("D:/Python projects/Citations/dois.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows([[doi] for doi in dois])

# from the dois list we create a list of citations

# now obtain citations for all of them

# create a Crossref object
cr = Crossref()

citations = []
not_identified = []

# try statement is responsible for ommiting warnings and 
# continuing the loop if a DOI is not found

for doi in dois:
    try:
        result = cn.content_negotiation(ids=doi, format="bibtex")
        if result:
            citations.append(result)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            not_identified.append(doi)
            print(f"Warning: {doi} not identified")
        else:
            raise e

if not_identified:
    print("These DOIs were not identified:")
    print("\n".join(not_identified))

# change the path of saving if needed
# "\n\n" is to add one empty line between citation entries
with open("D:/Python projects/Citations/citations.bib", "w") as f:
    f.write("\n\n".join(citations))

# now convert month format from string e.g. {feb} to numeric {2}
# note: correct month formats are:
# month = {2}
# mont = feb
# but NOT month = {feb}

# Define a dictionary to convert month names to numbers
month_dict = {"jan": "1", "feb": "2", "mar": "3", "apr": "4",
              "may": "5", "jun": "6", "jul": "7", "aug": "8",
              "sep": "9", "oct": "10", "nov": "11", "dec": "12"}

# Read the contents of the file
with open("D:/Python projects/Citations/citations.bib", "r") as f:
    contents = f.read()

# Replace the month names with numbers
contents = re.sub(r"month = \{([a-zA-Z]{3})\}", lambda match: "month = {" + month_dict.get(match.group(1).lower(), match.group(1)) + "}", contents)

# Write the modified contents to the file
with open("D:/Python projects/Citations/citations_modified.bib", "w") as f:
    f.write(contents)


# Remove the first citation file if needed
# os.remove("citations.bib") 

# File "citations_modified.bib" can be now placed in the
# LaTeX project folder and linked to the citation system

# end

