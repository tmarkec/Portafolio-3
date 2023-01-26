# **Hangman**

Hangman is a Python terminal game, a player's objective is to identify a hidden words. In each round, the player guesses a letter of the alphabet, if it is present in the word all instances are revealed, otherwise one of the hangman's body parts is drawn in on the gibbet and player lose their life. The game ends in a win if the word entirly revealed by correct guesses, and ends in loss if the hangman's body is completely revealed in stead.

## Table of contents 
* [Hangman](#hangman)
    * [User Experience](#user-experience)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
        * [Colored Text](#colored-text)
        * [Technology Used](#technology-used)
          * [Languages](#languages)
		  * [Libraries](#libraries)
    * [Flow Chart](#flow-chart)
    * [Testing](#testing)
        * [Testing User Stories](*testing-user-stories)
        * [Validation Testing](#validation-testing)
        * [Bugs](#bugs)
            * [Bugs Fixed](#bug-fixed)
    * [Future features](*future-features)
    * [Deployment](#deployment)
    * [Credits](#credits)


## User experience

### Project Goals

- Is to provide user with interesting game that interact with user as much as possible with features such as option for user to put his name which will be shown on the game screen, option for user to pick difficulty level for the game, help if user is strugling and option to either play again or if he decide not to to present user with new clear thank you screen.

### User Stories

- As a player, I want to be able to create username for the game
- As a player, I want to be able to know rules of the game
- As a player, I want the be able to pick the level of difficulty for the game
- As a player, I want the game to show me progress in the game either by winning or loosing.
- As a player, I want warning message to apear on the screen if I accidently enter an invalid character, number or just repeat the letter I used already
- As a player, I want to get some message if I win, and if I lose I want to know what was the secret word
- As a player, I want some help/hint if my attempts are not going well and I'm really close to loosing the game
- As a player, after every game I want to be able have option to play again or not

### Coloured Text

- Coloured text will be shown accross the game, to make user more intersted in the game. Wrong inputs accross the game will be shown in red colour. Colours in the game are imported from Python Colorama Model

### Technology Used
- #### Languages:
   - Phyton
- #### Libraries
  * [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
  * [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git
  * [Heroku](https://id.heroku.com)
    * Heroku was used to deploy the live project
  * [Lucidchart](https://lucid.app/)
    * Lucidchart was used to create the flowchart
  * [PEP8](http://pep8online.com/)
    * The PEP8 was used to validate all the Python code
  * [Patorjk](https://patorjk.com)
    * Patorjk (ASCII Art Generator) was used to create banner accross the game


## Flow Chart

Planning of this project was based on the flow charts using the platform Lucid Charts.

## Testing

### Testing user stories

1. As a player, I want to be able to create user name for the game

| **Feature**  | **Action**                  | **Expected Result**                                          | **Actual Result** |
| ------------ | --------------------------- | ------------------------------------------------------------ | ----------------- |
| Welcome screen | There is username input bellow "Hangman" banner" | Type your username and press enter, your name will appear in later stages of the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/input-name.png">
</details>

2. As a player, I want to be able to know rules of the game

| **Feature** | **Action**                           | **Expected Result**                                           | **Actual Result** |
| ----------- | ------------------------------------ | ------------------------------------------------------------- | ----------------- |
| Hangman rules screen | On second screen type "R" and press "Enter" that will lead you to separated screen which will display rules of the game | Game rules are shown on separated screen | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/alert-window.png">
</details>

3. As a player, I want the be able to pick the level of difficulty for the game

| **Feature** | **Action**                                         | **Expected Result**                            | **Actual Result** |
| ----------- | -------------------------------------------------- | ---------------------------------------------- | ----------------- |
| Choose level screen | After reading rules or just skipping them, you come to screen with 3 difficulty options | By using keyboard difficulty level to be set for the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/check-input.png">
</details>
<details><summary>Screenshots</summary>
<img src="./readme-img/input-field-nmb.png">
</details>

4. As a player, I want the game to show me progress in the game either by winning or loosing.

| **Feature** | **Action**                                 | **Expected Result**                                                                     | **Actual Result** |
| ----------- | ------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------- |
| Game screen  | Start guessing random letters by inputing on keyboard and pressing enter | Hangman art is displayed depending on the progress and levels, message with remaining lives is shown so as secret word with right guessed letters is shown| Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/1-25.png">
</details>

5. As a player, I want warning message to apear on the screen if I accidently enter an invalid character, number or just repeat the letter I used already

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game screen | Type either special character, number or repeat letter you already guessed | Message to apear on top of the screen, to warn about invalid input and not to count as try in the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/try-higher-nmb.png">
</details>
<details><summary>Screenshots</summary>
<img src="./readme-img/try-lower-nmb.png">
</details>

6. As a player, I want to get some message if I win, and if I lose I want to know what was the secret word

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game screen  | By either winning or loosing game new screen will display | Message top tell me If I won the game and message with completed art of hangman with secret word to apear on the screen | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/already-tried.png">
</details>

7. As a player, after every game I want to be able have option to play again or not

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| End game screen  | After finishing game message with options for the user will apear on the screen | By pressing "Y" to be dirrected to choose level for another game, or by pressing "N" to be displayed some message | Works as expected |


8. As a user, I want to be able to either play again, or to start new game with new username

| **Feature** | **Action**                | **Expected Result**                                                  | **Actual Result** |
| ----------- | ------------------------- | -------------------------------------------------------------------- | ----------------- |
| Game page   | Click on either on "Go back" or "Play again" button | User should be taken to "Landing page" so he can create new username, or new game should start for the user | Work as expected  |

<details><summary>Screenshots</summary>
<img src="./readme-img/back.png">
</details>

### Validation testing

### Bugs

## Future features

## Deployment

## Credits