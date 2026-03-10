class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
                continue

            elif bill == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
                continue

            else:
                if tens >= 1 and fives >= 1:
                    fives -= 1
                    tens -= 1
                    continue

                elif fives >= 3:
                    fives -= 3
                    continue
                
                else:
                    return False
        
        return True


            
            