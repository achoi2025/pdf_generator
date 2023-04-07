<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/achoi2025/pdf_generator">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">User-Friendly PDF Generator for Making Awards 🥇</h1>
<br />
</div>


<!-- ABOUT THE PROJECT -->
## About The Project 📚

The tool is created to **support teachers** who need to send out different types of awards to students. The template could be **easily manipulated** using the buttons implemented using GUI. 

Here's why you should use this tool:
* Making the awards for all medals is just burdensome. Use this tool to quickly generate memorable digital awards.
* It's user-friendly. Overwhelmed with thousands of buttons? This one only has eight...!
* Memory-effective. You don't need extra space in your computer to run this program.


### Built With

* <img src="https://img.shields.io/badge/Python-002323?style=flat&logo=Python&logoColor=blue"/>

___

<!-- USAGE EXAMPLES -->

## User Interface

|Button|Feature|
|:--:|:--:|
|Start|Start the program|
|Load Json| Load user-defined layout|
|Save Json| Save user-defined layout|
|Add Image| Add image to the layout|
|Add Text| Add text to the layout|
|Remove Item| Remove existing items|
|PDF Gen.| Export PDF of the layout|
|Finish| Close the program|

___
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* activate anaconda
  ```sh
  conda -n pdf python=3.8
  conda activate pdf
  ```
* reportlab
  ```sh
  pip install reportlab
  ```
* pdf2image
    ```sh
    pip install pdf2image
    ```
* poppler
    ```sh
    conda install -c conda-forge poppler
    ```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/achoi2025/pdf_generator.git
   ```

