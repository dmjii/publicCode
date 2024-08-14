function playGame(){
    //player one gets a random value
    var playerOne = Math.random();
    playerOne = Math.floor((playerOne * 6) + 1);
    if (playerOne === 1){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice1.png")
    }
    if (playerOne === 2){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice2.png")
    }
    if (playerOne === 3){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice3.png")
    }
    if (playerOne === 4){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice4.png")
    }
    if (playerOne === 5){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice5.png")
    }
    if (playerOne === 6){
        document.querySelector(".img1").setAttribute("src", "\\images\\dice6.png")
    }

    //player two gets a random value
    var playerTwo = Math.random();
    playerTwo = Math.floor((playerTwo * 6) + 1);
    if (playerTwo=== 1){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice1.png")
    }
    if (playerTwo === 2){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice2.png")
    }
    if (playerTwo === 3){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice3.png")
    }
    if (playerTwo === 4){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice4.png")
    }
    if (playerTwo === 5){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice5.png")
    }
    if (playerTwo === 6){
        document.querySelector(".img2").setAttribute("src", "\\images\\dice6.png")
    }

    //determine a winner
    if (playerOne === playerTwo){
        document.querySelector("h1").textContent = "It's a draw!";
    } else{
        if (playerOne > playerTwo){
            document.querySelector("h1").textContent = "Player 1 Wins!";
        } else{
                document.querySelector("h1").textContent = "Player 2 Wins!";
        }
    }
}
document.querySelector("#clickme").addEventListener("click", playGame);