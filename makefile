
0p.pdf: 0p.tex
	runtex 0p

0h.pdf: 0h.tex
	runtex 0h



clean:
	rm -f *.aux *.blg *.nav *.vrb *.bbl *.log *.out *.snm *.toc

