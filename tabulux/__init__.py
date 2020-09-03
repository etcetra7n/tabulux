# -*- encoding: UTF-8 -*-
# -*- Indentation: 4 Spaces -*-
'''
A package for tablular operation and for making making tabular data
This needs a lot of development, and this project is hosted on github for developmental purpose, 
in which anyone can contribute, smallest of which are appreciated
Check out the source code at https://github.com/John-pix/Tabulator-Python
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
        table_obj = table(
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
    def column_length(self):
        '''
        Syntax:
            table_obj.column_length()

        where:
            table_obj = a table object

        returns integer representing the number of columns in 'table_obj'
        '''
        return self.column_len
    def row_length(self):
        '''
        Syntax:
            table_obj.row_length()

         where:
            table_obj = a table object

        returns integer representing the number of rows in 'table_obj'
        '''
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
    def head(self, column):
        '''
        Syntax:
            table_obj.head(column_number):
            where:
               table_obj      =  A table object
               column_number  =  the column number, whose heading you want, as an integer

        returns the heading of the specified 'column_number' of 'table_obj' as a string.
        '''

        heads = self.heads()
 
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

    def cell(self, row, column):
        '''
        Syntax:
            table1.cell(row, column)
            where,
            table1 = table object
            row    = integer representing the row number (starting from 0), or, 
                     the heading of the column as string
            column = integer representing the column number (starting from 0)
        returns the Cell Content of the specified location as String. 
        If the cell is not defined in the table or the rows or column given is out of bounds, a CellOutOfBoundsException is raised
        '''
        table = self._get_layout()
        if row >= self.row_len:
            raise CellOutOfBoundsException(row, column)
        elif column >= self.column_len:
            raise CellOutOfBoundsException(row,column)

        if type(row) is str:
            return self.layout[row][column]
        elif type(column) is int:
            table = self._get_layout()

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

    def change_content(self, row, column, new_content):
        '''
        Use change_content() method to change the heading of a cell
        Syntax:
            table_obj.change_content(row_ID, column_ID, new_content)
        where, 
            table_obj   =  a table object
            row_ID      =  an integer representing the column number(starts from 0)
            column_ID   =  an integer representing the column number(starts from 0), or the heading of the column as a string
            new_content =  a string containg the new content

        changes the heading of the specified column to 'new_head'
        Aditionaly, it also returns the old content of the cell
        '''

        if row >= self.row_len:
            raise CellOutOfBoundsException(row, column)
        if column >= self.column_len:
            raise CellOutOfBoundsException(row, column)
        
        if type(column) is str:
            old_content = self.layout[column][row]
            self.layout[column][row] = new_content
            return old_content
        elif type(column) is int:
            heads = self.heads()
            old_content = self.layout[heads[column]][row]
            self.layout[heads[column]][row] = new_content
            return old_content
        else:
            raise TypeError

    def add(self, x1, y1, x2, y2):
        '''
        The add method can be used to add two cells, if the cells are integers or can be converted to integers,
        Syntax:
            table_obj.add(row1, column1, row2, column2)
        where:
            table_obj  = a table object
            row1       = cell row of the first cell as an integer
            column1    = cell column of the first cell as an integer, or the heading of the column as a string
            row2       = cell row of the second cell as an integer
            column2    = cell column of the second cell as an integer, or the heading of the column as a string

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
            return ((int(self.layout[y1][x1])) + (int(self.layout[y2][x2])))
        except:
            raise TypeError

    def add_all(self, x1, x2, y1, y2):
        '''
        The add_all() method can be used to add all the cells from a cell to another cell, if all their values are integers
        Syntax:
            table_obj.add_all(from_row, from_column, to_row, to_column)

        where:
            table_obj   = a table object
            from_row    = row number of the first cell
            from_column = column number of the first cell
            to_row      = row number of the last cell
            to_column   = column number of the last cell

        returns the sum of all the content of cells between, and including the specified cells
        If any cell content cannot be converted to an integer, 'TypeError' is raised
        '''
        try:
            if type(y1)is str:
                y1 = self.heads().index(y1)
            if type(y2) is str:
                y2 = (self.heads().index(y2))+1
        except:
            raise CellOutOfBoundsException(y1, y2)

        x2 += 1
        total_sum = 0
        heads = self.heads()
        table = self._get_layout()
        try:
            for head in heads[y1:y2]:
                for row in table[head][x1:x2]:
                    total_sum += (int(row))
        except:
            raise 

        return total_sum








        
