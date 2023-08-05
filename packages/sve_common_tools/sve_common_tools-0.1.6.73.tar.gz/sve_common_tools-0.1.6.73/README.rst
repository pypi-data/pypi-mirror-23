=========================================
sve_common_tools
=========================================

.. sectnum::

.. contents:: Indice

SSHManager
~~~~~~~~~~~~~~~~~~~~~~~~~

Classe di gestione SSH tramite paramiko
   ::

     import sve_common_tools as svect

     cp = '.*(\@host1> )$'
     re1 = '.*(a\.b\.c\.d).*[>] $'
     ssh_manager = svect.SSHManager(username='xxxx', password='yyyy', host='a.b.c.d', timeout=10)
     command_output = ssh_manager.connect(re_string=cp, timeout=10)
     command_output = ssh_manager.send_command('ls -lrt', re_string=re1)
     command_output = ssh_manager.send_command('date', re_string=re1)

     Note: se la RegExp non ritorna il buffer, scatta il timeout ed è generata una Exception


FileUtils
~~~~~~~~~~~~~~~~~~~~~~~~~

Classe di gestione operazioni su blocchi di testo
 - **costanti**

   ::

     raise_msg_header_not_found = 'HEADER_NOT_FOUND'

 - **def strip_rows(command_output)**

   ::

     import sve_common_tools as svect

     command_output = "\nROW1 ROW1    \n\nROW2 ROW2\n\n"
     result = "\nROW1 ROW1\n\nROW2 ROW2\n\n"
     multiline_header = svect.FileUtils.strip_rows(command_output=command_output)
     self.assertTrue(multiline_header == result)

 - **def remove_skip_rows(multiline_str, skip_str_array, skip_empty_lines)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\n\n-----------\nROW2 ROW2\n=======\n"
     skip_str_array=["---", "===="]
     result = "ROW1 ROW1\nROW2 ROW2\n"
     multiline_header = svect.FileUtils.remove_skip_rows(multiline_str=multiline_str,
                                                         skip_str_array=skip_str_array,
                                                         skip_empty_lines=True)
     self.assertTrue(multiline_header == result)

 - **def check_header_string_array(multiline_str, header_str_array)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1    H1   \nDATA"
     header_str_array = [['BASE', 'HEADER1 H1', 'STR'],
                         ['VAR1', '^(HEADER1).*(H1).*$', 'REGEXP']]
     found_header, label_header, string_header = svect.FileUtils.check_header_string_array(
               multiline_str=multiline_str,
               header_str_array=header_str_array)
     self.assertTrue(found_header == True)
     self.assertTrue(label_header == "VAR1")
     self.assertTrue(string_header == "HEADER1    H1   ")

 - **def remove_before_header_string(multiline_str, header_str)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1 H1\nDATA\n"
     header_str = "HEADER1 H1"
     result = "DATA\n"
     outr = svect.FileUtils.remove_before_header_string(multiline_str=multiline_str,
                                                        header_str=header_str)
     self.assertTrue(outr == result)

 - **def remove_after_footer_string(multiline_str, footer_str)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1 H1\nDATA\nFOOTER F1\nDATA2\n"
     footer_str = "FOO"
     result = "ROW1 ROW1\nHEADER1 H1\nDATA\n"
     outr = svect.FileUtils.remove_after_footer_string(multiline_str=multiline_str,
                                                       footer_str=footer_str)
     self.assertTrue(outr == result)

 - **def extract_block(multiline_str, starting_row, ending_row, add_ending_row)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1 H1\nDATA\nDATA3\nFOOTER F1\nDATA2\n"
     starting_row = "HEADER1 H1"
     footer_str = "FOOTER F1"
     result = "HEADER1 H1\nDATA\nDATA3\n"
     outr = svect.FileUtils.extract_block(multiline_str=multiline_str,
                                          starting_row=starting_row,
                                          ending_row=footer_str,
                                          add_ending_row=False)
     self.assertTrue(outr == result)

 - **def add_char_to_every_row_if_not_exist(multiline_str, character)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\n\nROW2 ROW2\n\n"
     result = "ROW1 ROW1:\n:\nROW2 ROW2:\n:\n"
     outr = svect.FileUtils.add_char_to_every_row_if_not_exist(multiline_str=multiline_str,
                                                               character=":")
     self.assertTrue(outr == result)

 - **def parse_exact_table(multiline_str, header_column_position)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1 H1\nDATA\nFOOTER F1\nDATA2\n"
     multiline_str = "H1   H2   | H3\nROW1 ROW1 | ROW1\nROW2 ROW2 | ROW2\nROW3 ROW3 | ROW3\n"
     h = "H1   H2   | H3"
     col_init = [[h.find('H1'), None],
                 [h.find('H2'), h.find('|')],
                 [h.find('H3'), None]]
     result = [['H1', 'H2', 'H3'],
               ['ROW1', 'ROW1', 'ROW1'],
               ['ROW2', 'ROW2', 'ROW2'],
               ['ROW3', 'ROW3', 'ROW3']]
     outr = svect.FileUtils.parse_exact_table(multiline_str=multiline_str,
                                              header_column_position=col_init)
     self.assertTrue(outr == result)

     Nota: se la riga e' interamente vuota non e' inserita in matrice

 - **def create_htmltable(command_output_array_table, first_row_html_header)**
   ::

     import sve_common_tools as svect

     multiline_str = "ROW1 ROW1\nHEADER1 H1\nDATA\nFOOTER F1\nDATA2\n"
     command_output_array_table = [['H1', 'H2', 'H3'],
                                   ['ROW1', 'ROW1', 'ROW1'],
                                    ['ROW2', 'ROW2', 'ROW2']]
        result = """<table style="color:black" border="1" cellpadding="5">
                 <thead>
                 <th>H1</th>
                 <th>H2</th>
                 <th>H3</th>
                 </thead>
                 <tbody>
                 <tr>
                 <td>ROW1</td>
                 <td>ROW1</td>
                 <td>ROW1</td>
                 </tr>
                 <tr>
                 <td>ROW2</td>
                 <td>ROW2</td>
                 <td>ROW2</td>
                 </tr>
                 </tbody>
                 </table>
                 """
        outr = svect.FileUtils.create_htmltable(command_output_array_table=command_output_array_table,
                                                first_row_html_header=True)
        self.assertTrue(outr == result)

TestingHelper
~~~~~~~~~~~~~~~~~~~~~~~~~

Classe di utility per unit-test

 - **get_input_and_output(self, in_file_name, out_file_name)**
   ::

     import sve_common_tools as svect

     th = svect.TestingHelper(basedir=os.path.dirname(os.path.realpath(__file__)))
     in_text, out_text = self.th.get_input_and_output('FILE_IN.txt', 'FILE_OUT.txt')

