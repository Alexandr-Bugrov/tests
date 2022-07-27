import unittest
from unittest.mock import patch
from parameterized import parameterized
from main import get_doc_owner_name, check_document_existance, get_all_doc_owners_names, remove_doc_from_shelf, \
    add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, show_document_info
from list_and_dict import test_documents, test_directories




# def revers():
#     global directories_dict
#     directories_dict = test_directories.copy()
#     global documents_list
#     documents_list = test_documents.copy()


class SecretaryProgramTests(unittest.TestCase):

    # def tearDown(self) -> None:
    #     revers()

    def test_check_document_existance(self):
        documents_list = test_documents.copy()
        self.assertEqual(check_document_existance('10006', documents_list), True)
        self.assertEqual(check_document_existance('1234', documents_list), False)

    def test_get_doc_owner_name(self):
        documents_list = test_documents.copy()
        with patch('builtins.input', return_value='10006'):
            self.assertEqual(get_doc_owner_name(documents_list), "Аристарх Павлов")

    def test_get_all_doc_owners_names(self):
        documents_list = test_documents.copy()
        self.assertEqual(get_all_doc_owners_names(documents_list), {"Василий Гупкин", "Геннадий Покемонов",
                                                                    "Аристарх Павлов"
                                                                    }
                         )

    def test_remove_doc_from_shelf(self):
        directories_dict = test_directories.copy()
        remove_doc_from_shelf('11-2', directories_dict)
        self.assertEqual(directories_dict['1'], ['2207 876234', '5455 028765'])

    @parameterized.expand(
        [
            ('1', ('1', False)),
            ('4', ('4', True))
        ]
    )
    def test_add_new_shelf(self, income_, result):
        directories_dict = test_directories.copy()
        self.assertEqual(add_new_shelf(income_, directories_dict), result)

    def test_append_doc_to_shelf(self):
        directories_dict = test_directories.copy()
        result = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': ['1234']
        }
        append_doc_to_shelf('1234', '5', directories_dict)
        self.assertEqual(directories_dict, result)
        print(directories_dict)
        print('test_append_doc_to_shelf')

    @patch('builtins.input')
    def test_get_doc_shelf(self, mock_input):
        directories_dict = test_directories.copy()
        documents_list = test_documents.copy()
        mock_input.return_value = '10006'
        self.assertEqual(get_doc_shelf(directories_dict, documents_list), '2')


    @patch('builtins.input')
    def test_delete_doc(self, mock_input):
        directories_dict = test_directories.copy()
        documents_list = test_documents.copy()
        result1 = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        ]
        result2 = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': [],
            '3': []
        }
        mock_input.return_value = '10006'
        delete_doc(documents_list, directories_dict)
        self.assertEqual(documents_list, result1)
        self.assertEqual(directories_dict, result2)
        print(directories_dict)
        print('test_delete_doc')

    def test_show_document_info(self):
        documents_list = test_documents.copy()
        self.assertEqual(show_document_info(documents_list[0]), 'passport 2207 876234 Василий Гупкин')