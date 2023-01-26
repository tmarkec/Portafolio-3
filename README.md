# **Hangman**

Hangman is a Python terminal game, a player's objective is to identify a hidden words. In each round, the player guesses a letter of the alphabet, if it is present in the word all instances are revealed, otherwise one of the hangman's body parts is drawn in on the gibbet and player lose their life. The game ends in a win if the word entirly revealed by correct guesses, and ends in loss if the hangman's body is completely revealed in stead.


  - [View the Live Website Here](https://hangers.herokuapp.com/)
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
        * [Testing User Stories](#testing-user-stories)
        * [Validation Testing](#validation-testing)
        * [Bugs](#bugs)
        * [Other Testing](#other-testing)
    * [Future Features](#future-features)
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

### Testing User Stories

 - As a player, I want to be able to create user name for the game

| **Feature**  | **Action**                  | **Expected Result**                                          | **Actual Result** |
| ------------ | --------------------------- | ------------------------------------------------------------ | ----------------- |
| Welcome screen | There is username input bellow "Hangman" title | Type your username and press enter, your name will appear in later stages of the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/input-name.png">
</details>

-  As a player, I want to be able to know rules of the game

| **Feature** | **Action**                           | **Expected Result**                                           | **Actual Result** |
| ----------- | ------------------------------------ | ------------------------------------------------------------- | ----------------- |
| Hangman rules screen | On second screen type "R" and press "Enter" that will lead you to separated screen which will display rules of the game | Game rules are shown on separated screen | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/alert-window.png">
</details>

 - As a player, I want the be able to pick the level of difficulty for the game

| **Feature** | **Action**                                         | **Expected Result**                            | **Actual Result** |
| ----------- | -------------------------------------------------- | ---------------------------------------------- | ----------------- |
| Choose level screen | After reading rules or just skipping them, you come to screen with 3 difficulty options | By using keyboard difficulty level to be set for the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/check-input.png">
</details>
<details><summary>Screenshots</summary>
<img src="./readme-img/input-field-nmb.png">
</details>

-  As a player, I want the game to show me progress in the game either by winning or loosing.

| **Feature** | **Action**                                 | **Expected Result**                                                                     | **Actual Result** |
| ----------- | ------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------- |
| Game screen  | Start guessing random letters by inputing on keyboard and pressing enter | Hangman art is displayed depending on the progress and levels, message with remaining lives is shown so as secret word with right guessed letters is shown| Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/1-25.png">
</details>

-  As a player, I want warning message to apear on the screen if I accidently enter an invalid character, number or just repeat the letter I used already

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game screen | Type either special character, number or repeat letter you already guessed | Message to apear on top of the screen, to warn about invalid input and not to count as try in the game | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/try-higher-nmb.png">
</details>
<details><summary>Screenshots</summary>
<img src="./readme-img/try-lower-nmb.png">
</details>

-  As a player, I want to get some message if I win, and if I lose I want to know what was the secret word

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game screen  | By either winning or loosing game new screen will display | Message top tell me If I won the game and message with completed art of hangman with secret word to apear on the screen | Works as expected |

<details><summary>Screenshots</summary>
<img src="./readme-img/already-tried.png">
</details>

-  As a player, after every game I want to be able have option to play again or not

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| End game screen  | After finishing game message with options for the user will apear on the screen | By pressing "Y" to be dirrected to choose level for another game, or by pressing "N" to be displayed some message | Works as expected |


-  As a user, I want to be able to either play again, or to start new game with new username

| **Feature** | **Action**                | **Expected Result**                                                  | **Actual Result** |
| ----------- | ------------------------- | -------------------------------------------------------------------- | ----------------- |
| Game page   | Click on either on "Go back" or "Play again" button | User should be taken to "Landing page" so he can create new username, or new game should start for the user | Work as expected  |

<details><summary>Screenshots</summary>
<img src="./readme-img/back.png">
</details>

 ### Validation Testing
- Used PEP8 Python Validator to validate my code

- <details><summary>Validated code</summary>
      <img src="assets/readme_img/validation_code.png">
      </details>

 ### Bugs
| **Bug**                                                                                                         | **Fix**                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couldn't connect function levels() to the game() function to upload difficulty level across game| Redo whole function levels() with changed while loop|
| User name wasn't appearing across the game      | Created global variable called name                                                                                             |
| After reading rules for the game and playing the game user was only able to play game twice before error message appeard, basically user was stuck in levels() function                                                   | Created new function to ask user if he wish to read rules or not and seprated rules() function from levels() function          |
| Poor visual presentation of the game   | Introduced colorama and add spacing to the print statemants across the game       |
| In levels() function user had to confirm his choice twice before he was able to continue with game                   | created global variable lives, which were later on called for user tries instead levels() function                                                                                                   |
| After finishing game once user was only able to choose difficulty level before terminal was cut out                            | called game() function bellow levels() function in end_game() function                                                                                                    |
| Print statemants from different screens were pilling up on top of each other, with user inputs and progress of the game                          | Imported os and created function which was used across the game to clear the terminal screen                                 |
| Too long lines during code                   | Run and formated code through black.vercel.app                              |
                                                                                                         
 ### Other Testing
  - I've tested accross the game that user can only input alphabet letters, no special characters, spaces and numbers were allowed. I've tested that for required letters to chose level, play game, read rules etc user will only move to required stage for the game if he inputs right letter which was describe in the message.

## Future Features
   - Features that I would like to add to the game would be, different categories that user can pick to guess secret word
   - Use API services to randomly get word rather than storing it in folders
   - User to be able to use hint if he gets stuck
   - Add scorelist to the screen with option for user to compare his score to score of the other users 
## Deployment
### Gitpod and git
 -  I created a repository in Github, named it p3-guess-the-word-game, and used the template Code-Institute-org/python-essentials-template
 -  Once the repository is created, click the green button to the right (Gitpod) to open Gitpod
 -  In the terminal I've used the run.py file provided by the template
 -  I created a docs folder to hold PDF:s and images
 -  Once folders and files are created I used Git commands to add the changes in the files to the staging area and push the changes to my repository

### Heroku
This project was deployed using Code Institutes mock terminal for Heroku.

-  Log in to Heroku and click "New" and "Create new app"
-  Name the new app and click "Create new app".
-  In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
-  While still in "Settings", click "Reveal Config Vars" and add the following; KEY: PORT, VALUE: 8000.
-  Click on "Deploy" and select your deploy method and search for repository name.
-  Click "Connect" on selected repository.
-  Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
-  Heroku will now deploy the app.

## Credits
- Code & Content
  - I give credits to [Stack overflow](https://www.stackoverflow.com/), [MDN Web Docs](https://developer.mozilla.org/en-US/) & [W3 Schools](https://www.w3schools.com/) for helping me resolve issues with Python while coding through
  - Inspiration and guidance/problem solving through project came from [kite](https://www.youtube.com/@KiteHQ), [Sanjin Dedic](https://www.youtube.com/@SanjinDedic), [Tech with Tim](https://www.youtube.com/@TechWithTim) 
   youtube channels, and [Geeksforgeeks](https://www.geeksforgeeks.org/), [Codefather](https://codefather.tech/) websites
  - Credits for code that clear screen was found on [stackoverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
  - Credits for my hangman art goes to  [Ascii](https://ascii.co.uk/art/hangman)
  - To create banner for my page with title name I used [Patorjk](https://patorjk.com/)
  - Giving credits to [Lucid chart](ttps://www.lucidchart.com/) for providing tools to easily create my flow chart

- Acknowledgment
  - Special thank you goes to mentor Narander Singh who helped me to finish my project
  - I would like to thank tuttor support from Code Institue for their help, as well as whole Code Institue for giving me opportunity to attend this course and to work on this project
  - I would also like to thank my collegaues for their support
  - Last but not least I would like to thank our coordinator Irene from Code Institute for giving guidance and schedules on daily basis in the classroom