#感谢chatgpt
#我是真不会搞这些
def create_paper():
    paper_width = 60
    paper_height = 20
    
    # 创建纸的二维列表，用于存储ASCII字符
    paper = [[' ' for _ in range(paper_width)] for _ in range(paper_height)]
    
    # 添加撕过的痕迹
    for i in range(5):
        for j in range(10):
            paper[i][j] = '/'
    
    # 添加标题
    title = "不跑路协议"
    title_start_pos = (paper_width-5 - len(title)) // 2
    for i, char in enumerate(title):
        paper[8][title_start_pos+i] = char
    
    # 添加内容
    content = "不管做成什么样，不可跑路"
    content_start_pos = (paper_width-10 - len(content)) // 2
    for i, char in enumerate(content):
        paper[10][content_start_pos+i] = char
    
    # 添加署名
    signature = "2023.8.16"
    signature_pos = (paper_height - 2, paper_width - len(signature) - 2)
    for i, char in enumerate(signature):
        paper[signature_pos[0]][signature_pos[1]+i] = char
    
    # 添加颜色
    colorized_paper = colorize_paper(paper)
    
    # 打印纸
    for row in colorized_paper:
        print(''.join(row))

def colorize_paper(paper):
    # 添加颜色代码
    color_codes = {
        '/': '\033[31m',   # 撕过的痕迹 - 红色
        '不': '\033[34m',  # 内容中的字 - 蓝色
    }
    
    # 创建带有颜色的纸的二维列表
    colorized_paper = [[' ' for _ in range(len(paper[0]))] for _ in range(len(paper))]
    
    for row_idx, row in enumerate(paper):
        for col_idx, char in enumerate(row):
            if char not in color_codes:
                # 没有颜色代码的字符直接复制
                colorized_paper[row_idx][col_idx] = char
            else:
                # 添加颜色代码的字符
                colorized_paper[row_idx][col_idx] = color_codes[char] + char + '\033[0m'
    
    return colorized_paper

# 创建纸
create_paper()