import random

class EightPuzzle:
    def __init__(self):
        self.goal_state = [[1,2,3], [4,5,6], [7,8,0]]
        self.current_state = []
        
    def generate_random_puzzle(self):
        nums = list(range(9))
        random.shuffle(nums)
        self.current_state = [nums[:3], nums[3:6], nums[6:]]
        
    def print_puzzle(self):
        for row in self.current_state:
            print(row)
    
    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == 0:
                    return (i, j)
    
    def move_left(self):
        blank_i, blank_j = self.get_blank_position()
        if blank_j > 0:
            self.current_state[blank_i][blank_j], self.current_state[blank_i][blank_j-1] = \
                self.current_state[blank_i][blank_j-1], self.current_state[blank_i][blank_j]
    
    def move_right(self):
        blank_i, blank_j = self.get_blank_position()
        if blank_j < 2:
            self.current_state[blank_i][blank_j], self.current_state[blank_i][blank_j+1] = \
                self.current_state[blank_i][blank_j+1], self.current_state[blank_i][blank_j]
    
    def move_up(self):
        blank_i, blank_j = self.get_blank_position()
        if blank_i > 0:
            self.current_state[blank_i][blank_j], self.current_state[blank_i-1][blank_j] = \
                self.current_state[blank_i-1][blank_j], self.current_state[blank_i][blank_j]
    
    def move_down(self):
        blank_i, blank_j = self.get_blank_position()
        if blank_i < 2:
            self.current_state[blank_i][blank_j], self.current_state[blank_i+1][blank_j] = \
                self.current_state[blank_i+1][blank_j], self.current_state[blank_i][blank_j]
    
    def is_goal_state(self):
        return self.current_state == self.goal_state
