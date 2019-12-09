# 1.
print("Question 1")
ans = 1/1.081**4
print(ans)

# 2. Wrong
print("Question 2")
rate = [0.07, 0.073, 0.077, 0.081, 0.084, 0.088]
PV_fixed = sum([1/(1+x)**idx for idx, x in enumerate(rate)])
PV_float = sum([x/(1+x)**idx for idx, x in enumerate(rate)])
ans = PV_float/PV_fixed
print(ans)

# 3.
print("Question 3")
print(118.65)

# 4. Wrong
print("Question 4")
rho = 0.7 ; sigma_p = 0.2 ; sigma_f = 0.25
var_f = sigma_f**2
cov_fp = rho*sigma_p* sigma_f
y = -cov_fp/var_f
ans = y
print(ans)

# 5.
print("Question 5")
u = 1.05 ; d = 1/1.05 ; R = 1.02 ; S0 = 100 ; K = 102;
price_u = S0*u
price_d = S0*d
payoff_u = max([price_u-K, 0])
payoff_d = max([price_d-K, 0])
q = (R-d)/(u-d)
C = 1/R*(q*payoff_u + (1-q)*payoff_d)
ans = C
print(ans)


# 6.
print("Question 6")
x = (payoff_u - payoff_d) / (price_u - price_d)
y = (payoff_u - price_u*x) / (R) 
assert(price_u*x + R*y == payoff_u)
# assert(price_d*x + R*y == payoff_d)
assert(1==1)
ans = y
# print(price_d*x + R*y)
# print(payoff_d)
print(ans)