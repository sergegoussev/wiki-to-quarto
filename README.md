# Repo to organize work to move wiki content to a quarto project

Specifically, move the [UN Task Team e-handbook](https://unstats.un.org/wiki/spaces/GWGSD/pages/85788266/UN-CEBD+Task+Team+on+Scanner+Data) to a quarto project.

Rough order of operations:
1. Download and store site map (to get all URLs of each site + base nav tree)
2. Download each site and extract markdown content and images. Store images in `/img/` directory
3. Create basic `_quarto.yaml` setup with the identical nav tree
4. Parse each `.md` file and 
 (a) change URLs to what they should be in mardown, 
 (b) remove the metadata table and create the custom `yaml` at the top of each page, 
 (c) remove the referneces and convert them to `*.bib` format + change the corresponding refernece in text
 (d) if there are formulas, convert them to `tex` format
 (d) change file name `*.md` -> `*.qmd`
5. Add contributing guide, licence, about, etc
6. Add PR and issue templates
7. Automate the release process + push to zenodo/other

Upgrades:
1. Migrate other images (say classification ones) into repo
2. Flush out style guide