class Stack:
    def __init__(self, data=None):
        # 스택을 저장할 리스트 초기화
        if data is None:
            data = []
        self.data = data
        self.len=len(data)

    def push(self, x):
        """스택에 원소 x를 추가"""
        # TODO: 여기에 코드 작성
        self.data.append(x)
        self.len+=1

    def pop(self):
        """가장 위에 있는 원소를 제거하고 반환 (비어있으면 None 또는 예외 처리)"""
        # TODO: 여기에 코드 작성
        t=self.data.pop() if self.len>0 else -1
        self.len= self.len  -1 if self.len>0 else 0
        return t

    def top(self):
        """가장 위에 있는 원소를 반환 (제거하지 않음)"""
        # TODO: 여기에 코드 작성
        return self.data[-1] if self.len>0 else -1


    def empty(self):
        """스택이 비어있으면 True, 아니면 False"""
        # TODO: 여기에 코드 작성
        return 1 if self.len==0 else 0


    def size(self):
        """스택의 크기(원소 개수)를 반환"""
        # TODO: 여기에 코드 작성
        return self.len if self.len>0 else 0
    def __str__(self):
        return str(self.data)
