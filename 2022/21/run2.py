import re
d=re.sub(" ([-+*/]) ([a-z]+)",r"()\1\2()",open("input.txt").read().replace(":","=lambda:"))
exec(d+"\nprint(int(root()))")
d=re.sub("(root.*)[-+*/](.*)",r"g\1>\2\n\1!=\2",d)
exec(d+"\ni=1;s=9**9;humn=lambda:i;g=groot()\nwhile root():\n i+=s\n if g!=groot():g=groot();s*=-1/9;\nprint(int(i))")
