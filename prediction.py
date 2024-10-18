import pygame as py
import random

horoscope_data = {
    "మేషం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement.",
        ]
    },
    "వృషభం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "మిథునం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
}
# Horoscope data for Cancer, Leo, and Virgo
horoscope_data.update({
    " కర్కాటకం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "సింహం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "కన్యా": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    }
})
# Horoscope data for Libra, Scorpio, and Sagittarius
horoscope_data.update({
    "తులా": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "వృశ్చికం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "ధనుస్సు": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    }
})
# Horoscope data for Capricorn, Aquarius, and Pisces
horoscope_data.update({
    "మకరం": {
      "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
            "Your dedication will lead to a successful outcome."
        ]
    },
    "కుంభం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    },
    "మీనం": {
        "Students": [
            "Focus on your studies, success is coming.",
            "Today is a great day for starting new projects.",
            "You will find a new learning opportunity.",
            "Avoid overconfidence in exams.",
        ],
        "Business": [
            "A new opportunity in business will arise.",
            "Avoid making hasty financial decisions.",
            "Focus on your long-term goals.",
            "Be cautious with investments today.",
        ],
        "Politics": [
            "Collaborating with others will improve your reach.",
            "Avoid making any controversial statements today.",
            "You will gain supporters from unexpected places.",
            "Rivals will attempt to undermine you — stay strong.",
        ],
        "Teachers": [
            "Be patient with slow learners.",
            "New opportunities for professional growth will come.",
            "Your hard work is about to be recognized.",
            "A student may inspire you with their question.",
            "Collaboration with colleagues will enhance your work."
        ],
        "Farmers": [
            "Avoid hasty decisions regarding your crops.",
            "Your hard work will soon pay off.",
            "Seek advice from experienced farmers today.",
            "Weather changes may work in your favor.",
            "Prepare for unexpected challenges.",
        ],
        "Daily Wage Workers": [
            "Your hard work will be appreciated by others.",
            "Take care of your health while working long hours.",
            "Stay patient, a better job is coming soon.",
            "Today might be physically demanding —r est when needed.",
            "Look for opportunities to improve your skills."
        ],
        "Employees": [
            "A promotion may be in your near future.",
            "You will impress your superiors with your work.",
            "An important task may come your way today.",
            "You will build a stronger relationship with your colleagues.",
            "A challenge at work will test your skills.",
            "Seek feedback from your manager for improvement."
        ]
    }
})

py.init()

# Screen dimensions
screen=py.display.set_mode((1300,700))
py.display.set_caption("astrology")


# fonts
font = py.font.Font('Avenir.ttf', 20)

# Input variables
zodiac_sign = ""
occupation = ""
active_input = None

# State control
show_prediction = False
prediction_text = ""

# Define text input rectangles (placed after the labels)
zodiac_box = py.Rect(300, 50, 300, 40)  # Adjusted X position to appear after the label
occupation_box = py.Rect(300, 120, 300, 40)  # Adjusted X position to appear after the label
get_prediction_box = py.Rect(50, 190, 200, 40)
back_box = py.Rect(50, 500, 100, 40)

# Function to get prediction based on user input
def get_prediction(zodiac, occupation):
    try:
        return random.choice(horoscope_data[zodiac][occupation])
    except KeyError:
        return "Invalid Zodiac or Occupation. Please select valid options."

# Main loop
running = True
while running:
    screen.fill("GRAY")

    # Event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if zodiac_box.collidepoint(event.pos):
                active_input = "zodiac"
            elif occupation_box.collidepoint(event.pos):
                active_input = "occupation"
            elif get_prediction_box.collidepoint(event.pos):
                if zodiac_sign and occupation:
                    prediction_text = get_prediction(zodiac_sign, occupation)
                    show_prediction = True
                else:
                    prediction_text = "Please fill in both fields."
                    show_prediction = True
            elif back_box.collidepoint(event.pos):
                show_prediction = False
                zodiac_sign = ""
                occupation = ""
        elif event.type == py.KEYDOWN:
            if active_input == "zodiac":
                if event.key == py.K_BACKSPACE:
                    zodiac_sign = zodiac_sign[:-1]
                else:
                    zodiac_sign += event.unicode
            elif active_input == "occupation":
                if event.key == py.K_BACKSPACE:
                    occupation = occupation[:-1]
                else:
                    occupation += event.unicode

    # Render input fields
    py.draw.rect(screen, "BLUE", zodiac_box, 2)
    py.draw.rect(screen, "BLUE", occupation_box, 2)
    py.draw.rect(screen, "BLUE", get_prediction_box, 2)
    
    if show_prediction:
        py.draw.rect(screen, "BLUE", back_box, 2)

    # Render text
    zodiac_label = font.render("Zodiac Sign:", True, "BLACK")
    screen.blit(zodiac_label, (50, 55))  # Label for Zodiac Sign (before the input box)

    occupation_label = font.render("Occupation:", True, "BLACK")
    screen.blit(occupation_label, (50, 125))  # Label for Occupation (before the input box)

    # Render text inside the input fields
    zodiac_text = font.render(zodiac_sign, True, "BLACK")
    screen.blit(zodiac_text, (zodiac_box.x + 5, zodiac_box.y + 5))

    occupation_text = font.render(occupation, True, "BLACK")
    screen.blit(occupation_text, (occupation_box.x + 5, occupation_box.y + 5))

    get_prediction_label = font.render("Get Prediction", True, "BLACK")
    screen.blit(get_prediction_label, (60, 200))

    if show_prediction:
        prediction_label = small_font.render(prediction_text, True, "BLACK")
        screen.blit(prediction_label, (50, 250))
        
        back_label = font.render("Back", True, "BLACK")
        screen.blit(back_label, (60, 500))

    # Update the screen
    py.display.flip()

py.quit()
