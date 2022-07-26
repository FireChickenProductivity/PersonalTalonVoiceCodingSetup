
class TextContainer:
    def __init__(self, start, end, invalid_left_boundary = '', invalid_right_boundary = ''):
        self.start = start
        self.end = end
        self.invalid_left_boundary = invalid_left_boundary
        self.invalid_right_boundary = invalid_right_boundary

    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
   
    def valid_left_boundary_of_text_at(self, text, index):
        if self.invalid_left_boundary == '':
            return True
        return not sub_string_at_matches_reverse(text, index, self.invalid_left_boundary)
    def valid_right_boundary_of_text_at(self, text, index):
        if self.invalid_right_boundary == '':
            return True
        return not sub_string_at_matches(text, index + len(self.get_start()), self.invalid_right_boundary)
    



class SplitStringIgnoringContainersState:
    def __init__(self):
        self.result = []
        self.inside_container = False
        self.current_string = ''
        self.remaining_string = ''
        self.container = None
    def set_remaining_string(self, value):
        self.remaining_string = value
    def is_inside_container(self):
        return self.inside_container
    def update_result(self):
        self.result.append(self.current_string)
        self.current_string = ''
    def get_result(self):
        return self.result
    def handle_unclosed_container_in_current_string_if_present_given_containers(self, containers):
        unclosed_container_search_result = left_most_unclosed_container(self.remaining_string, containers)
        if unclosed_container_search_result != None:
            self.container = unclosed_container_search_result
            self.inside_container = True
       
    def handle_container_given_separator(self, separator):
        container_ending = self.remaining_string.find(self.container.get_end())
        if container_ending > 0:
            container_ending += len(self.container.get_end())
            self.current_string += self.remaining_string[ : container_ending]
            self.remaining_string = self.remaining_string[ container_ending : ]
            self.inside_container = False
        else:
            self.current_string += self.remaining_string + separator
    def add_the_remaining_string_to_the_current_string(self):
        self.current_string += self.remaining_string
    def add_text_to_current_string(self, text):
        self.current_string += text

def split_string_ignoring_containers(text, separator, containers):
    original_split = text.split(separator)
    state = SplitStringIgnoringContainersState()
    for text_part in original_split:
        state.set_remaining_string(text_part)
        if state.is_inside_container():
            state.handle_container_given_separator(separator)
        if not state.is_inside_container():
            state.handle_unclosed_container_in_current_string_if_present_given_containers(containers)
            state.add_the_remaining_string_to_the_current_string()
            if state.is_inside_container():
                state.add_text_to_current_string(separator)
            else:
                state.update_result()
    return state.get_result()
        
def left_most_unclosed_container(text, containers):
    index = 0
    while index < len(text):
        for container in containers:
            if sub_string_at_matches(text, index, container.get_start()) and container.get_end() not in text \
                and container.valid_right_boundary_of_text_at(text, index) and container.valid_left_boundary_of_text_at(text, index):
                return container
        index += 1
    return None

def sub_string_at_matches(text, index, sub_string):
    if len(sub_string) + index > len(text):
        return False
    return text[index : len(sub_string) + index] == sub_string

def sub_string_at_matches_reverse(text, index, sub_string):
    if index < len(sub_string):
        return False
    return sub_string_at_matches(text, index - len(sub_string),sub_string)

