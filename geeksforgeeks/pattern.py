#1) Python Program to print the pattern ‘G’

def Pattern(line):
    pat=""
    for i in range(0,line):   
        for j in range(0,line):    
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))): 
                pat=pat+"*"  
            else:     
                pat=pat+" "  
        pat=pat+"\n"  
    return pat
  
# Driver Code
line = 7
print(Pattern(line))

output:

 ***  
 *     
 *     
 * *** 
 *   * 
 *   * 
  ***  


## 2)  Python Program to print an Inverted Star Pattern

n=6
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')

output:

******
 *****
  ****
   ***
    **
     *


# 3) Python Program to print double sided stair-case pattern

def pattern(n):
    for i in range(1,n+1):
        k =i + 1 if(i % 2 != 0) else i
        for g in range(k,n):
            if g>=k:
                print(end="  ")
        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")
n = 10
pattern(n)

output:

                 *   * 
                 *   * 
             *   *   *   * 
             *   *   *   * 
         *   *   *   *   *   * 
         *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 

# 4) Python Program to print with your own font

name = "GEEk"
 
length = len(name)
l = ""
 
for x in range(0, length):
    c = name[x]
    c = c.upper()
     
    if (c == "A"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "G"):
        print("..######..\n..#.......\n..#.####..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "I"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n..######..\n\n")
         
    elif (c == "J"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n..#.##....\n..####....\n\n")
         
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......", end = " ")
        print("\n..#..#....\n..#...#...\n\n")
         
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..#...##..\n\n")
         
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..######..\n\n")
         
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...", end = " ")
        print("\n..#...#...\n..#....#..\n\n")
         
    elif (c == "S"):
        print("..######..\n..#.......\n..######..", end = " ")
        print("\n.......#..\n..######..\n\n")
         
    elif (c == "T"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n...#..#...\n....##....\n\n")
         
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
        print("\n..##..##..\n..#....#..\n\n")
         
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n...#..#...\n..#....#..\n\n")
         
    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....", end = " ")
        print("\n....#.....\n..######..\n\n")
         
    elif (c == " "):
        print("..........\n..........\n..........", end = " ")
        print("\n..........\n\n")
         
    elif (c == "."):
        print("----..----\n\n")

output:

..######..
..#.......
..#.####.. 
..#....#..
..#####...


..######..
..#.......
..#####... 
..#.......
..######..


..######..
..#.......
..#####... 
..#.......
..######..


..#...#...
..#..#....
..##...... 
..#..#....
..#...#...



