b1_pages = int(input())
b1_lines = int(input())
b2_pages = int(input())
b2_lines = int(input())
r_speed = int(input())
w_speed = int(input())
time_give = int(input())


b1_all_lines = b1_lines * b1_pages
b2_all_lines = b2_lines * b2_pages

r_time = b1_all_lines / r_speed
w_ti = b2_all_lines / w_speed
w_time = r_time + w_ti

action = ""
if 0 <= time_give <= r_time :
    action = "READ"
    lines_read = (r_speed * time_give)
    page_read = int( lines_read // b1_lines )
    line_n = int( lines_read % b1_lines )
    if line_n ==0:
        line_n = b1_lines
    print(f'{action} {page_read} {line_n}')
elif w_time >= time_give > r_time :
    action = "WRITE"
    lines_written = (w_speed * (time_give - r_time))
    page_written = int (lines_written // b2_lines)
    line_n = int( lines_written % b2_lines )
    if line_n == 0:
        line_n = b2_lines
    print(f'{action} {page_written} {line_n}')
else:
    action = "not writing nor reading"




