
# Strings & Arrays (or rather lists in Python)

# 1.1 check if all chars in string are unique
# time complexity should be O(N), i.e. runs in linear time
def isunique(s):
    seen = {}
    for ch in s:
        if ch in seen: return False
        seen[ch] = 1
    return True

# 1.2 check if one string is permutation of the other
# time is again O(N)
def ispermut(s, other):
    if len(s) != len(other): return False
    m = {}
    for c in s: m[c] = m.get(c, 0) + 1
    for c in other:
        if m.get(c) is None: return False
        m[c] = m.get(c, 0) - 1
        if m[c] < 0: return False

    if sum(m.values()) != 0: return False
    return True 

# 1.3 replace spaces in string with %20
# again O(N)
def URLify(s):
    for idx, c in enumerate(chs:=list(s)):
        if chs[idx] == " ": chs[idx] = "%20"
    return ''.join(chs)

# 1.4 check if string is a permutation of a palindrom
# should be O(N)
def ispalindrom_permut(s):
    s = s.replace(" ", '').lower()
    # we count '' as palindrom
    if len(s) == 0 or len(s) == 1: return True

    # cbaba is permut of abcba, thus should be True
    counts = {}
    for c in s: counts[c] = counts.get(c, 0) + 1
    # each char needs to have a counterpart, abba -> aa bb
    if len(s) % 2 == 0: return all(cnt % 2 == 0 for cnt in counts.values())
    # if s len is odd, only one char can occur once
    return list(counts.values()).count(1) == 1 and all(cnt in {1,2} for cnt in counts.values())

# 1.5 check if other is one (or 0) edits (insert, replace or delete) away from s
# is again O(N), linear time
def one_away(s: str, other: str):
    if abs(len(s) - len(other)) > 1: return False
    if len(s) == len(other): return sum([a != b for a, b in zip(s, other)]) in {0, 1}

    # swap to handle delete as insert
    if len(s) > len(other):
        s, other = other, s
    # handle insertion, e.g. "pales" to "palbes" requires one insert
    inserted = False
    if len(s) < len(other):
        for i, c in enumerate(s):
            if other[i+1 if inserted else i] != c:
                if inserted: return False
                inserted = True
    return True

# 1.6 compress (here squeeze) string with character counts, e.g. aabbbc -> a2b3c1
# Notes: lowercase and uppercase characters allowed, nothing else,
# is compressed string not shorter than original one, return the latter.
# should be O(N) because we go through each character once, despite having an inner loop
def squeeze_with_counts(s: str):
    out = ""
    i = 0
    while i < len(s):
        cnt = 1
        curr = s[i]
        j = i+1
        while j < len(s) and s[j] == curr:
            cnt += 1
            j += 1

        out += curr + str(cnt)
        # implicitly fallbacks to i+=1 if inner loop is not entered, cute
        i = j
        cnt = 1

    ret = out if len(out) < len(s) else s
    return ret

# 1.7 Rotate matrix
# NxN Matrix, where each pixel has 4 bytes, rotate the image/matrix by 90 degrees clockwhise. try to do it in place as well.
# Runtime is O(N^2), need to touch each element of matrix.
def mat_rotate(mat):
    N = len(mat) # cute
    # 4 bytes could be RGB where each pos has sth. like [255, 255, 0, 0.5]. last dim here is the alpha channel with range [0,1]
    # we need to move each element at pos (i,j), let's start with simple scalar values. example 3x3 matrix is
    # init out with zeros and same length
    out = [[0 for col in row] for row in mat]
    # move each element at pos (i,j) to (j, N-1-i)
    for i in range(N): # iter over rows
        for j in range(N): # now cols
            out[j][N-1-i] = mat[i][j]
    return out

# Optimal solution that works in-place and thus is more space efficient. Still O(N^2) runtime though
# Although it's more space efficient, it takes a lot longer to get the idea
def mat_rotate_space(mat): # modifies mat in-place!
    N = len(mat)
    for layer in range(int(N/2)):
        last = N-1 - layer
        offset = 0
        for i in range(layer, last):
            top = mat[layer][i]
            # could also do offset = i - layer instead
            offset += 1

            # move left (bottom) to top (left)
            mat[layer][i] = mat[last - offset][layer]

            # move bottom (right) to left (bottom)
            mat[last - offset][layer] = mat[last][last - offset]

            # move right (top) to bottom (right)
            mat[last][last - offset] = mat[layer + offset][last]

            # move top (left) to right (top)
            mat[layer + offset][last] = top

    return mat

