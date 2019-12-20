import numpy as np

def translationMatrix(dx=0, dy=0, dz=0):
    """ Return matrix for translation along vector (dx, dy, dz). """

    return np.array([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,0],
                     [dx,dy,dz,1]])

def scaleMatrix(sx=0, sy=0, sz=0):
    """ Return matrix for scaling equally along all axes centred on the point (cx,cy,cz). """
    
    return np.array([[sx, 0,  0,  0],
                     [0,  sy, 0,  0],
                     [0,  0,  sz, 0],
                     [0,  0,  0,  1]])

def rotateXMatrix(radians):
    """ Return matrix for rotating about the x-axis by 'radians' radians """
    
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[1, 0, 0, 0],
                     [0, c,-s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])

def rotateYMatrix(radians):
    """ Return matrix for rotating about the y-axis by 'radians' radians """

    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])

def rotateZMatrix(radians):
    """ Return matrix for rotating about the z-axis by 'radians' radians """

    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[c,-s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def rotateXMatrixCentre(radians, (cx, cy, cz)):
    """ Return matrix for rotating about the x-axis by 'radians' radians """

    c = np.cos(radians)
    s = np.sin(radians)
    dy = -s*cz+(1-c)*cy
    dz = s*cy+(1-c)*cz
    return np.array([[1,  0,  0, 0],
                     [0,  c, -s, 0],
                     [0,  s,  c, 0],
                     [0, dy, dz, 1]])

def rotateYMatrixCentre(radians, (cx, cy, cz)):
    """ Return matrix for rotating about the x-axis by 'radians' radians """

    c = np.cos(radians)
    s = np.sin(radians)
    dx = -s*cz+(1-c)*cx
    dz = s*cx+(1-c)*cz
    return np.array([[ c, 0, -s, 0],
                     [ 0, 1,  0, 0],
                     [ s, 0,  c, 0],
                     [dx, 0, dz, 1]])

def rotateZMatrixCentre(radians, (cx, cy, cz)):
    """ Return matrix for rotating about the x-axis by 'radians' radians """

    c = np.cos(radians)
    s = np.sin(radians)
    dx = -s*cy+(1-c)*cx
    dy = s*cx+(1-c)*cy
    return np.array([[ c, -s, 0, 0],
                     [ s,  c, 0, 0],
                     [ 0,  0, 1, 0],
                     [dx, dy, 0, 1]])

class Wireframe:
    def __init__(self):
        self.nodes = np.zeros((0, 4))
        self.edges = []

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    def addEdges(self, edgeList):
        self.edges += edgeList

    def transform(self, matrix):
        """ Apply a transformation defined by a given matrix. """
        self.nodes = np.dot(self.nodes, matrix)

    def outputNodes(self):
        print "\n --- Nodes --- "
        for i, (x, y, z, _) in enumerate(self.nodes):
            print "   %d: (%d, %d, %d)" % (i, x, y, z)

    def outputEdges(self):
        print "\n --- Edges --- "
        for i, (node1, node2) in enumerate(self.edges):
            print "   %d: %d -> %d" % (i, node1, node2)

    def findCentre(self):
        num_nodes = len(self.nodes)
        meanX = sum([node[0] for node in self.nodes]) / num_nodes
        meanY = sum([node[1] for node in self.nodes]) / num_nodes
        meanZ = sum([node[2] for node in self.nodes]) / num_nodes
        
        return (meanX, meanY, meanZ)

if __name__ == "__main__":
    cube = Wireframe()
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube.addNodes(np.array(cube_nodes))
    
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0,8,2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])
    
    cube.outputNodes()
    cube.outputEdges()
