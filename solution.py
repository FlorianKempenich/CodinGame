import sys
# import math


def debug(msg):
    print(msg, file=sys.stderr)


def main():
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in input().split()]
    links = []
    exits = []
    for i in range(l):
        n1, n2 = [int(j) for j in input().split()]
        links.append(Link(n1, n2))
    for i in range(e):
        ei = int(input())
        exits.append(ei)

    game = Game(links, exits)

    while True:
        si = int(input())
        game.set_skynet_location(si)

        next_to_cut = game.next_exit_link()
        if next_to_cut:
            game.cut_link(next_to_cut)


class Link:
    def __init__(self, node1: int, node2: int):
        self.n1 = node1
        self.n2 = node2

    def contains_node(self, node):
        return self.n1 == node or self.n2 == node

    def __eq__(self, other):
        return (self.n1 == other.n1 and self.n2 == other.n2) \
            or (self.n1 == other.n2 and self.n2 == other.n1)

    def __repr__(self):
        return f'{{{self.n1} - {self.n2}}}'


class Game:
    def __init__(self, links, exits):
        self.links = links
        self.links_cut = []
        self.exits = exits
        self.skynet = None

    def set_skynet_location(self, skynet_node: int):
        self.skynet = skynet_node

    def cut_link(self, to_cut: Link):
        def execute_cut_cmd():
            print(f'{to_cut.n1} {to_cut.n2}')

        try:
            self.links.remove(to_cut)
            self.links_cut.append(to_cut)
            execute_cut_cmd()
        except ValueError:
            debug(f"Link {to_cut} not found!")
            raise

    def next_exit_link(self):
        def skynet_is_on_exit_link():
            for ex in self.exits:
                link = Link(self.skynet, ex)
                if link in self.links:
                    return True, link
            return False, None

        def is_exit_link(link):
            for ex in self.exits:
                if link.contains_node(ex):
                    return True
            return False

        skynet_is_on_exit_link, skynet_exit_link = skynet_is_on_exit_link()
        if skynet_is_on_exit_link:
            return skynet_exit_link

        for li in self.links:
            if is_exit_link(li):
                return li
        return None


if __name__ == "__main__":
    main()
