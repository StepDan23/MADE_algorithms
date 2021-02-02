_A_COEF = 2 ** 16
_B_COEF = 2 ** 30


def get_cum_sum_arr(size, first_elem, x, y):
    arr = [0 for _ in range(size)]
    arr[0] = first_elem
    prev_val = first_elem
    for i in range(1, size):
        cur_val = (x * prev_val + y) % _A_COEF
        arr[i] = arr[i - 1] + cur_val
        prev_val = cur_val
    return arr


n_elements, x, y, a_0 = map(int, input().split())
m_queries, z, t, b_0 = map(int, input().split())
cum_sum_arr = get_cum_sum_arr(n_elements, a_0, x, y)


def rsq(left_index, right_index):
    if left_index == 0:
        return cum_sum_arr[right_index]
    return cum_sum_arr[right_index] - cum_sum_arr[left_index - 1]


prev_b = (z * b_0 + t) % _B_COEF
ans = rsq(*sorted([b_0 % n_elements, prev_b % n_elements]))
for _ in range(1, m_queries):
    left = (z * prev_b + t) % _B_COEF
    right = (z * left + t) % _B_COEF
    prev_b = right
    ans += rsq(*sorted([left % n_elements, right % n_elements]))
print(ans)

# входные данныеСкопировать
# 3 1 2 3
# 3 1 -1 4
# выходные данныеСкопировать
# 23
