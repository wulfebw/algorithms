'''
trie implementation
tree with n children nodes
each node contains indicator of whether a sequence ends at its position
also the letter it stores
children stored in array 
if child exists then it is not None

functions implemented by the tree / nodes
1. insert
2. contains

Trie contains a list of TrieNodes, so the Trie object acts as a root 
this way the trie node can always be associated with a letter 

TrieNode contains a map, why do a list? same look up time 
ok do a map?
no because want consistent traversal
ok so do a list then 
'''
import nltk.corpus
import sys

letter2idx = dict()
idx2letter = dict()
for i, lidx in enumerate(range(ord('a'), ord('z') + 1)):
    letter2idx[chr(lidx)] = i
    idx2letter[i] = chr(lidx)

class TrieNode(object):

    def __init__(self, letter, flag, n):
        self.letter = letter 
        self.flag = flag
        self.n = n
        self.children = [None] * n

    def insert(self, s):
        '''
        Description:
            - recusively calls inset until string is one letter. At that point 
            creates the child node if necessary and sets its flag to True.
        '''
        # check if child exists and if not create it 
        letter = s[0]
        if letter not in letter2idx.keys():
            return
        idx = letter2idx[letter]
        if not self.children[idx]:
            self.children[idx] = TrieNode(letter, False, self.n)

        # child exists at this point
        # if letter is the last in the word set flag to true and stop
        # otherwise continue on recursively
        if len(s) == 1:
            self.children[idx].flag = True
        else:
            self.children[idx].insert(s[1:])

    def contains(self, s, prefix=False):
        '''
        Description:
            - check if this node or children node contain the word s 
        '''
        # if len of the word is 1, then the word ends at this node
        # just return flag 
        if len(s) == 0:
            # if prefix true, then once we get to this point we know that 
            # either (a) this node indicates a word or (b) b/c this node 
            # exists, it must have been created to allow for a word with 
            # the prefix so far
            return self.flag or prefix

        # otherwise, check if corresponding child node exists
        # if not, then does not contain the word, if so then call recursively
        else:
            if s[0] not in letter2idx.keys():
                return False
            idx = letter2idx[s[0]]
            if self.children[idx]:
                return self.children[idx].contains(s[1:], prefix)
            else:
                return False

    def is_prefix(self, s):
        return self.contains(s, prefix=True)

    def print_all(self, prefix):
        postfix = self.letter if self.letter is not None else ''
        if self.flag:
            print(prefix + postfix)

        for child in self.children:
            if child:
                child.print_all(prefix + postfix)

class Trie(object):

    def __init__(self, n=26):
        self.root = TrieNode(None, False, n)

    def insert(self, s):
        self.root.insert(s)

    def contains(self, s):
        return self.root.contains(s)

    def is_prefix(self, s):
        return self.root.is_prefix(s)

    def print_all(self):
        self.root.print_all('')

    def load_english(self, maxlen=50):
        n = len(nltk.corpus.words.words())
        for i, word in enumerate(nltk.corpus.words.words()):
            if len(word) < maxlen:
                sys.stdout.write('\r{} / {}'.format(i+1, n))
                self.root.insert(word.lower())
        print('\nloaded!')

if __name__ == '__main__':
    words = [
        'hi',
        'hello',
        'hell',
        'hill',
        'hip',
        'hindrance'
    ]
    t = Trie()
    for word in words:
        t.insert(word)

    t.print_all()

    print('\nreal words')
    for word in words:
        print('{} {}'.format(word, t.contains(word)))

    fake_words = [
        'hipp',
        'hii',
        'hel',
        'help',
        'alpha',
        'hind',
        'i',
        '',
        'ello'
    ]
    print('\nfake words')
    for word in fake_words:
        print('{} {}'.format(word, t.contains(word)))

    t = Trie()
    t.load_english(maxlen=6)











