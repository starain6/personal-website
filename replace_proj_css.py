# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到项目CSS区块的起始和结束行号（0-indexed）
# 起始: line 553 (1-indexed: 554) = "    /* ═══════...PRO... */
# 结束: line 693 (1-indexed: 694) = "    }" (最后一个响应式块的结束)
# 实际结束位置在 @media (max-width: 900px) 块结束后

start = None
end = None

for i, line in enumerate(lines):
    if 'PROJ' in line or 'Carousel' in line or 'proj-gallery-wrap' in line:
        if start is None:
            # 往前找到注释开始行
            for j in range(i, -1, -1):
                if 'PROJ' in lines[j] or '══' in lines[j]:
                    start = j
                    break
            if start is None:
                start = i
    # 找到 @media (max-width: 900px) 中 proj-nav-next 后的第一个非proj相关}
    # 更简单：找到 694 行附近的 }

# 直接用精确行号（从上面读取结果得知）
# 起始行: 553 (0-indexed) = "    /* ═...PRO..."
# 结束行: 693 (0-indexed) = "    }" (最后一个响应式)

# 重新找：找到 proj-gallery-wrap 的 { 到下一个同级 section 的 CSS 之前
for i, line in enumerate(lines):
    if 'proj-gallery-wrap' in line and start is None:
        # 往前找注释开始
        for j in range(i-1, -1, -1):
            if '══' in lines[j] and 'PROJ' in lines[j]:
                start = j
                break
        if start is None:
            start = i
        print(f"Start line: {start+1}: {lines[start].strip()}")
        break

# 找结束：从 start 往后找到 edu-list 之前
for i in range(start+1, len(lines)):
    if 'EDUCATION' in lines[i] or 'edu-list' in lines[i]:
        end = i
        print(f"End line: {end+1}: {lines[end].strip()}")
        break

print(f"Replacing lines {start+1} to {end}")
