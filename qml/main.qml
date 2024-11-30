import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.3
import QtQuick.Dialogs 1.3

import "Components"
import "Consts"
import "Menu"
import "Viewer" 

ApplicationWindow {
    visible: true
    width: 1280
    height: 720

    Images { id: images }

    Menu {
        id: menu
        width: parent.width
        onImageSelected: {
            imageViewer.imagePath = fileUrl
        }
    }

    ImageViewer {
        id: imageViewer
        width: parent.width
        height: parent.height - menu.height
    }
}
