import cv2
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Texture, CardMaker

class ARApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # USB kamera
        self.cap = cv2.VideoCapture(0)
        ret, frame = self.cap.read()
        if not ret:
            print("Kamera acilmadi.")
            exit()

        h, w, c = frame.shape

        # Texture ayarı
        self.tex = Texture("camera")
        self.tex.setup2dTexture(w, h, Texture.T_unsigned_byte, Texture.F_rgb8)

        # Kamera görüntüsünü düzleme koy
        cm = CardMaker("bg")
        cm.setFrame(-4, 4, -3, 3)
        card = self.render.attachNewNode(cm.generate())
        card.setTexture(self.tex)
        card.setPos(0, 10, 0)

        self.taskMgr.add(self.updateCamera, "UpdateCamera")

        # Küp ekle
        self.cube = self.loader.loadModel("box.egg")
        self.cube.reparentTo(self.render)
        self.cube.setScale(0.5)
        self.cube.setPos(0, 8, 0)

        # Küpü döndürme task'i
        self.taskMgr.add(self.rotateCube, "RotateCube")

    def updateCamera(self, task):
        ret, frame = self.cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb_frame = cv2.flip(rgb_frame, 0)
            self.tex.setRamImageAs(rgb_frame.tobytes(), "RGB")
        return task.cont

    def rotateCube(self, task):
        # Küpü her karede biraz döndür
        self.cube.setH(self.cube.getH() + 1)  # Heading (Y ekseni etrafında)
        self.cube.setP(self.cube.getP() + 0.5) # Pitch (X ekseni etrafında)
        self.cube.setR(self.cube.getR() + 0.2) # Roll (Z ekseni etrafında)
        return task.cont

ARApp().run()