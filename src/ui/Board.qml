import QtQuick 2.15


function isBlack(index){
    return (index % 2 == 0 && index %8 == 0) || (index % 2 == 1 && index %8 == 1)
}
