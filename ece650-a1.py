import sys
import copy
import re

lane = {}
vertic = []
isection = []
node = []


def validation(strn):
    check = strn.strip()
    try:
        if (check[0] == 'a'):
            obj = re.match(r'\s*[a-z]\s*["](\s*[A-z]+\s*)+["](\s*\(\s*[-]?\d+\s*\,\s*[-]?\d+\s*\)){2,}', strn)

            if (obj.end() == len(strn) - 1):
                return "true"
            else:
                return "false"

        elif (check[0] == 'c'):
            obj = re.match(r'\s*[a-z]\s*["][\w|\W]+["](\s*\(\s*[-]?\d+\s*\,\s*[-]?\d+\s*\)){2,}', strn)
            if (obj.end() == len(strn) - 1):
                return "true"
            else:
                return "false"
        elif (check[0] == 'r'):
            obj = re.match(r'\s*[a-z]\s*["](\s*[A-z]+\s*)+["]', strn)
            if (obj.end() == len(strn) - 1):
                return "true"
            else:
                return "false"
        elif (check[0] == 'g'):
            obj = re.match(r'\s*[a-z]\s*', strn)
            return "true"


    except:
        return "false"




def inputcheck(input):

    in1 = ' '.join(input.split())
    in2 = in1.split('"')
    first = in2[0].strip()
    rlt = []
    if first not in ['a', 'c', 'r', 'g', '']:
        sys.stderr.write("Error: Invalid command \n")
    if first == 'a' or first == 'c' or first == 'r':
        if len(in2) != 3:
            sys.stderr.write("Error: street name is not properly given \n")
        name = in2[1]
        if name == '':
            sys.stderr.write("Error: No street name \n")
            raise IndexError
        points = in2[2].strip()
        rlt.append(first)
        rlt.append(name)
        rlt.append(points)
    elif first == 'g':
        if len(in2) != 1:
            sys.stderr.write("Error: Invalid Input \n")
            raise IndexError
        rlt.append(first)
    return rlt




def coordextracting(str):


    rlt = []
    i = 0
    in1 = []
    in2 = []
    while str[i] != ',':
        in1.append(str[i])
        i = i + 1
    if len(in1) == 0:
        raise ValueError
    temporary1 = ''.join(in1)
    rlt.append(float(temporary1))
    i = i + 1
    while str[i] != ')':
        in2.append(str[i])
        i = i + 1
    if len(in2) == 0:
        raise ValueError
    temporary2 = ''.join(in2)
    rlt.append(float(temporary2))
    return rlt



def intersectionfun(x1, y1, x2, y2, w1, z1, w2, z2):


    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1
    a2 = z2 - z1
    b2 = w1 - w2
    c2 = a2 * w1 + b2 * z1
    slopesDif = a1 * b2 - a2 * b1
    if (slopesDif != 0):
        x = (b2 * c1 - b1 * c2) / slopesDif
        y = (a1 * c2 - a2 * c1) / slopesDif
        if x >= min([x1, x2]) and x <= max([x1, x2]) and x >= min([w1, w2]) and x <= max([w1, w2]) and y >= min(
                [y1, y2]) and y <= max([y1, y2]) and y >= min([z1, z2]) and y <= max([z1, z2]):
            return [round(x, 2), round(y, 2)]
    else:
        if (x1 == w1 and y1 == z1) or (x1 == w2 and y1 == z2):
            return [x1, y1]
        elif (x2 == w1 and y2 == z1) or (x2 == w2 and y2 == z2):
            return [x2, y2]


def printGraph(vertices, nodes):

    
    c = 0
    for e, f in vertic:
        #print str(c) + ' : (%.2f, %.2f)' % (e, f)#vertic is output
        c = c + 1
    sys.stdout.write("V {}".format(c))
    sys.stdout.write("\n")	
   



    nodeli = []
    nodeli.append("E ")
    nodeli.append('{ ')
    for i in range(0, len(nodes)):
        nodeli.append('<')
        nodeli.append(str(nodes[i][0]))
        nodeli.append(',')
        nodeli.append(str(nodes[i][1]))
        nodeli.append('>')
        if i != len(nodes) - 1:
            nodeli.append(',')
            #nodeli.append('\n')

    nodeli.append('}')
    sys.stdout.write(''.join(nodeli))#
    sys.stdout.write("\n")	
    sys.stdout.flush()

def commandA():

    if lane.has_key(valinput[1].lower()):
        sys.stderr.write("Error: street already exists\n")


    else:
        temporary = valinput[2]
        coordn = ''.join(temporary.split())
        # pointsError(points + '\n')
        twocoordn = coordn.split('(')
        if len(twocoordn) < 3:
            sys.stderr.write("Error: Invalid Input \n")

        finalcoord = []
        for i in range(1, len(twocoordn)):
            finalcoord.append(coordextracting(twocoordn[i]))

        for i in range(1, len(finalcoord)):
            if finalcoord[i] == finalcoord[i - 1]:
                sys.stderr.write("Error: Invalid input- Same coordinates for a single street\n")
                raise IndexError

        lane[valinput[1].lower()] = finalcoord

