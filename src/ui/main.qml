import QtQuick 2.15
import QtQuick.Controls 2.15


function isBlack(index){
    return (index % 2 == 0 && index %8 == 0) || (index % 2 == 1 && index %8 == 1)
}

Window {
    visible: true
    width: 600
    height: 500
    title: "Chess"
    // Board form board.qml
    Rectangle {
        width: 400; height: 400; color: "black"

        Grid {
            x: 8; y: 8
            rows: 8; columns: 8;

            Repeater { model: 64
               Rectangle {
                    width: 50; height: 50
                    color: Board.isBlack(index)  ? "black" : "white"
               }
            }
        }
    }
}

