from math import gcd

class TreeNode(object):
  def __init__(self, data=None):
    self.children = []
    self.data = data

class PermutationTree(object):
  def __init__(self, nums):
    self.nums = nums
    self.root = TreeNode()
    self.initializeTree()
    self.buildPermutationTree(self.root, nums)

  def initializeTree(self):
    for i in self.nums:
      self.root.children.append(TreeNode(i))

  def buildPermutationTree(self, root, nums):
    # Recursively build a permutation tree
    for child in root.children:
      copy_nums = nums.copy()
      copy_nums.remove(child.data)
      for num in copy_nums:
        child.children.append(TreeNode(num))
      self.buildPermutationTree(child, copy_nums)

  def print_tree(self, root, visited=[], numSpaces=0):
    if id(root) not in visited:
      print("--" * numSpaces + str(root.data))
      numSpaces += 1
      visited.append(id(root))
      for child in root.children:
        self.print_tree(child, visited, numSpaces)
    else:
      numSpaces -= 1

class ResidueNumberSystem():
  # We implement a residue number system with constant look-up times
  def __init__(self, bases):
    self.bases = bases
    # Look up table generation for numbers that are not "large"
    # As defined, "large" means > 1000
    self.createInt2RNS_LUT()
    self.createAdditionLUT()
    self.createMultiplicationLUT()
    self.maxInt = prod(self.bases)

  def intToRns(self, rhs):
    # Non-constant time intToRns function for LUT generation
    return list(map(lambda x: rhs % self.bases[x], range(len(self.bases))))

  def rnsToInt(self, rns):
    # Convert a RNS to an integer
    for key, value in self.lut.items():
      if rns == value:
        return key

  def createInt2RNS_LUT(self):
    # Create the look up table for integer conversion
    self.lut = {}
    for i in range(1001):
      self.lut[i] = self.intToRns(i)

  def createAdditionLUT(self):
    # Create the addition look up table
    self.addLut = {}
    for i in self.bases:
      m = []
      for x in range(0, i):
        row = []
        for y in range(0, i):
          row.append((x + y) % i)
        m.append(row)
      self.addLut[i] = m
  
  def createMultiplicationLUT(self):
    # Create the multiplication look up table
    self.multLut = {}
    for i in self.bases:
      m = []
      for x in range(0, i):
        row = []
        for y in range(0, i):
          row.append((x * y) % i)
        m.append(row)
      self.multLut[i] = m
  
  def add(self, n1 : int, n2 : int):
    # Addition of two integers using constant look-up time
    if not n1 in range(0, self.maxInt) and not n2 in range(0, self.maxInt):
      return ValueError("Either parameter is not valid. RNS Overflow will occur")
    n1RNS = self.lut[n1]
    n2RNS = self.lut[n2]
    resultRNS = list(map(lambda x: self.addLut[self.bases[x]][n1RNS[x]][n2RNS[x]], range(len(self.bases))))
    return resultRNS
  
  def multiply(self, n1 : int, n2 : int):
    # Constant lookup time for multiplication
    if not n1 in range(0, self.maxInt) and not n2 in range(0, self.maxInt):
      return ValueError("Either parameter is not valid. RNS Overflow will occur")
    n1RNS = self.lut[n1]
    n2RNS = self.lut[n2]
    resultRNS = list(map(lambda x: self.multLut[self.bases[x]][n1RNS[x]][n2RNS[x]], range(len(self.bases))))
    return resultRNS

def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def get_lcm(l):
  lcm = l[0]
  for i in l[1:]:
    lcm = lcm * i // gcd(lcm, i)
  return lcm

def findMMI(o, m):
  # Find MMI in O(m) time
  o = o % m
  for x in range(1, m):
    if ((o * x) % m == 1):
      return x
  return 1

def prod(l):
  num = 1
  for i in l:
    num *= i
  return num
