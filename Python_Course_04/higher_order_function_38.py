# def divisor(x):
#     def divident(y):
#         return y / x
#     return divident
#
# divide = divisor(3)
# print(divide(9))

def small(y):
    def larger(x):
        return x - y
    return larger

minus = small(3)
print(minus(10))
