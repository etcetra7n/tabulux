import tabulux
import pyperclip

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
        print("        used column number for cell = 1     ")
        print("        used row number for cell    = 1     ")
        print("        copy                        = True\n")
        print("        output: ",end='')
        print(test_case_2.cell(1,1,copy=True))
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

     # <chage method>
        print("running 'chage' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used new_content = 'new content")
        print("        used row         = 3")
        print("        used column      = 2")
        print("        new table = ")
        test_case_1.change(3,2,'new content')
        test_case_1.display()
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        paste            = True")
        print("        used row         = 1")
        print("        used column      = 0")
        pyperclip.copy("new")
        print("        content in clipboard = 'new'")
        print("        new table: ")
        test_case_2.change(1,0,'new content',paste=True)
        test_case_2.display()
       # </test case 2>
     # </chage_content method>

        print('\n--------------------------------------------\n')

     # <add method>
        print("running 'add' method:")
       # <test case 1>
        print("    test case 1 not possible as there are no integer cells")

       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        first cell addres   = row- 0, column- 1")
        print("        second cell address = row- 1, column- 1")
        print("        return value= ",end='')
        print(test_case_2.add(0,1,1,1))
       # </test case 2>
     # </add method>

        print('\n--------------------------------------------\n')

     # <add_all method>
        print("running 'add_all' method:")
       # <test case 1>
        print("    test case 1 not possible as there are no integer cells")

       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        first cell addres   = row- 0, column- 1")
        print("        second cell address = row- 1, column- 1")
        print("        return value= ",end='')
        print(test_case_2.add_all(0,1,1,1))
       # </test case 2>
     # </add_all method>

        print('\n--------------------------------------------\n')

     # <html method>
        print("running 'html' method:")
       # <test case 1>
        print("    test case 1:")
        print("        used method call attributes: display=True, copy=True, indent=4")
        print("        Output: ")
        test_case_1.html(display=True, copy=True, indent=4)
        print("        printing clipboard to ensure that copy-paste feature is working")
        print(pyperclip.paste())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        used method call attributes: display=False, copy=False, indent=2")
        print("        return value: ")
        print(test_case_2.html(display=False, copy=False, indent=2))
       # </test case 2>
     # </html method>

        print('\n--------------------------------------------\n')


if __name__ == "__main__":
    unittest.test()
