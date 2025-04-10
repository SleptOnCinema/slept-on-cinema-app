import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Slept-On Cinema Companion",
    page_icon="🎬",
    layout="centered"
)

# Dictionary of movies with their metadata (using real podcast episodes)
movies = {
    "Celtic Pride": {
        "year": 1996,
        "director": "Tom DeCerchio",
        "rt_score": "9% Critics, 32% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/celtic-pride",
        "quote": "They kidnapped Utah's star player!",
        "drink_pairing": "Oversized drinks - stadium beer cups",
        "bolo_moments": ["Slow-motion sports footage", "Dan Aykroyd's quirky wardrobe choices", "Classic 90s trash talk"],
        "trivia": "Stars Dan Aykroyd and Daniel Stern as obsessed Celtics fans, with Damon Wayans as the kidnapped Utah Jazz star.",
        "similar_movies": ["Double Impact", "Undisputed"]
    },
    "Double Impact": {
        "year": 1991,
        "director": "Sheldon Lettich",
        "rt_score": "40% Critics, 43% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/double-impact",
        "quote": "Double the impact, double the fun!",
        "drink_pairing": "Hong Kong Sour and a Hong Kong Boilermaker",
        "bolo_moments": ["Classic Van Damme splits", "Twin brother contrasting personalities", "Final confrontation"],
        "trivia": "Jean-Claude Van Damme played both twins, requiring innovative filming techniques for the era.",
        "similar_movies": ["Undisputed", "Timecop"]
    },
    "Undisputed": {
        "year": 2002,
        "director": "Walter Hill",
        "rt_score": "48% Critics, 38% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/undisputed",
        "quote": "Two undefeated champions. One prison. The ultimate fight.",
        "drink_pairing": "Ringside beer or classic prison Pruno",
        "bolo_moments": ["Slaps", "Welding scenes", "Master P cameos", "Barbed wire", "Strange fruit-eating scene"],
        "trivia": "Features Ving Rhames and Wesley Snipes as rival boxers in a prison setting. Bombed in theaters but became a cult classic with three sequels.",
        "similar_movies": ["Celtic Pride", "Double Impact"]
    },
    "Entrapment": {
        "year": 1999,
        "director": "Jon Amiel",
        "rt_score": "38% Critics, 39% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/entrapment",
        "quote": "It's all about the score.",
        "drink_pairing": "Sophisticated martini with a twist",
        "bolo_moments": ["Laser security system scene", "Rooftop training sequences", "Sean Connery's suave charm"],
        "trivia": "The film stars Sean Connery and Catherine Zeta-Jones as a pair of art thieves planning a major heist.",
        "similar_movies": ["The Meg", "2 Fast 2 Furious"]
    },
    "The Meg": {
        "year": 2018,
        "director": "Jon Turteltaub",
        "rt_score": "46% Critics, 42% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/the-meg",
        "quote": "Chew on this!",
        "drink_pairing": "Deep blue ocean cocktail (blue curaçao and vodka)",
        "bolo_moments": ["Giant shark jump scares", "Jason Statham's underwater heroics", "Beach panic scene"],
        "trivia": "Based on Steve Alten's 1997 book 'Meg: A Novel of Deep Terror' about a prehistoric Megalodon shark.",
        "similar_movies": ["Annabelle", "The Nun"]
    },
    "Annabelle": {
        "year": 2014,
        "director": "John R. Leonetti",
        "rt_score": "29% Critics, 36% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/annabelle",
        "quote": "Before The Conjuring, there was Annabelle.",
        "drink_pairing": "Blood-red wine or crimson cocktail",
        "bolo_moments": ["Doll's subtle movements", "Basement scenes", "Cult ritual moments"],
        "trivia": "Spin-off of The Conjuring, focusing on the origins of the possessed Annabelle doll.",
        "similar_movies": ["The Nun", "Jeepers Creepers"]
    },
    "The Nun": {
        "year": 2018,
        "director": "Corin Hardy",
        "rt_score": "26% Critics, 37% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/the-nun",
        "quote": "Pray for forgiveness.",
        "drink_pairing": "Dark abbey-style beer or black sangria",
        "bolo_moments": ["Shadowy nun appearances", "Abbey exploration scenes", "Holy relic scenes"],
        "trivia": "Part of The Conjuring Universe, this film explores the origins of the demonic nun Valak first seen in The Conjuring 2.",
        "similar_movies": ["Annabelle", "Jeepers Creepers"]
    },
    "Jeepers Creepers": {
        "year": 2001,
        "director": "Victor Salva",
        "rt_score": "45% Critics, 36% Audience",
        "episode_link": "https://sleptoncinema.com/podcast-player/966/jeepers-creepers.mp3",
        "quote": "Every 23rd spring, for 23 days, it gets to eat.",
        "drink_pairing": "Rustic whiskey or backroad beer",
        "bolo_moments": ["The abandoned church", "The Creeper's truck pursuit", "Mysterious wall of bodies"],
        "trivia": "The film's title comes from the 1938 song 'Jeepers Creepers' which is featured in the movie.",
        "similar_movies": ["Lake Placid", "Annabelle"]
    },
    "Lake Placid": {
        "year": 1999,
        "director": "Steve Miner",
        "rt_score": "40% Critics, 39% Audience",
        "episode_link": "https://sleptoncinema.com/podcast-player/971/lake-placid.mp3",
        "quote": "You'll never know what bit you.",
        "drink_pairing": "Swamp water cocktail (midori and vodka)",
        "bolo_moments": ["Giant crocodile attacks", "Betty White's eccentric character", "Underwater tension scenes"],
        "trivia": "Despite being called 'Lake Placid', the film has nothing to do with the real Lake Placid in New York.",
        "similar_movies": ["The Meg", "Jeepers Creepers"]
    },
    "Timecop": {
        "year": 1994,
        "director": "Peter Hyams",
        "rt_score": "44% Critics, 42% Audience",
        "episode_link": "https://sleptoncinema.com/podcast-player/969/timecop.mp3",
        "quote": "His job is to police the past to protect our future.",
        "drink_pairing": "Futuristic blue electric lemonade",
        "bolo_moments": ["Van Damme's epic splits", "Time travel effects", "The 'same matter can't occupy same space' rule in action"],
        "trivia": "Based on a Dark Horse Comics series, this sci-fi action film stars Jean-Claude Van Damme as a police officer who works for a special agency that regulates time travel.",
        "similar_movies": ["Double Impact", "Surviving the Game"]
    },
    "Surviving the Game": {
        "year": 1994,
        "director": "Ernest R. Dickerson",
        "rt_score": "33% Critics, 36% Audience",
        "episode_link": "https://sleptoncinema.com/podcast-player/970/surviving-the-game.mp3",
        "quote": "The most dangerous game of all is man.",
        "drink_pairing": "Rugged bourbon on the rocks",
        "bolo_moments": ["Ice-T's survival skills", "Rutger Hauer's menacing character", "Forest chase sequences"],
        "trivia": "Loosely based on the 1924 short story 'The Most Dangerous Game' by Richard Connell, featuring Ice-T as a homeless man who becomes the target of a group of wealthy hunters.",
        "similar_movies": ["Timecop", "Undisputed"]
    },
    "2 Fast 2 Furious": {
        "year": 2003,
        "director": "John Singleton",
        "rt_score": "36% Critics, 50% Audience",
        "episode_link": "https://shows.acast.com/slept-on-cinema/episodes/2-fast-2-furious",
        "quote": "How fast do you like it?",
        "drink_pairing": "NOS energy drink with vodka",
        "bolo_moments": ["Ejector seat scene", "Bridge jump", "Rat in a bucket interrogation technique"],
        "trivia": "This was the only Fast & Furious film directed by John Singleton, the acclaimed director of 'Boyz n the Hood'.",
        "similar_movies": ["Timecop", "Double Impact"]
    }
}

