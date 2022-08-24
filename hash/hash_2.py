def solution(phone_book):
    phone_book.sort()
    dict_ = dict()
    for i in phone_book:
        dict_[i] = 1
    
    for i in phone_book:#123 ,456 ,789
        for k in range(len(i)+1): #1, 12 ,123
            if i[:k] in dict_ and  i[:k] != i:
                return False
    return True

"""
    def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
"""