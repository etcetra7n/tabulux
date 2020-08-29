import tabulux

class unittest:
    def create_test_classes():
        tast_case_1 = table(
            {
                'head-A' :['Content-A1','ContentA2'   ],
                'Head-B' :['Content-B1'  ,'Content-B2']
            }  
        )
        tast_case_2 = table(
            {
                'Name':['John','Peter'],
                'Age' :['15'  ,'20'   ]
            }  
        )

        return [test_case_1, test_case_2]
    
    def test():
     # <creating and printing test cases>
        test_class = create_test_class()
        print("2 table object created")
        print("test case 1:\n    {\n    'head-A' :['Content-A1','ContentA2'   ],\n    'Head-B' :['Content-B1'  ,'Content-B2']\n}")
        print("test case 2:\n    {\n    'Name':['John','Peter','Alex'],\n    'Age' :['15'  ,'20'   ,'35'  ]\n} ")
     # </test case created and printed>

        print('\n--------------------------------------------\n')

     # <column length method>
        print("running 'column_length' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = "+ test_case_1.column_length())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output = "+ test_case_2.column_length())
       # </test case 2>
     # </column length method>

        print('\n--------------------------------------------\n')

     # <row length method>
        print("running 'row length' method:")
       # <test case 1>
        print("    test case 1:")
        print("        output = "+ test_case_1.row_length())
       # </test case 1>
       # <test case 2>
        print("    test case 2:")
        print("        output = "+ test_case_2.row_length())
       # </test case 2>
     # </row length method>

        print('\n--------------------------------------------\n')

     # <>




if __name__ == "__main__":
    unittest.test()
