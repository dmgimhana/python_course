import decimal
from decimal import Decimal;


print(decimal.getcontext())

print(decimal.getcontext().rounding)
print(decimal.getcontext().prec)

decimal.getcontext().prec = 6

print(decimal.getcontext())

g_ctx = decimal.getcontext()
g_ctx.rounding = decimal.ROUND_HALF_UP 
# g_ctx.rounding = 'ROUND_HALF_UP' // can also be used

print(decimal.getcontext())

g_ctx.prec = 28
g_ctx.rounding = 'ROUND_HALF_EVEN'

print(decimal.getcontext())

print(type(decimal.getcontext()))

print(type(decimal.localcontext()))

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    print("#############Inside local context######################")
    print(type(ctx))
    print(ctx)
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print("###################Let's print our context###################")
    print(decimal.getcontext())
    # Get context does not always return the global context, it always return the current context
    print(id(ctx) == id(decimal.getcontext()))
    print('##########Rounding##########')
    print(round(x, 1))
    print(round(y, 1))
print(round(x, 1))
print(round(y, 1))

