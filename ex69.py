# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    for i in range(len(moves)):
        for j in range(0, len(board)):
            if board[j][moves[i] - 1] != 0:
                if len(stack) != 0 and stack[-1] == board[j][moves[i] - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
            else:
                continue
        
    return answer