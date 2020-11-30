def get_atmospheric_density(height):

    if height <= 500:
        return 1.2250
    elif height <= 1000:
        return 1.1673
    elif height <= 1500:
        return 1.1117
    elif height <= 2000:
        return 1.0581
    elif height <= 2500:
        return 1.0065
    elif height <= 3000:
        return 0.9569
    elif height <= 4000:
        return 0.9093
    elif height <= 5000:
        return 0.8194
    elif height <= 6000:
        return 0.7365
    elif height <= 7000:
        return 0.6601
    elif height <= 8000:
        return 0.59
    elif height <= 9000:
        return 0.5258
    elif height <= 10000:
        return 0.4671
    elif height <= 11000:
        return 0.4135
    elif height <= 12000:
        return 0.3648
    elif height <= 14000:
        return 0.3119
    elif height <= 16000:
        return 0.2279
    elif height <= 18000:
        return 0.1665
    elif height <= 20000:
        return 0.1216
    elif height <= 24000:
        return 0.0889
    elif height <= 28000:
        return 0.0469
    elif height <= 32000:
        return 0.0251
    elif height <= 36000:
        return 0.0136
    elif height <= 40000:
        return 7.26 * 10**(-3)
    elif height <= 50000:
        return 4.00 * 10**(-3)
    elif height <= 60000:
        return 1.03 * 10**(-3)
    elif height <= 80000:
        return 3.00 * 10**(-4)
    elif height <= 100000:
        return 1.85 * 10**(-5)
    else:
        return 0
