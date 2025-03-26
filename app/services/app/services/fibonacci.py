from typing import List

class FibonacciService:
    @staticmethod
    def generate(n: int) -> List[int]:
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be non-negative integer")
        
        if n == 0:
            return []
        
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence[:n]
