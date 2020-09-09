tabulux
=======

This package is for performing tablular operations and for making making tabular data.

[Download this documetation](https://drive.google.com/uc?export=download&id=1rnqRuhxC5cBvK7LbjSIZ4LqcNUxlRAeu)
This module requires 'pyperclip', for using the copy-paste feature
You can still use this module without pyperclip, but it is strongly recommended to install pyperclip
[visit PyPI-Pyperclip](https://pypi.org/project/pyperclip/)

Import using:

    import tabulux

Create a table object using the *`table`* class

syntax:

    table_obj = tabulux.table(   
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

+ **column_length()** - returns the column length 
+ **row_length()** - returns the row length
+ **heads()** - returns the all the headings of the table as a list of strings
+ **head()** - returns the heading of the specified column as a string
+ **cell()** - returns the content of a specified cell
+ **display()** - prints the data in the table in a tabulated form
+ **row()** - returns a specific row from the table as a list of string
+ **column()** - returns a specific column from the table as a list of string
+ **change()** - use this to change the content of a cell after the creation of the table
+ **add()** returns the sum of two cell content
+ **add_all()** - returns the sum of a series of cells
+ **html()** - returns the html code of the table

column_length()
----------------

Use this method when you need the column length of the table

Syntax:

    table_obj.column_length(copy={True/False})

where:
  `table_obj` = a table object
  `copy`      = This boolean attribute copies the result as text to your clipboard (False by default)

returns integer representing the number of column in `table_obj`

row_length()
------------

Use this method when you need the number of rows of the table

Syntax:

    table_obj.row_length(copy={True/False})

where:
  `table_obj` = a table object
  `copy`      = This boolean attribute copies the result as text to your clipboard (False by default)

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

    table_obj.head(column_number, copy={True/False})

where:
  `table_obj`      =  A table object
  `column_number`  =  An integer representing the column number, whose heading you want
  `copy`           =  A boolean- if True, copies the heading to your clipboard(False by default)

returns the heading of the specified column of the table as a string.

cell()
------

Syntax:

Use this method when you need the cell content of a cell

    table_obj.cell(row_ID, column_ID, copy={True/False})

where,
  `table_obj` = table object
  `row`       = integer representing the row number (starting from 0), or, the heading of the column as a string
  `column`    = integer representing the column number (starting from 0)
  `copy`      = a boolean, if true- copies the result to your clipboard(False,by default)

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

change()
--------

Use change() method to change the content of a cell

Syntax:

	table_obj.change(row_ID, column_ID, new_content)
	
where, 
  `table_obj`   =  a table object
  `row_ID`      =  an integer representing the column number(starts from 0)
  `column_ID`   =  an integer representing the column number(starts from 0), or the heading of the column as a string
  `new_content` =  a string containg the new content
  
changes the of the specified column to the content in `new_content`

you can also set a cell content to whatever text copied to your clipboard, by setting the 'paste' argument to True

Syntax:

	table_obj.change(row_ID, column_ID, new_content, paste=True)
	
the 'new_content' is ignored if paste is set to True, so you can leave the new content as `""`
This cange the cell in the specified location to the text in the clipboard.

Aditionaly, this method also returns the old content of the specified cell

add()
------

The add method can be used to add two cells, if the cells are integers or can be converted to integers,
Syntax:

	table_obj.add(row1, column1, row2, column2, copy={True/False})
	
where:
  `table_obj`    = a table object
  `row1`       = cell row of the first cell as an integer
  `column1`    = cell column of the first cell as an integer, or the heading of the column as a string
  `row2 `      = cell row of the second cell as an integer
  `column2`    = cell column of the second cell as an integer, or the heading of the column as a string
  `copy`       = If this boolean attribute is set to True, the result will be copied to your clipboard(False by default)

returns the sum of the two cells

add_all()
---------

The add_all() method can be used to add all the cells from a cell to another cell, if all their values are integers

Syntax:

	table_obj.add_all(from_row, from_column, to_row, to_column, copy={True/False})

where:
  `table_obj`   = a table object
  `from_row`    = row number of the first cell
  `from_column` = column number of the first cell
  `to_row`      = row number of the last cell
  `to_column`   = column number of the last cell
  `copy`        = a boolean, if True- the result will be copied to your clipboard (False by default)

returns the sum of all the content of cells between the specified cells.

If any cell content cannot be converted to an integer, 'TypeError' is raised

NOTE: The the ending cell address(to_row, to_column) is not included in the sum.

html()
------

The 'html()' method is used to get the html snippet of a table.
Syntax:

	table_obj.html(display={True/False}, copy={True/False}, indent={int})

where:
  `table_obj` = a table object
  `display`   = if set to True, this boolean attribute will display the html snippet in the console\terminal, (False by default)
  `copy`      = this boolean attribute, if set to True, copies the html snippet to you clipboard, and can by pasted to your html file(False by default)
  `indent`    = indentation spaces that sould be applied, as integer (4 by default)

returns the html snippet of the table as a string, from and including <table> to <\/table>


[Take me to this project's github repository page](https://github.com/John-pix/Tabulux-Python)


