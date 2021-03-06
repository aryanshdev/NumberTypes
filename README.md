# NumberTypes
Python Module to identify various types of Numbers Faster and Easier

- Can Identify Numbers as Even, Odd etc
- Find Total Occurence of a Specific type of number in a Given Range 
- All Funtions have their own help descriptions<br>
and more

## Installation

Using pip - 
```
pip install numbertypes
```

## Usage

To start using module ```numbertypes``` import it -
```python
import numbertypes <or> import numbertypes as nt 
```

<br>

## Functions 

There are 2 types of Functions Defined in the module

- **Normal** : take number(s) as input and return True if the belong to certain type.
- **Range Based** : take a range as input and return the frequncy of such numbers 
	which belong to a certain type. 

### List Of Normal Functions :
***(not in any specific sequence)***

- even
- odd
- composite
- prime
- twin_prime
- perfect_square
- emirp
- armstrong
- factorion
- palindrome
- narcissistic
- neon
- spy
- buzz
- automorphic

### List Of Range Based Functions :
***(not in any specific sequence)***

- even_in_range
- odd_in_range
- prime_in_range
- twin_prime_in_range
- palindrome_in_range
- factorion_in_range
- composite_in_range
- armstrong_in_range
- narcissistic_in_range
- neon_in_range
- spy_in_range
- emirp_in_range
- perfect_square_in_range
- buzz_in_range
- automorphic_in_range

## Normal Functions Usage

Common Syntax For all functions is
```python
FunctionName(Number To Test)
```
All these Functions return **True** if the number passed as argument belongs to the group, else **False**.

Usage Example :
```python
>>> even(9)
False
>>> odd(9)
True
>>> prime(13)
True
```

## Range Based Functions Usage

Common Syntax For all functions is
```python
FunctionName(starting=0,ending=0,shownumbers=False)
```
**Both starting and ending have default values = 0 and shownumbers has default value = *False*.** ***ending value is included in funtion calculations***

### shownumbers
when shownumbers is set to **True**  ***(default False)***, functions will print all the numbers that belong to that group.

Usage Example :
```python
>>> even_in_range(50)
25
>>> print("Total +",prime_in_range(69,420,True)
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
251
257
263
269
271
277
281
283
293
307
311
313
317
331
337
347
349
353
359
367
373
379
383
389
397
401
409
419
Total = 62
```
## Seeking Help

if you need help about any function type ```help(<function name>)``` for help related to that function.

	
**Try On Your Own And Explore the Various Types OF Numbers....**