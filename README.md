Translate Instructions to Cycles
________________________________
* compile your source
* translate the dump 

        avr-objdump -zS source.elf | python avr-cycles.py
The script simply replaces instructions found in the .csv table line by line.
* example output snippet 

| Normal | Translated |
|-----|------|
|`[...]`|`[...]`|
|`ISR(TIMER1_COMPA_vect) {`         |`ISR(TIMER1_COMPA_vect) {`|
|` 2b8: 1f 92 push r1`              |` 2b8: 1f 92 [[PUSH -> 2]] r1`|
|` 2ba: 0f 92 push r0`              |` 2ba: 0f 92 [[PUSH -> 2]] r0`|
|` 2bc: 0f b6 in   r0, 0x3f ; 63`   |` 2bc: 0f b6 [[IN -> 1]]   r0, 0x3f ; 63`|
|` 2be: 0f 92 push r0`              |` 2be: 0f 92 [[PUSH -> 2]] r0`|
|` 2c0: 11 24 eor  r1, r1`          |` 2c0: 11 24 [[EOR -> 1]]  r1, r1`|
|` 2c2: 0b b6 in   r0, 0x3b ; 59`   |` 2c2: 0b b6 [[IN -> 1]]   r0, 0x3b ; 59`|
|` 2c4: 0f 92 push r0`              |` 2c4: 0f 92 [[PUSH -> 2]] r0`|
|` 2c6: 8f 93 push r24`             |` 2c6: 8f 93 [[PUSH -> 2]] r24`|
|` 2c8: 9f 93 push r25`             |` 2c8: 9f 93 [[PUSH -> 2]] r25`|
|` 2ca: ef 93 push r30`             |` 2ca: ef 93 [[PUSH -> 2]] r30`|
|` 2cc: ff 93 push r31`             |` 2cc: ff 93 [[PUSH -> 2]] r31`|
|`[...]`|`[...]`|

Obtain Cycle Table
__________________
* convert the manual to text

        pdftotext -layout atmel-xxx-datasheet.pdf foo.txt
* grab the 1st and last column of the instruction set summary section 
(i.e. block selection with Geany: ctrl + shift + click)
* store the columns to 

        instruction-tables/atmel-xxx-xxx.csv

Configuration - avr-cycles.conf
_____________
Modify the `instructionTable` field for your needs:

        {
            "instructionTablesFolder" : "instruction-tables",
            "instructionTable" : "atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561.csv",
            "___instructionTable" : "atmel-8303-8-bit-avr-microcontroller-tinyavr-attiny1634.csv"
        }
