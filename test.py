import tabulux

class unittest:
    def create_test_cases():
        case_1 = tabulux.table(
            {
            'head-A':['Content-A1','Content-A2','Content-A3','Content-A4'],
            'Head-B':['Content-B1','Content-B2','Content-B3','Content-B4'],
            'Head-C':['Content-C1','Content-C2','Content-C3','Content-C4']
            }
        )
        case_2 = tabulux.table(
            {
            'Name':['John','Peter'],
            'Age' :['15'  ,'20'   ],
            }  
        )

        return [case_1, case_2]
    
    def test():
     # <creating and printing test cases>
        test_cases = unittest.create_test_cases()
        test_case_1 = test_cases[0]
        test_case_2 = test_cases[1]
        print("2 table object created")
        print("test case 1:\n    {\n        'head-A' :['Content-A1', 'ContentA2', 'ContentA3', 'ContentA4' ],\n        'Head-B' :['Content-B1'  ,'Content-B2', 'Content-B3', 'Content-B4' ],\n        'Head-C':['Content-C1', 'Content-C2', 'Content-C3', 'Content-C4' ]\n    }")
        print("test case 2:\n    {\n        'Name':['John','Peter'],\n        'Age' :['15'  ,'20'   ]\n    } ")
     # </test case created and printed>

        print('\n--------------------------------------------\n')

     # <column_length method>
        print("running 'column_length' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = ", end='')
        print(test_case_1.column_length())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output = ",end='')
        print(test_case_2.column_length())
       # </test case 2>
     # </column_length method>

        print('\n--------------------------------------------\n')

     # <row_length method>
        print("running 'row_length' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = ",end='')
        print(test_case_1.row_length())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output = ",end='')
        print(test_case_2.row_length())
       # </test case 2>
     # </row_length method>

        print('\n--------------------------------------------\n')

     # <_get_layout method>
        print("running '_get_layout' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = ",end='')
        print(test_case_1._get_layout())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output: ",end = '')
        print(test_case_2._get_layout())
       # </test case 2>
     # </_get_layout method>
     
        print('\n--------------------------------------------\n')

     # <heads method>
        print("running 'heads' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = ",end='')
        print(test_case_1.heads())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output: ",end='')
        print(test_case_2.heads())
       # </test case 2>
     # </heads method>

        print('\n--------------------------------------------\n')

     # <head method>
        print("running 'head' method:")
        print("used column number for heads = 1")
       # <test case 1>
        print("    test case 1:")
        print("        output = ",end='')
        print(test_case_1.head(1))
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output: ",end='')
        print(test_case_2.head(1))
       # </test case 2>
     # </head method>

        print('\n--------------------------------------------\n')

     # <display method>
        print("running 'display' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output: ")
        test_case_1.display()
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output: ")
        test_case_2.display()
       # </test case 2>
     # </display method>

        print('\n--------------------------------------------\n')

     # <cell method>
        print("running 'cell' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used column number for cell = 1")
        print("        used row number for cell = 2\n")
        print("        output = ",end='')
        print(test_case_1.cell(2,1))
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        used column number for cell = 1")
        print("        used row number for cell = 1\n")
        print("        output: ",end='')
        print(test_case_2.cell(1,1))
       # </test case 2>
     # </cell method>

        print('\n--------------------------------------------\n')

     # <row method>
        print("running 'row' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used row number = 3\n")
        print("        output = ",end='')
        print(test_case_1.row(3))
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        used row number = 1\n")
        print("        output: ",end='')
        print(test_case_2.row(1))
       # </test case 2>
     # </row method>

        print('\n--------------------------------------------\n')

     # <column method>
        print("running 'column' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used column number = 0")
        print("        output = ",end='')
        print(test_case_1.column(0))
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        used column number = 0")
        print("        output: ",end='')
        print(test_case_2.column(0))
       # </test case 2>
     # </column method>

        print('\n--------------------------------------------\n')

     # <chage_content method>
        print("running 'column' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used new_content = 'new content")
        print("        used row         = 3")
        print("        used column      = 2")
        print("        new table = ",end='')
        test_case_1.change_content(3,2,'new content')
        print(test_case_1.display())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        used new_content = 'new content'")
        print("        used row         = 1")
        print("        used column      = 0")
        print("        new table: ",end='')
        test_case_2.change_content(1,0,'new content')
        test_case_2.diplay()
       # </test case 2>
     # </chage_content method>

        print('\n--------------------------------------------\n')

     # <>


if __name__ == "__main__":
    unittest.test()
