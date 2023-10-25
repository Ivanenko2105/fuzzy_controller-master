function transformToBlock(circleID, blockID) {
    const circle = document.getElementById(circleID);
    const block = document.getElementById(blockID);
    circle.style.transform = 'scale(0)';
    circle.style.display = 'none';
    block.style.transform = 'scale(1)';
    block.style.display = 'flex';
}

function transformToCircle(circleID, blockID) {
    const circle = document.getElementById(circleID);
    const block = document.getElementById(blockID);
    block.style.transform = 'scale(0)';
    block.style.display = 'none';
    circle.style.transform = 'scale(1)';
    circle.style.display = 'flex';
}

// Function to check input and perform animation for circle 1
function checkInput1() {
    const input1_1 = document.getElementById("field1_1").value;
    const input1_2 = document.getElementById("field1_2").value;
    const input1_3 = document.getElementById("field1_3").value;
    const input1_4 = document.getElementById("field1_4").value;
    if (!isNaN(input1_1) && !isNaN(input1_2) && !isNaN(input1_3) && !isNaN(input1_4)) {
        document.getElementById("block1").style.display = "none";
        document.getElementById("circle1").style.display = "none";
        document.getElementById("circle2").style.display = "inline-flex";
    }
}

function changeFormStyle(blockID, circleID, buttonID) {
    const elements = Array.from(document.querySelector('#block1 input'));

    for (const i in elements)
        i.disabled = true;
    
    const block = document.getElementById(blockID);
    const circle = document.getElementById(circleID);
    const button = document.getElementById(buttonID);
    block.style.backgroundColor = "#a9e434";
    block.style.border = "1px solid #a9e434";
    circle.style.backgroundColor = "#a9e434";
    button.style.backgroundColor = "#a9e434";
    button.style.border = "#a9e434";
    button.addEventListener('mouseover', () => {
        button.style.backgroundColor = '#e8f8c6';
      });
}

// // Function to check input and perform animation for circle 2
// function checkInput2() {
//     const input2_1 = document.getElementById("field2_1").value;
//     const input2_2 = document.getElementById("field2_2").value;
//     const input2_3 = document.getElementById("field2_3").value;
//     const input2_4 = document.getElementById("field2_4").value;
//     // Add code to check the range
//     if (valid_range) {
//         document.getElementById("block2").style.display = "none";
//         document.getElementById("circle2").style.display = "none";
//         document.getElementById("circle3").style.display = "inline-flex";
//     }
// }