import random
from pandas import DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})
data.head()
print(data)

robot = []
human = []

for i in lst:
    if i == 'robot':
        robot.append(1)
    else:
        robot.append(0)

for i in lst:
    if i == 'human':
        human.append(1)
    else:
        human.append(0)

data_one_hot = DataFrame({'robot': robot, 'human': human})
print(data_one_hot)
