from director.director import Director
from computer.accer import Accer
from computer.budget import Budget

computer_builder = Director(Accer())
computer_builder.build_computer()

computer = computer_builder.get_computer()
computer.display()