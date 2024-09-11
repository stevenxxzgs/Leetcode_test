
# kmp 学习
# 前缀函数定义 pi ATAATA的pi是3，ATAAT的pi是2，ATAA的pi是1
# 1. 直接从第i位开始判断，i-1的pi都已经填好
'''
for i in range(len(str)):
    len = pi[i-1]
    if( str[i] == str[len] ):
        pi[i] = len + 1
''' 
# 2. 如果是str[i] != str[len]的情况，就进行第二长的pi
'''
for i in range(len(str)):
    len = pi[i-1]
    if (str[i] != str[len] ):
        len = pi_2nd(i-1)
        if ( str[i] == str[len] ):
'''
# 3. 如果第二长的pi还是让str[i] != str[len]，就继续找第三长的
'''
for i in range(len(str)):
    len = pi[i-1]
    if (str[i] != str[len] ):
        len = pi_2nd(i-1)
    if (str[i] != str[len] ): 
        len = pi_3rd(i-1)
        ...
'''
# 4. 合并这个循环处理，就会变成
'''
for i in range(len(str)):
    len = pi[i-1]
    while(str[i] != str[len]):
        len = pi_next(i-1)
'''
# 5. 这里还有一个情况，就是len不能小于零了
'''
for i in range(len(str)):
    len = pi[i-1]
    while( len != 0 and str[i] != str[len]):
        len = pi_next(i-1)
'''
# 6. 就剩最后一步，怎么求pi_next，
# 这里是根据前缀函数的定义，len本身往前移一位，对应的pi
'''
for i in range(len(str)):
    len = pi[i-1]
    while( len != 0 and str[i] != str[len]):
        len = pi(len-1)
    if( str[i] == str[len] ):
        pi[i] = len + 1
'''