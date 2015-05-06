# requires html to pdf converter: http://wkhtmltopdf.org/

pdf = *p.pdf *h.pdf syllabus.pdf re.pdf demo.pdf
py  = 1p.py 2p.py re.py demo.py


all: ${pdf} ${py}

syllabus.pdf: syllabus.tex
	runtex $<

%p.pdf: %p.tex
	runtex $<

%h.pdf: %h.tex
	runtex $<

re.pdf: re.html
	wkhtmltopdf --page-size Letter $< $@

re.html: re.ipynb
	ipython nbconvert --to html --template full $<

demo.pdf: demo.html
	wkhtmltopdf --page-size Letter $< $@

demo.html: demo.ipynb
	ipython nbconvert --to html --template full $<

%.py: %.ipynb
	ipython nbconvert --to python $<


clean:
	rm -f *.aux *.blg *.nav *.vrb *.bbl *.log *.out *.snm *.toc
	rm -f re.html demo.html
