
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for x in [c for c in coinValueList if c <=cents]:
            if minCoins[cents - x] + 1 < coinCount:
                coinCount = minCoins[cents - x] + 1
                newCoin = x
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins
def printresult(change,minCoins,coinsUsed):
    for x in range(1,change+1):
        info = "{} must need {} coins :"
        print(info.format(x,minCoins[x]),end=" ")
        while x > 0:
            thisCoin = coinsUsed[x]
            print(thisCoin,end = " ")
            x = x - thisCoin
            
        print("")

def main():
    coinValueList = [1,5,10,19,25]
    minCoins = [0] * 64
    coinsUsed =[0] * 64
    dpMakeChange(coinValueList,63,minCoins,coinsUsed)
    print(minCoins)
    print(coinsUsed)
    printresult(63,minCoins,coinsUsed)

if __name__ == '__main__':
    main()