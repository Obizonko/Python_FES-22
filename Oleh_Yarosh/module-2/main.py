import random
from owner import Owner
from team import Team


def main():
    owner = Owner()
    team = Team(owner)
    team.run()


if __name__ == '__main__':
    main()
