# -*- coding-UTF-8 -*-
# -*- Indentation Spaces: 4 -*-
'''
A package for printing data in tabular form

This needs a lot of development, and this project is hosted on github for developmental purpose, 
in which anyone can contribute, smallest of which are appreciated

Check out the source code at https://github.com/John-pix/Tabulator-Python
'''
class CellOutOfBoundsException(Exception):

    def __init__(self, row, column, message="Cell Location Not Found"):
        self.row = row
        self.column = column
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Row = {self.row}; Column = {self.column}'

class create:
    '''
    A table object is created using the create method
        Syntax : 
        tableA = create(
            {
                'Head1':['content-A1',content-A2',],
                'Head2':['content-B1',content-B2',],
            }
        ) 

        Now the table object is stored in the variable 'tableA'
    '''
    def __init__(layout):
        
        self.layout = layout
        self.row = len(layout)
        self.column = len(layout[0])
    def getColumnLength(self):
        '''
        Syntax:
            getColumnLength(self)
        returns integer representing the number of column
        '''
        return self.column
    def getRowLength(self):
        '''
        Syntax:
            getRowLength(self)
        returns integer representing the number of row
        '''
        return self.row
    def _get_layout(self):
        return self.layout

    def printTable(self):
        '''
        Syntax : 
        tableA = create(
            {
                'Head1':['content-A1',content-A2',],
                'Head2':['content-B1',content-B2',],
            }
        ) 
        printTable(tableA)
        Output:
               Head1    |  Head2
             -----------------------
             content-A1 | Content-B1
             content-A2 | Content-B2
        
        '''
        table = _get_layout(self)
        titles = []
        for title in table:
            titles.append(title)

        print('|',end = '')
        for title in titles:    #for printing the headings
            print(title,end=' | ')

        print("\n-----------",end='')

        for column in range(getRow(self)):
            print()
            for row in titles:
                print(table[row][column], end = ' | ')

    def getHeads(self)
        '''
        Syntax :
            getHeads(self)

        returns a 'list' of string representing the each heading of the table
        '''
        table = _get_layout(self)
        heads = []
        for head in table:
            heads.append(head)
        return heads
    
    def getHead(self, row):
        '''
        Syntax:
            getHeads(Table_obj, row):

        returns a string containing of the heading at the 'row' parameter, where 'row' is an integer value
        '''

        table = _get_layout(self)
        heads = []
        for head in table:
            heads.append(head)
        return heads[row]

    def getCell(self, row, column):
        '''
        Syntax:
            getCell(self, row, column)

            where,
            row    = integer representing the row number (starting from 0), or, 
                     the heading of the table as string

            column = integer representing the column number (starting from 0)

        returns the Cell Content of the specified locationas String. 

        If the cell is not defined in the cell or the rows and column given is out of bounds, a CellOutOfBoundsException is raised
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
            heads = []
            for head in table:
                heads.append(head)

            return table[heads[row]][column]

        def getRow(self, column):
            '''
            You can use the getRow method to get all the row elements as a list

            Syntax:
                getRow(table_obj, columnID)

                where:
                    table_obj = a table object
                    rowID     = an integer representing the column number (starts from 0)

            For example, the columID of 2 would return a list containing the second row from all columns
            A 'CellOutOfBoundsException' is raised if the specified row exceeds the number of rows in the table

            '''
            if column > self.column:
                raise CellOutOfBoundsException('X', column)

            table = _get_layout(self)
            extracted_row = []
            
            heads = getHeads(self)
            for head in heads:
                extracted_row.append(table[head][column])
            
            return extracted_row
        
        def getColumn(self, row):
            '''
            You could use the getColumn function to get list containing all the whole column, under a specified row
            Syntax:
                getColmn(table1, rowID)

                where:
                    table1 = a table object
                    rowID  = an integer which represents row number, whose columns must be returned(starting from 0) or,
                             the heading of the column,(as string), whose values must be returned
            '''

            if row > self.row:
                raise CellOutOfBoundsException(row, 'X')

            if type(row) is str:
                return self.layout[row]
            elif type(row) is int:
                return _get_layout(self)[getHead(self, row)]


