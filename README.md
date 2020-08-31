tabulux
=======

This package is for performing tablular operations and for making making tabular data.

Import using:

    import tabulux

Create a table object using the *`table`* class

syntax:

    table_obj = table(   
        {   
        'Head-A':['Content-A1','Content-A2',],   
        'Head-B':['Content-B1','Content-B2',],   
        }   
    )   

Now the table object have been saved to 'table_obj'

A Virtul table of the above object can be imagined like this:

    | Head-A      | Head-B      |
    |-------------+-------------|
    | Content-A1  | Content-B1  |
    | Content-A2  | Content-B2  |

Available functions and methods:
===============================

+ column_length() - returns the column length 
+ row_length() - returns the row length
+ column(column_ID) - returns all the elements in the `column_ID` as a list.
+ row(row_ID) - returns all elements of the `row_ID`
+ heads() - returns the all the headings of the table as a list of strings
+ head(column_ID) - returns the heading of the specified column as a string
+ cell(row_ID, column_ID) - returns the content of the cell at the specified location
+ display() - prints the data in the table in a tabulated form

column_length()
----------------

Use this method when you need the column length of the table

Syntax:

    table_obj.column_length()

where:
  `table_obj` = a table object

returns integer representing the number of column in `table_obj`

row_length()
------------

Use this method when you need the number of rows of the table

Syntax:

    table_obj.row_length()

where:
  `table_obj` = a table object

returns integer representing the number of rows in `table_obj`

column()
-------

You could use the column() method to get a list containing all the elements in the specified column as a list

Syntax:

    table_obj.column(column_number)

where:
  `table_obj`      = a table object
  `column_number`  = an integer which represents column number (starting from 0) or, the heading of the column (as a string)

returns all the elements from the specified column as list of strings. The column headings are not returned

A `CellOutOfBoundsException` is raised if the specified column exceeds the number of columns in the table

row()
------

You can use the row() method to get all the elements in a specified row in the table as a list

Syntax:

    table_obj.row(row_number)

where:
  `table_obj`      = a table object
  `row_number`     = an integer representing the row number (starts from 0)

returns all the elements from the specified row as list of strings.

A `CellOutOfBoundsException` is raised if the specified row exceeds the number of rows in the table

heads()
-------

Use heads() when you want all the headings of the table

Syntax :

    table_obj.heads()
 
where:
  `table_obj` = a table object

returns a list of string representing the each heading of the table

head()
------

Use head() when you want a heading of a specific column from the table

Syntax:

    table_obj.head(column_number):

where:
  `table_obj`      =  A table object
  `column_number`  =  An integer representing the column number, whose heading you want

returns the heading of the specified column of the table as a string.

cell()
------

Syntax:

Use this method when you need the cell content of a cell

    table_obj.cell(row_ID, column_ID)

where,
  `table_obj` = table object
  `row`       = integer representing the row number (starting from 0), or, the heading of the column as a string
  `column`    = integer representing the column number (starting from 0)

returns the Cell Content of the specified location as String. 

If the cell is not defined in the table or the rows or column given is out of bounds, a `CellOutOfBoundsException` is raised

display()
---------

Use this method when you need to print the table in the console

Syntax :

    table_obj.display()

where:
  `table_obj` = a table object

Output:
  prints data in `table_obj` in a tabular form
  Here is how the table would be printed:

    |Head-A |  Head-B | 
    -------------------
    |content-A1 | Content-B1 | 
    |content-A2 | Content-B2 | 

This method does not return anything


This needs a lot of development, and this project is hosted on github for developmental purpose, 
in which anyone can contribute, smallest of which are appreciated. 
[Take me to this project's github repository page](https://github.com/John-pix/Tabulux-Python)
