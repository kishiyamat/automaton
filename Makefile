report.pdf: report.md
	cat report.md | sed -e 's/、/，/g' | sed -e 's/。/．/g' | pandoc -V geometry:margin=1in --filter pandoc-citeproc --bibliography=report.bib -o report.pdf --latex-engine=lualatex --smart --standalone
