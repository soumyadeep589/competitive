'''
def main():
    n = 5
    x = 4
    z = 3 * x * x + 2 * x + 4 // x + 8  # Use integer division // 48 + 8 + 1 + 8  = 65
    
    for c in range(1, n + 1): # 1 to 5
        for k in range(1, c + 1): 
            print(chr(z), end='')
            z += 1
        print("\n")

if __name__ == "__main__":
    main()

A
B C
D E F
G H I J
K L M N O

'''

'''
Write a query to change the table accordingly

weight
5.67
34.567
365.253
34

weight	kg	gms
5.67	5	67
34.567	34	567
365.253	365	253
34	34	0

-- Add new columns
ALTER TABLE weights
ADD COLUMN kg INT,
ADD COLUMN gms INT;

-- Update the new columns with calculated values
UPDATE weights
SET 
    kg = FLOOR(weight),
    gms = ROUND((weight - FLOOR(weight)) * 1000);

'''

def main():
    n = 5
    x = 4
    z = 3 * x * x + 2 * x + 4 // x + 8  # Use integer division // 48 + 8 + 1 + 8  = 65
    
    for c in range(1, n + 1): # 1 to 5
        for k in range(1, c + 1): 
            print(chr(z), end='')
            z += 1
        print("\n")

if __name__ == "__main__":
    main()

