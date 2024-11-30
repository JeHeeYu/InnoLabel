import QtQuick 2.15

Item {
    id: imageViewer
    property alias imagePath: image.source

    Image {
        id: image
        anchors.centerIn: parent
        fillMode: Image.PreserveAspectFit
        source: ""
        width: parent.width
        height: parent.height
    }
}
