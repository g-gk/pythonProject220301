# Некорректные логины
logins = input().split(',')
bad_logins = []
for login in logins:
    if not all(c.isalnum() or c == '_' for c in login):
        bad_logins.append(login)
mx = max(bad_logins, key=len, default=0)
print('\n'.join(log.rjust(len(mx)) for log in sorted(bad_logins)))
