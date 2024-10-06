import math

cases = int(input())

MOD = 10**9 + 7

# def solve(LEN, K):
#   if LEN == 1:
#     if K == 0: return 1
#     elif K == 1: return 2
#     else: return 4

#   sbagliate = 0
#   if K > 0:
#     sbagliate = solve(LEN-1, K-1)

#   return sbagliate + solve(LEN-1, K)

def binNet(n, k):
  math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def fact(n, times):
  accum = n
  counter = 1
  while(counter != times):
    accum *= n - counter
    counter += 1
  return accum


def solve(LEN, K):
  #bilanciate base (2n n) - (2n n+1)
  tot = binNet(2*LEN, LEN) - (2*LEN, LEN+1)
  tot += fact(n, k)

"""
while cases > 0:
  cases -= 1
  line1 = input().split(" ")
  LEN, K = int(line1[0]), int(line1[1])
  print(LEN, K, "->", solve(LEN, K))
"""
# k0 = 1
# k1 = 2
# k>1 = 4

# k0 -> 1 ()
# )( () k1 = 2
# )), ((, (), )( k2 = 4

# N = 1
# () k >= 0 1 comb
# )( k >= 1 1 comb

# (( k >= 2 1 comb  ( () )
# )) k >= 2 1 comb

# N = 2
# Explanation
# In the first query there are 5 strings of length 4 that are 1-valid. They are highlighted below:
# • In (()) ) the sequence (()) is valid, but also 1-valid.
# • In ()() ) the sequence ()() is valid, but also 1-valid.
# • In ())( ) the sequence ())( is invalid, but 1-valid.
# • In )(() ) the sequence )(() is invalid, but 1-valid.
# • In )()( ) the sequence )()( is invalid, but 1-valid

# You need to write Q lines containing each the result of the i-th query: for each query, print the number
# of strings of length 2Ni that are Ki-valid, modulo 1 000 000 007.

# LEN
# )(

# (())
# )()(

# )

# 5 62 242

