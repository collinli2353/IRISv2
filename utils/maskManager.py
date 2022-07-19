from collections import deque

class maskManager():

    def __init__(self, max_saves=30):
        self.mask_queue = deque([])
        self.p = -1
        self.max_saves = max_saves

    def updateNewChange(self, new_msk):
        q_len = len(self.mask_queue)
        if q_len == self.max_saves:
            self.mask_queue.popleft()
            self.p -= 1
            q_len -= 1

        # current mask is at the right most of the queue
        if self.p == (q_len - 1):
            self.mask_queue.append(new_msk.copy())
            self.p += 1
        elif self.p > (q_len - 1):
            print("---->>>> Error: mask pointer is outside the queue")
            self.p = (q_len - 1)
        elif self.p < (q_len - 1):
            while (self.p < (q_len - 1)):
                self.mask_queue.pop()
                q_len = len(self.mask_queue)
            self.mask_queue.append(new_msk.copy())
            self.p += 1

        print('---->>>> Update: Queue length {} p position {}'.format(len(self.mask_queue), self.p))

    def undoMaskChange(self, old_mask):
        if self.p == 0:
            pre_mask = self.mask_queue[self.p]
        elif self.p < 0:
            pre_mask = old_mask
        elif self.p > 0:
            self.p -= 1
            pre_mask = self.mask_queue[self.p]

        print('---->>>> Undo: Queue length {} p position {}'.format(len(self.mask_queue), self.p))

        return pre_mask.copy()

    def redoMaskChange(self, old_mask):
        q_len = len(self.mask_queue)

        if self.p >= q_len-1:
            pre_mask = old_mask
        elif self.p < q_len-1:
            self.p += 1
            pre_mask = self.mask_queue[self.p]

        print('---->>>> Init: Queue length {} p position {}'.format(len(self.mask_queue), self.p))

        return pre_mask.copy()

    def initNewQueue(self, msk):
        self.mask_queue.clear()
        self.mask_queue.append(msk.copy())
        self.p = 0
        print('---->>>> Init: Queue length {} p position {}'.format(len(self.mask_queue), self.p))

    def print(self):
        print(self.mask_queue)