# App header
st.title("🎬 Slept-On Cinema Companion")
st.markdown("*Discover bonus content from your favorite underrated movies!*")

# Create two columns for the header section
header_col1, header_col2 = st.columns([2, 1])

with header_col1:
    st.markdown("## Explore misjudged movie gems covered on the podcast")
    st.markdown("Each featured film has a Rotten Tomatoes score below 50% in either Critics or Audience score.")

with header_col2:
    st.markdown("### Hosted by:")
    st.markdown("**StanSteamer** & **GrobeStreet**")

# Movie selection section
st.markdown("---")
st.subheader("Choose a Movie")

# Create two columns for selection
select_col1, select_col2 = st.columns([3, 1])

with select_col1:
    # Option 1: Select from dropdown
    selected_movie = st.selectbox(
        "Pick a movie we've covered:",
        [""] + sorted(list(movies.keys()))
    )

with select_col2:
    # Option 2: Surprise Me button
    if st.button("Surprise Me! 🎲", use_container_width=True):
        selected_movie = random.choice(list(movies.keys()))

# Display movie information
if selected_movie:
    movie_data = movies[selected_movie]
    
    st.markdown("---")
    
    # Create two columns for the main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header(selected_movie)
        st.caption(f"{movie_data['year']} • Directed by {movie_data['director']}")
        st.markdown(f"*\"{movie_data['quote']}\"*")
        
        # RT score with color coding
        rt_score = movie_data['rt_score']
        st.markdown(f"**Rotten Tomatoes:** {rt_score}")
        
    with col2:
        # Episode link as a prominent button
        st.markdown("### Listen to the Episode")
        st.markdown(f"[🎧 Hear our full discussion]({movie_data['episode_link']})")
        
        if st.button("Play Episode", use_container_width=True):
            st.markdown(f"<script>window.open('{movie_data['episode_link']}', '_blank');</script>", unsafe_allow_html=True)
    
    # Create tabs for different content
    tab1, tab2, tab3, tab4 = st.tabs(["BOLO Moments", "Drink Pairing", "Trivia", "Similar Movies"])
    
    with tab1:
        st.subheader("👀 BOLO (Be On the Look Out)")
        st.markdown("Watch for these key moments without spoiling the experience:")
        for moment in movie_data["bolo_moments"]:
            st.markdown(f"- {moment}")
    
    with tab2:
        st.subheader("🍹 Drink Pairing")
        st.markdown("The hosts recommend:")
        st.info(movie_data["drink_pairing"])
    
    with tab3:
        st.subheader("🎲 Behind the Scenes Trivia")
        st.markdown(movie_data["trivia"])
    
    with tab4:
        st.subheader("🎬 If You Liked This Movie...")
        st.markdown("You might enjoy these other films we've covered:")
        for similar_movie in movie_data["similar_movies"]:
            if similar_movie in movies:
                similar_data = movies[similar_movie]
                st.markdown(f"- **[{similar_movie}]({similar_data['episode_link']})** ({similar_data['year']})")
                st.caption(f"   *{similar_data['quote']}*")

else:
    # Show welcome message if no movie selected
    st.info("👆 Select a movie above or click 'Surprise Me!' to discover a random gem from our podcast!")
    
    # Display a teaser of movie posters or logos
    st.markdown("### Movies We've Covered")
    cols = st.columns(3)
    movie_list = list(movies.keys())
    for i, col in enumerate(cols):
        if i < len(movie_list):
            with col:
                st.markdown(f"**{movie_list[i]}** ({movies[movie_list[i]]['year']})")
                st.caption(f"{movies[movie_list[i]]['rt_score']}")

# Footer
st.markdown("---")
st.markdown("© Slept-On Cinema Podcast | Find us on [Instagram](https://instagram.com/sleptoncinema) and [Twitter/X](https://twitter.com/sleptoncinema)")
