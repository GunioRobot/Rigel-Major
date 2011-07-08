#!/usr/bin/python3.1
route = 10
print (route, type(route))
int(route)                  ## Prints value as integer
str(route)                  ## Prints value as string

route = 100                 ## Define variable route
route = (str(route))        ## Change route var to string
print (route, type(route)) ## Print value of route and its class

a = "one","two","three"     ## Create a tuple and tie it to variable a
print (str(a[0]))           ## Print index 0 from tuple in var a as a string

a = "0","one","two","three" ## Modify tuple with an integer at index 0
print (int(a[0]))           ## Print index 0 from tuple in var a as an integer

len ('phrase')              ## Prints length of string
len(a[0]), len(a[1])        ## Prints length as a tuple (1, 3)
len(a[0]); len(a[1])        ## Prints length as two strings, one per line

list_a = ['0', 'one', 'two', 'three']   ## create a list and tie it to variable list_a
list_a.append('four')       ## Append item to list in var list_a
x = 'five'                  ## Assign variable x
list_a.append(x)            ## Append variable x to list list_a
list.append(list_a, 'six')  ## Another way of appending to a list_a
list.append(list_a, x)      ## Append a value from a variable
list.insert(list_a, 3, 'sam')   ## Insert a value (sam) as third item in the list list_a
list.remove(list_a,'sam')   ## Remove first occurance of value (sam)
var1 in list_a              ## Check for presence of var1 in list list_a
var1 not in list_a          ## Check for absence of var1 from list list_a

for num in list_a:          ## for loop, where an item list is read, and echoed back
	print('This is number', num)
	
try:                        ## Exception handling example, where a word is checked for
	'one' in list_a         ## in a list
	print('one is in list_a')
except ValueError as err:
	print(err)
	
mystr = '1a1b1c1d'          ## String will be splt, at every occurance of '1'
re.split('1', mystr)

mylist_i = (re.findall('[0-9]', mystr)) ## Extract all numbers from a string, and create a list
a = list(range(0,10,1))    ## Create a list of numbers from 0 through 9, incrementing by one

## Regex in Python
p = re.compile('[a-z]+',re.IGNORECASE)  ## create a MatchObject, which we store in variable 'p'
q = p.match('sam')          ## Create a variable with string with regex result based on string 'sam'

## File selection using regex
for file in glob.glob('pathname'):
    print(file)

## Use formatting with print %i=integer, %s is a string
print ('The value of x is %s, while the value of x is %i' % (x,y))

## Basic module structure and how it is called
def mymod(x,y):
    print(x, 'is a', type(x))
    print (y, 'is a', type(y))
## How to call a module
mymod(one,two)

## Testing for presence of characters in a string, or integers in a list or tuple
var2 = [1,2,3]
if 'a' in var1:
    print(var1, 'contains a')
if 1 in var2:
    print(var2, 'contains 1')

## Testing if files in a directory have execute permission     
for dirpath, dirnames, filenames in os.walk('/tmp'):
    for file in filenames: 
        path = os.path.join(dirpath,file)
        x = os.access(path, os.X_OK)
        if x == True:
            print(path,'Good')
        else:
            print(path,'Not Exec')
	    
	    

## sorting of lists and other collection types
myvar = sorted(['one','two','three','four'])

## Sort by length of string
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)

## Conditionals in print() function
print('foo' if a > b else 'bar')	## this will return 'foo' or 'bar' depending on condition

## Using a text format string to format input values
fmt = 'Adding %s to %s equals %s.'
mytup = ('one','two','three')
print(fmt % mytup)

## String Templates
import string
ab = string.Template('$x, is $x!')
ab.substitute(x = 'today') ## Result: 'today, is today!'

import string
abc = string.Template('$a, should always come before $b')
abc.substitute(a = 'today', b = 'tomorrow') ## Result: 'today, should always come before tomorrow'

user = os.getenv('USERNAME')
ab = string.Template('Are you sure you are $x?')
ab.substitute(x=user) ## Result: 'Are you sure you are szaydel?'

'%s should always be smaller than %s' % (1,2)	## string formatting using %s

print (('% 5d' % 1110) + '\n' + ('% 5d' % -110))

## Various os.*** functionality
os.environ['PATH'].split(':')	## Create tuple of all paths in the PATH

## Dealing with dates
today = datetime.date.today()  # get today's date as a datetime type  
todaystr = today.isoformat()   # get string representation: YYYY-MM-DD from a datetime type.  
todaystr = datetime.date.today().isoformat()    ## get today's date as a datetime type
timenow = datetime.datetime.now().strftime("%Y%m%d,%H%M%S") ## today's date '20110112,183351'

## Dealing with paths

# .. use os.path.join()
if not os.path.exists(os.path.join('/home/build/test/sandboxes/', todaystr)):  
    os.mkdir(os.path.join('/home/build/test/sandboxes/', todaystr))
else:
    'do something'


if os.path.exists('/home/build/test/sandboxes/'+todaystr+'/new_sandbox/Makefile'):  
    os.system("make >make_results.txt 2>&1")

## .. change to the right directory
os.chdir(os.path.join('/home/build/test/sandboxes/', todaystr, '/new_sandbox/'))