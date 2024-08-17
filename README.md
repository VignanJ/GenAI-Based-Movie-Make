# GenAI-Based-Movie-Maker
This project provides an AI-powered tool to generate movie details based on a given genre. The tool uses natural language processing to suggest a movie title, generate a brief plot summary, and recommend a cast list for the specified genre.

## Features

- **Movie Title Generation:** Generate a creative movie title based on the selected genre.
- **Plot Summary:** Generate a brief and engaging plot summary for the movie title.
- **Cast Recommendation:** Suggest a list of five actors who would fit well in the generated movie.

## Technology Stack

- **Streamlit:** For creating the interactive web application.
- **Cohere API:** For generating movie titles, plots, and cast recommendations.
- **LangChain:** For chaining the prompts and managing the flow of data.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/movie-title-plot-cast-generator.git
    cd movie-title-plot-cast-generator
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
   
   - Create a file named `.env` in the root directory of the project.
   - Add your Cohere API key to the `.env` file:

     ```plaintext
     COHERE_API_KEY=your_cohere_api_key_here
     ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run main.py
    ```

2. **Access the application:**
   Open your browser and go to `http://localhost:8501`.

3. **Select a genre:**
   Use the sidebar to select a genre. The app will generate a movie title, plot, and cast list based on your selection.

## Code Overview

- **`stlit.py`:** The Streamlit app code. Handles user input, calls the `sf.generate_movie_details` function, and displays the results.
- **`sl.py`:** Contains the `generate_movie_details` function which uses the Cohere API to generate the movie details.
- **`requirements.txt`:** Lists the Python dependencies required for the project.


## Acknowledgments

- **Cohere:** For providing the API for generating text.
- **LangChain:** For simplifying the management of prompts and chains.

