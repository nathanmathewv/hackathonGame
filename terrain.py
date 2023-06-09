from mainGame import *
def makeblock(i, j, block_size):
    return Block(i*block_size, HEIGHT//2-j*block_size, block_size)

def makemap(objects, s):
    temp = [makeblock(3, 2, s ),
            makeblock(3, 3, s),
            makeblock(4, 3, s),
            makeblock(6, 4, s),
            makeblock(7, 4, s),
            makeblock(8, 4, s),
            makeblock(9, 4, s),
            makeblock(9, 5, s),
            makeblock(11, 1, s),
            makeblock(12, 1, s),
            makeblock(13, 1, s),
            makeblock(14, 1, s),
            makeblock(13, 2, s),
            makeblock(15, 3, s),
            makeblock(15, 4, s),
            makeblock(16, 3, s),
            makeblock(16, 4, s),
            makeblock(18, 3, s),
            makeblock(19, 3, s),
            makeblock(20, 3, s),
            makeblock(21, 3, s),
            makeblock(22, 3, s),
            makeblock(22, 2, s),
            makeblock(25, 3, s),
            makeblock(26, 3, s),
            makeblock(26, 4, s),
            makeblock(27, 3, s),
            makeblock(27, 4, s),
            makeblock(28, 3, s),
            makeblock(29, 3, s),
            makeblock(30, 3, s),
            makeblock(33, 4, s),
            makeblock(34, 4, s),
            makeblock(36, 3, s),
            makeblock(38, 2, s),
            makeblock(38, 5, s),
            makeblock(39, 2, s),
            makeblock(40, 3, s),
            makeblock(41, 3, s),
            makeblock(44, 3, s),
            makeblock(45, 3, s),
            makeblock(46, 3, s),
            makeblock(47, 4, s),
            makeblock(46, 4, s),
            makeblock(50, 3, s),
            makeblock(52, 5, s),
            makeblock(53, 3, s),
            makeblock(54, 3, s),
            makeblock(54, 4, s),
            makeblock(55, 3, s), 
            makeblock(55, 4, s),
            makeblock(56, 3, s),
            makeblock(57, 3, s),
            makeblock(58, 3, s),
            makeblock(58, 2, s),
            makeblock(60, 2, s),
            makeblock(60, 3, s),
            makeblock(60, 4, s),
            makeblock(60, 5, s),
            makeblock(60, 6, s),
        ]
            
    
    objects.extend(temp)

    return objects


