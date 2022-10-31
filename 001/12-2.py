s = '0' + '1111111211211211211211211211211222222222' + '0'
print(s)
print(s.count('2'))
while '00' not in s:
    s = s.replace('021', '102', 1)
    s = s.replace('022', '301', 1)
    s = s.replace('02', '20', 1)
    s = s.replace('01', '10', 1)
    # s = s.replace('021', '120', 1)
    # s = s.replace('022', '310', 1)
cnt1 = s.count('1')
cnt2 = s.count('2')
cnt3 = s.count('3')
print(s)
print(cnt1, cnt2, cnt3)
# 17
