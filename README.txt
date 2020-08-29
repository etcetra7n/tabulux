This package is for some tablular operation and for making making tabular data

A table object can be made and printed

syntax:

    import ConsoleTabulator
    table_obj = table(  
        {
        'Head-A':['Content-A1','Content-A2',],
        'Head-B':['Content-B1','Content-B2',],
        }   
    )

Result when printed using 'print' method:
    _______________________
   |  Head-A   |  Head-B   |
   |-----------+-----------|
   |Content-A1 |Content-B1 |
   |Content-A2 |Content-B2 |
    ───────────────────────

There are also many other methods to get the information about table, like row(returns the number of row), row_length(returs the row length) etc. 
all of these are mentioned in the PyPI page of this package.

This needs a lot of development, and this project is hosted on github for developmental purpose, 
in which anyone can contribute, smallest of which are appreciated
