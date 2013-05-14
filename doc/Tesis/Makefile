thesis.pdf: cap*.tex *.bib Imagenes/*
	rm *.aux *.log *.bbl *.blg thesis.pdf
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

clean:
	rm  *.aux *.log *.bbl *.blg thesis.pdf
