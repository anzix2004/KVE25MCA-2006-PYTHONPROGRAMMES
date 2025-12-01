m_list = []
n = int(input("Enter the limit: "))
i = 0

while i < n:
    m = int(input("Enter the numbers: "))
    if m < 100:
        m_list.append(m)
    else:
        m_list.append("Over")
    i += 1

print("List:", m_list)