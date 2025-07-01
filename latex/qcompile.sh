#/bin/bash

# rm ${file}.aux
# rm ${file}.bbl
# rm ${file}.blg

# fileName='diffusionMatDes'
# fileDate='10Jan25'
# file="${fileName}_${fileDate}"
file="doc"

# cp $template/lib.bib .
# subl ${file}.tex
pdflatex -shell-escape ${file}.tex
evince ${file}.pdf &
# bibtex ${file}.aux
biber ${file}
pdflatex -shell-escape ${file}
# pdflatex --shell-escape ${file}

# cp ${file}.pdf $temp/${fileName}.pdf
# dropbox sharelink $temp/${fileName}.pdf

# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=${file}_compressed.pdf $file.pdf
# evince ${file}_compressed.pdf & 

