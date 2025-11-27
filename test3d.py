from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Hazır panda modelini yükle
        panda = self.loader.loadModel("panda")   # Panda3D ile birlikte gelir
        panda.reparentTo(self.render)
        panda.setScale(0.08)   # model çok büyük, küçült
        panda.setPos(0, 10, 0)  # kameranın önüne koy

        self.panda = panda
        self.taskMgr.add(self.spinPanda, "SpinPandaTask")

        # Kamerayı ayarla
        self.camera.setPos(0, -20, 5)
        self.camera.lookAt(0, 0, 0)

    def spinPanda(self, task):
        angle = task.time * 50
        self.panda.setHpr(angle, 0, 0)
        return task.cont

app = MyApp()
app.run()