# -*- coding: UTF-8 -*-
# -*- Indentation Spaces: 4 -*-
'''
A package for printing data in tabular form

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
        table1 = table(
            {
                'Head1':['content-A1',content-A2',],
                'Head2':['content-B1',content-B2',],
            }
        ) 

        Now the table object is stored in the variable 'table1'
        Note: every column should contain same number of elements'
    '''
    def __init__(layout):
        
        self.layout = layout
        self.row = len(layout[0])
        self.column = len(layout)
    def column_length(self):
        '''
        Syntax:
            table1.column_length()
        returns integer representing the number of columns in 'table1'
        '''
        return self.column
    def row_length(self):
        '''
        Syntax:
            table1.row_length()
        returns integer representing the number of rows in 'table1'
        '''
        return self.row

    def _get_layout(self):
        return self.layout

    def heads(self):
        Syntax :
            table1.heads()
           
            where:
               table1 = a table object

        returns a 'list' of string representing the each heading of 'table1'
        '''
        table = _get_layout(self)
        heads = []
        for head in table:
            heads.append(head)
        return heads

    def head(self, column):
        '''
        Syntax:
            table1.head(column_number):
            where:
               table1         =  A table object
               column_number  =  an integer

        returns a heading of the specified 'column_number' of 'table1' as a string.
        '''

        table = _get_layout(self)
        heads = heads(self)
 
        return heads[column]


    def print(self):
        '''
        Syntax :
            table1.print()
        Output:
            prints data in 'table1' in tabular form
            Here is how the table would be printed:
                   Head1    |  Head2
                 -----------+-----------
                 content-A1 | Content-B1
                 content-A2 | Content-B2
        
        '''
        table = _get_layout(self)
        heads = heads(self)

        print('|',end = '')
        for head in heads:    #for printing the headings
            print(head,end=' | ')

        print("\n-----------",end='')

        for column in range(row(self)):
            print()
            for row in heads:
                print(table[row][column], end = ' | ')

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
        table = _get_layout(self)
        if row > self.row:
            raise CellOutOfBoundsException(row, column)
        elif column > self.column:
            raise CellOutOfBoundsException(row,column)

        if type(row) is str:
            return self.layout[row][column]
        elif type(column) is int:
            table = _get_layout(self)
            heads = heads(self)

        return table[heads[row]][column]

        def row(self, row_number):
            '''
            You can use the row() method to get all the row elements in the table as a list

            Syntax:
                table1.row(row_number)

                where:
                    table1      = a table object
                    row_number  = an integer representing the row number (starts from 0)

            For example, the row_number of 2 would return a list containing the values from second row from all columns
            A 'CellOutOfBoundsException' is raised if the specified row exceeds the number of rows in the table

            '''
            if row_number > self.row:
                raise CellOutOfBoundsException(row_number, 'X')

            table = _get_layout(self)
            extracted_row = []
            
            heads = heads(self)
            for head in heads:
                extracted_row.append(table[head][row_number])
            
            return extracted_row
        
        def column(self, column_number):
            '''
            You could use the getColumn function to get list containing all the whole column, under a specified row
            Syntax:
                table1.column(column_number)

                where:
                    table1         = a table object
                    column_number  = an integer which represents column number, whose cells must be returned(starting from 0) or,
                                     the heading of the column,(as string), whose values must be returned
            '''

            if column_number > self.column:
                raise CellOutOfBoundsException('X', column_number)

            if type(column_number) is str:
                return self.layout[column_number]
            elif type(column_number) is int:
                return self.layout[head(self, column_number)]


