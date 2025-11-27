import cv2
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Texture, CardMaker

class ARApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cap = cv2.VideoCapture(1)

        ret, frame = self.cap.read()
        if not ret:
            print("Kamera acilmadi.")
            exit()

        h, w, c = frame.shape

        # Texture boyutlarını ve formatını BGR olarak ayarla
        self.tex = Texture("camera")
        self.tex.setup2dTexture(w, h, Texture.T_unsigned_byte, Texture.F_rgb8)
        cm = CardMaker("bg")
        cm.setFrameFullscreenQuad()
        card = self.render2d.attachNewNode(cm.generate())
        card.setTexture(self.tex)

        self.taskMgr.add(self.updateCamera, "UpdateCamera")

    def updateCamera(self, task):
        ret, frame = self.cap.read()
        if ret:
            # Görüntüyü ters çevirmek gerekirse flip uygula
            frame = cv2.flip(frame, 0)  # 0 → dikey ters çevir
            # BGR formatında doğrudan aktar
            self.tex.setRamImage(frame)
        return task.cont

ARApp().run()