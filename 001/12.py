s = '0' + '212121212212112111212121221212121212121' + '0'
print(s)
while '00' not in s:
    s = s.replace('021', '102', 1)
    s = s.replace('022', '301', 1)
    s = s.replace('02', '20', 1)
    s = s.replace('01', '10', 1)

cnt1 = s.count('1')
cnt2 = s.count('2')
cnt3 = s.count('3')
# if cnt1 == 27 or cnt2 == 9 or cnt3 == 4:
print(s)
print(cnt1, cnt2, cnt3)
