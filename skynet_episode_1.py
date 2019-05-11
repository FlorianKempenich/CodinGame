import sys


def debug(msg):
    print(msg, file=sys.stderr)


def main():
    game = Game.initialize_from_input()

    while True:
        def read_skynet_location():
            return int(input())

        game.set_skynet_location(read_skynet_location())
        next_to_cut = game.next_link_to_cut()
        if next_to_cut:
            game.cut_link(next_to_cut)
        else:
            debug("No link to cut. Waiting")
            game.wait()


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
    @classmethod
    def initialize_from_input(cls):
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

        return cls(links, exits)

    def __init__(self, links, exits, proactive=True):
        self.links = links
        self.links_cut = []
        self.exits = exits
        self.skynet = None
        self.proactive = proactive

    def set_skynet_location(self, skynet_node: int):
        self.skynet = skynet_node

    def next_link_to_cut(self):
        def find_skynet_exit_link():
            for ex in self.exits:
                link = Link(self.skynet, ex)
                if link in self.links:
                    return link
            return None

        def find_random_skynet_link():
            for li in self.links:
                if li.contains_node(self.skynet):
                    return li
            debug("Skynet is trapped, no links to cut")
            return None

        skynet_exit_link = find_skynet_exit_link()
        if skynet_exit_link:
            return skynet_exit_link

        if self.proactive:
            return find_random_skynet_link()
        else:
            return None

    def cut_link(self, to_cut: Link):
        try:
            self.links.remove(to_cut)
            self.links_cut.append(to_cut)
            Cmd.cut(to_cut).execute()
        except ValueError:
            debug(f"Link {to_cut} not found!")
            raise

    def wait(self):
        Cmd.wait().execute()


class Cmd:
    class _cmd:
        def execute(self):
            print(self.text_cmd)

    class _cut_cmd(_cmd):
        def __init__(self, link_to_cut):
            self.text_cmd = f'{link_to_cut.n1} {link_to_cut.n2}'

    class _wait_cmd(_cmd):
        def __init__(self):
            self.text_cmd = 'wait'

    @classmethod
    def cut(cls, link):
        return cls._cut_cmd(link)

    @classmethod
    def wait(cls):
        return cls._wait_cmd()


if __name__ == "__main__":
    main()
