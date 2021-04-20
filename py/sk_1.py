import matplotlib.pyplot as plt

s = 0.4
alpha = 0.4
g_n = 0
delta = 0.1
k_0 = 6.263
prior_list = []

prior = s * k_0 ** alpha / (1 + g_n) + (1 - delta) * k_0 / (1 + g_n)
for t in range(100):
    prior_list.append(prior)
    prior = s * prior ** alpha / (1 + g_n) + (1 - delta) * prior / (1 + g_n)

plt.plot(prior_list)
plt.title('Evolution of the capital stock in Economy 2 starting from the steady state level of capital when s = 0.3')
plt.show()

debug = 1

# end of file
