# Cryptid-destroyer-1000

So me and my friends got into Cryptid recently. It an amazing game, you can check it out right [here](https://www.ultraboardgames.com/cryptid/game-rules.php). The rule is simple, most importantly, this is essentially a leetcode question that is little too long.

So, I really want to destroy my friends (such as blind picking location with highest possibility of being a viable location and fuck everyone's game) I decided to make this python script

idea to solve is simple, we do a sweep algorithm through the entire map, each tile we decide how many condition it meets, and at the end tell the player which tile satisfy the most amount of condition.

There is a catch though, based on the rule for Cryptid, we will have exactly 1 block on the map that will eventually fit the requirement, that means there will be exactly 1 answer, thus a unique block that satisfy at least 4 condition, is typically more favoured than another block that also satisfy at least 4 condition that is not unique.

Oh and btw there is an amazing blog on how to code hex coord, check it out https://www.redblobgames.com/grids/hexagons/ 

There are couple miles stones I want to achieve on my way to complete the development

## Phase 1, new born (IN PROGRESS)
* Using Command-line interface to display each block
* able to display a general hotspots, a.k.a locations where a high possibility of things happening is marked
* when enter specific coordinate, I will be able to retrieva all information relevant to that location
* give warning for players when multiple tiles all satisfy the same condition
* AI only suggest the best place to launch a search, but not questions

## PHase 2, your little virtual assitance
* AI now has the ability to track the input of each player, based on the response it will list out potential cues each player recieved
* AI now also eliminate blocks that doesn't fit a cue of a player, a.k.a even if a block satisfy many condition, if one of player's cue is known to eliminate this block, it receive a score of 0

## Phase3, become human
* AI can either be treated as a player (a.k.a manually input the cue of the player) or be treated as a *blind* player, which means it doesn't receive any cue, and just trying to predict the board.
* To achieve the previous point, AI need to be able to suggest a good location to ask a specific player as well, ideally clean out the player with most mystery and obtain as much information as possible (unless AI itself is playing, and asking too much might reveal your secret, but we will leave this phase to future where we will try to use neural network to train a better AI)

## Phase4, art of communication
* In this phase we focus on hosting/graphically present our product. We will stop using command line interface and exchange everything with a graphical user interphase, simply using a react frontend and a python backend, hosted on some cheap website
* Start sharing website around and get more people interested into this game

## Phase5, the unthinkable
* With Pytorch/Tensorflow, start training a GAN neural networks that specializes in the game with goal to defeat the current version of the AI, ideally train AI for 3, 4, 5 player game mode. in particular, there are quiet a few areas of concerns.
  * Sometimes it bad to ask a specific question, cause the next player might just win because you ask a good question
  * Sometimes it better to just ask a safe question and skip the term, thus AI will need to know how to make safe plays
* Problem, where tf do I find the GPU power to do it, though game is simple so it might not take too much resources

