# -*- encoding: UTF-8 -*- 
# -*- Indentation: 4 Spaces -*- 

import os
import sys
try:
    import pyperclip
except ImportError:
    pass

'''
A package for tablular operation and for making making tabular data
This project is hosted on github for developmental purpose, 
in which anyone can contribute, smallest of which are appreciated
Check out the source code at https://github.com/John-pix/Tabulator-Python
Download the documentation at https://drive.google.com/uc?export=download&id=1PBXYawIaA7vfTOCT6JjsfPOhitKGjmHZ

Requirments:
    'pyperclip' module for copy-paste feature, you can still use without it but you cant use the copy-past features
    download pyperclip from https://pypi.org/project/pyperclip/
'''
class CellOutOfBoundsException(Exception):

    def __init__(self, row, column, message="Cell Not Found"):
        self.row = row
        self.column = column
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Row = {self.row}; Column = {self.column}'

class table:
    '''
    A table object is created using the table class
        Syntax : 
        table_obj = tabulux.table(
            {
                'Head1':['content-A1',content-A2',],
                'Head2':['content-B1',content-B2',],
            }
        ) 
    Now the table object is stored in the variable 'table_obj'
    Note: every column should contain same number of elements'
    '''
    def __init__(self, layout):
        
        self.layout = layout
        self.row_len = len(layout[list(layout)[0]])
        self.column_len = len(layout)
        
    def column_length(self, copy=False):
        '''
        Use this method when you need the column length of the table

        Syntax:

            table_obj.column_length(copy={True/False})

        where:
          `table_obj` = a table object
          `copy`      = This attribute copies the result as text to your clipboard (False by default)

        returns integer representing the number of column in `table_obj`
        '''
        if copy:
            pyperclip.copy(self.column_len)
        return self.column_len
    def row_length(self, copy=False):
        '''
        Use this method when you need the number of rows of the table

        Syntax:

            table_obj.row_length(copy={True/False})

        where:
          `table_obj` = a table object
          `copy`      = This attribute copies the result as text to your clipboard (False by default)

        returns integer representing the number of rows in `table_obj`
        '''
        if copy:
            pyperclip.copy(self.row_len)
        return self.row_len

    def _get_layout(self):
        return self.layout

    def heads(self):
        '''
        Syntax :
            table_obj.heads()
           
            where:
               table_obj = a table object

        returns a 'list' of string representing the each heading of 'table_obj'
        '''
        table = self._get_layout()
        heads = []
        for head in table:
            heads.append(head)
        return heads
    def head(self, column, copy=False):
        '''
        Use head() when you want a heading of a specific column from the table

        Syntax:

            table_obj.head(column_number, copy={True/False})

        where:
          `table_obj`      =  A table object
          `column_number`  =  An integer representing the column number, whose heading you want
          `copy`           =  A boolean- if True, copies the heading to your clipboard(False by default)

        returns the heading of the specified column of the table as a string.
        '''

        heads = self.heads()

        if copy:
            pyperclip.copy(heads[column])
 
        return heads[column]


    def display(self):
        '''
        Syntax :
            table1.display()
        Output:
            prints data in 'table1' in tabular form
            Here is how the table would be printed:
                 |Head-A |  Head-B | 
                 -------------------
                 |content-A1 | Content-B1 | 
                 |content-A2 | Content-B2 | 
        
        '''
        table = self._get_layout()
        heads = self.heads()

        print('|',end = '')
        for head in heads:    #for printing the headings
            print(head,end=' | ')

        print("\n-----------",end='')

        for row in range(self.row_len):
            print('\n',end='|')
            for column in heads:
                print(table[column][row], end = ' | ')
        print()
        return

    def cell(self, row, column, copy= False):
        '''
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
        '''
        
        table = self._get_layout()
        
        if row >= self.row_len:
            raise CellOutOfBoundsException(row, column)
        elif column >= self.column_len:
            raise CellOutOfBoundsException(row,column)

        if type(column) is str:
            if copy == True:
                pyperclip.copy(table[row][column])
            return table[row][column]
        elif type(column) is int:
            if copy == True:
                pyperclip.copy(table[self.heads()[row]][column])
            return table[self.heads()[row]][column]

    def row(self, row_number):
        '''
        You can use the row() method to get all the row elements in the table as a list
        Syntax:
            table_obj.row(row_number)
            where:
                table_obj   = a table object
                row_number  = an integer representing the row number (starts from 0)
        For example, the row_number of 2 would return a list containing the values from second row from all columns
        A 'CellOutOfBoundsException' is raised if the specified row exceeds the number of rows in the table
        '''
        if row_number >= self.row_len:
            raise CellOutOfBoundsException(row_number, 'X')

        table = self._get_layout()
        extracted_row = []
            
        heads = self.heads()
        for head in heads:
            extracted_row.append(table[head][row_number])
            
        return extracted_row
        
    def column(self, column_number):
        '''
        You could use the getColumn function to get list containing all the whole column, under a specified row
        Syntax:
            table_obj.column(column_number)
            where:
                table_obj      = a table object
                column_number  = an integer which represents column number, whose cells must be returned(starting from 0) or,
                                 the heading of the column,(as string), whose values must be returned
            '''

        if column_number >= self.column_len:
            raise CellOutOfBoundsException('X', column_number)

        if type(column_number) is str:
            return self.layout[column_number]
        elif type(column_number) is int:
            return self.layout[self.head(column_number)]

    def change(self, row, column, new_content, paste=False):
        '''
        Use change() method to change the content of a cell

        Syntax:

            table_obj.change(row_ID, column_ID, new_content)
            
        where, 
          table_obj   =  a table object
          row_ID      =  an integer representing the column number(starts from 0)
          column_ID   =  an integer representing the column number(starts from 0), or the heading of the column as a string
          new_content =  a string containg the new content
          
        changes the of the specified column to the content in `new_content`

        you can also set a cell content to whatever text copied to your clipboard, by setting the 'paste' argument to True

        Syntax:

            table_obj.change(row_ID, column_ID, new_content, paste=True)
            
        the 'new_content' is ignored if paste is set to True, so you can leave the new content as `""`
        This cange the cell in the specified location to the text in the clipboard.

        Aditionaly, this method also returns the old content of the specified cell
        '''

        if row >= self.row_len:
            raise CellOutOfBoundsException(row, column)
        if column >= self.column_len:
            raise CellOutOfBoundsException(row, column)
        
        if type(column) is str:
            old_content = self.layout[column][row]
            if paste == True:
                self.layout[column][row] = pyperclip.paste()
            else:
                self.layout[column][row] = new_content
            return old_content
        elif type(column) is int:
            heads = self.heads()
            old_content = self.layout[heads[column]][row]
            if paste == True:
                self.layout[heads[column]][row] = pyperclip.paste()
            else:
                self.layout[heads[column]][row] = new_content
            return old_content
        else:
            raise TypeError

    def add(self, x1, y1, x2, y2, copy=False):
        '''
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

        '''
        try:
            if type(y1)is int:
                y1 = self.head(y1)
            if type(y2) is int:
                y2 = self.head(y2)
        except:
            raise CellOutOfBoundsException(y1, y2)
        try:
            if copy:
                pyperclip.copy(str(int(self.layout[y1][x1])) + (int(self.layout[y2][x2])))
            return ((int(self.layout[y1][x1])) + (int(self.layout[y2][x2])))
        except:
            raise TypeError

    def add_all(self, x1, x2, y1, y2, copy=False):
        '''
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
        '''
        try:
            if type(x2)is str:
                y1 = self.heads().index(y1)
            if type(y2) is str:
                y2 = (self.heads().index(y2)) 
        except:
            raise CellOutOfBoundsException(y1, y2)

        total_sum = 0
        heads = self.heads()
        table = self._get_layout()
        try:
            for head in heads[x2:y2]:
                for row in table[head][x1:y1]:
                    total_sum += (int(row))
        except:
            raise

        if copy:
            pyperclip.copy(str(total_sum))

        return total_sum

    def html(self, display=False, copy=False, indent=4):
        '''
        The 'html()' method os used to get the html snippet of a table.
        Syntax:
            table_obj.html(display={True/False}, copy={True/False}, indent={int})

        where:
            table_obj = a table object
            display   = this attribute will display the html snippet in the console\terminal, if set to True(False by default)
            copy      = this attribute, if set to True, copies the html snippet to you clipboard, and can by pasted to your html file(False by default)
            indent    = indentation spaces that sould be applied (4 by default)

        returns the html snippet of the table as a string from, and including <table> to </table>
        '''
        html = ""
        heads = self.heads()
        table = self._get_layout()
        # The newline charecter for windows is "\r\n", but in linux, it is "\n", so the platform would have to be checked using sys.platform to enable cross-platform functionality
        if sys.platform.startswith('win'):
            html += "<table>\r\n"
            html += " "*(indent) + "<tr>" + "\r\n"
            for head in heads:
                html += " "*(indent*2) + f"<th>{head}</th>" + "\r\n"
            html += " "*(indent) + "</tr>" + "\r\n"

            for row in range(self.row_len):
                html += " "*(indent) + "<tr>" + "\r\n"
                for head in heads:
                    html += " "*(indent*2) + f"<td>{table[head][row]}</td>" + "\r\n"
                html += " "*(indent) + "</tr>" + "\r\n"
                
                
        else: # most other platforms use '\n' as newline
            html += "<table>\n"
            html += " "*(indent) + "<tr>" + "\n"
            for head in heads:
                html += " "*(indent*2) + f"<th>{head}</th>" + "\n"
            html += " "*(indent) + "</tr>" + "\n"

            for row in range(self.row_len):
                html += " "*(indent) + "<tr>" + "\n"
                for head in heads:
                    html += " "*(indent*2) + f"<td>{table[head][row]}</td>" + "\n"
                html += " "*(indent) + "</tr>" + "\n"

        html += "</table>"

        if display:
            print(html)

        if copy:
            pyperclip.copy(html)

        return html