"""1.8 Zero Matrix
If an element in the MxN matrix is zero (0) set its row and column to zeros.
Runtime should be O(M * N), need to go through each element in matrix.
Space is O(Z) where Z is the number of zeros in the matrix. O(Z) < O(M + N), the latter would be the worst case (all zeros)
"""
def zero_mat(mat):
    # (idx, row/col) -> True
    tozero = {}
    M = len(mat)
    N = len(mat[0])

    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if col == 0:
                tozero[(i, "row")] = True
                tozero[(j, "col")] = True

    for k in tozero.keys():
        idx = k[0]
        if k[1] == "row": mat[idx] = [0 for _ in range(N)]
        else:
            for i in range(M): mat[i][idx] = 0
    
    return mat

# Sorting & Search

# Runtime is O(log n). Say n is the length of the list, 2^k = n => k = log n (base 2)
def binary_search(list_sorted, ele):
    start = 0
    end = len(list_sorted) - 1
    while start <= end:
        mid = int((start + end) / 2)
        current = list_sorted[mid]

        if current < ele: start = mid + 1
        elif current > ele: end = mid - 1
        else: return True

    return False

# Stacks & Queues

# Track 3 stacks in one array (list), each stack gets 1/3 of the list size as capacity, no resizing
class ThreeStacks:
    def __init__(self, stack_size):
        # list to store the values of the three stacks
        self.ls = [0] * stack_size*3
        self.stack_size = stack_size
        # stack num to current top of stack
        self.stack_ptrs = {i: i * stack_size for i in range(3)}

    def push(self, stack_num, val):
        assert not self.isfull(stack_num), f"stack {stack_num} is already full"
        self.ls[self.stack_ptrs[stack_num] + 1] = val
        self.stack_ptrs[stack_num] += 1

    def pop(self, stack_num):
        assert not self.isempty(stack_num), f"stack {stack_num} is empty, cannot pop"
        val = self.ls[self.stack_ptrs[stack_num]]
        self.stack_ptrs[stack_num] -= 1
        return val

    def isfull(self, stack_num):
        start = stack_num * self.stack_size
        return self.stack_ptrs[stack_num] - start == 3

    def isempty(self, stack_num):
        start = stack_num * self.stack_size
        return self.stack_ptrs[stack_num] == start

# 3.6 Animal Shelter. Implement queue using a LinkedList.
# The shelter hand out animals on first-in first-out basis, i.e. the animal which has been in the shelter
# the longest gets out first. One can choose the type of animal, dog or cat, but still the same rule applies.
class Node:
    def __init__(self, value):
        # value should be tuple (name, dog/cat)
        self.value = value
        self.next = None

from enum import Enum

class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"

class AnimalShelter:
    def __init__(self):
        # repr shelter queue as singly LinkedList (forward pointers only)
        self.head = None
        # to have O(1) enqueue 
        self.last = None

    def enqueue(self, animal):
        n = Node(animal)
        # queue is still empty 
        if self.head is None:
            self.head = n
            self.last = n
        else: # add to end of queue
            self.last.next = n
            self.last = n

    # NOTE: to make dequeue O(1) as well we would need internally two queues, one for dogs, one for cats
    def dequeue(self, kind): # animal kind is 'Dog' or 'Cat'
        if self.head is None: return None
        prev = None
        curr = self.head
        while curr is not None:
            # found animal of desired kind 
            if curr.value[1] == kind:
                # we remove from start of list
                if prev is None: self.head = curr.next
                # remove from middle or end of list
                else: prev.next = curr.next

                if self.head is None: self.last = self.head
                elif curr == self.last: self.last = prev
                return curr.value

            prev = curr
            curr = curr.next
        return None

    def peek(self, kind):
        if self.head is None: return None
        curr = self.head
        while curr is not None:
            # found animal of desired kind 
            if curr.value[1] == kind: return curr.value
            curr = curr.next
        return None

    def __repr__(self):
        if self.head is None: return "| |"
        curr = self.head
        vals = []
        while curr is not None:
            vals.append(f"{curr.value[1].value} {curr.value[0]}")
            curr = curr.next
        return " <- ".join(vals)
