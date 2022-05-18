# This Makefile is designed to be simple and readable.  It does not
# aim at portability.  It requires GNU Make.

BISON = bison
# JAVAC = javac
PYTHON = python

all: Calc.py

%.py %.html %.gv: %.y
	$(BISON) $(BISONFLAGS) --html --graph -o $*.py $<

# %.class: %.java
# 	$(JAVAC) $(JAVACFLAGS) $<

run: Calc.py
	@echo "Type arithmetic expressions.  Quit with ctrl-d."
	$(PYTHON) $(JAVAFLAGS) Calc

clean:
	rm -f *.py Calc.py Calc.html Calc.xml Calc.gv
