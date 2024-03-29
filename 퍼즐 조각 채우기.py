# 문제 설명
# 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. 게임 보드와 테이블은 모두 각 칸이 1x1 크기인 정사각 격자 모양입니다. 이때, 다음 규칙에 따라 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈칸에 채우면 됩니다.

# 조각은 한 번에 하나씩 채워 넣습니다.
# 조각을 회전시킬 수 있습니다.
# 조각을 뒤집을 수는 없습니다.
# 게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.
# 다음은 퍼즐 조각을 채우는 예시입니다.

# puzzle_5.png

# 위 그림에서 왼쪽은 현재 게임 보드의 상태를, 오른쪽은 테이블 위에 놓인 퍼즐 조각들을 나타냅니다. 테이블 위에 놓인 퍼즐 조각들 또한 마찬가지로 [상,하,좌,우]로 인접해 붙어있는 경우는 없으며, 흰 칸은 퍼즐이 놓이지 않은 빈 공간을 나타냅니다. 모든 퍼즐 조각은 격자 칸에 딱 맞게 놓여있으며, 격자 칸을 벗어나거나, 걸쳐 있는 등 잘못 놓인 경우는 없습니다.

# 이때, 아래 그림과 같이 3,4,5번 조각을 격자 칸에 놓으면 규칙에 어긋나므로 불가능한 경우입니다.

# puzzle_6.png

# 3번 조각을 놓고 4번 조각을 놓기 전에 위쪽으로 인접한 칸에 빈칸이 생깁니다.
# 5번 조각의 양 옆으로 인접한 칸에 빈칸이 생깁니다.
# 다음은 규칙에 맞게 최대한 많은 조각을 게임 보드에 채워 넣은 모습입니다.

# puzzle_7.png

# 최대한 많은 조각을 채워 넣으면 총 14칸을 채울 수 있습니다.

# 현재 게임 보드의 상태 game_board, 테이블 위에 놓인 퍼즐 조각의 상태 table이 매개변수로 주어집니다. 규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ game_board의 행 길이 ≤ 50
# game_board의 각 열 길이 = game_board의 행 길이
# 즉, 게임 보드는 정사각 격자 모양입니다.
# game_board의 모든 원소는 0 또는 1입니다.
# 0은 빈칸, 1은 이미 채워진 칸을 나타냅니다.
# 퍼즐 조각이 놓일 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
# table의 행 길이 = game_board의 행 길이
# table의 각 열 길이 = table의 행 길이
# 즉, 테이블은 game_board와 같은 크기의 정사각 격자 모양입니다.
# table의 모든 원소는 0 또는 1입니다.
# 0은 빈칸, 1은 조각이 놓인 칸을 나타냅니다.
# 퍼즐 조각은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
# game_board에는 반드시 하나 이상의 빈칸이 있습니다.
# table에는 반드시 하나 이상의 블록이 놓여 있습니다.
# 입출력 예
# game_board	table	result
# [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	14
# [[0,0,0],[1,1,0],[1,1,1]]	[[1,1,1],[1,0,0],[0,0,0]]	0
# 입출력 예 설명
# 입출력 예 #1

# 입력은 다음과 같은 형태이며, 문제의 예시와 같습니다.

# puzzle_9.png

# 입출력 예 #2

# 블록의 회전은 가능하지만, 뒤집을 수는 없습니다.

# python
from collections import deque

d = [[-1,0],[0,1],[1,0],[0,-1]]

def spin(block): #puzzle조각 90도 돌리기
	spin_block = [[0]*len(block) for _ in range(len(block[0]))]
	for row in range(len(block)):
		for col in range(len(block[0])):
			spin_block[col][len(spin_block[0])-1-row] = block[row][col]
	return spin_block

def catch_piece(table,row,col): #table로 puzzle조각 추출
	R,C = len(table),len(table)
	piece = [[0]*C for _ in range(R)]
	piece[row][col] = 1
	q = deque([[row,col]])
	while q:
		r,c = q.popleft()
		piece[r][c] = 1
		table[r][c] = 0
		for i in d:
			dr,dc = i
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if table[r+dr][c+dc] == 1:
					table[r+dr][c+dc] = 0
					piece[r+dr][c+dc] = 1
					q.append([r+dr,c+dc])

	r_piece = []
	for i in piece: #가로 0제거
		if sum(i) != 0:
			r_piece.append(i)

	r_piece = spin(r_piece)
	c_piece = []
	for i in r_piece: #세로 0제거
		if sum(i) != 0:
			c_piece.append(i)

	return c_piece,table

def compare(game_board,piece,row,col): #row col기준 game board에서 piece랑 비교
	R,C = len(game_board),len(game_board)
	cnt = 0
	for r in range(len(piece)):
		for c in range(len(piece[0])):
			if piece[r][c] == 1 and game_board[row+r][col+c] == 2:
				cnt += 1
			elif piece[r][c] == 0 and game_board[row+r][col+c] == 1:
				continue
			else:
				return 0
	return cnt


def solution(game_board,table):
	answer = 0
	piece = deque()
	R,C = len(game_board),len(game_board)
	for row in range(R):
		for col in range(C):
			if table[row][col] == 1:
				p,table=catch_piece(table,row,col)
				piece.append(p)

	for row in range(R): 			#game board 시작 rowc ol
		for col in range(C):
			if game_board[row][col] == 0:
				q = deque([[row,col]])
				min_row,max_row = row,row
				min_col,max_col = col,col
				while q:	#빈칸 추출
					r,c = q.popleft()
					game_board[r][c] = 2
					for i in d:
						dr,dc = i
						if 0 <= r+dr < R and 0 <= c+dc < C:
							if game_board[r+dr][c+dc] == 0:
								q.append([r+dr,c+dc])
								min_row,max_row = min(min_row,r+dr),max(max_row,r+dr)
								min_col,max_col = min(min_col,c+dc),max(max_col,c+dc)
								game_board[r+dr][c+dc] = 2

				result = 0
				for p in range(len(piece)): #빈칸 puzzle조각과 비교
					for _ in range(4):
						if piece[p][0][0] == -1:
							break
						if len(piece[p]) == max_row-min_row+1 and len(piece[p][0]) == max_col-min_col+1:
							result = compare(game_board,piece[p],min_row,min_col)

							if result > 0:
								answer += result
								piece[p][0][0] = -1
								break
						piece[p] = spin(piece[p])
					if result > 0:
						break

	return answer