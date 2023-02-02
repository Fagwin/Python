# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N # and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For # # example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So # # for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the #beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. #Both strings will only contains lowercase alphabetic characters.

# SOLUTION

def MinWindowSubstring(strArr):
  N, K = strArr #Get each element of strArr
  ind = {}

  kchars = [] #Hashtable for characters in K
  kcharsInd = {} #Dictionnary to keep number of occurences for each character in K

  #Stock each character in k in a hashtable
  #And Count the number of occurence of one character in K
  for k in range(len(K)):
    if K[k] in kchars:
      kcharsInd[K[k]] += 1
    else : 
      kchars.append(K[k])
      kcharsInd[K[k]] = 1
  # print(kchars)
  # print(kcharsInd)

  #Get the smallest window
  #Stard by reducing the number of letter
  smallN = N
  minWindow = []
  n = len(N)-1
  l = 0
  while n >= 0 or l < len(N):
    if N[n] not in kchars:
      smallN = smallN[l:n]
      n=n-1
    elif N[l] not in kchars:
      smallN = N[l:n]
      n=n-1
    else:
      break
  # print(smallN)

  smallNL = []
  minWindowL = []
  lind = []
  for i in range(len(N)):
    if N[i] in kchars:
      if smallNL.count(N[i]) < kcharsInd[N[i]] :
        minWindowL.append(i)
        smallNL =N[minWindowL[0]:i+1]
        lind = list(range(minWindowL[0], i+1))
  # print(minWindowL)
  # print(smallNL)
  # print(lind)
  
  smallNR = []
  minWindowR = []
  rind = []
  for i in range(len(N)):
    j = len(N)-i-1
    if N[j] in kchars:
      if smallNR.count(N[j]) < kcharsInd[N[j]]:
        minWindowR.append(j)
        smallNR =N[j:minWindowR[0]+1]
        rind = list(range(j, minWindowR[0]+1))
  # print(smallNR)
  # print(minWindowR[::-1])
  # print(rind)

  minWindowR = minWindowR[::-1]

  smallestWinInd = [x for x in lind if x in rind]
  smallestWin = ""
  for i in smallestWinInd:
    smallestWin += N[i]
  
  # code goes here
  return smallestWin

# keep this function call here 
print(MinWindowSubstring(input()))
