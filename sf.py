from langchain_cohere.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from ckey import cohere_key

import os
os.environ['COHERE_API_KEY'] = cohere_key
llm = Cohere(
    temperature=0.9  # Set the temperature here
)

def generate_movie_details(genre):
    # chain 1: movie title generation
    prompt_template_title = PromptTemplate(
        input_variables=['genre'],
        template="I want to create a movie in the {genre} genre. Suggest only one proper, creative movie title related to this genre. just give the movie title in the output no character should be given."
    )

    title_chain = LLMChain(llm=llm, prompt=prompt_template_title, output_key="movie_title")

    # chain 2: plot generation
    prompt_template_plot = PromptTemplate(
        input_variables=['movie_title'],
        template="Generate a brief plot summary for a movie titled '{movie_title}'. Keep it concise, engaging, and relevant to the {genre} genre and relevant {movie_title} title . No additional text is needed."
    )

    plot_chain = LLMChain(llm=llm, prompt=prompt_template_plot, output_key="plot")

    # chain 3: cast list generation
    prompt_template_cast = PromptTemplate(
        input_variables=['movie_title'],
        template="Suggest a list of five actors who would fit well in the movie titled '{movie_title}'. Return the list as a comma-separated list. Just give the names, no extra characters."
    )

    cast_chain = LLMChain(llm=llm, prompt=prompt_template_cast, output_key="cast")

    chain = SequentialChain(
        chains=[title_chain, plot_chain, cast_chain],
        input_variables=['genre'],
        output_variables=['movie_title', 'plot', 'cast']
    )

    response = chain({'genre': genre})
    return response

if __name__ == "__main__":
    print(generate_movie_details("horror"))
