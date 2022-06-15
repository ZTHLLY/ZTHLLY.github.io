#this code can show you the last result of the programme
def func():
    print("the last result is:")
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)

#now you can input your formula
expression = input("please input the expression:\n")

# this code can calculate the output of the 'a' and 'b'
def cal(a,b,c):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        return a/b

# this code can change the input into another form to make the calculation more convenient
def middle2behind(expression):
    result = []  # the list of output
    stack = []
    for item in expression:
        if item.isnumeric():  # put the item into result list if the item is number
            result.append(item)
        else:  # if the item is other character
            if len(stack) == 0:  # push stack if the stack is empty
                stack.append(item)
            elif item in '-*/+(':  # push stack if the item in '+-*/('
                stack.append(item)
            elif item == ')':  # pop stack if the item is ')'
                t = stack.pop()
                while t != '(':#stop pop the stack if meet the '('
                    result.append(t)
                    t = stack.pop()
    return "".join(result)

    #test01=(((2+3)*(4*5))+(1(2+3)))
    #print(middle2behind(expression))
    #the output is "23+45**123++"
    #the code have no problem

# this code can calculate the result of the formula you input just now
def cal_final(expression):
    result=[]
    list=[]
    for i in expression:
        list.append(i)

    for i in list:
        if i.isnumeric():
            result.append(i)
        else:
            a=int(result.pop())#pop the two number and calculate
            b=int(result.pop())
            new=cal(b,a,i)
            result.append(new)#push the result in stack
    res=result.pop()# finally the only one number is the result
    return res

    #test02=(((2*(3+2))+5)/2)
    #print(cal_final(middle2behind(test02)))
    # the output is 7.5 , the code can calculate the result

def visualoutput_and_writeinfile(b):
    print("the result at this time is ")
    lenth=len(b)
    counter=0
    z=open("data.txt","w")
    z.write("")
    z.close()
    for i in range(lenth):
        if b[i]=='(':
           counter+=1
        elif b[i]==')':
            counter-=1
        elif b[i] in  "+-*/":
            z = open("data.txt", "a")#this part can let the result be written into file
            z.write(" "*(counter-1)*3)
            z.write(b[i])
            z.write("\n")
            z.close()
            print(" "*(counter-1)*2, b[i])# to make the tree more visual, I print more space, but the tree can still be seen
        else:
            z = open("data.txt", "a")
            z.write(" "*counter*3)
            z.write(b[i])
            z.write("\n")
            z.close()
            print(" "*counter*2, b[i])
    #test03=((1+3)*4)
    #visualoutput_and_writeinfile(test03)
    # the out put is:
    #      1
    #    +
    #      3
    #  *
    #    4
    # the code have no problem

# this code and the next code show the judgement
def judgement(a):
    # the basic judge of the expression
    if a[0] !='(' or a[-1]!=')':
        print("please give a correct expression")
        return False
    b=len(a)
    counter_left=0
    counter_right=0
    counter_oper=0
    counter_num=0

    for i in range(b):
        if a[i]=="(":
            counter_left+=1
        elif a[i] == ")":
            counter_right+=1;
        elif a[i] in "+-*/":
            counter_oper+=1
        elif a[i] in "1234567890":
            counter_num+=1

# Three kinds of error can be found in this part of code
    if counter_right-counter_left!=0:
        print("Not a valid expression, bracket mismatched.")
        #print(counter, counter_num, counter_oper)
        return False
    elif counter_num>counter_oper+1 and counter_left>counter_oper:
        #print(counter_left, counter_num, counter_oper)
        print("Not a valid expression, operator missing.")
        return False
    elif counter_oper<counter_left:
        print("Not a valid expression, wrong number of operands.")
        return False
    else:
        return True


    #test04=(((1+3)+3)
    #print(judgement(expression))
    # The output is     Not a valid expression, bracket mismatched.
    #                   False

    #test05=((1+2)3)
    #print(judgement(expression))
    # The output is     Not a valid expression, operator missing.
    #                   False

    #test06=((3/4)*(3))
    #print(judgement(expression))
    # The output is     Not a valid expression, wrong number of operands.
    #                   False

# this part of code show the other error judgement
def judgement2(a):
    b=len(a)
    list=[]
    stack=[]
    counter=0
    counter_oper=0
    incounter=0
    for i in range(b):
        if a[i]=='(' or a[i]==')' or a[i] in '+-*/':
            list.append(a[i])
    a=''.join(list)

    for i in range(len(a)):
        #stack=[]
        if a[i]=='(' or a[i] in '+-*/':
            stack.append(a[i])
            incounter+=1
        elif a[i]==')' and stack[incounter-2]=='(' and stack[incounter-1] in '+-*/':
                stack.pop()
                stack.pop()
                incounter-=2
    # print(a)
    #print(stack)
    for i in range(len(stack)):
        if stack[i]=='(':
            counter+=1
        else:
            counter_oper+=1

    #print(counter,counter_oper)
    if stack==[]:
        return True
    elif counter<counter_oper and counter!=0:
        print("Not a valid expression, wrong number of operands.")
        return False
    elif counter==0 and counter<counter_oper:
        print("Not a valid expression, brackets mismatched.")
        return False

    # test07=(1+1+1)
    #print(judgement2(expression))
    # the output is     Not a valid expression, wrong number of operands.
    #                  False

    # test07=(3+2)/(1-4)
    #print(judgement2(expression))
    # the output is     Not a valid expression, brackets mismatched.
    #                  False

func()
if judgement(expression):
    if judgement2(expression):
        visualoutput_and_writeinfile(expression)
        behind_express = middle2behind(expression)
        print("the answer of the expression is:",cal_final(behind_express))














