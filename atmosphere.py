h = [0, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 14000, 16000, 180000, 20000, 24000, 28000, 32000, 36000, 40000, 50000, 60000, 80000, 100000, 150000, 200000

p = [1.225, 1.1673, 1.1117, 1.0581, 1.0065, 0.9569, 0.9093, 0.8194, 0.7365, 0.6601, 0.59, 0.5258, 0.4671, 0.4135, 0.3648, 0.3119, 0.2279, 0.1665, 0.1216, 0.0889, 0.0469, 0.0251, 0.0136, 7.26 * 10**(-3), 4 * 10**(-3), 1.03 * 10**(-3), 3 * 10**(-4), 1.85 * 10**(-5), 5.55 * 10**(-7), 2 * 10**(-9), 2.52 * 10**(-10)]
     
def get_atmospheric_density(height):
     
    if height >= 200000:
        return 0
    else:
        i = 0
        while height >= h[i]:
            i +=1
        return p[i-1] + (p[i] - p[i-1]) / (h[i] - h[i-1]) * (height - h[i-1])
