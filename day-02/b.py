def is_safe(sequence):
    if len(sequence) < 2:
        return True
    
    increasing = all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))
    decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))

    if not increasing and not decreasing:
        return False

    for i in range(1, len(sequence)):
        diff = abs(sequence[i] - sequence[i-1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def can_become_safe_by_removal(sequence):
    for i in range(len(sequence)):
        new_sequence = sequence[:i] + sequence[i+1:]
        
        if is_safe(new_sequence):
            return True
    return False

def check_report(sequence):
    if is_safe(sequence):
        return 1
    elif can_become_safe_by_removal(sequence):
        return 1
    else:
        return 0

lst = []
with open("data.txt") as f:
    for item in f:
        lst.append(list(map(int, item.split(" "))))
del f

result = 0
for index, seq in enumerate(lst): 
    print(f"{index}->{check_report(seq)}")
    result += check_report(seq)

print(result)