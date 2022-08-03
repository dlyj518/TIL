import random
class ClassHelper:
    pass
    # 아래에 코드를 작성하시오.
    def __init__(self, students):
        self.students = students
    def pick(self, n):
        choose = sorted(random.sample(range(len(self.students)), n))
        picked = [self.students[i] for i in choose]
        return picked
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])
ch.pick(1) 
ch.pick(1) 
ch.pick(2) 
ch.pick(3) 
ch.pick(4) 