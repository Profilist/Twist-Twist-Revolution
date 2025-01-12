# Twist Twist Revolution
> A computer vision rhythm game that challenges players to hit directional arrows in sync with the music using webcam hand movements.

![Logo](https://i.imgur.com/AwA3C5r.jpg)

## How to Play
1. Launch the game and allow webcam access.
2. Use your hands to move into the respective locations of the arrows on screen.
3. Match the arrows in sync with the music to score points and maintain your HP.
4. Press P to play/pause music during gameplay.

## Features
- **Interactive Gameplay**: Use real-time hand movements to hit arrows, as detected through your webcam.
- **Dynamic Scoring System**: Earn points based on timing accuracy, with rankings like Marvelous, Perfect, Great, or Miss.
- **Health Points (HP)**: Stay in the game by maintaining HP above 0.

## How I Built It
- Programming Languages: **Python**
- Libraries and Tools:
  - **Pygame**: For game mechanics, rendering, and interactivity.
  - **OpenCV**: To process webcam input and detect hand positions.
  - **MediaPipe**: For advanced hand tracking and gesture recognition.

## Installation
1. Clone this repository:
  ```bash
   git clone https://github.com/Profilist/twist-twist-revolution.git
  ```
2. Navigate to the project directory:
  ```bash
  cd twist-twist-revolution
  ```
3. Install the required dependencies:
  ```bash
pip install -r requirements.txt
```
4. Run the game
  ```bash
  python main.py
  ```

## Assets
All assets, including images and sound effects, are stored in the assets folder.
