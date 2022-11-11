## Read data from input file
n = int(input())
record_list = []
for i in range(n):
    temp_input = input().split(' ')
    record_list.append(temp_input)
print(record_list)

# Validation
allValid = True
errorCodes = []
isValid_list = []

for record in record_list:
    # list of isValid status
    if record[1] == 'true':
        isValid_list.append(True)
    elif record[1] == 'false':
        isValid_list.append(False)

    # if false, append error to errorCodes
    if record[1]=='false':
        errorCodes.append(record[2])

if sum(isValid_list) == n:
    allValid = True
else:
    allValid = False

if allValid == True:
    print("Yes")
else:
    print("No")
    print(' '.join([str(err) for err in errorCodes]))