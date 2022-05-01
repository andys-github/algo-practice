class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def merge_lists(head_1, head_2):
  new_list = None

  if head_1 and head_2:
    if head_1.val <= head_2.val:
      new_list = head_1
      head_1 = head_1.next
    else:
      new_list = head_2
      head_2 = head_2.next
  elif head_1:
    return head_1
  else:
    return head_2

  merge(head_1, head_2, new_list)

  return new_list


def merge(head_1, head_2, new_list):
  if new_list is None:
    return

  if head_1 and head_2:
    if head_1.val <= head_2.val:
      new_list.next = head_1
      head_1 = head_1.next
    else:
      new_list.next = head_2
      head_2 = head_2.next
  elif head_1:
    new_list.next = head_1
    return
  else:
    new_list.next = head_2
    return

  merge(head_1, head_2, new_list.next)


# ----------------- TEST 01 -------------------------------
h = Node(30)
# 30

p = Node(15)
q = Node(67)
p.next = q
# 15 -> 67

ll = merge_lists(h, p)
# 15 -> 30 -> 67

while ll is not None:
  print(ll.val)
  ll = ll.next



# ----------------- TEST 02 -------------------------------
a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(1)
r = Node(8)
s = Node(9)
t = Node(10)
q.next = r
r.next = s
s.next = t
# 1 -> 8 -> 9 -> 10

ll = merge_lists(a, q)
# 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28

while ll is not None:
  print(ll.val)
  ll = ll.next
