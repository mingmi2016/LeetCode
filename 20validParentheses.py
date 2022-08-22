


s = input("please input string:")

#   空字符串返回True
#if s == "":
#    return True

# 空字符串的另外一种写法
if len(s) == 0:
    print("True")


#   通过列表实现栈,stack.append(x) stack.pop()
stack = [] 
for c in s:
    if  (c=='(' or c=='[' or c=='{' ):
        stack.append(c)
    else:
        if len(stack) == 0:
            print("False")
        else:
            temp = stack.pop()
            if c == '(':
                if temp  != ")":
                  print("False")
                  exit()
            if c == '{':
                if temp  != "}":
                  print("False")
                  exit()
            if c == '[':
                if temp  != "]":
                  print("False")
                  exit()

if len(stack) != 0:
   print("False")
   exit()
else:
   print("True")
   exit()














