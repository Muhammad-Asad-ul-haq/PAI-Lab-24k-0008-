transactionLog = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'}
]

productCatalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub'
}

def ProcessTransaction(TransactionList):
    result = {}
    for t in TransactionList:
        cust = t['customerId']
        prod = t['productId']
        if cust not in result:
            result[cust] = set()
        result[cust].add(prod)
    return result

def FindFrequentPair(TransactionList):
    data = {}
    for t in TransactionList:
        cust = t['customerId']
        prod = t['productId']
        if cust not in data:
            data[cust] = set()
        data[cust].add(prod)

    pairCount = {}
    for items in data.values():
        itemsList = list(items)
        for i in range(len(itemsList)):
            for j in range(i + 1, len(itemsList)):
                a = itemsList[i]
                b = itemsList[j]
                if a > b:
                    a, b = b, a
                pair = (a, b)
                if pair in pairCount:
                    pairCount[pair] += 1
                else:
                    pairCount[pair] = 1
    return pairCount

def GetRecommendations(productId, pairs):
    rec = {}
    for pair, count in pairs.items():
        p1, p2 = pair
        if productId == p1:
            other = p2
        elif productId == p2:
            other = p1
        else:
            continue

        if other in rec:
            rec[other] += count
        else:
            rec[other] = count
    sortedRec = sorted(rec.items(), key=lambda x: x[1], reverse=True)
    return sortedRec

def GetGenerateReport(productId, recList, catalog):
    if not recList:
        print("No co-purchase data available.")
        return
    num = 1
    for pid, count in recList:
        print(num, ".", catalog.get(pid, pid), "(co-purchased", count, "times)")
        num = num + 1

result = ProcessTransaction(transactionLog)
print(result)

pairs = FindFrequentPair(transactionLog)
print(pairs)

recommend = GetRecommendations('prod_15', pairs)
print("Recommendations for prod_15:", recommend)

sample = [('prod_12', 2), ('prod_15', 2)]
GetGenerateReport('prod_12', sample, productCatalog)
