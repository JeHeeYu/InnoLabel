import QtQuick 2.15
import QtQuick.Dialogs 1.3
import "../Components"
import "../Consts"

Item {
    id: root

    property var imageFiles: []
    property int currentIndex: 0 
    property string currentImage: "" 

    signal imageSelected(string fileUrl) 

    Images { id: images }

    Row {
        ImageComponent {
            source: images.back
            width: 30
            height: 30
            onImageClick: {
                if (currentIndex > 0) {
                    currentIndex--
                    currentImage = imageFiles[currentIndex]
                    imageSelected(currentImage)
                }
            }
        }

        ImageComponent {
            source: images.folderOpen
            width: 30
            height: 30
            onImageClick: {
                fileDialog.open()
            }
        }

        ImageComponent {
            source: images.next
            width: 30
            height: 30
            onImageClick: {
                if (currentIndex < imageFiles.length - 1) {
                    currentIndex++
                    currentImage = imageFiles[currentIndex]
                    imageSelected(currentImage)
                }
            }
        }
    }

    FileDialog {
        id: fileDialog
        title: "Select an Image Folder"
        folder: shortcuts.home
        selectFolder: true
        onAccepted: {
            imageProvider.getImageFiles(fileDialog.folder)
        }
    }

    Component.onCompleted: {
        imageProvider.imageFilesChanged.connect((files) => {
            root.imageFiles = files
            if (files.length > 0) {
                currentImage = files[0]
                imageSelected(currentImage)
            }
        })
    }
}
