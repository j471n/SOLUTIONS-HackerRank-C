import statistics

class LeastSqaureRL:

    def pearson(X, Y, num):

        for i in range(len(X)):
            num += (X[i] - xMean) * (Y[i] - yMean)
        den = len(X) * statistics.pstdev(X) * statistics.pstdev(Y)
        return (num / den)

    def linearRegressor(X, Y, num, xMean, yMean):
        b = LeastSqaureRL.pearson(X, Y, num) * (statistics.pstdev(Y) / statistics.pstdev(X))
        a = yMean - (b * xMean)
        return (a, b)


if __name__ == '__main__':
    x = 80
    num = 0
    X = [95, 85, 80, 70, 60]
    Y = [85, 95, 70, 65, 70]
    xMean = statistics.mean(X)
    yMean = statistics.mean(Y)
    y = LeastSqaureRL.linearRegressor(X, Y, num, xMean, yMean)[0] + LeastSqaureRL.linearRegressor(X, Y, num, xMean, yMean)[1] * x

    print(round(y, 3))
    
    
