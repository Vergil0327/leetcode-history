# Intuition

transform a and b into array with size equals 26 because they only consists of lowercase English characters.

ex1.
aba => arr1 = [2,1,0,0,0,...]
caa => arr2 = [2,0,1,0,0,...]

ex2.
dabadd = arr1 = [2,1,0,3,0,...,0]
cda    = arr2 = [1,0,1,1,0,...,0]

arr1 = [X,X,X,X,...]
arr2 = [Y,Y,Y,Y,...]

try from "a" to "z":

if we set upperlimit of arr1 to arr1[i] and make arr2 greater than arr1[i], then
`required operations = sum(arr1[i+1:]) + sum(arr2[:i+1])`
where **0 <= i < 25** because arr1[i] can't be character "z", or we can't make arr2 valid

if we set lowerlimit of arr1 to arr1[i] and make arr2 lower than arr1[i], then
`required operations = sum(arr1[:i]) + sum(arr2[i:])`
where **1 <= i < 26** because arr1[i] can't be character "a", or we can't make arr2 valid

if we make arr1 and arr2 only one distinct character, then
`minimum required operations = sum(arr1) - max(arr1) + sum(arr2) - max(arr2)`
