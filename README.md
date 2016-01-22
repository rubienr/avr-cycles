Translate instructions to cycles
________________________________
* compile your source
* translate the dump 

        avr-objdump -zS source.elf | python avr-cycles.py


Obtain cycle table
__________________
* convert the manual to text

        pdftotext -layout atmega-xxx-manual.pdf foo.txt
* grab the 1st and last column of the instruction set summary section 
(i.e. block selection with Geany: ctrl + shift + click)
* store the columns to 

        tables/atmega-xxx-instruction-2-cycle.csv
