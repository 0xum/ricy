from PyQt6.QtWidgets import QApplication,QMenu
from PyQt6.QtCore import Qt,QTimer
app=QApplication([]);app.setApplicationName('verificar-menu-kde')
m=QMenu();sub=m.addMenu('Create New');sub.addAction('Pasta…');sub.addAction('Text File…')
for s in ['Open Folder With','Paste Clipboard Contents…','Ordenar por','Change View Mode']:m.addAction(s)
m.ensurePolished();m.show();app.processEvents()
print('Style',app.style().objectName(),'Translucent',m.testAttribute(Qt.WidgetAttribute.WA_TranslucentBackground),'font',m.font().toString(),'rects',[m.actionGeometry(a).height() for a in m.actions()],flush=True)
im=m.grab().toImage();print('corner alpha',im.pixelColor(0,0).alpha(),flush=True)
QTimer.singleShot(1000,app.quit);app.exec()
