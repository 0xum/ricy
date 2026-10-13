// Exercise Qt ownership of a real generic plugin through application shutdown.
#include <QApplication>
#include <QTimer>
#include <QWidget>

int main(int argc, char **argv)
{
    QCoreApplication::setApplicationName("dolphin");
    QApplication app(argc, argv);
    QWidget window;
    window.show();
    QTimer::singleShot(100, &app, &QCoreApplication::quit);
    return app.exec();
}
