
class Node(object):

    def __init__(self, d, l=None, r=None):
        self.d = d
        self.l = l 
        self.r = r

    def __repr__(self):
        return str(self.d)

    def lca_shit(self, a, b, a_flag, b_flag):
        # base cases
        if b_flag and self.d == a:
            return None, True, True
        elif a_flag and self.d == b:
            return None, True, True
        elif self.d == a:
            a_flag = True
        elif self.d == b:
            b_flag = True

        # recursive
        if self.l:
            l_a, l_a_flag, l_b_flag = self.l.lca(a, b, a_flag, b_flag)
            if l_a_flag and l_b_flag and l_a is not None:
                return l_a, True, True
        else:
            l_a = None
            l_a_flag = False
            l_b_flag = False

        if self.r:
            r_a, r_a_flag, r_b_flag = self.r.lca(a, b, a_flag, b_flag)
            if r_a_flag and r_b_flag and r_a is not None:
                return r_a, True, True
        else:
            r_a = None
            r_a_flag = False
            r_b_flag = False

        # at this point if both r_a and l_a are None
        # and a_flag and b_flag are True, self is the lca
        if (l_a_flag and r_b_flag) or (l_b_flag and r_a_flag):
            return self, True, True
        else:
            return None, l_a_flag or r_a_flag or a_flag, l_b_flag or r_b_flag or b_flag

    def lca(self, a, b):

        if self.d == a or self.d == b:
            return self

        if self.l:
            l_lca = self.l.lca(a, b)
        else:
            l_lca = None
        if self.r:
            r_lca = self.r.lca(a,b)
        else:
            r_lca = None

        if l_lca and r_lca:
            return self 
        else:
            if l_lca:
                return l_lca
            else:
                return r_lca

if __name__ == '__main__':

    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    inputs = [
        (4,5),
        (4,6),
        (3,4),
        (2,4),
        (4,7),
        (1,7),
        (7,1)
    ]

    for (a,b) in inputs:
        print(n1.lca(a,b))


