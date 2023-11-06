class SeatManager:

    def __init__(self, n: int):
        self.l = [i for i in range(1, n+1)]
        print(self.l)
        

    def reserve(self) -> int:
        temp = self.l.pop(0)
        return temp
        

    def unreserve(self, seatNumber: int) -> None:
        n = len(self.l)
        flag = 0
        for i in range(n):
            if self.l[i] > seatNumber:
                self.l.insert(i, seatNumber)
                flag = 1
                break
        if flag == 0:
            self.l.append(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)