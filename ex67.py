# [PCCE 기출문제] 9번 / 이웃한 칸

def solution(board, h, w):
    answer = 0
    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(len(dx)):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer