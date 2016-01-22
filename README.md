Translate Instructions to Cycles
________________________________
* compile your source
* translate the dump 

        avr-objdump -zS source.elf | python avr-cycles.py
The script simply replaces instructions found in the .csv table line by line.
* example 

        ISR(TIMER1_COMPA_vect) {
        2fc:   1f 92           [[PUSH -> 2]]   r1
        2fe:   0f 92           [[PUSH -> 2]]   r0
        300:   0f b6           [[IN -> 1]]     r0, 0x3f        ; 63
        302:   0f 92           [[PUSH -> 2]]   r0
        304:   11 24           [[EOR -> 1]]    r1, r1
        306:   8f 93           [[PUSH -> 2]]   r24
        [...]

where "PUSH -> 2" indicates a PUSH consumes 2 cycles 

Obtain Cycle Table
__________________
* convert the manual to text

        pdftotext -layout atmega-xxx-manual.pdf foo.txt
* grab the 1st and last column of the instruction set summary section 
(i.e. block selection with Geany: ctrl + shift + click)
* store the columns to 

        tables/atmega-xxx-instruction-2-cycle.csv
