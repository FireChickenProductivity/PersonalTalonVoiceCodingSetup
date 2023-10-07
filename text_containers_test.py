try:
    from text_containers import * 
    PARENTHESES_CONTAINER = TextContainer('(', ')')
    ANGLE_CONTAINER = TextContainer('<', '>')
except: pass

import unittest

class TestSubStringAtMatches(unittest.TestCase):
    def test_sub_at_matches_handles_empty_sub_string(self):
        for index in range(len('testing')):
            self.sub_at_matches_test('testing', index, '', True)
        
    def test_longer_string_fails(self):
        self.sub_at_matches_test('test', 0, 'tests', False)
    
    def test_index_too_far_fails(self):
        self.sub_at_matches_test('test', 4, 'st', False)
        self.sub_at_matches_test('test', 5, 't', False)
        self.sub_at_matches_test('test', 1, 'test', False)
    
    def test_these_simple_cases_should_be_true(self):
        self.sub_at_matches_test('test', 0, 'test', True)
        self.sub_at_matches_test('test', 0, 'tes', True)
        self.sub_at_matches_test('test', 0, 'te', True)
        self.sub_at_matches_test('test', 0, 't', True)
        self.sub_at_matches_test('testing', 3, 'ti', True)
    def sub_at_matches_test(self, text, index, sub_string, expected):
        self.assertEqual(sub_string_at_matches(text, index, sub_string), expected)

class TestsSubStringAtMatchesReverse(unittest.TestCase):
    def test_handles_empty_sub_string(self):
        for index in range(len('testing')):
            self.function_test('testing', index, '', True)
    
    def test_these_simple_cases_should_be_true(self):
        self.function_test('test', 1, 't', True)
        self.function_test('test', 2,'te', True)
        self.function_test('test', 3, 'tes', True)
        self.function_test('test', 3, 'es', True)
        self.function_test('test', 3, 's', True)

    def test_longer_string_fails(self):
        self.function_test('testing', 4, 'fest', False)
        self.function_test('testing', 4, 'fst', False)
    
    def test_index_too_far_fails(self):
        self.function_test('testing', 0, 't', False)
        self.function_test('testing', 1, 'te', False)
        
    def function_test(self, text, index, sub_string, expected):
        self.assertEqual(sub_string_at_matches_reverse(text, index, sub_string), expected)

class TestLeftMostUnclosedContainer(unittest.TestCase):
    def test_no_containers_gives_none(self):
        containers = set_up_containers()
        text = 'chicken'

        self.assertEqual(left_most_unclosed_container(text, containers), None)
    def test_no_container_beginnings_gives_none(self):
        containers = set_up_containers()
        text = 'ch>experimenting)>'

        self.assertEqual(left_most_unclosed_container(text, containers), None)
    def test_only_closed_containers_gives_none(self):
        containers = set_up_containers()
        text = '(cl<o>sed)'

        self.assertEqual(left_most_unclosed_container(text, containers), None)
    def test_gives_leftmost(self):
        containers = set_up_containers()
        text = '(chicken<testing'

        self.assertEqual(left_most_unclosed_container(text, containers), PARENTHESES_CONTAINER)
    def test_gives_leftmost_unclosed(self):
        containers = set_up_containers()
        text = '(chicken<testing)'

        self.assertEqual(left_most_unclosed_container(text, containers), ANGLE_CONTAINER)


def set_up_containers():
    containers = []
    containers.append(PARENTHESES_CONTAINER)
    containers.append(ANGLE_CONTAINER)
    return containers

SIMPLE_SPLIT_TESTCASE = 'HashMap<int, String>,variable'
SIMPLE_SPLIT_TEST_CASE_EXPECTED_RESULT = ['HashMap<int, String>', 'variable']
class TestSplitStringIgnoringContainers(unittest.TestCase):
    def test_can_handle_no_separator(self):
        separator = '?'
        text = SIMPLE_SPLIT_TESTCASE
        containers = set_up_containers()

        expected_result = [SIMPLE_SPLIT_TESTCASE]
        result = split_string_ignoring_containers(text, separator, containers)

        self.assertEqual(result, expected_result)
    
    def test_can_handle_simple_case(self):
        separator = ','
        text = SIMPLE_SPLIT_TESTCASE
        containers = set_up_containers()

        expected_result = SIMPLE_SPLIT_TEST_CASE_EXPECTED_RESULT
        result = split_string_ignoring_containers(text, separator, containers)
        print(result)
        print(expected_result)
        self.assertEqual(result, expected_result)

        


if __name__ == '__main__':
    unittest.main()