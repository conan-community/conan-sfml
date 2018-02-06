#include "SFML/Audio.hpp"
#include "SFML/Graphics.hpp"

int main()
{
    // Create the main window
    sf::RenderWindow window(sf::VideoMode(620, 388), "Conan SFML window");
    // Load a sprite to display
    sf::Texture texture;
    sf::IntRect area = sf::IntRect(0, 0, 620, 388);
    sf::Image image;
    image.loadFromFile("../../../cute_image.jpg");
    if (!texture.loadFromImage(image))
        return EXIT_FAILURE;
    sf::Sprite sprite(texture, area);
    // Create a graphical text to display
    sf::Font font;
    if (!font.loadFromFile("../../../arial.ttf"))
        return EXIT_FAILURE;
    sf::Text text("Conan rules!!!", font, 100);
    // Load a music to play
    sf::Music music;
    if (!music.openFromFile("../../../nice_music.ogg"))
        return EXIT_FAILURE;
    // Play the music
    music.play();
    // Start the game loop
    while (window.isOpen())
    {
        // Process events
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window : exit
            if (event.type == sf::Event::Closed)
                window.close();
        }
        // Clear screen
        window.clear();
        // Draw the sprite
        window.draw(sprite);
        // Draw the string
        window.draw(text);
        // Update the window
        window.display();
    }
    return EXIT_SUCCESS;
}