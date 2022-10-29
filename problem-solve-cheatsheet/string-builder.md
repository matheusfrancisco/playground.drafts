## String Builder
String is immutable
String concatenation += is expensive

O(n)

```python
# O(n^2)
def appendNtimesUsingStringConcat(c: str, n: int) -> str:
    out_str = ""
    for i in range(n):
        out_str += c    # O(s) where s = length(out_str)
        
    return out_str
    
# O(n)
def appendNtimesUsingStringJoin(c: str, n: int) -> str:
    list = []
    for i in range(n):
        list.append(c);   # O(1)
        
    return "".join(list)

```

String is immutable, meaning you can't change it once created. 
When you concatenate two strings, it doesn’t simply add one string at 
the end of another; it creates a new string (ouch). 
Use a StringBuilder instead (or string.join() on a list in Python),
which essentially is a List<Character>.

· String += c → linear
· StringBuilder.append(c) → constant

