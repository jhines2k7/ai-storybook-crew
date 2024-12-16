# AI Storybook Project

This project uses the CrewAI framework to create a team of agents that collaborate to produce a short story, ad copy, and social media content for a product launch campaign.

## Project Structure

The project is structured as follows:

-   `agent_playground.py`: A script to test individual agents and tasks.
-   `agents.py`: Defines the agents used in the project, including their roles, goals, and backstories.
-   `main.py`: The main script that sets up and runs the CrewAI workflow.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `tasks.py`: Defines the tasks that the agents perform, including descriptions, expected outputs, and tools.
-   `seo/keywords.txt`: A list of keywords used for SEO optimization.
-   `tools/`: Contains custom tools used by the agents.
-   `output_files/`: Directory where the output files are stored.

## Agents

The project uses the following agents:

-   `CreativeDirector`: Leads the team in developing innovative short stories.
-   `Researcher`: Gathers and analyzes data to provide the writing team with a solid foundation of knowledge.
-   `FantasyWriter`: Creates a fantasy narrative.
-   `Editor`: Refines and elevates the creative output of the team.
-   `WebDeveloper`: Handles the technical aspects of posting the content online.
-   `Copywriter`: Crafts compelling and engaging copy for ads and social media.
-   `SEOSpecialist`: Optimizes content for search engines.
-   `SocialMediaManager`: Plans and executes social media campaigns.
-   `ArtDirector`: Leads the visual direction of the project.

## Tasks

The project includes the following tasks:

-   `develop_creative_brief`: Develops a creative brief for the project.
-   `review_creative_brief`: Reviews the creative brief.
-   `create_seo_brief`: Creates an SEO brief for the project.
-   `develop_social_media_plan`: Develops a social media plan.
-   `write_ad_copy`: Writes ad copy for the product.
-   `write_social_media_posts`: Writes social media posts for the product.
-   `write_story`: Writes a short story based on the creative and SEO briefs.
-   `convert_to_html`: Converts the story to an HTML fragment.

## How to Run the Project

1.  Clone the repository.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3.  Set up your environment variables in a `.env` file.
4.  Run the `main.py` script:

    ```bash
    python main.py
    ```

## Output

The output files, including the creative brief, SEO brief, social media plan, ad copy, social media posts, story, and HTML fragment, are stored in the `output_files/` directory.

## Contributing

Feel free to contribute to this project by submitting pull requests.

## License

This project is licensed under the MIT License.
