import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.3

import "Components"
import "Consts"
 
ApplicationWindow{
    visible: true;
    width: 1280;
    height: 720

    Images { id: images }

        ImageComponent {
        source: images.folderOpen
        width: 30
        height: 30
    }
}