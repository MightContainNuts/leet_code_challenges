#1352. Product of the Last K Numbers

class ProductOfNumbers:

    def __init__(self):
        self.results =[1]
        self.last_zero_index = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.results.append(1)
            self.last_zero_index = len(self.results) - 1
        else:
            self.results.append(num * self.results[-1])
        return None

    def getProduct(self, k: int) -> int:
        if self.last_zero_index >= len(self.results) - k:
            return 0
        return self.results[-1] // self.results[-(k + 1)]







if __name__ == '__main__':
    methods = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    params = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    results =[]
    s= ProductOfNumbers()

    for method, param in zip(methods, params):
        if method == "ProductOfNumbers":
            continue
        func = getattr(s, method)
        results.append(func(*param))



    print(s.results)
    print(results)


