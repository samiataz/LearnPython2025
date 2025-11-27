from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeomVertexFormat, GeomVertexData, Geom, GeomNode
from panda3d.core import GeomTriangles, GeomVertexWriter

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Kamerayı ayarla
        self.camera.setPos(0, -6, 2)
        self.camera.lookAt(0, 0, 0)

        # Vertex formatı
        format = GeomVertexFormat.getV3()
        vdata = GeomVertexData("cube", format, Geom.UHStatic)

        # 8 köşe tanımla
        vertex = GeomVertexWriter(vdata, "vertex")
        points = [
            (-1, -1, -1),
            ( 1, -1, -1),
            ( 1,  1, -1),
            (-1,  1, -1),
            (-1, -1,  1),
            ( 1, -1,  1),
            ( 1,  1,  1),
            (-1,  1,  1),
        ]
        for p in points:
            vertex.addData3f(*p)

        # Üçgenler (12 tane)
        tris = GeomTriangles(Geom.UHStatic)
        faces = [
            (0,1,2), (0,2,3),   # alt
            (4,5,6), (4,6,7),   # üst
            (0,1,5), (0,5,4),   # ön
            (2,3,7), (2,7,6),   # arka
            (1,2,6), (1,6,5),   # sağ
            (0,3,7), (0,7,4),   # sol
        ]
        for f in faces:
            tris.addVertices(*f)

        # Geometriyi oluştur
        geom = Geom(vdata)
        geom.addPrimitive(tris)
        node = GeomNode("cube")
        node.addGeom(geom)

        # Sahneye ekle
        self.cube = self.render.attachNewNode(node)
        self.cube.setColor(1, 0, 0, 1)   # kırmızı
        self.cube.setScale(0.5)

        # Döndürme task'i
        self.taskMgr.add(self.spinCube, "SpinCubeTask")

    def spinCube(self, task):
        angle = task.time * 50
        self.cube.setHpr(angle, angle, 0)
        return task.cont

app = MyApp()
app.run()