def CommandC():
    if lane.has_key(valinput[1].lower()):
        temporary = valinput[2]
        coordn = ''.join(temporary.split())
        # pointsError(points + '\n')
        twocoordn = coordn.split('(')

        if len(twocoordn) < 3:
           sys.stderr.write("Error: Invalid input \n")

        finalcoord = []
        for i in range(1, len(twocoordn)):
            finalcoord.append(coordextracting(twocoordn[i]))

        for i in range(1, len(finalcoord)):
            if finalcoord[i] == finalcoord[i - 1]:
                sys.stderr.write("Error:Invalid input- Same coordinates for a single street\n")
                raise IndexError

        lane[valinput[1].lower()] = finalcoord

    else:
      sys.stderr.write("Error: street does not exist to add please use command a instead of c")


def CommandR():

    if valinput[2] != '':
        sys.stderr.write("Error: Invalid input \n")
    elif lane.has_key(valinput[1].lower()) == True:
        del lane[valinput[1].lower()]
    else:
        sys.stderr.write("Error: street does not exist \n ")



while True:
    try:
        input = sys.stdin.readline()#input
        valinput = inputcheck(input)#valinput
        s = validation(input)
        if(s=="true"):
            if valinput[0] == 'a':
                commandA()


            elif valinput[0] == 'c':
                CommandC()



            elif valinput[0] == 'r':
                CommandR()


            elif valinput[0] == 'g':
                vertic = []
                node = []
                isection = []
                edg = []
                temporary = lane.values()
                edg = copy.deepcopy(lane.values())
                for i in range(0, len(edg)):
                    edg[i].append('\n')

                for i in range(0, len(temporary)):
                    for j in range(i + 1, len(temporary)):
                        k = 0
                        while k < (len(temporary[i]) - 1):
                            l = 0
                            while l < (len(temporary[j]) - 1):
                                inters = intersectionfun(temporary[i][k][0], temporary[i][k][1], temporary[i][k + 1][0],
                                                            temporary[i][k + 1][1], temporary[j][l][0], temporary[j][l][1],
                                                            temporary[j][l + 1][0], temporary[j][l + 1][1])
                                if inters != None:
                                    if inters not in isection:
                                        isection.append(inters)
                                    q = edg[i].index(temporary[i][k])
                                    z = edg[j].index(temporary[j][l])
                                    while edg[i][q + 1] != '\n':
                                        if min([edg[i][q][0], edg[i][q + 1][0]]) <= inters[0] <= max(
                                                [edg[i][q][0], edg[i][q + 1][0]]) and min(
                                                [edg[i][q + 1][1], edg[i][q][1]]) <= inters[1] <= max(
                                                [edg[i][q][1], edg[i][q + 1][1]]):
                                            if edg[i][q] != inters and edg[i][q + 1] != inters:
                                                edg[i].insert(q + 1, inters)
                                            break
                                        q = q + 1
                                    while edg[j][z + 1] != '\n':
                                        if min([edg[j][z + 1][0], edg[j][z][0]]) <= inters[0] <= max(
                                                [edg[j][z][0], edg[j][z + 1][0]]) and min(
                                                [edg[j][z + 1][1], edg[j][z][1]]) <= inters[1] <= max(
                                                [edg[j][z][1], edg[j][z + 1][1]]):
                                            if edg[j][z] != inters and edg[j][z + 1] != inters:
                                                edg[j].insert(z + 1, inters)
                                            break
                                        z = z + 1
                                l = l + 1
                            k = k + 1
                # find nodes and vertices
                vertic = copy.deepcopy(isection)
                for x in isection:
                    for i in range(0, len(edg)):
                        for j in range(0, len(edg[i]) - 1):
                            if x == edg[i][j]:
                                a = vertic.index(x)
                                if j - 1 >= 0:
                                    if edg[i][j - 1] != '\n':
                                        if edg[i][j - 1] not in vertic:
                                            vertic.append(edg[i][j - 1])
                                        b = vertic.index(edg[i][j - 1])
                                        minab = min(a, b)
                                        maxab = max(a, b)
                                        if [minab, maxab] not in node:
                                            node.append([minab, maxab])
                                if j + 1 < len(edg[i]):
                                    if edg[i][j + 1] != '\n':
                                        if edg[i][j + 1] not in vertic:
                                            vertic.append(edg[i][j + 1])
                                        c = vertic.index(edg[i][j + 1])
                                        minac = min(a, c)
                                        maxac = max(a, c)
                                        if [minac, maxac] not in node:
                                            node.append([minac, maxac])

                # print vertices and nodes

                printGraph(vertic, node)

        else:
            sys.stderr.write("Error:Wrong format\n")



    except EOFError:
        break
    except IndexError:
        pass
    except (RuntimeError, TypeError, NameError):
        pass
