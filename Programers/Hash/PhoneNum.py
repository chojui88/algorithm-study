def solution(phone_book):
    phone_book = set(phone_book)
    for i in phone_book:
        number = ""
        
        for j in i:
            number += j
            if number in phone_book  and number != i:
                return False
                    
    return True
        
