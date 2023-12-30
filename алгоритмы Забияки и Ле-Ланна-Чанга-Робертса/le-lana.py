from random import randint
ELECTION = 0
NEW_LEAD = 1
class Node:
    def __init__(self, node):
        self.next_node = node
        self.random = randint(1, 5)
        self.is_participant = False
        self.is_leader = False
        self.leader = False

    def start_election(self):
        print("{} SENDIND MESSAGE!.".format(self.random))
        self.is_participant = True
        self.forward((ELECTION, self.random))

    def forward(self, message):
        self.next_node.accept(message)

    def accept(self, message):
        group, uuid = message
        if group == ELECTION:
            if uuid > self.random:
                print("{} IS UPDATING AND SENDING.".format(self.random))
                self.is_participant = True
                self.forward((ELECTION, uuid))
            if uuid < self.random:
                print("{} IS UPDATING AND SENDING.".format(self.random))
                self.is_participant = True
                self.forward((ELECTION, self.random))
            if uuid == self.random:
                print("{} BECAME THE LEADER".format(self.random))
                self.is_participant = False
                self.is_leader = True
                self.leader = self.random
                self.forward((NEW_LEAD, self.random))
        if group == NEW_LEAD:
            if uuid == self.random:
                return
            if uuid != self.random:
                print("{} BECAME THE LEADER.".format(self.random))
                self.leader = uuid
                self.forward((NEW_LEAD, uuid))

#контекст процесса содержит его уникальный номер, node
def spawn(count=5):
    nodes = [Node(None)]
    for _ in range(count - 1):
        node = Node(None)
        nodes[-1].next_node = node
        nodes.append(node)
    nodes[-1].next_node = nodes[0]
    return nodes

if __name__ == '__main__':
    spawn(10)[0].start_election()