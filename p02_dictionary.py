d1 = {
    "hello": 10, "world": 25
}

print("key가 hello인 항목의 value는?")
print(d1["hello"])

keys = [ "hello", "are_you_there", "world" ]
for key in keys:
  print('-- Key:', key)
  print('--- Value:', d1[key])

'''
-- Key: hello
--- Value: 10
-- Key: are_you_there
Traceback (most recent call last):
  File "D:/Lectures/2023_2/git/python/p02_dictionary.py", line 14, in <module>
    print('--- Value:', d1[key])
KeyError: 'are_you_there'
'''
